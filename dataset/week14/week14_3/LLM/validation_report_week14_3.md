# Validation Evidence Report

- Generated: 2026-06-02 05:56:19
- Prediction file: `E:\project\test510\week14_runs\week14_3\LLM_pipeline_pred_week14_3.json`
- Truth file: `E:\project\test510\dataset\week14\week14_3\val_grouped.json`
- Input file: `E:\project\test510\week14_runs\week14_3\val_formal_input.json`
- Prediction rows: 200
- Truth rows: 200
- Weighted score: `0.505805`

## Score Summary

| Field | Weight | Macro F1 | Weighted component | Truth distribution | Prediction distribution |
|---|---:|---:|---:|---|---|
| promise_status | 0.20 | 0.959793 | 0.191959 | Yes=164, No=36 | Yes=159, No=41 |
| verification_timeline | 0.15 | 0.198001 | 0.029700 | already=79, between_2_and_5_years=44, more_than_5_years=40, N/A=36, within_2_years=1 | N/A=129, between_2_and_5_years=49, more_than_5_years=19, already=3 |
| evidence_status | 0.30 | 0.751223 | 0.225367 | Yes=132, N/A=36, No=32 | Yes=148, N/A=41, No=11 |
| evidence_quality | 0.35 | 0.167940 | 0.058779 | Clear=111, N/A=68, Not Clear=21 | N/A=165, Not Clear=19, Clear=12, Misleading=4 |

## promise_status

### Per-Label Metrics

| Label | Precision | Recall | F1 | Support |
|---|---:|---:|---:|---:|
| Yes | 1.000000 | 0.969512 | 0.984520 | 164 |
| No | 0.878049 | 1.000000 | 0.935065 | 36 |

### Confusion Matrix

Rows are truth labels; columns are predicted labels.

| Truth \ Pred | Yes | No |
|---|---:|---:|
| Yes | 159 | 5 |
| No | 0 | 36 |

### Largest Gaps

- `Yes` -> `No`: 5 rows

### Example Mismatches

- ID `10146` true=`Yes` pred=`No` text=`我們遵循保證作業的國際最佳實務，包括國際審計與保證標準委員會頒布的《國際保證作業標準》（ISAE）3000（修訂版）—非屬歷史財務資訊審計與核閱的保證作業》，執行了數據保證查驗作業。為確保保證程序的一致性，我們依據 DNV 的保證方法學 VeriSustain 執行工作，僅應用與本次活動特定目的的相關的部分。此方法學確保遵循倫理要求，並要求規劃與執行保證作業以達到預期保證等級。 Professional ESG Sustainab...`
- ID `10244` true=`Yes` pred=`No` text=`導入產品永續性及生產 a. 減少材料使用 b. 採用回收材料 c. 模組化設計 d. 最佳運輸材積設計 e. 綠色生產製造 Professional ESG Sustainability Report Analysis Assistant. Extract text from a scanned image of a corporate ESG report. * Full text extraction. * Tables mu...`
- ID `10407` true=`Yes` pred=`No` text=`聯發科技提供具競爭力的薪酬福利、多元學習環境及具成就感的工作內容，吸引全球優秀人才。2024 年全球計畫招聘 1,440 人，共收到 21,680 份履歷，為預計招聘人數的 15 倍，聘用到任率約 85%，展現具吸引力的雇主品牌。 Professional ESG Sustainability Report Analysis Assistant. Extract text from a scanned page of an ESG...`
- ID `10644` true=`Yes` pred=`No` text=`本公司內部績效評核分別以「董事會績效考核自評問卷」、「董事成員績效評估自評問卷」、「薪酬委員會績效考核自評問卷」與「審計委員會績效考核自評問卷」進行評估，滿分為 5 分 ( 非常同意 5 分；同意 4 分；普通 3 分；不同意 2 分；非常不同意 1 分)，2024 年董事會暨功能性委員會績效評估結果皆高於 4.5 分，整體績效俱佳，董事及功能性委員會對於各項評核指標運作多為非常認同，整體運作良好，符合公司治理要求。本公司外部評核...`
- ID `10659` true=`Yes` pred=`No` text=`以經營理念出發制定本公司「永續發展實務守則」，並勾勒出本公司「永續發展政策」，透過企業公民擔當，提升國家經濟貢獻，改善員工、社區、社會之生活品質，促進以永續發展為本之競爭優勢，實踐永續發展之目標。 Professional ESG Sustainability Report Analysis Assistant. An image (two pages of an ESG report). 1. Complete text ext...`

