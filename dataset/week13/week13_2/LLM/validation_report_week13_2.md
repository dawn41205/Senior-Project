# Validation Evidence Report

- Generated: 2026-05-25 08:17:13
- Prediction file: `E:\project\test510\week13_runs\week13_2\LLM_pipeline_pred_week13_2.json`
- Truth file: `E:\project\test510\dataset\week13\week13_2\val_grouped.json`
- Input file: `E:\project\test510\week13_runs\week13_2\val_formal_input.json`
- Prediction rows: 200
- Truth rows: 200
- Weighted score: `0.628468`

## Score Summary

| Field | Weight | Macro F1 | Weighted component | Truth distribution | Prediction distribution |
|---|---:|---:|---:|---|---|
| promise_status | 0.20 | 0.773960 | 0.154792 | Yes=156, No=44 | Yes=160, No=40 |
| verification_timeline | 0.15 | 0.524562 | 0.078684 | already=74, N/A=44, more_than_5_years=41, between_2_and_5_years=40, within_2_years=1 | already=89, more_than_5_years=44, N/A=42, between_2_and_5_years=21, within_2_years=4 |
| evidence_status | 0.30 | 0.744449 | 0.223335 | Yes=136, N/A=44, No=20 | Yes=132, N/A=57, No=11 |
| evidence_quality | 0.35 | 0.490448 | 0.171657 | Clear=112, N/A=64, Not Clear=24 | Clear=112, N/A=70, Not Clear=17, Misleading=1 |

## promise_status

### Per-Label Metrics

| Label | Precision | Recall | F1 | Support |
|---|---:|---:|---:|---:|
| Yes | 0.893750 | 0.916667 | 0.905063 | 156 |
| No | 0.675000 | 0.613636 | 0.642857 | 44 |

### Confusion Matrix

Rows are truth labels; columns are predicted labels.

| Truth \ Pred | Yes | No |
|---|---:|---:|
| Yes | 143 | 13 |
| No | 17 | 27 |

### Largest Gaps

- `No` -> `Yes`: 17 rows
- `Yes` -> `No`: 13 rows

### Example Mismatches

