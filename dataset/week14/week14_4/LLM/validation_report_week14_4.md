# Validation Evidence Report

- Generated: 2026-06-02 06:43:40
- Prediction file: `E:\project\test510\week14_runs\week14_4\LLM_pipeline_pred_week14_4.json`
- Truth file: `E:\project\test510\dataset\week14\week14_4\val_grouped.json`
- Input file: `E:\project\test510\week14_runs\week14_4\val_formal_input.json`
- Prediction rows: 200
- Truth rows: 200
- Weighted score: `0.507873`

## Score Summary

| Field | Weight | Macro F1 | Weighted component | Truth distribution | Prediction distribution |
|---|---:|---:|---:|---|---|
| promise_status | 0.20 | 0.857069 | 0.171414 | Yes=159, No=41 | Yes=137, No=63 |
| verification_timeline | 0.15 | 0.317885 | 0.047683 | already=72, between_2_and_5_years=42, more_than_5_years=42, N/A=41, within_2_years=3 | N/A=132, between_2_and_5_years=51, more_than_5_years=14, within_2_years=2, already=1 |
| evidence_status | 0.30 | 0.699279 | 0.209784 | Yes=133, N/A=41, No=26 | Yes=123, N/A=63, No=14 |
| evidence_quality | 0.35 | 0.225694 | 0.078993 | Clear=108, N/A=67, Not Clear=25 | N/A=157, Clear=18, Not Clear=17, Misleading=8 |

## promise_status

### Per-Label Metrics

| Label | Precision | Recall | F1 | Support |
|---|---:|---:|---:|---:|
| Yes | 1.000000 | 0.861635 | 0.925676 | 159 |
| No | 0.650794 | 1.000000 | 0.788462 | 41 |

### Confusion Matrix

Rows are truth labels; columns are predicted labels.

| Truth \ Pred | Yes | No |
|---|---:|---:|
| Yes | 137 | 22 |
| No | 0 | 41 |

### Largest Gaps

- `Yes` -> `No`: 22 rows

### Example Mismatches

- ID `10077` true=`Yes` pred=`No` text=`本公司之風險管理範疇包含壽險、銀行、證券、投信、創投、資產管理等業種別，我們依循主管機關規範、國內外金融業風險管理實務與本公司風險管理政策，參酌經營業務與環境所需，建立相應之風險管理規範作為風險管理之依據，採用適當技術予以衡量各項風險，並評估潛在損失與關聯性。另因應氣候變遷風險，亦建立辨識及評估機制，並定期執行情境分析，據以評估對本公司整體營運與業務之財務影響。 Professional ESG Sustainability Re...`
- ID `10112` true=`Yes` pred=`No` text=`奇鋐重視員工意見表達與交流，設立完善的內部溝通管道。員工可透過公司網站了解政策宣示、產品資訊、營運狀況與變化、重大資訊、人才招募等，亦可透過電子信箱、廠區公佈欄，瞭解公司政策與營運狀況。公司目前在台灣有成立勞資會議、職工福利委員會，大陸廠皆成立職工代表大會，而越南廠區則有工會組織。勞資會議與職工代表大會和工會成員包括基層員工，公司定期舉行會議，與員工溝通協調公司的政策和管理事務，並對員工反映的公司管理、生活等方面的問題進行回覆解答...`
- ID `10113` true=`Yes` pred=`No` text=`我們深知永續議題的管理，是企業持續改善與長遠發展的關鍵。其包含企業面對議題如何整合內部資源擬定相關管理方針與各階段利害關係人的議合溝通。本公司透過多元管道蒐集相關回覆和建議，將其納入公司營運規劃中。 Professional ESG Sustainability Report Analysis Assistant. Extract text from a scanned image of an ESG report. Conver...`
- ID `10121` true=`Yes` pred=`No` text=`統一企業高度重視稅務治理，我們嚴格遵守所有稅務法規，並制定了具體的「稅務政策」和相關的稅務管理責任，以確保誠實申報納稅、評估和應對稅務風險、保持開放和誠實的溝通，以及提供資訊透明度。近三年支付之所得稅費用如下，另外，稅務政策可於公司網站 ( 公司政策項下之稅務政策 ) 下載 https://www.uni-president.com.tw/index.asp Professional ESG Sustainability Repo...`
- ID `10134` true=`Yes` pred=`No` text=`自 2024 年 3 月起於「給付預告通知」亦列示簡訊代表門號及簡訊中連結短網址之提醒文字，以利保戶辨識是否為公司的來電或發出的簡訊。另響應政府的政策，本公司率壽險業之先導入短碼簡訊，「68999」的商用簡碼讓保戶能識別真偽，有助於減少偽冒企業名義的詐騙簡訊橫行，降低財務損失的風險。 Professional ESG Sustainability Report Analysis Assistant. Extract text fr...`
- ID `10146` true=`Yes` pred=`No` text=`我們遵循保證作業的國際最佳實務，包括國際審計與保證標準委員會頒布的《國際保證作業標準》（ISAE）3000（修訂版）—非屬歷史財務資訊審計與核閱的保證作業》，執行了數據保證查驗作業。為確保保證程序的一致性，我們依據 DNV 的保證方法學 VeriSustain 執行工作，僅應用與本次活動特定目的的相關的部分。此方法學確保遵循倫理要求，並要求規劃與執行保證作業以達到預期保證等級。 Professional ESG Sustainab...`
- ID `10170` true=`Yes` pred=`No` text=`### 創新思維、整合研發、降低風險 台塑石化各廠皆設有專責之製程改善部門，編制專業化工技術人員從事製程改善之研究工作，針對穩定生產、提高產量、降低成本、增加產值、降低能源耗用及減少污染排放等項目研發改善技術，降低營運風險。 Professional ESG Sustainability Report Analysis Assistant. Extract all text from the provided scanned im...`
- ID `10244` true=`Yes` pred=`No` text=`導入產品永續性及生產 a. 減少材料使用 b. 採用回收材料 c. 模組化設計 d. 最佳運輸材積設計 e. 綠色生產製造 Professional ESG Sustainability Report Analysis Assistant. Extract text from a scanned image of a corporate ESG report. * Full text extraction. * Tables mu...`

