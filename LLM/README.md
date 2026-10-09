# ESG 承諾驗證：BERT＋RAG/LLM 核心程式

本資料夾整理專題系統的核心處理程式：PDF 抽文、正式輸入整理、BERT PS／ES 分類、相關案例檢索、LLM VT／EQ 判斷，以及結果一致性與信心分數輸出。

整理日期：2026-10-09。來源為專題目前使用的 `main_pipeline.py`、`rag_inference.py` 及其必要相依模組。這次僅整理原始碼並進行靜態核對，沒有執行訓練、推論、API 呼叫或評分，沒有新的執行成功或分數證據。

## 資料夾內容

```text
LLM/
├── README.md
├── requirements.txt
├── inference/
│   ├── main_pipeline.py
│   ├── rag_inference.py
│   ├── bert_thresholds.py
│   ├── eq_guideline_adjudicator.py
│   ├── esg_consistency.py
│   └── prediction_confidence.py
└── preparation/
    ├── pdf_gemini_parser.py
    ├── make_formal_input.py
    ├── rag_indexer.py
    ├── train_bert_fold_models.py
    └── week13_fold_utils.py
```

### inference：核心推論與輸出

| 檔案 | 用途 |
|---|---|
| `main_pipeline.py` | BERT 分別判斷承諾狀態 PS 與證據狀態 ES；呼叫 RAG/LLM 取得 VT／EQ；整合結果、套用一致性規則並輸出 JSON、CSV 與信心分數。 |
| `rag_inference.py` | BGE-M3／ChromaDB 向量檢索，BM25 補充；建立提示、呼叫 LLM、解析標籤與信心分數；SQLite 快取、重試與呼叫額度控制。 |
| `bert_thresholds.py` | 從原始模組節錄既有的門檻分類函式；未配置門檻時選擇最高機率類別。不包含門檻搜尋或校準 CLI。 |
| `eq_guideline_adjudicator.py` | 節錄既有證據品質規則與所需定義，供 RAG 流程使用；移除研究重播、評分與批次實驗 CLI。 |
| `esg_consistency.py` | 處理 PS／ES 與後續欄位間的邏輯一致性，例如非承諾資料的後續欄位使用 N/A。 |
| `prediction_confidence.py` | 信心分數範圍限制、格式正規化，以及 JSON／CSV 輸出。信心分數是模型／解析器訊號，不等同經校準的正確機率。 |

### preparation：前置處理與資源建置

| 檔案 | 用途 |
|---|---|
| `pdf_gemini_parser.py` | 下載已切割的單頁 PDF、轉成影像，使用多模態 LLM 抽取文字與 Markdown 表格，保存 SQLite 快取並產生含 `gemini_extracted_text` 的 JSON。既有實作讀取 PDF 第 0 頁，不是完整 PDF 的任意頁選取器。 |
| `make_formal_input.py` | 只保留允許的輸入欄位，移除答案與人工標註欄位。 |
| `rag_indexer.py` | 從訓練案例建立 BGE-M3／ChromaDB 與 jieba／BM25 索引。答案特徵開關固定關閉；訓練案例標籤可作為檢索範例的 metadata。 |
| `train_bert_fold_models.py` | 分別訓練 PS／ES 分類模型；模型選擇使用訓練資料內部 dev，不使用外部驗證／測試答案。 |
| `week13_fold_utils.py` | 訓練程式必要的分層內部 dev 切分工具；保留原名稱以維持匯入相容性。 |

## 核心資料流

PDF 抽文與正式輸入整理 → BERT PS／ES 分類 → RAG 取回訓練案例 → LLM VT／EQ 判斷 → 合併、標籤正規化與一致性檢查 → 預測與信心分數輸出。

PS 讀取原始 `data`；ES 讀取 `data` 與非重複的 PDF 抽取文字。RAG 查詢與 LLM 提示使用原始輸入及相關訓練案例。向量檢索優先，案例不足時使用 BM25 補充。

## 整理範圍與版本界線

