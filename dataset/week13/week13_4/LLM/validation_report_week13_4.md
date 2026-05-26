# Validation Evidence Report

- Generated: 2026-05-25 13:57:36
- Prediction file: `E:\project\test510\week13_runs\week13_4\LLM_pipeline_pred_week13_4.json`
- Truth file: `E:\project\test510\dataset\week13\week13_4\val_grouped.json`
- Input file: `E:\project\test510\week13_runs\week13_4\val_formal_input.json`
- Prediction rows: 200
- Truth rows: 200
- Weighted score: `0.617420`

## Score Summary

| Field | Weight | Macro F1 | Weighted component | Truth distribution | Prediction distribution |
|---|---:|---:|---:|---|---|
| promise_status | 0.20 | 0.811282 | 0.162256 | Yes=159, No=41 | Yes=166, No=34 |
| verification_timeline | 0.15 | 0.646895 | 0.097034 | already=72, between_2_and_5_years=42, more_than_5_years=42, N/A=41, within_2_years=3 | already=100, N/A=36, more_than_5_years=35, between_2_and_5_years=26, within_2_years=3 |
| evidence_status | 0.30 | 0.676821 | 0.203046 | Yes=133, N/A=41, No=26 | Yes=143, N/A=49, No=8 |
| evidence_quality | 0.35 | 0.443095 | 0.155083 | Clear=108, N/A=67, Not Clear=25 | Clear=117, N/A=60, Not Clear=23 |

## promise_status

### Per-Label Metrics

| Label | Precision | Recall | F1 | Support |
|---|---:|---:|---:|---:|
| Yes | 0.909639 | 0.949686 | 0.929231 | 159 |
| No | 0.764706 | 0.634146 | 0.693333 | 41 |

### Confusion Matrix

Rows are truth labels; columns are predicted labels.

| Truth \ Pred | Yes | No |
|---|---:|---:|
| Yes | 151 | 8 |
| No | 15 | 26 |

### Largest Gaps

- `No` -> `Yes`: 15 rows
- `Yes` -> `No`: 8 rows

### Example Mismatches