- ID `10070` true=`No` pred=`Yes` text=`2024 年，瑞昱廠務工程單位持續與供應管理中心、資訊技術處、研發中心共同落實節能減碳，共提出 26 項節能方案措施，包含針對空調、照明、空壓等設備，以及伺服器機房空調優化等措施，約共投入新臺幣 44,149 千元，2024 年整體節電率達 5.34 %、節電量達 2,705,480 度，約可節省新臺幣 12,446 千元電費支出，亦等同減少 9,734.97 GJ 的熱能排放，換算碳排放減量達 1,282.40 tCO₂e，相當...`
- ID `10250` true=`No` pred=`Yes` text=`以顧客為核心，用獨特的創意與巧思，從推動永續金融應用，到建立「防詐藍圖」，展現玉山在永續發展與民眾資產保護上的實際行動。透過科技驅動、場域深入與跨界合作，玉山不斷突破既有框架，打造創新服務與合作模式，堅定前行並創造長遠價值。 Professional ESG Sustainability Report Analysis Assistant. Extract all text from the provided image of a...`
- ID `10277` true=`No` pred=`Yes` text=`啟用台泥 DAKA 再生資源利用中心,每日最高處置200噸生活垃圾,運用處置過程產生的熱值替代部分燃料。中國大陸水泥廠合計每日生活垃圾處置量能600噸以上,作為替代燃料又避免垃圾囤積造成的甲烷問題。同時積極開發營建廢棄物處理服務,將建築拆除後的混凝土回收再利用。 Professional ESG Sustainability Report Analysis Assistant. Extract text from the prov...`
- ID `10313` true=`No` pred=`Yes` text=`依據集團各營運據點之實際狀況規劃再生能源使用，2024 年全球再生能源使用率達 66.77%。馬來西亞廠設置屋頂太陽能板自發自用，並於 2024 年取得 GBI 綠建築 Gold 等級認證。墨西哥廠 2025 年初取得 EDGE ADVANCED 等級認證，可節省 36% 能源消耗。進行製程改善，包含全球低耗電 PCBA 生產新線及減少機櫃產品測試閒置耗電。 Professional ESG sustainability repo...`
- ID `10339` true=`No` pred=`Yes` text=`因應國際近年對於公司治理及企業社會責任發展等議題之關注與趨勢之重視，鼓勵董事參與進修並向公司申報進修證明，公司揭露董事參與訓練、進修之相關紀錄同時可在公開資訊觀測站與公司 2024 年度年報 82-84 頁中查詢到相關資訊。 Professional ESG Sustainability Report Analysis Assistant. Extract all text from the provided image. Mai...`
- ID `10350` true=`No` pred=`Yes` text=`此外，各廠 ( 處 ) 亦每 2 ~ 3 個月安排與單位內同仁進行溝通座談會，並將溝通事項納入追蹤。所有新進人員於新進人員訓練中皆接受人權相關訓練，資深員工亦全數皆曾接受人權相關訓練 ( 除包含前述新進人員性騷擾防治及申訴管道宣導外，亦包含反歧視與職場不法侵害防治等內容 ) 時數 6,035 小時，計 1,491 人次受訓；另有辦理相關溝通及宣導會議，計有 10,486 小時。 Professional ESG Sustainab...`
- ID `10355` true=`No` pred=`Yes` text=`日月光投控逐一確認 17 項重大議題在上游採購、日月光生產廠區、客戶使用與社區等四大衝擊階段的影響。並對應 19 個 GRI Standard 主題以及 4 個日月光自訂主題，揭露屬於日月光投控的重大議題，公開揭露重大議題之雙重重大性影響範疇、管理方針、風險描述等內容。其他非重大議題，亦同步揭露於永續報告書中。 Professional ESG Sustainability Report Analysis Assistant. S...`
- ID `10393` true=`No` pred=`Yes` text=`台塑公司本著「取之於社會，用之於社會」的核心價值，在謀求發展的同時，也不忘回饋社會、造福人群，善盡優良企業社會責任，期能與當地社區共榮共存，同享發展成果，邁向永續未來。 Professional ESG Sustainability Report Analysis Assistant. Extract text from a scanned page of an ESG report. Convert tables to Mark...`

## verification_timeline

### Per-Label Metrics

| Label | Precision | Recall | F1 | Support |
|---|---:|---:|---:|---:|
| already | 0.561798 | 0.675676 | 0.613497 | 74 |
| within_2_years | 0.250000 | 1.000000 | 0.400000 | 1 |
| between_2_and_5_years | 0.571429 | 0.300000 | 0.393443 | 40 |
| more_than_5_years | 0.545455 | 0.585366 | 0.564706 | 41 |
| N/A | 0.666667 | 0.636364 | 0.651163 | 44 |

### Confusion Matrix

Rows are truth labels; columns are predicted labels.

| Truth \ Pred | already | within_2_years | between_2_and_5_years | more_than_5_years | N/A |
|---|---:|---:|---:|---:|---:|
| already | 50 | 1 | 5 | 8 | 10 |
| within_2_years | 0 | 1 | 0 | 0 | 0 |
| between_2_and_5_years | 19 | 1 | 12 | 8 | 0 |
| more_than_5_years | 10 | 1 | 2 | 24 | 4 |
| N/A | 10 | 0 | 2 | 4 | 28 |

### Largest Gaps

- `between_2_and_5_years` -> `already`: 19 rows
- `more_than_5_years` -> `already`: 10 rows
- `already` -> `N/A`: 10 rows
- `N/A` -> `already`: 10 rows
- `between_2_and_5_years` -> `more_than_5_years`: 8 rows
- `already` -> `more_than_5_years`: 8 rows
- `already` -> `between_2_and_5_years`: 5 rows
- `N/A` -> `more_than_5_years`: 4 rows

### Example Mismatches