- 推論入口只保留 BERT＋RAG/LLM 主路徑；移除舊 QLoRA 回退、煙霧測試捷徑、答案特徵分支、評分繪圖與 Codex 報告入口，以及重複初始化／寫檔敘述。
- 既有 BERT 推論、RAG、提示、解析、EQ 規則、一致性及信心分數的判斷邏輯未新增研究規則。RAG 原有提示相容分支仍保留；建議使用下表中的結構化輸出設定。
- 本資料夾展示專題核心，不包含後續競賽研究的多模型集成、selector、快取 action replay 或最後提交包組裝；不能單靠本資料夾宣稱重現最後一次競賽提交 CSV。
- 不包含資料集、模型權重、adapter、PDF、BM25 索引成品、ChromaDB／SQLite 快取、預測檔、圖表、報告、測試碼、日誌、AGENTS 文件或金鑰。

## 外部資源與設定

`requirements.txt` 列出原始碼引用的套件；版本未鎖定，本次未安裝或驗證套件相容性。Python 建議使用既有專題環境。BERT 模型權重、訓練資料、RAG 索引與 API 金鑰需另外準備，均不隨此資料夾上傳。

以下命令僅供使用說明，本次沒有執行：

```powershell
python -m pip install -r requirements.txt
python preparation/make_formal_input.py --input <增強輸入.json> --output <正式輸入.json>
python preparation/train_bert_fold_models.py --train <訓練資料.json> --output-root artifacts/bert
python preparation/rag_indexer.py
python inference/main_pipeline.py
```

從 `LLM` 資料夾執行時，下列資源路徑需指向實際外部檔案。各資料夾內必要的本地相依模組已一起保留。

| 環境變數 | 用途／建議值 |
|---|---|
| `INPUT_FILE` | `make_formal_input.py` 產生的正式輸入 JSON。 |
| `BERT_PS_MODEL_DIR` / `BERT_ES_MODEL_DIR` | PS／ES 模型目錄；缺少模型時入口會報錯。 |
| `BERT_THRESHOLD_FILE` | 既有模型門檻 JSON，可選；留空時使用最高機率。 |
| `RAG_INDEX_INPUT` / `RAG_INDEX_FALLBACK` | RAG 索引建置使用的訓練資料；驗證時必須只使用該 split 的 train。 |
| `RAG_CHROMA_DB_DIR` / `RAG_BM25_INDEX` | 建置與推論需使用同一組 ChromaDB／BM25 路徑。 |
| `GEMINI_API_KEY` | 只透過程序環境提供，勿寫入程式、README 或 Git。 |
| `GEMINI_MODEL_NAME` | 使用原專題環境中可用的模型名稱；本次未檢查 API 可用性。 |
| `RAG_STRUCTURED_OUTPUT` | 建議 `1`，使用既有結構化提示與輸出。 |
| `GEMINI_MAX_OUTPUT_TOKENS` | 既有 Week15 配置使用 `1200`。 |
| `GEMINI_MIN_INTERVAL_SECONDS` | 既有配置使用 `4.2`。 |
| `RAG_REQUIRE_COMPLETE` | 建議 `1`，快取缺少結果時報錯。 |
| `ENABLE_VT_EQ_POSTPROCESS` | 預設 `0`；是否啟用既有規則應沿用所選原始執行配置。 |
| `OUTPUT_FILE` / `OUTPUT_CSV` | 預測 JSON／CSV 路徑；輸出父目錄需事先存在。 |
| `WRITE_CONFIDENCE_OUTPUT` | 預設 `1`，另輸出四欄信心分數。 |
| `PDF_INPUT_JSON` / `PDF_OUTPUT_JSON` / `PDF_CACHE_DB` | PDF 前置抽文的輸入、增強 JSON 與快取路徑。 |

推論輸入只使用 `id`、`data`、`URL`／`pdf_url`、`page_number` 與可重現的 `gemini_extracted_text`。推論入口不讀取 `TRUTH_FILE`，也不執行答案評分；訓練資料標籤僅用於模型訓練與建立訓練案例庫。

CSV 標準欄位為 `id,promise_status,verification_timeline,evidence_status,evidence_quality`；信心分數版本另含四個對應的 `*_confidence` 欄位。舊時間標籤 `longer_than_5_years` 正規化為 `more_than_5_years`，不適用欄位輸出 `N/A`。
