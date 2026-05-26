# Validation Evidence Report

- Generated: 2026-05-26 00:36:53
- Prediction file: `E:\project\test510\week13_runs\week13_5\LLM_pipeline_pred_week13_5.json`
- Truth file: `E:\project\test510\dataset\week13\week13_5\val_grouped.json`
- Input file: `E:\project\test510\week13_runs\week13_5\val_formal_input.json`
- Prediction rows: 200
- Truth rows: 200
- Weighted score: `0.626504`

## Score Summary

| Field | Weight | Macro F1 | Weighted component | Truth distribution | Prediction distribution |
|---|---:|---:|---:|---|---|
| promise_status | 0.20 | 0.757576 | 0.151515 | Yes=157, No=43 | Yes=173, No=27 |
| verification_timeline | 0.15 | 0.547011 | 0.082052 | already=64, between_2_and_5_years=52, N/A=43, more_than_5_years=40, within_2_years=1 | already=98, more_than_5_years=48, N/A=28, between_2_and_5_years=24, within_2_years=2 |
| evidence_status | 0.30 | 0.779051 | 0.233715 | Yes=131, N/A=43, No=26 | Yes=122, N/A=49, No=29 |
| evidence_quality | 0.35 | 0.454920 | 0.159222 | Clear=106, N/A=69, Not Clear=25 | Clear=102, N/A=78, Not Clear=18, Misleading=2 |

## promise_status

### Per-Label Metrics

| Label | Precision | Recall | F1 | Support |
|---|---:|---:|---:|---:|
| Yes | 0.872832 | 0.961783 | 0.915152 | 157 |
| No | 0.777778 | 0.488372 | 0.600000 | 43 |

### Confusion Matrix

Rows are truth labels; columns are predicted labels.

| Truth \ Pred | Yes | No |
|---|---:|---:|
| Yes | 151 | 6 |
| No | 22 | 21 |

### Largest Gaps

- `No` -> `Yes`: 22 rows
- `Yes` -> `No`: 6 rows

### Example Mismatches