## verification_timeline

### Per-Label Metrics

| Label | Precision | Recall | F1 | Support |
|---|---:|---:|---:|---:|
| already | 0.000000 | 0.000000 | 0.000000 | 72 |
| within_2_years | 0.500000 | 0.333333 | 0.400000 | 3 |
| between_2_and_5_years | 0.294118 | 0.357143 | 0.322581 | 42 |
| more_than_5_years | 0.785714 | 0.261905 | 0.392857 | 42 |
| N/A | 0.310606 | 1.000000 | 0.473988 | 41 |

### Confusion Matrix

Rows are truth labels; columns are predicted labels.

| Truth \ Pred | already | within_2_years | between_2_and_5_years | more_than_5_years | N/A |
|---|---:|---:|---:|---:|---:|
| already | 0 | 1 | 31 | 3 | 37 |
| within_2_years | 1 | 1 | 0 | 0 | 1 |
| between_2_and_5_years | 0 | 0 | 15 | 0 | 27 |
| more_than_5_years | 0 | 0 | 5 | 11 | 26 |
| N/A | 0 | 0 | 0 | 0 | 41 |

### Largest Gaps

- `already` -> `N/A`: 37 rows
- `already` -> `between_2_and_5_years`: 31 rows
- `between_2_and_5_years` -> `N/A`: 27 rows
- `more_than_5_years` -> `N/A`: 26 rows
- `more_than_5_years` -> `between_2_and_5_years`: 5 rows
- `already` -> `more_than_5_years`: 3 rows
- `within_2_years` -> `N/A`: 1 rows
- `already` -> `within_2_years`: 1 rows

### Example Mismatches