- ID `10025` true=`between_2_and_5_years` pred=`already` text=`為避免因作業、活動或服務及設施等危害，造成同仁安全健康或公司財務損失，藉由建構 ISO 45001 安全衛生管理系統，持續推動安全衛生危害鑑別、風險機會評估，並採取適當預防措施或執行必要之控制方法，將風險控制在可接受的程度之下。 Professional ESG Sustainability Report Analysis Assistant. Extract text from the provided image. Preci...`
- ID `10177` true=`between_2_and_5_years` pred=`already` text=`台達秉持「環保 節能 愛地球」的經營使命，開發產品過程將綠色設計及循環設計之精神納入到生命週期中，持續開發創新節能產品及解決方案，提供高效率且可靠的節能整合方案與服務，從設計源頭減少廢棄物產生。我們持續提供循環設計相關教育訓練，包括從源頭改變、廢棄物即資源、維持高價值利用與思考循環路徑等原則，及導入循環設計、選擇低碳材料、提供產品使用權、延長產品生命、創造產品剩餘價值等策略，如在扇葉扇框使用消費後回收（Post Consumer ...`
- ID `10181` true=`between_2_and_5_years` pred=`already` text=`台新持續培養數位金融技能，除了藉由教育訓練提升現有員工的科技專業技能外，也積極招募外部數位科技人才，以快速提升整體數位技能。透過掌握金融科技發展趨勢，未來台新將積極布建數位金融生態環境，並且因應新世代趨勢進行科技人才培育，以更積極、穩健的腳步，落實企業永續經營。 Professional ESG Sustainability Report Analysis Assistant. Extract text from a scanne...`
- ID `10227` true=`between_2_and_5_years` pred=`already` text=`鴻海已展示了有效鑑別和公平評估對利害關係者的過程，其中已刻一系對來自廣泛來源的環境、社會和治理主題，對於其營運活動所帶來的衝擊的過程。其鑑別評估已透過定性化和定量相結合的目標愈來達成，本查證可持續提請佐證管道，透過多元管道與利害關係人揭露重大主題進展與成果，並透過決策流程提升與各方的互信與合作，持續優化企業溝通競爭力。 Professional ESG Sustainability Report Analysis Assistan...`
- ID `10245` true=`between_2_and_5_years` pred=`already` text=`陽明海運在全球各地長期經營業務，致力於尊重和維護國際公認的各項人權，並確保業務活動符合當地法律法規和國際標準，提供一個公正平等的工作環境，確保員工和合作夥伴的權益得到尊重和保障。在人權方面，尊重和維護國際公認的各項人權，絕不參與任何漠視與涉及人權侵害之活動。本公司參考國際人權法典 (International Bill of Human Rights)、聯合國全球盟約 (United Nations Global Compact)...`
- ID `10251` true=`between_2_and_5_years` pred=`already` text=`國泰奠基於勤辦公的資源，提供彈性工作時間及地點等支持性措施，讓具有照護需求的同仁不用陷入工作與家庭間的拔河抉擇。未來更將擴展至長者照顧，全力支持同仁平衡工作與家庭生活。育嬰留停需求的同仁也可運用 EAP (Employee Assistance Programs, EAP) 專業諮詢及線上學習等資源，獲得日常親子教養、理財規劃、返職前的技能暖身等資訊，減少復職時的摸索期，幫助同仁順利回歸職場。此外，國泰依法設計並落實特休假(有薪年...`
- ID `10270` true=`between_2_and_5_years` pred=`already` text=`另考量雙重重大性 ( 財務重大性與影響重大性 ) 原則，將依賴及影響程度與本集團評估範圍之金融資產金額交乘，並依據 GICS 行業板塊分類註2，其結果顯示原材料、金融及房地產為對自然環境產生較高依賴與影響的前三大產業。另參考 TNFD 金融業指引 (Sector guidance : Additional guidance for financial institutions v2.0)，金融業應優先關注 18 類自然環境敏感性產...`
- ID `10289` true=`between_2_and_5_years` pred=`already` text=`2024 年度平均每日放流水量為 4.3 萬噸，經廢水場處理後最終放流至台灣海峽海域，水質皆符合放流水標準，2024 年單位產品放流水量為 0.00055 百萬公升 / 噸，呈現穩定波動趨勢，未來將持續評估開發廢水回收再利用 ( 如製程酸水回收至排煙脫硫系統等 ) 及廢水處理設施改造提升回收量，持續降低單位產品廢水排放量。 Professional ESG Sustainability Report Analysis Assist...`