- ID `10036` true=`No` pred=`Yes` text=`2024 年提報董事會報告 - 陳報本公司合併報表子公司溫室氣體盤查及查證執行進度，共 4 次。 - 提報永續中長期目標設定情形。 - 提報並通過核議案訂定本公司維護生物多樣性暨零毀林承諾及修正本公司供應鏈管理政策。 - 提報本公司 2023 年永續報告書核議案，說明永續報告書編制內容包含： 1. 2023 年永續目標執行實績及 2024 年永續目標擬定 2. 重大議題鑑別、重要利害關係人鑑別、溝通管道、回應方式及頻率等溝通情形 ...`
- ID `10133` true=`No` pred=`Yes` text=`本報告書之組織邊界涵蓋國泰金控暨旗下主要子公司：國泰人壽、國泰世華銀行、國泰產險、國泰綜合證券、國泰投信，營運區域以台灣為主要核心揭露，並依資訊揭露需求，納入重要投資與授信對象、供應商及客戶，與價值鏈外更廣泛利害關係人之社區與社會大眾相關內容。針對重大議題，對應 GRI 準則揭露其相關內容，同時訂定重大議題短、長期目標，並揭露於本報告書。 Professional ESG Sustainability Report Analysi...`
- ID `10250` true=`No` pred=`Yes` text=`以顧客為核心，用獨特的創意與巧思，從推動永續金融應用，到建立「防詐藍圖」，展現玉山在永續發展與民眾資產保護上的實際行動。透過科技驅動、場域深入與跨界合作，玉山不斷突破既有框架，打造創新服務與合作模式，堅定前行並創造長遠價值。 Professional ESG Sustainability Report Analysis Assistant. Extract all text from the provided image of a...`
- ID `10265` true=`No` pred=`Yes` text=`PFAS具有致癌、持久不分解和易遷移的特性，同時該群組的物質具有優良的熱穩定性，因此該物質群組在世界範圍各行業的使用廣泛，歐盟的化學品管理局與美國環保署近年非常關注全氟與多氟烷基物質(PFAS)的限制使用情況，並陸續公佈相應的法規要求。AVC 2023年已發佈針對該物質群組的限制使用規範，同步進行全面排查，加強與上游供應商、下游客戶之間的溝通，完成相關方之間的物質揭露、物質汰換資訊的傳遞。2024年11月7日歐盟化學品管理局新增磷...`
- ID `10328` true=`No` pred=`Yes` text=`2024 緯創女子公開賽創下里程碑，首度實現 TLPGA 台灣女子職業高爾夫協會與 LET 歐洲女子巡迴賽的跨國合作認證。本賽事不僅躍升為歐巡重要賽事，更成為台巡史上最高獎金、最具規模的旗艦賽事。今年總獎金突破 100 萬美元，冠軍獎金高達 20 萬美元，吸引來自歐巡45 位菁英選手與台巡好手，總計 108 位頂尖選手齊聚，共同見證台灣職業高爾夫發展的重要里程碑。緯創資通自 2006 年即投入 TLPGA 賽事贊助，獎金規模逐年擴...`
- ID `10353` true=`No` pred=`Yes` text=`2024年所受理之客戶申訴與爭議案件為104件，7天內處理完成件數87件，處理完成比例84%，高於本公司客訴處理目標60%。1. 實際客訴48件均已妥處並結案： Professional ESG Sustainability Report Analysis Assistant. Extract all text from the provided image. Convert tables precisely into Markd...`
- ID `10389` true=`No` pred=`Yes` text=`本公司針對職場人權訂定「員工意見申訴及處理辦法」、「性騷擾防治申訴調查與懲戒處理辦法」，同仁可藉由專線電話、傳真、電子信箱、工會等多元管道進行申訴，相關申訴及意見反應案件均由專人負責處理，對申訴個案盡絕對保密之義務，目前申訴管道均正常運作。本公司亦實施「執行職務遭受不法侵害預防計畫書」，依計畫書執行各單位危害辨識風險評估及職安教育訓練等預防措施，成立處理小組（包含人事部門代表 / 法務代表 / 工會代表 / 職安人員），如有不法侵...`
- ID `10399` true=`No` pred=`Yes` text=`本公司參加各類協會，定期向主管機關提出政策建言，並透過協會廣泛和國際組織進行交流，協助政府推行金融政策，健全業務發展及增進同業之公共利益。以台北市銀行同業公會為例，配合主管機關推動綠色金融政策，協助會員機構辦理再生能源產業融資。 Professional ESG Sustainability Report Analysis Assistant. Extract text from a scanned image of an ESG...`

## verification_timeline

### Per-Label Metrics

| Label | Precision | Recall | F1 | Support |
|---|---:|---:|---:|---:|
| already | 0.479592 | 0.734375 | 0.580247 | 64 |
| within_2_years | 0.500000 | 1.000000 | 0.666667 | 1 |
| between_2_and_5_years | 0.583333 | 0.269231 | 0.368421 | 52 |
| more_than_5_years | 0.458333 | 0.550000 | 0.500000 | 40 |
| N/A | 0.785714 | 0.511628 | 0.619718 | 43 |

### Confusion Matrix

Rows are truth labels; columns are predicted labels.

| Truth \ Pred | already | within_2_years | between_2_and_5_years | more_than_5_years | N/A |
|---|---:|---:|---:|---:|---:|
| already | 47 | 0 | 3 | 11 | 3 |
| within_2_years | 0 | 1 | 0 | 0 | 0 |
| between_2_and_5_years | 22 | 0 | 14 | 13 | 3 |
| more_than_5_years | 13 | 0 | 5 | 22 | 0 |
| N/A | 16 | 1 | 2 | 2 | 22 |

### Largest Gaps

- `between_2_and_5_years` -> `already`: 22 rows
- `N/A` -> `already`: 16 rows
- `between_2_and_5_years` -> `more_than_5_years`: 13 rows
- `more_than_5_years` -> `already`: 13 rows
- `already` -> `more_than_5_years`: 11 rows
- `more_than_5_years` -> `between_2_and_5_years`: 5 rows
- `between_2_and_5_years` -> `N/A`: 3 rows
- `already` -> `between_2_and_5_years`: 3 rows

### Example Mismatches