- ID `10070` true=`No` pred=`Yes` text=`2024 年，瑞昱廠務工程單位持續與供應管理中心、資訊技術處、研發中心共同落實節能減碳，共提出 26 項節能方案措施，包含針對空調、照明、空壓等設備，以及伺服器機房空調優化等措施，約共投入新臺幣 44,149 千元，2024 年整體節電率達 5.34 %、節電量達 2,705,480 度，約可節省新臺幣 12,446 千元電費支出，亦等同減少 9,734.97 GJ 的熱能排放，換算碳排放減量達 1,282.40 tCO₂e，相當...`
- ID `10097` true=`No` pred=`Yes` text=`和泰汽車連續9年獲台灣企業永續研訓中心「台灣企業永續獎(TCSA)」。和泰汽車獲頒教育部體育署「運動企業認證」。Lexus RZ 450e 旗艦版限量上市。TOYOTA 一車一樹活動 90 萬棵植樹達成。和泰集團捐贈和泰 13 號捐血車；連續 13 年舉辦全台捐血車聯活動。和泰集團第七度舉辦志工植樹，保育台灣海岸線。和泰集團「導護志工裝備捐贈計畫」連續 14 年，累計捐贈 13 萬套。和泰集團「原夢代表隊」贊助嘉興國小獲「義大利安...`
- ID `10163` true=`No` pred=`Yes` text=`針對大部份初階團隊的共通需求，規劃 1 堂必修的「商業模式」及 2 堂選修的「跨界合作」、「Pitch 簡報」等培力課程，期待啟發團隊成員對現行提案的更多想像，並務實踏出落地的第一步。 Professional ESG Sustainability Report Analysis Assistant. Extract text from a scanned page of a corporate ESG report. Full ...`
- ID `10209` true=`No` pred=`Yes` text=`遠傳電信視連續兩年有交易之供應商為有效供應商，2024 年度有效供應商為 1,070 家，其中客戶裝置與資通訊類採購支出加總約佔遠傳整體採購金額 85.0 %，其中資通訊類數量最多占整體供應商家數的 54.2%，遠傳也針對資通訊類業務採取優等廠商 (Prefer Vendor) 機制，並建立 prefer vendor 的使用比例 KPI，提高優等廠商合作次數以降低營運風險，2024 年 Prefer vendor 採購金額執行比...`
- ID `10247` true=`No` pred=`Yes` text=`報告書揭露之數據及資料由各部門代表共同彙整、推動報告書編纂業務。本報告書透過利害關係人鑑別、重大永續主題辨識，彙整各部門資訊與永續績效指標等作業所集成。各部門資訊與永續績效指標完整性與正確性由各部門主管初步審核後，由股務統籌進行資訊數據再檢驗、內容規劃與編輯修訂等事宜。由內部行政流程審閱，並經董事會通過後公開揭露。 Professional ESG Sustainability Report Analysis Assistant....`
- ID `10350` true=`No` pred=`Yes` text=`此外，各廠 ( 處 ) 亦每 2 ~ 3 個月安排與單位內同仁進行溝通座談會，並將溝通事項納入追蹤。所有新進人員於新進人員訓練中皆接受人權相關訓練，資深員工亦全數皆曾接受人權相關訓練 ( 除包含前述新進人員性騷擾防治及申訴管道宣導外，亦包含反歧視與職場不法侵害防治等內容 ) 時數 6,035 小時，計 1,491 人次受訓；另有辦理相關溝通及宣導會議，計有 10,486 小時。 Professional ESG Sustainab...`
- ID `10363` true=`No` pred=`Yes` text=`中鋼產業類別屬於鋼鐵工業，主要產品為鋼板、棒線、熱軋、冷軋、電磁鋼捲、電磁鋼捲及熱浸鍍鋅鋼捲等鋼品，113 年產品 57.4% 內銷，42.6% 外銷，主要產品國內市占率逾五成，為目前國內最大鋼鐵公司；外銷主要對象為東南亞、歐洲、日本。為發揮經營綜效，中鋼進行多角化經營，業務範圍涵蓋鋼鐵、工程、工業材料、物流投資及綠能等五大事業群，價值鏈核心為中鋼本身，並涵蓋員工及協力人員，上游為礦料等原物料供應商，下游則涵蓋客戶及當地社區。 P...`
- ID `10388` true=`No` pred=`Yes` text=`為有系統清查及評估各廠處於營運過程中，使用各項化學品對環境造成衝擊之作業活動（含原物料、產品及半成品、設備維修及新產品開發等營運過程）及其影響程度，並針對較顯著之環境衝擊事項研擬管制對策，訂定「環境衝擊審查辦法」。確保各廠有害物質（含環保署列管化學物質及危害性化學物質）作業場所安全，除要求負責人員取得技術證照、廠內設置偵測及警報設備系統外；對於未使用之環保署列管化學物質，依法辦理聲明廢棄後，視為有害事業廢棄物管理並妥善處理。 Pr...`

## verification_timeline

### Per-Label Metrics

| Label | Precision | Recall | F1 | Support |
|---|---:|---:|---:|---:|
| already | 0.540000 | 0.750000 | 0.627907 | 72 |
| within_2_years | 1.000000 | 1.000000 | 1.000000 | 3 |
| between_2_and_5_years | 0.538462 | 0.333333 | 0.411765 | 42 |
| more_than_5_years | 0.542857 | 0.452381 | 0.493506 | 42 |
| N/A | 0.750000 | 0.658537 | 0.701299 | 41 |

### Confusion Matrix

Rows are truth labels; columns are predicted labels.

| Truth \ Pred | already | within_2_years | between_2_and_5_years | more_than_5_years | N/A |
|---|---:|---:|---:|---:|---:|
| already | 54 | 0 | 5 | 8 | 5 |
| within_2_years | 0 | 3 | 0 | 0 | 0 |
| between_2_and_5_years | 22 | 0 | 14 | 4 | 2 |
| more_than_5_years | 17 | 0 | 4 | 19 | 2 |
| N/A | 7 | 0 | 3 | 4 | 27 |

### Largest Gaps