## evidence_status

### Per-Label Metrics

| Label | Precision | Recall | F1 | Support |
|---|---:|---:|---:|---:|
| Yes | 0.924242 | 0.897059 | 0.910448 | 136 |
| No | 0.636364 | 0.350000 | 0.451613 | 20 |
| N/A | 0.771930 | 1.000000 | 0.871287 | 44 |

### Confusion Matrix

Rows are truth labels; columns are predicted labels.

| Truth \ Pred | Yes | No | N/A |
|---|---:|---:|---:|
| Yes | 122 | 4 | 10 |
| No | 10 | 7 | 3 |
| N/A | 0 | 0 | 44 |

### Largest Gaps

- `Yes` -> `N/A`: 10 rows
- `No` -> `Yes`: 10 rows
- `Yes` -> `No`: 4 rows
- `No` -> `N/A`: 3 rows

### Example Mismatches

- ID `10035` true=`Yes` pred=`N/A` text=`本集團以獨立超然之精神執行稽核業務，隸屬於董事會，協助董事會及高階管理階層審查與評估風險管理是否有效運作，包含評估第一道及第二道防線監控之有效性，並適時提出改進建議。內部稽核單位建立及執行集團內部稽核制度，查核與評估內部控制之有效性，並定期向審計委員會及董事會報告。對本公司每年至少辦理 1 次一般業務查核。 Professional ESG Sustainability Report Analysis Assistant. Ext...`
- ID `10120` true=`Yes` pred=`N/A` text=`金控及轄下子公司之企業核心價值為「誠信、親切、專業、創新」，首重以「誠信」是公司治理及企業永續經營的根本，而本公司本於廉潔、透明及負責之經營理念，建構誠信經營之企業文化及健全發展，以建立良好商業運作模式與風險控管機制，創造永續發展之經營環境，爰參照「富邦金控誠信經營守則」制定「富邦人壽誠信經營守則」並經董事會決議通過，並於公司內部網站、法令遵循網站公告予內、外勤同仁知悉。 Professional ESG Sustainabili...`
- ID `10164` true=`Yes` pred=`N/A` text=`我們需要更多資源投入永續供應鏈、影響力投資、建構自然生態系，以擴大自然生物多樣性市場；全球來自 51 個國家的 416 個組織採用自然相關財務揭露 (Taskforce on Nature-related Financial Disclosures, TNFD)，其中 45% 來自亞洲，顯示亞洲企業有意願在自然行動積極響應。 Professional ESG Sustainability Report Analysis Assis...`
- ID `10432` true=`Yes` pred=`N/A` text=`本行 2024 年個人放款約 73,574 件，年底餘額約新臺幣 3,538 億元。本行另推出多項具金融包容性精神之學貸、房貸及創業貸款等貸款專案，2024 年專案推動情形如下： Professional ESG Sustainability Report Analysis Assistant. Extract all text from the provided scanned page of a corporate ESG r...`
- ID `10442` true=`Yes` pred=`N/A` text=`服務本身就是人與人的交流，透過暖心的問好、精準的回應，提升服務的溫度及專業。另一方面，提供多元諮詢管道供客戶使用，並以完備處理流程及公平、合理、有效之原則，妥適處理客戶的寶貴意見，方能使服務的品質不斷提升、符合客戶之期待。 Professional ESG Sustainability Report Analysis Assistant. Two scanned pages (142 and 143) from a corpora...`
- ID `10457` true=`Yes` pred=`N/A` text=`\| 集團資訊策略委員會 \| 研議華南金融集團短、中、長期資訊策略及資訊發展相關重要議題。 \| • 每半年召開 1 次，惟得視業務需要隨時召開，2024 年共召開 2 次<br>• 平均出席率：98.15%(含委託出席為 100%) \| Professional ESG Sustainability Report Analysis Assistant. Two scanned pages (080 and 081) from a c...`
- ID `10529` true=`Yes` pred=`N/A` text=`資料內容以2024年1月1日至2024年12月31日為主。為求報告書內容完整性及資訊可比較性，部份資料回溯2022、2023年度，或提及未來行動方向。本公司每年發行永續報告書，本報告書於2025年8月發行；下一本報告書預定於2026年8月發行。 Professional ESG Sustainability Report Analysis Assistant. Extract text from a scanned page of...`
- ID `10589` true=`Yes` pred=`N/A` text=`與輔仁大學偏鄉課輔團隊合作，由大學生擔任大學伴，透過電腦、耳機及手寫板結合視訊科技，於每週二、四晚間為遠端小學伴進行線上一對一、量身訂製的課程，為孩子帶來心靈陪伴及學習的好榜樣。辦理實體體驗活動，提供小學伴參與多元活動的機會、開拓視野。自 2009 年起到 2024 年止，累計參與計劃的小學伴有 4,086 人次、大學伴 6,329 人次、課輔時數為 118,248.5 小時。 Professional ESG Sustainab...`

