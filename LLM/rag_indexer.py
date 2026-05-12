import json
import os
import chromadb
from sentence_transformers import SentenceTransformer
from rank_bm25 import BM25Okapi
import jieba
import pickle
from tqdm import tqdm
import warnings
warnings.filterwarnings('ignore')

INPUT_JSON = "vpesg4k_train_1000_enhanced.json"
FALLBACK_JSON = "vpesg4k_train_1000.json"

CHROMA_DB_DIR = "chroma_db"
BM25_INDEX_PATH = "bm25_index.pkl"

def main():
    print("啟動混合式知識庫建置 (ChromaDB Vector + BM25 Lexical) ...")
    print("必備套件: pip install chromadb sentence-transformers rank_bm25 jieba tqdm\n")
    
    # 決定讀取哪個檔案
    if os.path.exists(INPUT_JSON):
        file_to_load = INPUT_JSON
        print(f"[OK] 找到 Gemini 增強版資料，載入: {file_to_load}")
    elif os.path.exists(FALLBACK_JSON):
        file_to_load = FALLBACK_JSON
        print(f"[WARN] 找不到增強版資料，退回使用原始資料: {file_to_load}")
    else:
        print("[FAIL] 找不到任何資料檔案，建置失敗。")
        return
        
    with open(file_to_load, "r", encoding="utf-8") as f:
        data = json.load(f)
        
    print("\n[1/4] 載入 SentenceTransformer 模型 (BAAI/bge-m3)...")
    # 強制使用 CPU 以避免 RTX 4060 (8GB) 顯存溢出
    encoder = SentenceTransformer("BAAI/bge-m3", device="cpu")
    
    print("[2/4] 初始化 ChromaDB 持久化資料庫...")
    client = chromadb.PersistentClient(path=CHROMA_DB_DIR)
    
    # 清除舊有的 esg_kb 以防重複疊加
    try:
        client.delete_collection("esg_kb")
        print("  - 已清空舊有索引。")
    except:
        pass
    collection = client.create_collection("esg_kb")
    
    print("[3/4] 準備文本萃取與 Metadata 建構...")
    ids = []
    documents = []
    metadatas = []
    tokenized_corpus = []   # BM25 需要的斷詞庫
    
    for item in tqdm(data, desc="Text processing"):
        doc_id = str(item['id'])
        company = item['company']
        
        # 使用多模態抽取的 Markdown，若無則降級為原始純文字
        text_content = item.get('gemini_extracted_text', "")
        if not text_content:
            text_content = item.get('data', "")
            
        promise_str = item.get('promise_string', "")
        
        # 組合作為檢索基底的文本 (讓承諾和上下文都被涵蓋進去)
        full_text = f"承諾：{promise_str}\n\n報告內文：\n{text_content}"
        
        ids.append(doc_id)
        documents.append(full_text)
        
        # 關鍵防洩漏 Metadata (以供 $ne 語法過濾)
        metadatas.append({
            "id": item['id'],
            "company": company,
            "promise_status": item.get('promise_status', ''),
            "verification_timeline": item.get('verification_timeline', ''),
            "evidence_status": item.get('evidence_status', ''),
            "evidence_quality": item.get('evidence_quality', '')
        })
        
        # BM25的分詞 (使用 jieba 針對中文斷詞)
        tokens = jieba.lcut(full_text)
        tokenized_corpus.append(tokens)

    print("\n[4/4] 執行 BGE-M3 向量嵌入並寫入資料庫...")
    # 在 8GB VRAM 限制下，適當控制 batch_size 以防 OOM
    batch_size = 32
    
    for i in tqdm(range(0, len(ids), batch_size), desc="ChromaDB Embedding & Upsert"):
        batch_ids = ids[i:i+batch_size]
        batch_docs = documents[i:i+batch_size]
        batch_metas = metadatas[i:i+batch_size]
        
        # 動態轉化為向量 (自動調用 GPU 如果可用)
        batch_embeddings = encoder.encode(batch_docs, show_progress_bar=False).tolist()
        
        collection.add(
            ids=batch_ids,
            documents=batch_docs,
            metadatas=batch_metas,
            embeddings=batch_embeddings
        )
        
    print(f"  ► ChromaDB 建置成功！資料庫擁有 {collection.count()} 筆向量記錄。")
    
    print("\n同場加映：建構 BM25 稀疏矩陣 (Lexical Search) ...")
    bm25 = BM25Okapi(tokenized_corpus)
    
    # 儲存完整的 BM25 檢索需要對應的原始特徵庫
    bm25_store = {
        "bm25": bm25,
        "ids": ids,
        "tokenized_corpus": tokenized_corpus
    }
    
    with open(BM25_INDEX_PATH, "wb") as f:
        pickle.dump(bm25_store, f)
        
    print(f"  ► BM25 Index 已儲存至 {BM25_INDEX_PATH}。")
    print("\n[Done] 混合檢索 (Hybrid Indexing) 完成！")

if __name__ == "__main__":
    main()