- `between_2_and_5_years` -> `already`: 22 rows
- `more_than_5_years` -> `already`: 17 rows
- `already` -> `more_than_5_years`: 8 rows
- `N/A` -> `already`: 7 rows
- `already` -> `N/A`: 5 rows
- `already` -> `between_2_and_5_years`: 5 rows
- `between_2_and_5_years` -> `more_than_5_years`: 4 rows
- `N/A` -> `more_than_5_years`: 4 rows

### Example Mismatches

- ID `10113` true=`between_2_and_5_years` pred=`already` text=`我們深知永續議題的管理，是企業持續改善與長遠發展的關鍵。其包含企業面對議題如何整合內部資源擬定相關管理方針與各階段利害關係人的議合溝通。本公司透過多元管道蒐集相關回覆和建議，將其納入公司營運規劃中。 Professional ESG Sustainability Report Analysis Assistant. Extract text from a scanned image of an ESG report. Conver...`
- ID `10172` true=`between_2_and_5_years` pred=`already` text=`非常榮幸獲得職安衛人員的殊榮，這不僅是對我個人的肯定，更是對我們團隊長期投入職安工作的支持與鼓勵。從事職業安全衛生工作以來，我深刻體會到，「安全」絕非一人之責，而是全體同仁共同建立、共同維護的一種文化。很開心能在緯穎與一群重視安全、積極落實制度的夥伴一起努力，使得每一次風險評估、每一場教育訓練、每一次巡檢，都能發揮實質成效，不僅守護了同仁的健康與生命安全，也一步步形塑出屬於緯穎的職安衛文化。這份榮耀不只屬於我，更屬於所有在安全衛生...`
- ID `10181` true=`between_2_and_5_years` pred=`already` text=`台新持續培養數位金融技能，除了藉由教育訓練提升現有員工的科技專業技能外，也積極招募外部數位科技人才，以快速提升整體數位技能。透過掌握金融科技發展趨勢，未來台新將積極布建數位金融生態環境，並且因應新世代趨勢進行科技人才培育，以更積極、穩健的腳步，落實企業永續經營。 Professional ESG Sustainability Report Analysis Assistant. Extract text from a scanne...`
- ID `10226` true=`between_2_and_5_years` pred=`already` text=`和泰集團自 2022 年啟動「原夢代表隊」公益計畫，攜手集團內各事業體，共同整合資源，長期支持新竹縣尖石鄉嘉興國小與五峰鄉桃山國小的泰雅族兒童合唱團。此計畫旨在幫助這些擁有音樂天賦的孩子，在成長與學習的過程中，接觸多元職業與環境，拓展視野並提升對未來職業的想像。 Professional ESG Sustainability Report Analysis Assistant. Extract all text from the ...`
- ID `10235` true=`between_2_and_5_years` pred=`already` text=`TOYOTA 自 2017 年 4 月啟動「一車一樹」植樹計畫，每售出一台 TOYOTA 新車，即為車主在台灣種下一棵樹，投入經費更超過三億元，在財團法人慈心有機農業發展基金會的協助下，為全台 17 縣市及離島澎湖、金門、馬祖陸續建立起綠色長城。自 2019 年起舉辦車主志工植樹活動，邀請 TOYOTA 車主與民眾共同響應，讓每一位參與者體驗親手種下樹苗的感動，一起成為守護台灣海岸線的重要推手。 2024 年也於宜蘭壯圍海岸舉辦「...`
- ID `10258` true=`between_2_and_5_years` pred=`already` text=`雖目前評估供應鏈對本行營運之影響甚微，本行仍將持續關注供應商供貨之穩定度，並適時開發新供應商，以提高替代性。此外，為提升供應商的氣候風險準備度，本行未來將舉辦供應商大會，宣導氣候風險相關防範措施與救災知識，並建議高風險供應商設置防洪設備。 Professional ESG Sustainability Report Analysis Assistant. An image of a page from a corporate ES...`
- ID `10356` true=`between_2_and_5_years` pred=`already` text=`台塑工業 ( 寧波 ) 公司也致力於廢棄物管理並減量，主要透過末端處置進行。 Professional ESG Sustainability Report Analysis Assistant. Extract all text from a scanned image of an ESG report. Convert tables to Markdown format precisely. The user specifica...`
- ID `10366` true=`between_2_and_5_years` pred=`already` text=`國巨集團深知人才全球化趨勢，將更著重於跨國人才培育，多數公司藉由海外輸入優秀人才，國巨集團則是希望由本地輸出優秀人力到海外分公司。國巨未來人才發展策略將是透過招募、留才、培育，達到歷練不同功能別職務、跨國及跨文化的管理能力。 Professional ESG Sustainability Report Analysis Assistant. Extract text from a scanned page of an ESG re...`