- ID `10004` true=`already` pred=`N/A` text=`面對這些全球與國內政策的推動，富邦人壽秉持永續經營理念，積極透過永續金融的投資力量，引導被投資公司與企業進行永續轉型，除非資金明確用於綠能轉型計畫，不再新增投資燃煤比重超過 50% 的電廠。同時，針對燃料煤開採、運輸業、燃料煤發電及非典型油氣產業，制定嚴格的准入與撤資標準，積極引導資金流向低碳與可再生能源領域，展現對環境永續的堅定承諾，並連續 4 年榮獲「台灣永續投資典範機構獎 – 機構影響力 (壽險組)」殊榮，在責任投資與推動企...`
- ID `10063` true=`already` pred=`N/A` text=`第一銀行持續提升身心障礙及外籍客戶使用ATM之便利性，2024年底全台共計543台ATM符合輪椅客戶使用，其中符合無障礙環境(如坡道等)之ATM有523台(含容膝ATM5台)，又有232台為提供視障民眾使用之語音ATM，並已新增存款功能，視障民眾可透過耳機插座插入耳機，進入無障礙語音模式，各項操作位置設有點字說明，供其觸覺清楚辨識，並藉由語音引導視障民眾按步驟操作，讓視障民眾不借助他人即可自行操作ATM完成所需交易或查詢；2023...`
- ID `10065` true=`already` pred=`N/A` text=`台積公司藉由 TDDM 方法學，每年依照不同的調查目的，執行重大議題的盤點與分析，形塑一個完整的調查週期。首年進行議題蒐集、調查與分析，重新定義具重大性的永續議題，並於次一年度檢視重大議題的變化，探討重大議題之間的因果關係，進而掌握重大議題與行動方案間的相互關聯，確保行動有效性。民國 112 年，台積公司邀請 1,693 位內外部利害關係人，以及超過 233 位負責推動永續業務的公司主管及同仁綜合考量利害關係人關注、組織營運衝擊與...`
- ID `10077` true=`already` pred=`N/A` text=`本公司之風險管理範疇包含壽險、銀行、證券、投信、創投、資產管理等業種別，我們依循主管機關規範、國內外金融業風險管理實務與本公司風險管理政策，參酌經營業務與環境所需，建立相應之風險管理規範作為風險管理之依據，採用適當技術予以衡量各項風險，並評估潛在損失與關聯性。另因應氣候變遷風險，亦建立辨識及評估機制，並定期執行情境分析，據以評估對本公司整體營運與業務之財務影響。 Professional ESG Sustainability Re...`
- ID `10102` true=`already` pred=`N/A` text=`為增進管理階層及一般員工在洗錢防制及打擊資恐方面之觀念，2024 年度金控董事在公司治理課程亦持續納入防制洗錢及打擊資恐教育訓練，針對集團洗錢防制專責主管 / 人員亦投入相當之教育訓練，總教育訓練時數達 647 小時；此外集團對金控及銀行、人壽、證券、投信、投顧、期貨、融資租賃等子公司之員工所提供之教育訓練方式，包含實體、線上 e-learning 及外部教育訓練課程，合計教育訓練時數為 41,571.44 小時，參加之員工人次為...`
- ID `10121` true=`already` pred=`N/A` text=`統一企業高度重視稅務治理，我們嚴格遵守所有稅務法規，並制定了具體的「稅務政策」和相關的稅務管理責任，以確保誠實申報納稅、評估和應對稅務風險、保持開放和誠實的溝通，以及提供資訊透明度。近三年支付之所得稅費用如下，另外，稅務政策可於公司網站 ( 公司政策項下之稅務政策 ) 下載 https://www.uni-president.com.tw/index.asp Professional ESG Sustainability Repo...`
- ID `10134` true=`already` pred=`N/A` text=`自 2024 年 3 月起於「給付預告通知」亦列示簡訊代表門號及簡訊中連結短網址之提醒文字，以利保戶辨識是否為公司的來電或發出的簡訊。另響應政府的政策，本公司率壽險業之先導入短碼簡訊，「68999」的商用簡碼讓保戶能識別真偽，有助於減少偽冒企業名義的詐騙簡訊橫行，降低財務損失的風險。 Professional ESG Sustainability Report Analysis Assistant. Extract text fr...`
- ID `10170` true=`already` pred=`N/A` text=`### 創新思維、整合研發、降低風險 台塑石化各廠皆設有專責之製程改善部門，編制專業化工技術人員從事製程改善之研究工作，針對穩定生產、提高產量、降低成本、增加產值、降低能源耗用及減少污染排放等項目研發改善技術，降低營運風險。 Professional ESG Sustainability Report Analysis Assistant. Extract all text from the provided scanned im...`

