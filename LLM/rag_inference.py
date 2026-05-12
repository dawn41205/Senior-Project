import os
import json
import time
import sqlite3
import requests
import chromadb
from sentence_transformers import SentenceTransformer
import jieba
import pickle
import torch
import warnings
from tqdm import tqdm
import re
import google.generativeai as genai

warnings.filterwarnings('ignore')

CHROMA_DB_DIR = "chroma_db"
BM25_INDEX_PATH = "bm25_index.pkl"
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY", "")
MODEL_NAME = "gemma-4-31b-it"

if GEMINI_API_KEY:
    genai.configure(api_key=GEMINI_API_KEY)
    # 優化生成參數：限制字數與隨機性
    generation_config = {
        "temperature": 0.0,
        "max_output_tokens": 300,
        "candidate_count": 1,
    }
    gemini_model = genai.GenerativeModel(
        model_name=MODEL_NAME,
        generation_config=generation_config
    )
else:
    print("[Warning] 找不到 GEMINI_API_KEY，RAG 推論將無法執行。")
    gemini_model = None

DB_NAME = "inference_cache.db"

TIMELINE_CLASSES = ["already", "within_2_years", "between_2_and_5_years", "longer_than_5_years", "N/A"]
QUALITY_CLASSES = ["Clear", "Not Clear", "Misleading", "N/A"]