## evidence_status

### Per-Label Metrics

| Label | Precision | Recall | F1 | Support |
|---|---:|---:|---:|---:|
| Yes | 0.853147 | 0.917293 | 0.884058 | 133 |
| No | 0.500000 | 0.153846 | 0.235294 | 26 |
| N/A | 0.836735 | 1.000000 | 0.911111 | 41 |

### Confusion Matrix

Rows are truth labels; columns are predicted labels.

| Truth \ Pred | Yes | No | N/A |
|---|---:|---:|---:|
| Yes | 122 | 4 | 7 |
| No | 21 | 4 | 1 |
| N/A | 0 | 0 | 41 |

### Largest Gaps

- `No` -> `Yes`: 21 rows
- `Yes` -> `N/A`: 7 rows
- `Yes` -> `No`: 4 rows
- `No` -> `N/A`: 1 rows

### Example Mismatches

- ID `10022` true=`No` pred=`Yes` text=`玉山金控除了面對氣候環境風險外，也積極尋找轉型的契機，在氣候相關的機會面向涵蓋了：資源使用效率、產品和服務、市場拓展及營運韌性等多個方面。金融業身為市場力量的重要推手，須發揮正面的影響力，建立永續金融生態圈的正向循環。我們積極協力政府與企業共同推動淨零轉型，致力於引導民間資金流向對環境及社會有益之經濟活動，推動永續相關基礎建設及低碳產業、技術的發展，協助顧客淨零轉型，強化因應 ESG 相關風險的韌性，確保面對未來挑戰的發展潛力。 ...`
- ID `10113` true=`No` pred=`Yes` text=`我們深知永續議題的管理，是企業持續改善與長遠發展的關鍵。其包含企業面對議題如何整合內部資源擬定相關管理方針與各階段利害關係人的議合溝通。本公司透過多元管道蒐集相關回覆和建議，將其納入公司營運規劃中。 Professional ESG Sustainability Report Analysis Assistant. Extract text from a scanned image of an ESG report. Conver...`
- ID `10171` true=`No` pred=`Yes` text=`事業部門每週定期檢視研發進度及成果，並不定期拜訪客戶及供應商掌握市場走向，以確認產品功能符合市場及客戶需求。研發中心、技術研發中心自行開發技術及取得授權技術，並定期透過會議討論技術運用管理及成本效益控管。品質管理處依據各項管理系統，進行定期會議確保產品品質。 Professional ESG Sustainability Report Analysis Assistant. A scanned image of an ESG re...`
- ID `10172` true=`No` pred=`Yes` text=`非常榮幸獲得職安衛人員的殊榮，這不僅是對我個人的肯定，更是對我們團隊長期投入職安工作的支持與鼓勵。從事職業安全衛生工作以來，我深刻體會到，「安全」絕非一人之責，而是全體同仁共同建立、共同維護的一種文化。很開心能在緯穎與一群重視安全、積極落實制度的夥伴一起努力，使得每一次風險評估、每一場教育訓練、每一次巡檢，都能發揮實質成效，不僅守護了同仁的健康與生命安全，也一步步形塑出屬於緯穎的職安衛文化。這份榮耀不只屬於我，更屬於所有在安全衛生...`
- ID `10174` true=`No` pred=`Yes` text=`台泥將自然置於企業理念的核心，並將自然碳匯納入其 2050 淨零策略之中。呼應 COP15 通過的《昆明-蒙特婁全球生物多樣性框架》，台泥的自然相關行動對齊全球 2030 年目標與 2050 年願景，致力於與自然和諧共生，實現對生物多樣性的正向貢獻。自然，是全球經濟的基礎。全球一半以上的GDP、超過44兆美元，仰賴大自然的資源與提供的生態系服務。 Professional ESG Sustainability Report Ana...`
- ID `10181` true=`No` pred=`Yes` text=`台新持續培養數位金融技能，除了藉由教育訓練提升現有員工的科技專業技能外，也積極招募外部數位科技人才，以快速提升整體數位技能。透過掌握金融科技發展趨勢，未來台新將積極布建數位金融生態環境，並且因應新世代趨勢進行科技人才培育，以更積極、穩健的腳步，落實企業永續經營。 Professional ESG Sustainability Report Analysis Assistant. Extract text from a scanne...`
- ID `10258` true=`No` pred=`Yes` text=`雖目前評估供應鏈對本行營運之影響甚微，本行仍將持續關注供應商供貨之穩定度，並適時開發新供應商，以提高替代性。此外，為提升供應商的氣候風險準備度，本行未來將舉辦供應商大會，宣導氣候風險相關防範措施與救災知識，並建議高風險供應商設置防洪設備。 Professional ESG Sustainability Report Analysis Assistant. An image of a page from a corporate ES...`
- ID `10282` true=`No` pred=`Yes` text=`緯穎科技以「釋放數位能量，點燃永續創新」為願景，致力於推動各種類數位願景的同時，以創新實現永續。我們從「環境友善營運」、「員工與企業共善共榮」、「永續供應鏈」及「綠色創新」等四個面向，制定長期目標，並進一步將 ESG 績效連結薪酬制度，以深化永續管理，並推動永續發展與核心商業領域的對外倡議，透過參與及對話，深化公司在永續創新的影響力；同時積極參與社會關懷與環境保育等公益活動，與弱勢團體及當地社區等利害關係人議合，希望透過緯穎科技的...`