## evidence_status

### Per-Label Metrics

| Label | Precision | Recall | F1 | Support |
|---|---:|---:|---:|---:|
| Yes | 0.894309 | 0.827068 | 0.859375 | 133 |
| No | 0.642857 | 0.346154 | 0.450000 | 26 |
| N/A | 0.650794 | 1.000000 | 0.788462 | 41 |

### Confusion Matrix

Rows are truth labels; columns are predicted labels.

| Truth \ Pred | Yes | No | N/A |
|---|---:|---:|---:|
| Yes | 110 | 5 | 18 |
| No | 13 | 9 | 4 |
| N/A | 0 | 0 | 41 |

### Largest Gaps

- `Yes` -> `N/A`: 18 rows
- `No` -> `Yes`: 13 rows
- `Yes` -> `No`: 5 rows
- `No` -> `N/A`: 4 rows

### Example Mismatches

- ID `10077` true=`Yes` pred=`N/A` text=`本公司之風險管理範疇包含壽險、銀行、證券、投信、創投、資產管理等業種別，我們依循主管機關規範、國內外金融業風險管理實務與本公司風險管理政策，參酌經營業務與環境所需，建立相應之風險管理規範作為風險管理之依據，採用適當技術予以衡量各項風險，並評估潛在損失與關聯性。另因應氣候變遷風險，亦建立辨識及評估機制，並定期執行情境分析，據以評估對本公司整體營運與業務之財務影響。 Professional ESG Sustainability Re...`
- ID `10112` true=`Yes` pred=`N/A` text=`奇鋐重視員工意見表達與交流，設立完善的內部溝通管道。員工可透過公司網站了解政策宣示、產品資訊、營運狀況與變化、重大資訊、人才招募等，亦可透過電子信箱、廠區公佈欄，瞭解公司政策與營運狀況。公司目前在台灣有成立勞資會議、職工福利委員會，大陸廠皆成立職工代表大會，而越南廠區則有工會組織。勞資會議與職工代表大會和工會成員包括基層員工，公司定期舉行會議，與員工溝通協調公司的政策和管理事務，並對員工反映的公司管理、生活等方面的問題進行回覆解答...`
- ID `10121` true=`Yes` pred=`N/A` text=`統一企業高度重視稅務治理，我們嚴格遵守所有稅務法規，並制定了具體的「稅務政策」和相關的稅務管理責任，以確保誠實申報納稅、評估和應對稅務風險、保持開放和誠實的溝通，以及提供資訊透明度。近三年支付之所得稅費用如下，另外，稅務政策可於公司網站 ( 公司政策項下之稅務政策 ) 下載 https://www.uni-president.com.tw/index.asp Professional ESG Sustainability Repo...`
- ID `10134` true=`Yes` pred=`N/A` text=`自 2024 年 3 月起於「給付預告通知」亦列示簡訊代表門號及簡訊中連結短網址之提醒文字，以利保戶辨識是否為公司的來電或發出的簡訊。另響應政府的政策，本公司率壽險業之先導入短碼簡訊，「68999」的商用簡碼讓保戶能識別真偽，有助於減少偽冒企業名義的詐騙簡訊橫行，降低財務損失的風險。 Professional ESG Sustainability Report Analysis Assistant. Extract text fr...`
- ID `10146` true=`Yes` pred=`N/A` text=`我們遵循保證作業的國際最佳實務，包括國際審計與保證標準委員會頒布的《國際保證作業標準》（ISAE）3000（修訂版）—非屬歷史財務資訊審計與核閱的保證作業》，執行了數據保證查驗作業。為確保保證程序的一致性，我們依據 DNV 的保證方法學 VeriSustain 執行工作，僅應用與本次活動特定目的的相關的部分。此方法學確保遵循倫理要求，並要求規劃與執行保證作業以達到預期保證等級。 Professional ESG Sustainab...`
- ID `10170` true=`Yes` pred=`N/A` text=`### 創新思維、整合研發、降低風險 台塑石化各廠皆設有專責之製程改善部門，編制專業化工技術人員從事製程改善之研究工作，針對穩定生產、提高產量、降低成本、增加產值、降低能源耗用及減少污染排放等項目研發改善技術，降低營運風險。 Professional ESG Sustainability Report Analysis Assistant. Extract all text from the provided scanned im...`
- ID `10244` true=`Yes` pred=`N/A` text=`導入產品永續性及生產 a. 減少材料使用 b. 採用回收材料 c. 模組化設計 d. 最佳運輸材積設計 e. 綠色生產製造 Professional ESG Sustainability Report Analysis Assistant. Extract text from a scanned image of a corporate ESG report. * Full text extraction. * Tables mu...`
- ID `10287` true=`Yes` pred=`N/A` text=`### 低碳原物料的開發 CCL 產業減少碳足跡的方案中，除了節能與使用再生能源外，進行綠色產品配方設計來降低產品碳足跡是未來開發 CCL 產品的趨勢。高分子樹脂與功能性填料是 CCL 產品配方中的關鍵材料，選用低碳樹脂與回收再生填料是降低產品碳足跡的有效方案。在低碳樹脂方面，我們在配方設計上採用數種生質基環氧樹脂取代石化基環氧樹脂來達到產品配方低碳的目的。 Professional ESG Sustainability Repo...`