- ID `10037` true=`between_2_and_5_years` pred=`already` text=`誠信經營是公司治理內部控制機制重要的一環。研華會在事前辨識各項法令規章，並與內部相關單位溝通、衡量公司相關規則之制定與落實，以求符合法規。誠信經營中之法令遵循、反貪腐與反競爭概念與社會責任與公司商譽有重大關聯，為研華永續經營重點之一。 Professional ESG sustainability report analysis assistant. Extract text from a scanned page of a co...`
- ID `10113` true=`between_2_and_5_years` pred=`already` text=`我們深知永續議題的管理，是企業持續改善與長遠發展的關鍵。其包含企業面對議題如何整合內部資源擬定相關管理方針與各階段利害關係人的議合溝通。本公司透過多元管道蒐集相關回覆和建議，將其納入公司營運規劃中。 Professional ESG Sustainability Report Analysis Assistant. Extract text from a scanned image of an ESG report. Conver...`
- ID `10146` true=`between_2_and_5_years` pred=`already` text=`我們遵循保證作業的國際最佳實務，包括國際審計與保證標準委員會頒布的《國際保證作業標準》（ISAE）3000（修訂版）—非屬歷史財務資訊審計與核閱的保證作業》，執行了數據保證查驗作業。為確保保證程序的一致性，我們依據 DNV 的保證方法學 VeriSustain 執行工作，僅應用與本次活動特定目的的相關的部分。此方法學確保遵循倫理要求，並要求規劃與執行保證作業以達到預期保證等級。 Professional ESG Sustainab...`
- ID `10186` true=`between_2_and_5_years` pred=`already` text=`國巨各廠區依據環境政策執行環境管理系統，考量廠區地理位置、氣候、空氣品質、水質、土地使用、既有之污染物、自然資源可取得性及生物多樣性等環境狀況。為保持營運必須之穩定水資源，並管控國巨原水取用及廢水排水對環境造成之影響，各廠區皆訂定用水管理目標，在節約用水的同時，更積極提升循環回收水及用水效益。 Professional ESG Sustainability Report Analysis Assistant. Extract te...`
- ID `10226` true=`between_2_and_5_years` pred=`already` text=`和泰集團自 2022 年啟動「原夢代表隊」公益計畫，攜手集團內各事業體，共同整合資源，長期支持新竹縣尖石鄉嘉興國小與五峰鄉桃山國小的泰雅族兒童合唱團。此計畫旨在幫助這些擁有音樂天賦的孩子，在成長與學習的過程中，接觸多元職業與環境，拓展視野並提升對未來職業的想像。 Professional ESG Sustainability Report Analysis Assistant. Extract all text from the ...`
- ID `10227` true=`between_2_and_5_years` pred=`already` text=`鴻海已展示了有效鑑別和公平評估對利害關係者的過程，其中已刻一系對來自廣泛來源的環境、社會和治理主題，對於其營運活動所帶來的衝擊的過程。其鑑別評估已透過定性化和定量相結合的目標愈來達成，本查證可持續提請佐證管道，透過多元管道與利害關係人揭露重大主題進展與成果，並透過決策流程提升與各方的互信與合作，持續優化企業溝通競爭力。 Professional ESG Sustainability Report Analysis Assistan...`
- ID `10235` true=`between_2_and_5_years` pred=`already` text=`TOYOTA 自 2017 年 4 月啟動「一車一樹」植樹計畫，每售出一台 TOYOTA 新車，即為車主在台灣種下一棵樹，投入經費更超過三億元，在財團法人慈心有機農業發展基金會的協助下，為全台 17 縣市及離島澎湖、金門、馬祖陸續建立起綠色長城。自 2019 年起舉辦車主志工植樹活動，邀請 TOYOTA 車主與民眾共同響應，讓每一位參與者體驗親手種下樹苗的感動，一起成為守護台灣海岸線的重要推手。 2024 年也於宜蘭壯圍海岸舉辦「...`
- ID `10337` true=`between_2_and_5_years` pred=`already` text=`為預防及減緩重大職業安全衛生風險與衝擊，萬海定期針對現有營運活動進行風險評估。辦公室依照《安衛風險評估管制程序》進行管控，碼頭則參照《職安衛危害鑑別及風險評估管理程序》及《組織環境議題鑑別及風險機會管理程序》，依據制定的風險評估時機，辦理風險評估作業。 Professional ESG Sustainability Report Analysis Assistant. Extract text from a scanned pag...`