## evidence_quality

### Per-Label Metrics

| Label | Precision | Recall | F1 | Support |
|---|---:|---:|---:|---:|
| Clear | 0.752137 | 0.814815 | 0.782222 | 108 |
| Not Clear | 0.260870 | 0.240000 | 0.250000 | 25 |
| Misleading | 0.000000 | 0.000000 | 0.000000 | 0 |
| N/A | 0.783333 | 0.701493 | 0.740157 | 67 |

### Confusion Matrix

Rows are truth labels; columns are predicted labels.

| Truth \ Pred | Clear | Not Clear | Misleading | N/A |
|---|---:|---:|---:|---:|
| Clear | 88 | 10 | 0 | 10 |
| Not Clear | 16 | 6 | 0 | 3 |
| Misleading | 0 | 0 | 0 | 0 |
| N/A | 13 | 7 | 0 | 47 |

### Largest Gaps

- `Not Clear` -> `Clear`: 16 rows
- `N/A` -> `Clear`: 13 rows
- `Clear` -> `Not Clear`: 10 rows
- `Clear` -> `N/A`: 10 rows
- `N/A` -> `Not Clear`: 7 rows
- `Not Clear` -> `N/A`: 3 rows

### Example Mismatches

- ID `10020` true=`Not Clear` pred=`Clear` text=`鴻海堅持長期永續發展的承諾，明確訂定ESG目標，推動並落實行動策略，積極因應外部日益加劇的永續風險與機遇。我們聚焦於綠色智能、循環經濟、幸福發展、共贏共榮、鴻傳永續、海納治理六大核心策略，持續深化ESG數位智能管理平台與治理基礎，系統推進行動方案，實踐責任經營，創造永續價值。《行為準則》是鴻海規範全球廠區與員工商業行為的核心依據，也是處理與各類利益相關方關係的基本準則。如當地法律與本準則有所差異或衝突，我們將依法從事，同時遵循更高...`
- ID `10076` true=`Not Clear` pred=`Clear` text=`為更積極地回應全球自然目標 (Global Goal for Nature)，並持續關注生態環境、尊重生態平衡、維護瀕危物種。緯創於 2023 年逐步建構對自然暨生物多樣性保育依賴性與衝擊程度的評估方法及指標，並制定相關工作目標。我們致力於在 2050 年實現對自然正向 (Nature Positive) 的貢獻，同時也訂定對供應商有關生物多樣性和不毀林的行為準則，包括保護生態環境、禁止濫伐森林、保護自然棲息地、避免土地污染等。 ...`
- ID `10225` true=`Not Clear` pred=`Clear` text=`2022年11月10日，經董事會決議，由鴻海研究院李維斌執行長擔任資安長，並由鴻海研究院資通安全研究所(資安所)擔任資訊安全治理委員會秘書處，透過資安所負責集團前瞻研究之角色，關注資安治理、風險和合規之整合性國際趨勢與標準，並與資訊長充分協作，制定高層資安政策、督導集團資安政策之落實、建立集團資安的最佳實務，一起帶領鴻海建立全球高科技產業資安最佳典範，同時展現公司前瞻研究的實力。 委員會轄下分為資安治理工作小組、資安維運工作小組，...`
- ID `10226` true=`Not Clear` pred=`Clear` text=`和泰集團自 2022 年啟動「原夢代表隊」公益計畫，攜手集團內各事業體，共同整合資源，長期支持新竹縣尖石鄉嘉興國小與五峰鄉桃山國小的泰雅族兒童合唱團。此計畫旨在幫助這些擁有音樂天賦的孩子，在成長與學習的過程中，接觸多元職業與環境，拓展視野並提升對未來職業的想像。 Professional ESG Sustainability Report Analysis Assistant. Extract all text from the ...`
- ID `10356` true=`Not Clear` pred=`Clear` text=`台塑工業 ( 寧波 ) 公司也致力於廢棄物管理並減量，主要透過末端處置進行。 Professional ESG Sustainability Report Analysis Assistant. Extract all text from a scanned image of an ESG report. Convert tables to Markdown format precisely. The user specifica...`
- ID `10366` true=`Not Clear` pred=`Clear` text=`國巨集團深知人才全球化趨勢，將更著重於跨國人才培育，多數公司藉由海外輸入優秀人才，國巨集團則是希望由本地輸出優秀人力到海外分公司。國巨未來人才發展策略將是透過招募、留才、培育，達到歷練不同功能別職務、跨國及跨文化的管理能力。 Professional ESG Sustainability Report Analysis Assistant. Extract text from a scanned page of an ESG re...`
- ID `10419` true=`Not Clear` pred=`Clear` text=`為實現永續發展策略，秉持著「利他」的經營哲學，在追求公司持續成長的過程中，營運策略必須兼顧對社會與環境帶來之影響與衝擊。因此，整合 AI 技術同步展示於專利長遠永續規劃與佈局，邁向緯創「創新而永續」的願景。 Professional ESG Sustainability Report Analysis Assistant. Extract text from the provided scanned image of a corp...`
- ID `10576` true=`Not Clear` pred=`Clear` text=`本公司由張洪本副董事長擔任資安專責董事，並於本公司董事會下成立永續發展暨資安委員會，委員會成員皆由本公司董事擔任。該委員會統籌日月光投控之整體資訊安全策略發展與成熟度對標評估，負責資安風險管理之整體規劃與監督，督導各子公司資訊安全管理運作，並協調整合內外部技術資源與情資，以強化資安能量、降低潛在威脅與風險。永續發展暨資安委員會設置資安長 (CISO) 一職，由本公司行政長暨公司治理主管兼任，主責指示日月光投控資安風險管理架構、定期...`

## Evidence-Based Next Suggestions

- Focus first on `evidence_quality` because it has the lowest macro F1 in this report (0.4431).
- Inspect `evidence_status` label `No`: recall is 0.1538 over support 26.
- Inspect `evidence_quality` label `Not Clear`: recall is 0.2400 over support 25.
- Inspect `verification_timeline` label `between_2_and_5_years`: recall is 0.3333 over support 42.
- Review `verification_timeline` confusion `between_2_and_5_years` -> `already` (22 rows) before adding new rules.
- Review `evidence_status` confusion `No` -> `Yes` (21 rows) before adding new rules.
- Review `verification_timeline` confusion `more_than_5_years` -> `already` (17 rows) before adding new rules.

## Anti-Hallucination Note

The suggestions above are generated only from the prediction/truth comparison in this report. They are not proof of root cause; inspect the cited IDs and confusion pairs before changing code.