def setup_db():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS rag_predictions (
            id TEXT PRIMARY KEY,
            verification_timeline TEXT,
            evidence_quality TEXT,
            raw_response TEXT
        )
    ''')
    conn.commit()
    return conn

class HybridRetriever:
    def __init__(self):
        print("正在載入 RAG 混合檢索器 (ChromaDB + BM25)...")
        self.client = chromadb.PersistentClient(path=CHROMA_DB_DIR)
        self.collection = self.client.get_collection("esg_kb")
        
        device = "cuda" if torch.cuda.is_available() else "cpu"
        self.encoder = SentenceTransformer("BAAI/bge-m3", device=device)
        
        with open(BM25_INDEX_PATH, "rb") as f:
            self.bm25_store = pickle.load(f)
        self.bm25 = self.bm25_store["bm25"]
        self.bm25_ids = self.bm25_store["ids"]

    def retrieve(self, query: str, exclude_id: str, k=6):
        # 1. 向量檢索 (Vector Search)
        query_emb = self.encoder.encode([query], show_progress_bar=False).tolist()
        
        # 資料洩漏防護：使用 {$ne} metadata 過濾，確保不會撈到「題目自身」
        vector_results = self.collection.query(
            query_embeddings=query_emb,
            n_results=k*2, 
            where={"id": {"$ne": int(exclude_id)}}
        )
        
        # 2. 關鍵字檢索 (BM25)
        tokens = jieba.lcut(query)
        bm25_scores = self.bm25.get_scores(tokens)
        bm25_ranked = sorted(
            [(score, doc_id) for score, doc_id in zip(bm25_scores, self.bm25_ids) if str(doc_id) != str(exclude_id)],
            key=lambda x: x[0], reverse=True
        )[:k*2]
        
        # 合併與去重 (交錯取回)
        final_results = []
        seen = set()
        
        # 優先收集從 Vector 檢索到的高度語意相似文本
        if vector_results['ids'] and len(vector_results['ids']) > 0:
            for i, doc_id in enumerate(vector_results['ids'][0]):
                if doc_id not in seen:
                    final_results.append({
                        "id": doc_id,
                        "document": vector_results['documents'][0][i],
                        "metadata": vector_results['metadatas'][0][i]
                    })
                    seen.add(doc_id)
                    if len(final_results) >= k: break
                
        # 如果不足，利用 BM25 補充 (精準關鍵字匹配)
        if len(final_results) < k:
            bm25_id_list = [id_ for _, id_ in bm25_ranked if id_ not in seen][:k - len(final_results)]
            if bm25_id_list:
                bm25_docs = self.collection.get(ids=bm25_id_list)
                for i, doc_id in enumerate(bm25_docs["ids"]):
                    final_results.append({
                        "id": doc_id,
                        "document": bm25_docs['documents'][i],
                        "metadata": bm25_docs['metadatas'][i]
                    })

        return final_results

def query_gemini(prompt):
    """ 呼叫 AI Studio 的 Gemma-4-31b-it """
    if not gemini_model: return ""
    
    max_retries = 3
    for i in range(max_retries):
        try:
            # 配合 AI Studio 免費版限速
            time.sleep(2)
            response = gemini_model.generate_content(prompt)
            return response.text
        except Exception as e:
            if "429" in str(e):
                print(f"\n[Warning] Gemini Rate Limit (429)，等待 60 秒重試 (第 {i+1} 次)...")
                time.sleep(60)
                continue
            print(f"\n[Error] Gemini API 呼叫失敗: {e}")
    return ""

def parse_prediction(text, classes):
    """ 從生成的自然語言中強硬萃取出對應的分類標籤 (含模糊匹配) """
    text_lower = text.lower()
    
    # 第一輪：精確匹配 (按優先順序)
    for line in text.split('\n'):
        line_lower = line.lower().strip()
        if line_lower.startswith('timeline:') or line_lower.startswith('quality:'):
            for cls in classes:
                if cls.lower() in line_lower:
                    return cls
    
    # 第二輪：全文精確匹配
    for cls in classes:
        if cls.lower() in text_lower:
            return cls
    
    # 第三輪：模糊匹配 (處理常見變體)
    fuzzy_map = {
        "not_clear": "Not Clear",
        "notclear": "Not Clear",
        "not clear": "Not Clear",
        "unclear": "Not Clear",
        "2_and_5": "between_2_and_5_years",
        "2-5": "between_2_and_5_years",
        "2 to 5": "between_2_and_5_years",
        "within 2": "within_2_years",
        "longer than 5": "longer_than_5_years",
        "more than 5": "longer_than_5_years",
    }
    for pattern, cls in fuzzy_map.items():
        if pattern in text_lower:
            return cls
            
    # 如果沒抽到標準字詞，給予預設判定
    return "N/A"

def extract_reasoning(text):
    """ 從生成的字串中切出 Reasoning 的區塊 """
    match = re.search(r'Reasoning:\s*(.*?)(?=Timeline:|$)', text, re.IGNORECASE | re.DOTALL)
    if match:
        return match.group(1).strip()
    return "No reasoning provided."

def run_rag_inference(data_list):
    """ 被 Main Pipeline 呼叫的核心進入點 """
    print(f"\n啟動 RAG + {MODEL_NAME} 推論管線 (共 {len(data_list)} 筆測試)...")
    conn = setup_db()
    c = conn.cursor()
    
    try:
        retriever = HybridRetriever()
    except Exception as e:
        print(f"初始化檢索器失敗！請確認你已經跑過 rag_indexer.py。(錯誤: {e})")
        return {}
    
    predictions_map = {}
    reasoning_logs = []
    
    for item in tqdm(data_list, desc=f"RAG ({MODEL_NAME}) 處理進度", unit="篇"):
        doc_id = str(item['id'])
        
        # ======== SQLite 斷點保護機制 ========
        c.execute('SELECT verification_timeline, evidence_quality FROM rag_predictions WHERE id=?', (doc_id,))
        row = c.fetchone()
        if row:
            predictions_map[doc_id] = {
                "verification_timeline": row[0],
                "evidence_quality": row[1]
            }
            continue  # 已經推論過，直接跳過不浪費算力
            
        t = item.get('gemini_extracted_text', "")
        if not t: t = item.get('data', "")
        idx_prompt = t[:1500] # Context Window 有限，適度截斷
        promise_str = item.get('promise_string', "")
        
        # 規則攔截：若承諾為空，強制判斷為 N/A，不耗費 API 算力
        if not promise_str or promise_str.strip() == "":
            print(f"\n>>> [ID {doc_id}] 規則攔截：承諾為空，強制設為 N/A")
            
            c.execute('''
                INSERT OR REPLACE INTO rag_predictions (id, verification_timeline, evidence_quality, raw_response)
                VALUES (?, ?, ?, ?)
            ''', (doc_id, "N/A", "N/A", "Rule-based intercepted"))
            conn.commit()
            
            predictions_map[doc_id] = {
                "verification_timeline": "N/A",
                "evidence_quality": "N/A"
            }
            continue
            
        query_text = f"承諾：{promise_str}\n\n報告內文：\n{idx_prompt}"
        
        # RAG 檢索 Top-2
        retrieved_docs = retriever.retrieve(query_text, exclude_id=doc_id, k=2)
        
        icl_examples = ""
        for i, doc in enumerate(retrieved_docs):
            m = doc['metadata']
            icl_examples += f"[參考範例 {i+1}]\n內文片段：{doc['document'][:200]}...\n"
            icl_examples += f"這篇的 Timeline 是: {m.get('verification_timeline', 'N/A')}\n"
            icl_examples += f"這篇的 Quality 是: {m.get('evidence_quality', 'N/A')}\n\n"
            
        prompt = f"""你是 ESG 永續報告查驗委員。請依據以下規則判斷 Timeline 與 Quality。

### 1. 本次任務
欲查驗的承諾：{promise_str}
實際企業內文：{idx_prompt}

### 2. Timeline 判定規則
基準：以本報告書發布年 2024 年起算。
- 'already': 承諾已完成或正在實施，且內文有「已」「自XXXX年起」等實績證據。
- 'within_2_years': 預計 2025-2026 完成。
- 'between_2_and_5_years': 預計 2027-2029 完成，或承諾未標明完成年份。
- 'longer_than_5_years': 預計 2030 年後（含 2030/2040/2050 淨零目標）。
- 'N/A': 無具體承諾。
⚠️ 最長時間範圍原則：若承諾同時涉及短期措施與長期最終目標，以最終目標年限為準。
例如：「2024年已開始執行減碳，目標 2030 年減少 40%」→ 選 'longer_than_5_years'。
⚠️ 持續性作為：若承諾為「積極推動」「持續關懷」等未設終點的作為，選 'between_2_and_5_years'。
但若內文同時有明確的 2024 年執行實績數據，則改選 'already'。

### 3. Quality 判定決策樹（按順序檢查）
Step 1: 內文是否有此承諾的執行證據？ → 無 → 'N/A'
Step 2: 證據是否有具體數據（數字/百分比/金額/日期）且與承諾直接相關？ → 是 → 'Clear'
Step 3: 證據是否僅有模糊字眼（持續推動/努力改善/積極投入等）且完全缺乏具體數據？ → 是 → 'Not Clear'
Step 4: 證據與承諾關聯薄弱、嚴重偏題或轉移注意力？ → 是 → 'Misleading'

[Not Clear 範例]
承諾：「致力於建立以合作為基礎的價值體系」
內文：「推動供應鏈的低碳轉型，同時維護人權、保護環境和促進生物多樣性」
→ Quality: Not Clear（僅「推動」「維護」「促進」等模糊字眼，無具體數據）

### 4. 輸出格式（僅輸出這三行）
Reasoning: [一句話理由]
Timeline: [標籤]
Quality: [標籤]
"""
        
        # 呼叫 Gemma 進行推論
        response_text = query_gemini(prompt)
        
        # 如果 API 回傳為空，不能存入資料庫
        if not response_text or len(response_text.strip()) < 5:
            continue
        
        # NLP 正規化抽取
        reasoning_pred = extract_reasoning(response_text)
        timeline_pred = parse_prediction(response_text, TIMELINE_CLASSES)
        quality_pred = parse_prediction(response_text, QUALITY_CLASSES)
        
        # 保存 Reasoning Log 用於後續查核
        reasoning_logs.append({
            "id": doc_id,
            "promise_status": promise_str,
            "verification_timeline": timeline_pred,
            "evidence_quality": quality_pred,
            "reasoning": reasoning_pred,
            "raw_response": response_text
        })
        
        # 存入防呆資料庫
        c.execute('''
            INSERT OR REPLACE INTO rag_predictions (id, verification_timeline, evidence_quality, raw_response)
            VALUES (?, ?, ?, ?)
        ''', (doc_id, timeline_pred, quality_pred, response_text))
        conn.commit()
        
        # 即時輸出
        print(f"\n>>> [ID {doc_id}] 完成推論")
        print(f"    - Timeline: {timeline_pred}")
        print(f"    - Quality : {quality_pred}")
        print(f"    - Reason  : {reasoning_pred}")
        
        predictions_map[doc_id] = {
            "verification_timeline": timeline_pred,
            "evidence_quality": quality_pred
        }
        
    conn.close()
    
    # 將所有思考鏈輸出為 log 檔案供檢視
    if reasoning_logs:
        with open("reasoning_log.json", "w", encoding="utf-8") as f:
            json.dump(reasoning_logs, f, ensure_ascii=False, indent=4)
        print("\n[INFO] 已匯出 reasoning_log.json")
            
    return predictions_map

if __name__ == "__main__":
    print("這是一支功能模組，請透過 main_pipeline.py 來啟動整體預測流程。")
    print("若想單獨測試，可以修改本檔案底部。")