## evidence_status

### Per-Label Metrics

| Label | Precision | Recall | F1 | Support |
|---|---:|---:|---:|---:|
| Yes | 0.926230 | 0.862595 | 0.893281 | 131 |
| No | 0.482759 | 0.538462 | 0.509091 | 26 |
| N/A | 0.877551 | 1.000000 | 0.934783 | 43 |

### Confusion Matrix

Rows are truth labels; columns are predicted labels.

| Truth \ Pred | Yes | No | N/A |
|---|---:|---:|---:|
| Yes | 113 | 15 | 3 |
| No | 9 | 14 | 3 |
| N/A | 0 | 0 | 43 |

### Largest Gaps

- `Yes` -> `No`: 15 rows
- `No` -> `Yes`: 9 rows
- `Yes` -> `N/A`: 3 rows
- `No` -> `N/A`: 3 rows

### Example Mismatches

- ID `10003` true=`Yes` pred=`No` text=`III. 產品危害物質減免 (HSF) 短、中、長期目標設定 **1. 2024 年 目標和實績** * 已達標 * 詳述於 "產品各階段危害物質減免風險管理目標與成效" **2. 短期目標 2025~2026 年** * 監控 PFAS 中有害物質管制要求 * 減少 RoHS 豁免零件之使用，往 Lead Free 持續前進。 **3. 中長期目標 2026~2027 年** * 優化綠色管理系統審查作業提升效率。 Profes...`
- ID `10057` true=`Yes` pred=`No` text=`中華電信持續以 360 度全方位視角推動數位包容行動，多年來持續投入企業資源，普及電信基礎建設，確保全民均享基本通訊權益。我們發揮在資通訊領域的專業與核心優勢，致力於縮小數位落差，開拓數位時代下的多元可能。以「縮短數位落差」及「創造數位機會」兩大社會投資主軸，投注心力推動「企業志工」參與在地社區服務，積極賦能當地社區，藉助數位科技創造更多機會。 Professional ESG Sustainability Report Anal...`
- ID `10090` true=`Yes` pred=`No` text=`呼應萬海的企業精神與經營理念，企業營運以人為本，從內部到外部建立與利害關係人的信任關係。對內透過培養全體員工永續意識、視員工的需求提供多元職涯發展與生活照護，高度尊重人權以建立與員工之間的互信；對外網羅優秀的人才，為專業人才提供可發揮所能的舞台。透過全方位的安全管理，確保在營運過程中達到人安、航安、貨安，打造領先業界的高度安全性，以維持穩健的經營與競爭力。此外，萬海與合作夥伴攜手合作，共同發揮社會影響力，持續關注海洋生態與水資源議...`
- ID `10217` true=`Yes` pred=`No` text=`在緯創的戰略合作夥伴關係中，供應商扮演著至關重要的角色。我們深知，與供應商的合作不僅是實現業務成功的基石，也是落實公司永續發展目標的關鍵要素。因此，我們將永續責任採購列為六大永續發展策略之一，將永續發展的理念融入採購管理中，並從風險管理、競爭優勢和成本優化三大驅動力出發，遵循永續採購指南 (ISO 20400)，同時依循 RBA 行為準則，以確保供應商在環境、社會和治理方面，持續提升績效。 Professional ESG Sus...`
- ID `10303` true=`Yes` pred=`No` text=`企業價值觀是形塑企業文化的基石，也是推動永續發展的核心動能。中華電信致力於推動公司治理的四大價值觀，望將其內化為全體同仁的日常行為準則，引領全員朝共同目標邁進。我們堅信，價值觀的實踐不僅能凝聚團隊向心力、提升營運效率，更是驅動企業持續續創新與永續成長的關鍵力量，為公司開創長期穩健且具韌性的發展基礎。 Professional ESG Sustainability Report Analysis Assistant. Extract...`
- ID `10360` true=`Yes` pred=`No` text=`TSMC ESG AWARD 為台積公司推動永續文化的核心平台，鼓勵同仁提出連結公司 ESG 五大方向的新創好點子，並表彰組織的永續實績，以永續力促進創新力，創造美好改變。 Professional ESG Sustainability Report Analysis Assistant. Extract all text from the provided image of a corporate ESG report page...`
- ID `10466` true=`Yes` pred=`No` text=`馬來西亞廠 (WYMY) 為第一個取得 GBI (Green Building Index) 綠色建築 Gold 等級認證之營運據點。將持續在全球各地落實綠色建築標準，強化環保與節能策略。推動自然保育與永續發展，以促進環保、公益及企業責任交流，實現人與環境共好及身心平衡。 Professional ESG Sustainability Report Analysis Assistant. Extract all text from...`
- ID `10683` true=`Yes` pred=`No` text=`為提升客戶服務品質，合庫每年與消費者議合，充分傾聽並瞭解消費者對金融商品及服務的意見。針對客訴案件，也建立完善的分級制度及處理流程，確保在時效內有效解決客戶問題，維護客戶權益。 Professional ESG Sustainability Report Analysis Assistant. Extract text from a scanned ESG report page. Full text extraction, pr...`