## verification_timeline

### Per-Label Metrics

| Label | Precision | Recall | F1 | Support |
|---|---:|---:|---:|---:|
| already | 0.333333 | 0.012658 | 0.024390 | 79 |
| within_2_years | 0.000000 | 0.000000 | 0.000000 | 1 |
| between_2_and_5_years | 0.244898 | 0.272727 | 0.258065 | 44 |
| more_than_5_years | 0.421053 | 0.200000 | 0.271186 | 40 |
| N/A | 0.279070 | 1.000000 | 0.436364 | 36 |

### Confusion Matrix

Rows are truth labels; columns are predicted labels.

| Truth \ Pred | already | within_2_years | between_2_and_5_years | more_than_5_years | N/A |
|---|---:|---:|---:|---:|---:|
| already | 1 | 0 | 28 | 6 | 44 |
| within_2_years | 0 | 0 | 0 | 0 | 1 |
| between_2_and_5_years | 2 | 0 | 12 | 5 | 25 |
| more_than_5_years | 0 | 0 | 9 | 8 | 23 |
| N/A | 0 | 0 | 0 | 0 | 36 |

### Largest Gaps

- `already` -> `N/A`: 44 rows
- `already` -> `between_2_and_5_years`: 28 rows
- `between_2_and_5_years` -> `N/A`: 25 rows
- `more_than_5_years` -> `N/A`: 23 rows
- `more_than_5_years` -> `between_2_and_5_years`: 9 rows
- `already` -> `more_than_5_years`: 6 rows
- `between_2_and_5_years` -> `more_than_5_years`: 5 rows
- `between_2_and_5_years` -> `already`: 2 rows

### Example Mismatches

- ID `10004` true=`already` pred=`N/A` text=`面對這些全球與國內政策的推動，富邦人壽秉持永續經營理念，積極透過永續金融的投資力量，引導被投資公司與企業進行永續轉型，除非資金明確用於綠能轉型計畫，不再新增投資燃煤比重超過 50% 的電廠。同時，針對燃料煤開採、運輸業、燃料煤發電及非典型油氣產業，制定嚴格的准入與撤資標準，積極引導資金流向低碳與可再生能源領域，展現對環境永續的堅定承諾，並連續 4 年榮獲「台灣永續投資典範機構獎 – 機構影響力 (壽險組)」殊榮，在責任投資與推動企...`
- ID `10021` true=`already` pred=`N/A` text=`自 2005 年起陸續展開溫室氣體盤查作業，並通過第三方 ISO 14064 查證，以追蹤各營運據點之溫室氣體排放情況，持續積極尋求各項減碳與低碳方案。同時逐步導入子公司盤查作業。2024 年溫室氣體相較前一年度下降 3.2%，並首次進行內部盤查子公司溫室氣體作業。 Professional ESG Sustainability Report Analysis Assistant. Extract text from the pr...`
- ID `10065` true=`already` pred=`N/A` text=`台積公司藉由 TDDM 方法學，每年依照不同的調查目的，執行重大議題的盤點與分析，形塑一個完整的調查週期。首年進行議題蒐集、調查與分析，重新定義具重大性的永續議題，並於次一年度檢視重大議題的變化，探討重大議題之間的因果關係，進而掌握重大議題與行動方案間的相互關聯，確保行動有效性。民國 112 年，台積公司邀請 1,693 位內外部利害關係人，以及超過 233 位負責推動永續業務的公司主管及同仁綜合考量利害關係人關注、組織營運衝擊與...`
- ID `10072` true=`already` pred=`N/A` text=`投入光電及儲能案場 加入「富邦能源綠能投資平台」，在2024年加入「富邦能源綠能投資平台」，借重泓德能源的技術與經驗，投資380MW光電案場以及開發354 MW儲能案場，助力台灣再生能源儲能未來。 Professional ESG Sustainability Report Analysis Assistant. Extract text from a scanned page of an ESG report. * Full t...`
- ID `10086` true=`already` pred=`N/A` text=`為了讓 ISO 20400 永續採購指南系統建置的相關成員了解本公司導入永續採購的目的、對永續採購指南系統要求有足夠的認知、以及工具手法的運用，導入的過程共進行 4 場相關訓練課程 ( 共 133 人次參與 ) 與 9 場的輔導會議 ( 共 230 人次參與 )。同時將永續採購精神與要求融入既有的採購流程與供應商管理，並新增及修改內部文件。 Professional ESG Sustainability Report Analys...`
- ID `10119` true=`already` pred=`N/A` text=`和碩為了使全體員工都能獲得最完善的關注與照顧，我們鼓勵同仁利用各種管道提出建議，也設立多元溝通管道使同仁可充分表達意見，讓公司可以多方聽取同仁的聲音，藉以改善組織文化與環境氛圍。和碩視員工為重要的資產，除了讓員工樂於工作外，更重視員工生活與工作平衡點之間的經營，適時提供員工關懷及幫助，同時促進企業的高度生產力及員工穩定性。為使同仁隨時掌握公司脈動與經營方向，CEO也親自參與分批舉辦之「與CEO有約」，提供不同層次的溝通方式，透過面...`
- ID `10120` true=`already` pred=`N/A` text=`金控及轄下子公司之企業核心價值為「誠信、親切、專業、創新」，首重以「誠信」是公司治理及企業永續經營的根本，而本公司本於廉潔、透明及負責之經營理念，建構誠信經營之企業文化及健全發展，以建立良好商業運作模式與風險控管機制，創造永續發展之經營環境，爰參照「富邦金控誠信經營守則」制定「富邦人壽誠信經營守則」並經董事會決議通過，並於公司內部網站、法令遵循網站公告予內、外勤同仁知悉。 Professional ESG Sustainabili...`
- ID `10140` true=`already` pred=`N/A` text=`自 2024 第二季度起，研華秉持 ESG 理念，在環境面積極推動數位化以降低碳足跡，並有效運用雲端資源來提高能效。透過優化客服聊天機器人，導入 AI Agent 為客戶提供即時的產品資訊問答與多元服務。該年度由 AI Agent 協助之對話數量月增長率達 26.1%，對話滿意度亦提升 10%。 Professional ESG Sustainability Report Analysis Assistant. An image ...`