## evidence_quality

### Per-Label Metrics

| Label | Precision | Recall | F1 | Support |
|---|---:|---:|---:|---:|
| Clear | 0.722222 | 0.120370 | 0.206349 | 108 |
| Not Clear | 0.176471 | 0.120000 | 0.142857 | 25 |
| Misleading | 0.000000 | 0.000000 | 0.000000 | 0 |
| N/A | 0.394904 | 0.925373 | 0.553571 | 67 |

### Confusion Matrix

Rows are truth labels; columns are predicted labels.

| Truth \ Pred | Clear | Not Clear | Misleading | N/A |
|---|---:|---:|---:|---:|
| Clear | 13 | 14 | 5 | 76 |
| Not Clear | 2 | 3 | 1 | 19 |
| Misleading | 0 | 0 | 0 | 0 |
| N/A | 3 | 0 | 2 | 62 |

### Largest Gaps

- `Clear` -> `N/A`: 76 rows
- `Not Clear` -> `N/A`: 19 rows
- `Clear` -> `Not Clear`: 14 rows
- `Clear` -> `Misleading`: 5 rows
- `N/A` -> `Clear`: 3 rows
- `N/A` -> `Misleading`: 2 rows
- `Not Clear` -> `Clear`: 2 rows
- `Not Clear` -> `Misleading`: 1 rows

### Example Mismatches