## evidence_quality

### Per-Label Metrics

| Label | Precision | Recall | F1 | Support |
|---|---:|---:|---:|---:|
| Clear | 0.848214 | 0.848214 | 0.848214 | 112 |
| Not Clear | 0.352941 | 0.250000 | 0.292683 | 24 |
| Misleading | 0.000000 | 0.000000 | 0.000000 | 0 |
| N/A | 0.785714 | 0.859375 | 0.820896 | 64 |

### Confusion Matrix

Rows are truth labels; columns are predicted labels.

| Truth \ Pred | Clear | Not Clear | Misleading | N/A |
|---|---:|---:|---:|---:|
| Clear | 95 | 7 | 0 | 10 |
| Not Clear | 12 | 6 | 1 | 5 |
| Misleading | 0 | 0 | 0 | 0 |
| N/A | 5 | 4 | 0 | 55 |

### Largest Gaps

- `Not Clear` -> `Clear`: 12 rows
- `Clear` -> `N/A`: 10 rows
- `Clear` -> `Not Clear`: 7 rows
- `Not Clear` -> `N/A`: 5 rows
- `N/A` -> `Clear`: 5 rows
- `N/A` -> `Not Clear`: 4 rows
- `Not Clear` -> `Misleading`: 1 rows

### Example Mismatches