## evidence_status

### Per-Label Metrics

| Label | Precision | Recall | F1 | Support |
|---|---:|---:|---:|---:|
| Yes | 0.851351 | 0.954545 | 0.900000 | 132 |
| No | 0.818182 | 0.281250 | 0.418605 | 32 |
| N/A | 0.878049 | 1.000000 | 0.935065 | 36 |

### Confusion Matrix

Rows are truth labels; columns are predicted labels.

| Truth \ Pred | Yes | No | N/A |
|---|---:|---:|---:|
| Yes | 126 | 2 | 4 |
| No | 22 | 9 | 1 |
| N/A | 0 | 0 | 36 |

### Largest Gaps

- `No` -> `Yes`: 22 rows
- `Yes` -> `N/A`: 4 rows
- `Yes` -> `No`: 2 rows
- `No` -> `N/A`: 1 rows

### Example Mismatches

- ID `10001` true=`No` pred=`Yes` text=`聯發科技除在「工作規則」中依照勞基法明確規定「員工在產假期間公司不得終止勞動契約」外，為支持同仁與其家人度過人生不同階段，自 2024 年起提供女性員工在分娩前後計有 12 週共 84 天的產假；男性員工則可於其配偶懷孕期間陪同產檢或生（流）產日及前後 15 日間請假陪伴，兩者合計共有 10 天陪產（檢）假可運用，陪產（檢）假期間工資照常給付。 Professional ESG Sustainability Report Anal...`
- ID `10037` true=`No` pred=`Yes` text=`誠信經營是公司治理內部控制機制重要的一環。研華會在事前辨識各項法令規章，並與內部相關單位溝通、衡量公司相關規則之制定與落實，以求符合法規。誠信經營中之法令遵循、反貪腐與反競爭概念與社會責任與公司商譽有重大關聯，為研華永續經營重點之一。 Professional ESG sustainability report analysis assistant. Extract text from a scanned page of a co...`
- ID `10081` true=`No` pred=`Yes` text=`麥寮社教 ESG 永續發展示範園區致力於打造完整的生活機能與公共設施，融合教育、文化與生活，提升居民生活品質，成為地方特色與現代化社教的標竿，突破鄉鎮格局。園區同時作為社區休憩據點，結合戶外休閒、展覽表演及藝文活動，提供舒適的生活場域，促進親子交流，並營造友善的都市環境。 Professional ESG Sustainability Report Analysis Assistant. Extract all text from...`
- ID `10091` true=`No` pred=`Yes` text=`本公司依據人權風險評估結果，訂定相對應之減緩與補償措施，並定期追蹤執行結果。2024 年之人權關注議題中無高風險項目，故針對中風險項目設定預防與減緩措施。 Professional ESG Sustainability Report Analysis Assistant. An image of a page from a corporate ESG report (Yang Ming Marine Transport Corp....`
- ID `10118` true=`No` pred=`Yes` text=`本屆競賽冠軍團隊——廣太綠能，擁有微水力發電技術，與其高度應用潛力。於競賽提案規劃將微水力發電模組導入至日月光廠區的中水回收系統，運用既有管線的高低差進行發電，供應廠區內部用電。未來該技術亦可擴大應用，有助於推動綠電在地化發展，強化我國再生能源產業的韌性與自主性。 Professional ESG Sustainability Report Analysis Assistant. Extract all text from a s...`
- ID `10181` true=`No` pred=`Yes` text=`台新持續培養數位金融技能，除了藉由教育訓練提升現有員工的科技專業技能外，也積極招募外部數位科技人才，以快速提升整體數位技能。透過掌握金融科技發展趨勢，未來台新將積極布建數位金融生態環境，並且因應新世代趨勢進行科技人才培育，以更積極、穩健的腳步，落實企業永續經營。 Professional ESG Sustainability Report Analysis Assistant. Extract text from a scanne...`
- ID `10188` true=`No` pred=`Yes` text=`展望未來，富邦人壽將持續以「正向力量 豐富生命」的品牌精神為指引，深化「低碳、數位、激勵、影響」四大策略推動，積極實現永續願景。作為臺灣保險業的領導品牌，富邦人壽將持續發揮金融影響力，以創新思維與具體行動，為臺灣的永續發展注入更多正向動能。我們相信，唯有將 ESG 理念深植於企業文化，並以實際行動展現永續承諾，才能真正實現經濟、環境和社會的均衡發展，共同打造更美好的永續未來。 Professional ESG Sustainabi...`
- ID `10253` true=`No` pred=`Yes` text=`本公司對利害關係人建立相應之議合方式與管道，傾聽意見與回饋，每年亦定期向董事會陳報與利害關係人之溝通實績。 Professional ESG Sustainability Report Analysis Assistant. Extract text from a scanned page of an ESG report. Convert tables to Markdown format. Maintain precision...`

