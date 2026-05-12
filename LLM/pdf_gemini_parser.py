import os
import json
import sqlite3
import time
import requests
import fitz  # PyMuPDF (需要安裝: pip install PyMuPDF)
from io import BytesIO
from PIL import Image
import google.generativeai as genai
from tqdm import tqdm

# 設定常數
DB_NAME = "pdf_cache.db"
INPUT_JSON = "vpesg4k_train_1000.json"
OUTPUT_JSON = "vpesg4k_train_1000_enhanced.json"

# 從環境變數讀取 Gemini API Key
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY", "")
if not GEMINI_API_KEY:
    print("錯誤: 找不到 GEMINI_API_KEY 環境變數。")
    import sys
    sys.exit(1)

genai.configure(api_key=GEMINI_API_KEY)

# 採用 Google AI Studio 模型
MODEL_NAME = "gemma-4-31b-it"

def setup_db():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    # 建立快取資料表
    c.execute('''
        CREATE TABLE IF NOT EXISTS processed_pdfs (
            id INTEGER PRIMARY KEY,
            extracted_text TEXT,
            status TEXT
        )
    ''')
    conn.commit()
    return conn

def download_pdf_page_as_image(pdf_url):
    """從 URL 下載單頁 PDF 並轉為高解析度圖片 (PIL Image)"""
    response = requests.get(pdf_url, timeout=30)
    response.raise_for_status()
    
    # 使用 PyMuPDF (fitz) 開啟 PDF byte stream
    pdf_document = fitz.open(stream=response.content, filetype="pdf")
    
    # 由於 URL 提供的是切割好的單頁 PDF (例如 _page_48.pdf)，直接取第 0 頁
    page = pdf_document[0] 
    
    # 轉換為影像 (設定放大矩陣以提高 OCR 解析度)
    pix = page.get_pixmap(matrix=fitz.Matrix(2, 2))
    img_bytes = pix.tobytes("png")
    
    img = Image.open(BytesIO(img_bytes))
    return img

def process_record(record, conn):
    record_id = record.get('id', 'N/A')
    pdf_url = record.get('pdf_url', '')
    promise_string = record.get('promise_string', '')
    
    if not pdf_url:
        tqdm.write(f"ID {record_id} 遺漏 pdf_url，跳過萃取。")
        return
        
    c = conn.cursor()
    # 檢查是否已經成功處理過
    c.execute('SELECT status FROM processed_pdfs WHERE id = ?', (record_id,))
    row = c.fetchone()
    if row and row[0] == 'COMPLETED':
        return  # 直接跳過
        
    try:
        # 下載及轉換圖片
        img = download_pdf_page_as_image(pdf_url)
        
        # 準備多模態 Prompt
        prompt = f"""
你現在是一個專業的 ESG 永續報告分析助理。這是一張來自企業 ESG 報告書的掃描頁面。
請你將圖片中的文字完整提取出來。若是遭遇到「表格形式」的數據，請務必將其精準轉換為 Markdown Format 的表格來保留結構。

此外，由於這份報告跟以下承諾有關聯：
「{promise_string}」
請在提取過程中，保持該承諾的段落及其上下文的精準語意。

請直接輸出提取與整理後的 Markdown 文本，不要加入任何額外的問候語。
"""

        model = genai.GenerativeModel(MODEL_NAME)
        
        # 加入重試機制與超時設定
        max_retries = 3
        extracted_text = ""
        for attempt in range(max_retries):
            try:
                response = model.generate_content(
                    [prompt, img],
                    request_options={"timeout": 600}
                )
                extracted_text = response.text
                break
            except Exception as e:
                if attempt < max_retries - 1:
                    tqdm.write(f"ID {record_id} 請求超時或失敗 (嘗試 {attempt+1})，10秒後重試... ({e})")
                    time.sleep(10)
                else:
                    raise e

        # 成功後寫入 SQLite 保存
        c.execute('''
            INSERT OR REPLACE INTO processed_pdfs (id, extracted_text, status)
            VALUES (?, ?, ?)
        ''', (record_id, extracted_text, 'COMPLETED'))
        conn.commit()
            
    except Exception as e:
        tqdm.write(f"ID {record_id} 發生錯誤: {e}")
        c.execute('''
            INSERT OR REPLACE INTO processed_pdfs (id, extracted_text, status)
            VALUES (?, ?, ?)
        ''', (record_id, str(e), 'FAILED'))
        conn.commit()
    finally:
        # Gemma 4 每分鐘最多 15 次免費請求
        time.sleep(4)

def build_enhanced_json(conn):
    """將 SQLite 中的結果與原本的 JSON 合併，產出富含 Markdown 格式的新備份"""
    with open(INPUT_JSON, "r", encoding="utf-8") as f:
        data = json.load(f)
        
    c = conn.cursor()
    for record in data:
        c.execute('SELECT extracted_text, status FROM processed_pdfs WHERE id = ?', (record['id'],))
        row = c.fetchone()
        if row and row[1] == 'COMPLETED':
            record['gemini_extracted_text'] = row[0]
        else:
            record['gemini_extracted_text'] = record.get('data', '')
            
    with open(OUTPUT_JSON, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def main():
    print("啟動【格式感知】多模態 PDF 轉換管線 (Gemini API)...")
    print("必備套件: pip install requests PyMuPDF pillow google-generativeai tqdm\n")
    
    if not os.path.exists(INPUT_JSON):
        print(f"找不到檔案 {INPUT_JSON}，請確認檔案位置。")
        return
        
    conn = setup_db()
    
    with open(INPUT_JSON, "r", encoding="utf-8") as f:
        data = json.load(f)
        
    limit = len(data)
    if not GEMINI_API_KEY:
        print("Note: No API Key provided.")
        
    for record in tqdm(data[:limit], desc="處理 PDF 進度"):
        process_record(record, conn)
        
    build_enhanced_json(conn)
    
    print("\n✅ 資料集增強完畢！產出檔案: " + OUTPUT_JSON)
    print("Done! You can interrupt and restart anytime thanks to SQLite checkpointing.")
    conn.close()

if __name__ == "__main__":
    main()