## evidence_quality

### Per-Label Metrics

| Label | Precision | Recall | F1 | Support |
|---|---:|---:|---:|---:|
| Clear | 0.833333 | 0.801887 | 0.817308 | 106 |
| Not Clear | 0.222222 | 0.160000 | 0.186047 | 25 |
| Misleading | 0.000000 | 0.000000 | 0.000000 | 0 |
| N/A | 0.769231 | 0.869565 | 0.816327 | 69 |

### Confusion Matrix

Rows are truth labels; columns are predicted labels.

| Truth \ Pred | Clear | Not Clear | Misleading | N/A |
|---|---:|---:|---:|---:|
| Clear | 85 | 12 | 2 | 7 |
| Not Clear | 10 | 4 | 0 | 11 |
| Misleading | 0 | 0 | 0 | 0 |
| N/A | 7 | 2 | 0 | 60 |

### Largest Gaps

- `Clear` -> `Not Clear`: 12 rows
- `Not Clear` -> `N/A`: 11 rows
- `Not Clear` -> `Clear`: 10 rows
- `N/A` -> `Clear`: 7 rows
- `Clear` -> `N/A`: 7 rows
- `Clear` -> `Misleading`: 2 rows
- `N/A` -> `Not Clear`: 2 rows

### Example Mismatches