## evidence_quality

### Per-Label Metrics

| Label | Precision | Recall | F1 | Support |
|---|---:|---:|---:|---:|
| Clear | 0.583333 | 0.063063 | 0.113821 | 111 |
| Not Clear | 0.000000 | 0.000000 | 0.000000 | 21 |
| Misleading | 0.000000 | 0.000000 | 0.000000 | 0 |
| N/A | 0.393939 | 0.955882 | 0.557940 | 68 |

### Confusion Matrix

Rows are truth labels; columns are predicted labels.

| Truth \ Pred | Clear | Not Clear | Misleading | N/A |
|---|---:|---:|---:|---:|
| Clear | 7 | 18 | 2 | 84 |
| Not Clear | 3 | 0 | 2 | 16 |
| Misleading | 0 | 0 | 0 | 0 |
| N/A | 2 | 1 | 0 | 65 |

### Largest Gaps

- `Clear` -> `N/A`: 84 rows
- `Clear` -> `Not Clear`: 18 rows
- `Not Clear` -> `N/A`: 16 rows
- `Not Clear` -> `Clear`: 3 rows
- `N/A` -> `Clear`: 2 rows
- `Not Clear` -> `Misleading`: 2 rows
- `Clear` -> `Misleading`: 2 rows
- `N/A` -> `Not Clear`: 1 rows

### Example Mismatches