- ID `10016` true=`Not Clear` pred=`Clear` text=`廣達亦不定期進行小規模員工敬業度調查，2024年台灣廠區調查顯示，有80%員工願意在相同條件下繼續留任，其中女性員工投入度更達86%。為進一步了解績優員工的職場體驗，針對高績效同仁實施不記名投入度評估，結果顯示在成長機會與工作期待方面得分高，但在被肯定與讚賞的感受相對較低。對此，公司為主官規劃相關回饋訓練課程，透過情境模擬協助主管提升正向回饋能力。 **4 安心職場** **關於報告書** **管理者的話** **1 永續經營**...`
- ID `10080` true=`Not Clear` pred=`Clear` text=`為因應氣候變遷所帶來的風險與機會，本公司每年定期召開氣候變遷風險及機會會議，參考國際永續準則理事會 (International Sustainability Standards Board, ISSB) 發布之國際財務報導永續揭露準則第 S2 號 (IFRS S2) 氣候相關財務資訊揭露架構，提早進行因應及防範，進而降低氣候變遷對本公司之衝擊。相關資訊可進一步參考 2024 年氣候相關財務揭露報告書 (TCFD 報告書)，惟該報...`
- ID `10129` true=`Not Clear` pred=`Clear` text=`和泰汽車每年定期舉辦「違法零容忍」法律講座，藉由對「破窗理論」及「違法零容忍」觀念解說及業務上常見違法案例解說，對第一線人員進行法遵觀念強化溝通。透過實體講座課程，邀請各經銷商法務擔當擔任種子講師，無法參與實體課程的人員則施以線上課程與課後測驗，確實展現集團對於違法行為絕不姑息的決心。2024 年，已針對各項遵法辦理實體與線上課程，相關成果如下： Professional ESG Sustainability Report Ana...`
- ID `10251` true=`Not Clear` pred=`Clear` text=`國泰奠基於勤辦公的資源，提供彈性工作時間及地點等支持性措施，讓具有照護需求的同仁不用陷入工作與家庭間的拔河抉擇。未來更將擴展至長者照顧，全力支持同仁平衡工作與家庭生活。育嬰留停需求的同仁也可運用 EAP (Employee Assistance Programs, EAP) 專業諮詢及線上學習等資源，獲得日常親子教養、理財規劃、返職前的技能暖身等資訊，減少復職時的摸索期，幫助同仁順利回歸職場。此外，國泰依法設計並落實特休假(有薪年...`
- ID `10360` true=`Not Clear` pred=`Clear` text=`TSMC ESG AWARD 為台積公司推動永續文化的核心平台，鼓勵同仁提出連結公司 ESG 五大方向的新創好點子，並表彰組織的永續實績，以永續力促進創新力，創造美好改變。 Professional ESG Sustainability Report Analysis Assistant. Extract all text from the provided image of a corporate ESG report page...`
- ID `10419` true=`Not Clear` pred=`Clear` text=`為實現永續發展策略，秉持著「利他」的經營哲學，在追求公司持續成長的過程中，營運策略必須兼顧對社會與環境帶來之影響與衝擊。因此，整合 AI 技術同步展示於專利長遠永續規劃與佈局，邁向緯創「創新而永續」的願景。 Professional ESG Sustainability Report Analysis Assistant. Extract text from the provided scanned image of a corp...`
- ID `10512` true=`Not Clear` pred=`Clear` text=`亦針對重要資訊系統與網路服務建置的營運持續計畫，詳情請參閱CH1.6資訊安全。2024年4月3日花蓮發生芮氏規模7.1地震，台泥於第一時間啟動營運持續計畫，維持重要營運項目並儘速回復正常營運，減輕災害帶來的衝擊。台泥持續依災害管理四階段(減災、整備、應變、復原)，強化營運與應對天災的韌性。 Professional ESG Sustainability Report Analysis Assistant. An image of ...`
- ID `10684` true=`Not Clear` pred=`Clear` text=`本公司訂定集團與子公司授信及投資最高風險承擔限額以控管集團大額暴險；依各業別子公司訂定資本適足率警示水準以維持集團資本適足性；定期檢視各子公司信用風險、市場風險、利率風險、流動性風險、保險風險、作業風險及新興風險等主要風險監控指標，確實執行預警及停損機制；落實有效之內部控制制度以減少風險發生可能造成的損失。 Professional ESG Sustainability Report Analysis Assistant. Ext...`

## Evidence-Based Next Suggestions

- Focus first on `evidence_quality` because it has the lowest macro F1 in this report (0.4904).
- Inspect `evidence_quality` label `Not Clear`: recall is 0.2500 over support 24.
- Inspect `verification_timeline` label `between_2_and_5_years`: recall is 0.3000 over support 40.
- Inspect `evidence_status` label `No`: recall is 0.3500 over support 20.
- Review `verification_timeline` confusion `between_2_and_5_years` -> `already` (19 rows) before adding new rules.
- Review `promise_status` confusion `No` -> `Yes` (17 rows) before adding new rules.
- Review `promise_status` confusion `Yes` -> `No` (13 rows) before adding new rules.

## Anti-Hallucination Note

The suggestions above are generated only from the prediction/truth comparison in this report. They are not proof of root cause; inspect the cited IDs and confusion pairs before changing code.
