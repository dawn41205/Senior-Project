# ESG Promise Verification — 完整管線專案

## 📋 專案概述

本專案為 **VeriPromiseESG 2026** 競賽的完整管線，需預測四個欄位：

| 欄位 | 說明 | 類別 | 負責模組 | 權重 |
|------|------|------|----------|------|
| `promise_status` (PS) | 是否有承諾 | Yes / No | **BERT 分類器** | 0.20 |
| `verification_timeline` (VT) | 承諾時程 | already / within_2_years / between_2_and_5_years / longer_than_5_years / N/A | **RAG + LLM** | 0.15 |
| `evidence_status` (ES) | 是否有證據 | Yes / No / N/A | **BERT 分類器** | 0.30 |
| `evidence_quality` (EQ) | 證據品質 | Clear / Not Clear / Misleading / N/A | **RAG + LLM** | 0.35 |

**最終評分公式**：`0.2×PS + 0.15×VT + 0.3×ES + 0.35×EQ` (Weighted Macro F1)

---

## 🗂 檔案說明

### 資料檔案

| 檔案 | 說明 |
|------|------|
| `vpesg4k_train_1000.json` | 競賽原始資料集，1000 筆 ESG 報告段落，每筆包含 `data`（內文）、`promise_string`（承諾字串）、四個標籤欄位、`pdf_url` 等 |
| `vpesg4k_train_1000_enhanced.json` | 增強版資料集。在原始資料的基礎上，每筆多了一個 `gemini_extracted_text` 欄位，這是用 Gemini API 對 PDF 頁面「看圖轉文字」的結果（包含表格 Markdown 格式），比原始 `data` 欄位內容更豐富精準。**RAG 索引就是用這個欄位建的** |

### 預建 RAG 資源（不需重建，直接使用）

| 檔案 | 說明 |
|------|------|
| `chroma_db/` | ChromaDB 向量資料庫。使用 `BAAI/bge-m3` 模型對全部 1000 筆資料做向量嵌入，供 RAG 檢索時做「語意搜尋」（找意思最接近的段落） |
| `bm25_index.pkl` | BM25 關鍵字索引。使用 jieba 中文斷詞後建立的稀疏矩陣，供 RAG 檢索時做「關鍵字搜尋」（找包含相同詞彙的段落）。與 `chroma_db` 搭配使用，兩者合稱「混合檢索」 |

### 程式碼

| 檔案 | 說明 |
|------|------|
| `data_splitter.py` | 資料切分腳本。將 1000 筆切成 800 訓練 + 200 測試，使用 `train_test_split(test_size=0.2, random_state=42)`，與官方 baseline 完全一致 |
| `train_bert_dual.py` | **BERT 訓練腳本**。使用 `ckiplab/bert-base-chinese` 全量微調，同時訓練 PS 和 ES 兩個分類器。內建 WeightedTrainer 處理類別不平衡、斷點續訓等功能 |
| `main_pipeline.py` | **主管線**。整合 BERT (PS+ES) 與 RAG (VT+EQ) 的推論結果，套用後處理防呆規則，計算最終加權 F1 分數，並產出 `prediction.json` 提交檔 |
| `rag_inference.py` | **RAG 推論模組**。負責 VT 和 EQ 兩個欄位。流程：混合檢索相似段落 → 組裝 Prompt → 呼叫 Gemma-4-31b-it API → 解析回應。內建 SQLite 斷點保護，中斷後可續跑 |
| `rag_indexer.py` | **RAG 知識庫建置腳本**。讀取增強版資料集，用 BGE-M3 做向量嵌入存入 ChromaDB，同時用 jieba 斷詞建立 BM25 索引。**已預先跑過，一般不需要重跑**，除非你修改了資料集 |
| `pdf_gemini_parser.py` | **PDF 萃取腳本**。從每筆資料的 `pdf_url` 下載 PDF 頁面，用 Gemini 多模態 API 辨識圖片中的文字（含表格），產出 `vpesg4k_train_1000_enhanced.json`。**已預先跑過，一般不需要重跑** |