- ID `10004` true=`Clear` pred=`N/A` text=`面對這些全球與國內政策的推動，富邦人壽秉持永續經營理念，積極透過永續金融的投資力量，引導被投資公司與企業進行永續轉型，除非資金明確用於綠能轉型計畫，不再新增投資燃煤比重超過 50% 的電廠。同時，針對燃料煤開採、運輸業、燃料煤發電及非典型油氣產業，制定嚴格的准入與撤資標準，積極引導資金流向低碳與可再生能源領域，展現對環境永續的堅定承諾，並連續 4 年榮獲「台灣永續投資典範機構獎 – 機構影響力 (壽險組)」殊榮，在責任投資與推動企...`
- ID `10021` true=`Clear` pred=`N/A` text=`自 2005 年起陸續展開溫室氣體盤查作業，並通過第三方 ISO 14064 查證，以追蹤各營運據點之溫室氣體排放情況，持續積極尋求各項減碳與低碳方案。同時逐步導入子公司盤查作業。2024 年溫室氣體相較前一年度下降 3.2%，並首次進行內部盤查子公司溫室氣體作業。 Professional ESG Sustainability Report Analysis Assistant. Extract text from the pr...`
- ID `10033` true=`Clear` pred=`N/A` text=`為瞭解實體風險對本行據點資產之風險衝擊，針對本行各營運據點進行實體風險評估分析。本行以實體風險危害度 1~3 級 (24 小時內極端降雨頻率)、脆弱度 1~10 級 (淹水潛勢、坡地災害) 及暴露度 1~10 級 (暴險金額) 繪製風險敏感地圖，分別採用 RCP 8.5 及 RCP 2.6 作為風險衝擊之假設情境，進行本行據點資產在世紀中 (2036~2065) 的暴險分析，並提出對應之氣候風險管理策略。 Professional...`
- ID `10039` true=`Clear` pred=`N/A` text=`聯電集團除持續提升能源效率外，亦規劃多元能源使用，積極設置廠內再生能源，更將太陽能系統列為新建廠房標準設計建置項目，發電量連續 5 年增長。2024 年原規劃設置太陽光電 500kW 計畫調整，整併於 2025 年設置合計約 900kW。至 2024 年止，聯電集團已安裝峰值發電容量超過 14,000 瓩 (kWp) 之太陽光電系統，預估每年發電量達 15,000 MWh。惟太陽光電主要受氣候等因素影響，例如 2024 年台灣地區...`
- ID `10054` true=`Clear` pred=`N/A` text=`再生能源發展為全球能源轉型重要議題，為有效降低瑞昱集團全球營運據點碳排放量，瑞昱設定全集團於 2030 年再生能源佔比達 50 % 之目標。我們彙整各營運據點能源使用數據，掌握再生能源使用契機。2023 年瑞昱子公司蘇州瑞晟已完成簽約購買國際再生能源憑證 (I-REC)，自 2024 年起該廠區範疇二電力碳排量達淨零；瑞昱美國子公司 Cortina-Access 亦已於 2024 年向當地電力公司 San Jose Clean E...`
- ID `10065` true=`Clear` pred=`N/A` text=`台積公司藉由 TDDM 方法學，每年依照不同的調查目的，執行重大議題的盤點與分析，形塑一個完整的調查週期。首年進行議題蒐集、調查與分析，重新定義具重大性的永續議題，並於次一年度檢視重大議題的變化，探討重大議題之間的因果關係，進而掌握重大議題與行動方案間的相互關聯，確保行動有效性。民國 112 年，台積公司邀請 1,693 位內外部利害關係人，以及超過 233 位負責推動永續業務的公司主管及同仁綜合考量利害關係人關注、組織營運衝擊與...`
- ID `10067` true=`Clear` pred=`N/A` text=`統一超商每年持續投入大量教育訓練資源，針對不同階層、部門設計規劃不同課程，包含新進人員訓練、階層別訓練、門市、後勤公開班、通識課程、及各單位專業訓練。2024 年教育訓練總費用投入共 86,888 仟元，平均每人訓練費用 9,459 元，相較去年人均訓練費用多 2,424 元；全公司教育訓練總時數為 134,624 小時，平均每人受訓時數為 14.66 小時（註）。2024 年因應同仁工作型態，除了持續開辦實體課程，也積極打造數位...`
- ID `10072` true=`Clear` pred=`N/A` text=`投入光電及儲能案場 加入「富邦能源綠能投資平台」，在2024年加入「富邦能源綠能投資平台」，借重泓德能源的技術與經驗，投資380MW光電案場以及開發354 MW儲能案場，助力台灣再生能源儲能未來。 Professional ESG Sustainability Report Analysis Assistant. Extract text from a scanned page of an ESG report. * Full t...`

## Evidence-Based Next Suggestions

- Focus first on `evidence_quality` because it has the lowest macro F1 in this report (0.1679).
- Inspect `evidence_quality` label `Not Clear`: recall is 0.0000 over support 21.
- Inspect `verification_timeline` label `within_2_years`: recall is 0.0000 over support 1.
- Inspect `verification_timeline` label `already`: recall is 0.0127 over support 79.
- Review `evidence_quality` confusion `Clear` -> `N/A` (84 rows) before adding new rules.
- Review `verification_timeline` confusion `already` -> `N/A` (44 rows) before adding new rules.
- Review `verification_timeline` confusion `already` -> `between_2_and_5_years` (28 rows) before adding new rules.

## Anti-Hallucination Note

The suggestions above are generated only from the prediction/truth comparison in this report. They are not proof of root cause; inspect the cited IDs and confusion pairs before changing code.