- ID `10004` true=`Clear` pred=`Not Clear` text=`面對這些全球與國內政策的推動，富邦人壽秉持永續經營理念，積極透過永續金融的投資力量，引導被投資公司與企業進行永續轉型，除非資金明確用於綠能轉型計畫，不再新增投資燃煤比重超過 50% 的電廠。同時，針對燃料煤開採、運輸業、燃料煤發電及非典型油氣產業，制定嚴格的准入與撤資標準，積極引導資金流向低碳與可再生能源領域，展現對環境永續的堅定承諾，並連續 4 年榮獲「台灣永續投資典範機構獎 – 機構影響力 (壽險組)」殊榮，在責任投資與推動企...`
- ID `10035` true=`Clear` pred=`Not Clear` text=`本集團以獨立超然之精神執行稽核業務，隸屬於董事會，協助董事會及高階管理階層審查與評估風險管理是否有效運作，包含評估第一道及第二道防線監控之有效性，並適時提出改進建議。內部稽核單位建立及執行集團內部稽核制度，查核與評估內部控制之有效性，並定期向審計委員會及董事會報告。對本公司每年至少辦理 1 次一般業務查核。 Professional ESG Sustainability Report Analysis Assistant. Ext...`
- ID `10139` true=`Clear` pred=`Not Clear` text=`個人資料保護法新法施行前，本公司已具備維護個資之安全機制，包含制定「資料分級管理辦法」、「個人資料保護要點」、「資訊安全政策」、「資訊安全管理要點」等規範，明確制定個人資料之授權、使用、儲存、管理及銷毀等應遵循之保護程序，同時為展現高度重視客戶個人資料安全的堅持與承諾，並設立個人資料保護小組，確保落實個資法之執行。 Professional ESG Sustainability Report Analysis Assistant....`
- ID `10187` true=`Clear` pred=`Not Clear` text=`我們已建置完善的端到端資訊管理系統, 涵蓋從產品設計與開發、生產製造、採購與交貨至供應商管理的全流程。透過即時市場監控與回饋機制, 我們能快速響應市場變化, 做出最佳決策, 確保產品準時交付且符合質量與數量要求。主要生產基地分布於中國大陸的深圳、東莞、成都、武漢、嘉善, 以及越南河南, 同時在全球設有業務行銷與物流倉儲據點, 技術支援網絡隨時待命, 以便為來自亞洲、北美、南美及歐洲等地的客戶提供高效服務。為積極響應國際品牌客戶對永...`
- ID `10232` true=`Clear` pred=`Not Clear` text=`我們據以訂定 2023-2027 年中長期計畫，透過新世代商品及新形態服務導入，持續提升周邊價值鏈，加速移動轉型，期許讓和泰汽車及關係企業旗下各品牌，成為各產業中的領導標竿，透過「以新世代販賣思維，積極躍升市占率」、「智能服務及社群結合，融入顧客生活圈」、「策略轉型超前布局，價值鏈提升無上限」、「提升資源利用綜效，擴大集團規模」、「善盡企業社會責任，促進碳中和實現」等策略主軸，強化核心本業、客戶服務、集團管理、人才培育、社會責任等...`
- ID `10331` true=`Clear` pred=`Not Clear` text=`為鞏固誠信經營之企業文化，國泰金控制定《誠信經營政策暨守則》、《誠信經營作業程序及行為指南》及《員工行為守則》政策，要求同仁遵守內部相關規範以及禁止不誠信行為，且須以合法方式參與公共事務。國泰長期參與公會與協會，國泰金控李長庚總經理現任「中華民國銀行商業同業公會全國聯合會」常務理事、「台北市銀行商業同業公會」理事；國泰人壽劉上旗總經理現任「中華民國人壽保險商業同業公會」常務監事；國泰世華銀行郭明鑑董事長現任「中華民國銀行商業同業公...`
- ID `10458` true=`Clear` pred=`Not Clear` text=`日月光投控各子公司及廠區皆建立系統化的客戶投訴事件處理程序，客戶可透過電話、郵件、書面報告或是定期與不定期會議的管道提出申訴。當收到關於客戶產品不良抱怨事件後，將透過成立跨部門團隊，由各部門對應之專責人員進行確認，擬定改善對策並回饋客戶，定期召開討論會議，持續追蹤對策的有效性。 Professional ESG Sustainability Report Analysis Assistant. Extract text from ...`
- ID `10615` true=`Clear` pred=`Not Clear` text=`公共政策不僅會影響國家經濟發展，更能促進及帶動社會的進步。對此，我們積極參與相關公協會組織及活動，結合我們在資通訊技術的核心能力，支援對社會大眾有益的公共政策與活動，包括文化、藝術、體育等，積極發揮企業社會影響力。我們參與將近 100 個國內、外公協會，藉由與同業、異業間的交流與合作，提升中華電信的技術能力，展現中華電信在產業中的領航角色，帶動整體產業鏈的發展。 Professional ESG Sustainability Re...`

## Evidence-Based Next Suggestions

- Focus first on `evidence_quality` because it has the lowest macro F1 in this report (0.4549).
- Inspect `evidence_quality` label `Not Clear`: recall is 0.1600 over support 25.
- Inspect `verification_timeline` label `between_2_and_5_years`: recall is 0.2692 over support 52.
- Inspect `promise_status` label `No`: recall is 0.4884 over support 43.
- Review `verification_timeline` confusion `between_2_and_5_years` -> `already` (22 rows) before adding new rules.
- Review `promise_status` confusion `No` -> `Yes` (22 rows) before adding new rules.
- Review `verification_timeline` confusion `N/A` -> `already` (16 rows) before adding new rules.

## Anti-Hallucination Note

The suggestions above are generated only from the prediction/truth comparison in this report. They are not proof of root cause; inspect the cited IDs and confusion pairs before changing code.