---

## 🚀 執行步驟

### Step 0: 安裝依賴
```bash
pip install transformers datasets scikit-learn torch pandas
pip install chromadb sentence-transformers rank_bm25 jieba
pip install google-generativeai peft matplotlib
```

### Step 1: 切分資料集
```bash
python data_splitter.py
```
產生 `train_grouped.json` (800 筆) 和 `val_grouped.json` (200 筆)。

### Step 2: 訓練 BERT 分類器 (PS + ES)
```bash
python train_bert_dual.py
```
- 產生 `./bert_ps_model/` 和 `./bert_es_model/`
- 約需 5-6 分鐘 (RTX 4060)

### Step 3: 設定 Gemini API Key
```bash
# Windows PowerShell
$env:GEMINI_API_KEY = "你的API_KEY"

# Linux / Mac
export GEMINI_API_KEY="你的API_KEY"
```
申請位置：https://aistudio.google.com/apikey （免費版即可）

### Step 4: 執行完整管線
```bash
python main_pipeline.py
```
流程：
1. BERT 推論 PS → 約 2 秒
2. BERT 推論 ES → 約 2 秒
3. RAG + Gemma-4-31b-it 推論 VT/EQ → 約 40-60 分鐘（免費 API 有限速）
4. 合併結果 + 後處理規則 + 計算加權 F1

產出：
- `prediction.json` — 最終預測結果（提交用）
- `reasoning_log.json` — LLM 推理過程記錄
- `f1_scores_comparison.png` — 與 Baseline 的對比圖

---

## ⚠️ 重要技術筆記

### 1. PS 模型的 Data Leakage 陷阱
> **promise_string 有值 ↔ promise_status=Yes，是 100% 一對一映射！**

- PS 訓練/推論時**只能看 `data` 內文**，絕對禁止輸入 `promise_string`
- 如果輸入 promise_string，會達到 100% 準確率，但在比賽隱藏測試集上會崩盤
- `train_bert_dual.py` 第 84 行和 `main_pipeline.py` 第 122 行已有防護邏輯

### 2. ES 模型可以使用 promise_string
- ES 的任務是判斷「承諾是否有被執行」，需要同時看承諾內容和報告內文
- 輸入格式：`"承諾：{promise_string}\n\n報告內容：{data}"`
- N/A 類別的 promise_string 全為空 → BERT 自然學到此規律，這是合法的

### 3. ES 的 class_weight 設定
- `No` 類別只有約 18% 的樣本量，使用 balanced 公式只給 ~2.7x 不夠
- 手動設了 `weight=8.0` 來加強 No 的召回率（目前約 57%）
- 你可以調整此數值觀察效果

### 4. 後處理防呆規則（main_pipeline.py 第 221-230 行）
```
如果 PS == No → VT、ES、EQ 全部強制設為 N/A
如果 ES == No → EQ 強制設為 N/A
```
這是基於任務邏輯的硬規則，不論模型怎麼預測都會被覆蓋。

### 5. RAG 斷點續跑機制
- 推論結果即時存入 `inference_cache.db`（SQLite）
- 中途斷線只需重跑 `main_pipeline.py`，會自動跳過已完成的筆數
- 如需全部重新推論，刪除 `inference_cache.db` 即可

### 6. RAG 知識庫重建
- `chroma_db/` + `bm25_index.pkl` 已預先建好，可直接使用
- 若修改了資料集或想重建：`python rag_indexer.py`
- 索引使用的 Embedding 模型是 `BAAI/bge-m3`


## 🔧 比賽正式提交前
1. 將 `data_splitter.py` 中的 `test_size` 改為 `0`，使用全部 1000 筆做訓練
2. 重跑 `train_bert_dual.py` 全量訓練
3. 用比賽提供的隱藏測試集替換 `val_grouped.json`
4. 刪除 `inference_cache.db` 後重跑 `main_pipeline.py`