- ID `10004` true=`Clear` pred=`N/A` text=`面對這些全球與國內政策的推動，富邦人壽秉持永續經營理念，積極透過永續金融的投資力量，引導被投資公司與企業進行永續轉型，除非資金明確用於綠能轉型計畫，不再新增投資燃煤比重超過 50% 的電廠。同時，針對燃料煤開採、運輸業、燃料煤發電及非典型油氣產業，制定嚴格的准入與撤資標準，積極引導資金流向低碳與可再生能源領域，展現對環境永續的堅定承諾，並連續 4 年榮獲「台灣永續投資典範機構獎 – 機構影響力 (壽險組)」殊榮，在責任投資與推動企...`
- ID `10005` true=`Clear` pred=`N/A` text=`關注人才關鍵議題，新加坡亞洲新聞臺（CNA）特別製作專題《Taiwan’s tech industry taps female talent pool amid labour shortage》，在報導中聚焦基金會所舉辦的 Girls! TECH Action 科技女孩工作坊，探討企業如何透過教育計畫來翻轉科技產業中的性別失衡，有效地減少女性在 STEM 領域的管漏現象，並鼓勵更多國高中女生投入 STEM（科學、技術、工程與數學）...`
- ID `10031` true=`Clear` pred=`N/A` text=`近年全球暖化造成各地環境災害，國巨股份有限公司了解溫室氣體的排放將對環境造成傷害，基於關心生活，貢獻社會的精神，完成系統化的溫室氣體排放盤查與清冊建置，並制定內部文件化及查證程序等。期盼能達成能源節約、工業減廢、資源回收與再利用目標，共同為國內產業未來朝向低碳型經濟社會來努力。為有效管理本公司能源使用情況，防止浪費資源能源，並適時謀求提升使用效率，各廠均配合政府節能規定設定每年節電率 1%以上之目標，台灣廠區與中國廠區已於每年接受...`
- ID `10034` true=`Clear` pred=`N/A` text=`智邦科技所屬之網路通訊產業並非直接高度仰賴自然資源的產業，但鑑於生物多樣性流失風險已僅次於氣候風險，故響應聯合國「昆明 - 蒙特婁全球生物多樣性框架（GBF）」之「行動目標 15：企業責任」，參考「自然相關財務揭露計畫（The Taskforce on Nature-related Financial Disclosures, TNFD）」，以「LEAP」方法學，逐步盤點重要營運據點與生態系統服務之關聯。2024 年亦從自身做起，...`
- ID `10039` true=`Clear` pred=`N/A` text=`聯電集團除持續提升能源效率外，亦規劃多元能源使用，積極設置廠內再生能源，更將太陽能系統列為新建廠房標準設計建置項目，發電量連續 5 年增長。2024 年原規劃設置太陽光電 500kW 計畫調整，整併於 2025 年設置合計約 900kW。至 2024 年止，聯電集團已安裝峰值發電容量超過 14,000 瓩 (kWp) 之太陽光電系統，預估每年發電量達 15,000 MWh。惟太陽光電主要受氣候等因素影響，例如 2024 年台灣地區...`
- ID `10063` true=`Clear` pred=`N/A` text=`第一銀行持續提升身心障礙及外籍客戶使用ATM之便利性，2024年底全台共計543台ATM符合輪椅客戶使用，其中符合無障礙環境(如坡道等)之ATM有523台(含容膝ATM5台)，又有232台為提供視障民眾使用之語音ATM，並已新增存款功能，視障民眾可透過耳機插座插入耳機，進入無障礙語音模式，各項操作位置設有點字說明，供其觸覺清楚辨識，並藉由語音引導視障民眾按步驟操作，讓視障民眾不借助他人即可自行操作ATM完成所需交易或查詢；2023...`
- ID `10065` true=`Clear` pred=`N/A` text=`台積公司藉由 TDDM 方法學，每年依照不同的調查目的，執行重大議題的盤點與分析，形塑一個完整的調查週期。首年進行議題蒐集、調查與分析，重新定義具重大性的永續議題，並於次一年度檢視重大議題的變化，探討重大議題之間的因果關係，進而掌握重大議題與行動方案間的相互關聯，確保行動有效性。民國 112 年，台積公司邀請 1,693 位內外部利害關係人，以及超過 233 位負責推動永續業務的公司主管及同仁綜合考量利害關係人關注、組織營運衝擊與...`
- ID `10100` true=`Clear` pred=`N/A` text=`針對利害關係人所關切之重大人權議題，緯創從政策及內部規範之檢視著手，確保各項管理辦法之周延性，同時設定年度績效目標，定期追蹤相關工作計畫之執行成效，並持續依循 RBA 之管理架構進行日常作業稽核，針對缺失項目要求責任單位展開改善計畫，確保相關人權風險得以有效控管及降低。 Professional ESG Sustainability Report Analysis Assistant. Extract all text from ...`

## Evidence-Based Next Suggestions

- Focus first on `evidence_quality` because it has the lowest macro F1 in this report (0.2257).
- Inspect `verification_timeline` label `already`: recall is 0.0000 over support 72.
- Inspect `evidence_quality` label `Not Clear`: recall is 0.1200 over support 25.
- Inspect `evidence_quality` label `Clear`: recall is 0.1204 over support 108.
- Review `evidence_quality` confusion `Clear` -> `N/A` (76 rows) before adding new rules.
- Review `verification_timeline` confusion `already` -> `N/A` (37 rows) before adding new rules.
- Review `verification_timeline` confusion `already` -> `between_2_and_5_years` (31 rows) before adding new rules.

## Anti-Hallucination Note

The suggestions above are generated only from the prediction/truth comparison in this report. They are not proof of root cause; inspect the cited IDs and confusion pairs before changing code.
