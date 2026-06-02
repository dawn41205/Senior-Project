# Validation Evidence Report

- Generated: 2026-06-02 08:34:43
- Prediction file: `E:\project\test510\week14_runs\week14_5\LLM_pipeline_pred_week14_5.json`
- Truth file: `E:\project\test510\dataset\week14\week14_5\val_grouped.json`
- Input file: `E:\project\test510\week14_runs\week14_5\val_formal_input.json`
- Prediction rows: 200
- Truth rows: 200
- Weighted score: `0.531001`

## Score Summary

| Field | Weight | Macro F1 | Weighted component | Truth distribution | Prediction distribution |
|---|---:|---:|---:|---|---|
| promise_status | 0.20 | 0.957651 | 0.191530 | Yes=157, No=43 | Yes=151, No=49 |
| verification_timeline | 0.15 | 0.241506 | 0.036226 | already=64, between_2_and_5_years=52, N/A=43, more_than_5_years=40, within_2_years=1 | N/A=129, between_2_and_5_years=51, more_than_5_years=17, already=2, within_2_years=1 |
| evidence_status | 0.30 | 0.781854 | 0.234556 | Yes=131, N/A=43, No=26 | Yes=120, N/A=49, No=31 |
| evidence_quality | 0.35 | 0.196253 | 0.068688 | Clear=106, N/A=69, Not Clear=25 | N/A=164, Clear=13, Not Clear=12, Misleading=11 |

## promise_status

### Per-Label Metrics

| Label | Precision | Recall | F1 | Support |
|---|---:|---:|---:|---:|
| Yes | 1.000000 | 0.961783 | 0.980519 | 157 |
| No | 0.877551 | 1.000000 | 0.934783 | 43 |

### Confusion Matrix

Rows are truth labels; columns are predicted labels.

| Truth \ Pred | Yes | No |
|---|---:|---:|
| Yes | 151 | 6 |
| No | 0 | 43 |

### Largest Gaps

- `Yes` -> `No`: 6 rows

### Example Mismatches

- ID `10019` true=`Yes` pred=`No` text=`第二線個資保護專責單位負責督導、協調、監控個人資料保護相關事宜，應至少每年一次向董事會報告，如發現有重大違反個人資料保護相關法令之事件時，應即時向董事會報告。 Professional ESG Sustainability Report Analysis Assistant. Extract text from a scanned image of an ESG report page. Markdown. * Complete ...`
- ID `10146` true=`Yes` pred=`No` text=`我們遵循保證作業的國際最佳實務，包括國際審計與保證標準委員會頒布的《國際保證作業標準》（ISAE）3000（修訂版）—非屬歷史財務資訊審計與核閱的保證作業》，執行了數據保證查驗作業。為確保保證程序的一致性，我們依據 DNV 的保證方法學 VeriSustain 執行工作，僅應用與本次活動特定目的的相關的部分。此方法學確保遵循倫理要求，並要求規劃與執行保證作業以達到預期保證等級。 Professional ESG Sustainab...`
- ID `10244` true=`Yes` pred=`No` text=`導入產品永續性及生產 a. 減少材料使用 b. 採用回收材料 c. 模組化設計 d. 最佳運輸材積設計 e. 綠色生產製造 Professional ESG Sustainability Report Analysis Assistant. Extract text from a scanned image of a corporate ESG report. * Full text extraction. * Tables mu...`
- ID `10302` true=`Yes` pred=`No` text=`A、B、C、D 四個等級。若供應商被評為 C 級或 D 級，瑞昱將積極輔導與協助改善；而若供應商連續三次被評為 D 級或連續五次未達 B 級，則暫時取消合作資格。 Professional ESG Sustainability Report Analysis Assistant. Extract text from a scanned page of an ESG report. Markdown. * Extract all t...`
- ID `10805` true=`Yes` pred=`No` text=`江蘇句容廠也將建置16.6MWh儲能系統，穩定廠區太陽能發電、節省電費外，更參與電力交易。台泥儲能亦將於句容設立超高性能混凝土(UHPC)工廠，結合太陽能自發自用，打造新一代低碳UHPC EnergyArk儲能櫃，並攜手當地供應鏈拓展市場。 Professional ESG Sustainability Report Analysis Assistant. Extract all text from the provided im...`
- ID `10960` true=`Yes` pred=`No` text=`風險應變 ■ 依據辨識風險與機會的等級與優先順序，制定相關之管理計畫 ■ 各功能單位配合氣候議題之因應措施及執行策略確實執行 Professional ESG Sustainability Report Analysis Assistant. Scan page from a corporate ESG report. Extract all text completely. Convert tables/structured d...`

## verification_timeline

### Per-Label Metrics

| Label | Precision | Recall | F1 | Support |
|---|---:|---:|---:|---:|
| already | 0.500000 | 0.015625 | 0.030303 | 64 |
| within_2_years | 0.000000 | 0.000000 | 0.000000 | 1 |
| between_2_and_5_years | 0.294118 | 0.288462 | 0.291262 | 52 |
| more_than_5_years | 0.647059 | 0.275000 | 0.385965 | 40 |
| N/A | 0.333333 | 1.000000 | 0.500000 | 43 |

### Confusion Matrix

Rows are truth labels; columns are predicted labels.

| Truth \ Pred | already | within_2_years | between_2_and_5_years | more_than_5_years | N/A |
|---|---:|---:|---:|---:|---:|
| already | 1 | 1 | 29 | 3 | 30 |
| within_2_years | 0 | 0 | 1 | 0 | 0 |
| between_2_and_5_years | 1 | 0 | 15 | 3 | 33 |
| more_than_5_years | 0 | 0 | 6 | 11 | 23 |
| N/A | 0 | 0 | 0 | 0 | 43 |

### Largest Gaps

- `between_2_and_5_years` -> `N/A`: 33 rows
- `already` -> `N/A`: 30 rows
- `already` -> `between_2_and_5_years`: 29 rows
- `more_than_5_years` -> `N/A`: 23 rows
- `more_than_5_years` -> `between_2_and_5_years`: 6 rows
- `between_2_and_5_years` -> `more_than_5_years`: 3 rows
- `already` -> `more_than_5_years`: 3 rows
- `between_2_and_5_years` -> `already`: 1 rows

### Example Mismatches

- ID `10023` true=`between_2_and_5_years` pred=`N/A` text=`台泥致力打造安全工作環境，訂有《職業安全衛生管理相關內部控制政策》，適用於員工、派駐外包工作者及承攬商，實現零工傷願景。現行安全管理規章包含《職業安全衛生管理規章》、《職業安全衛生管理計畫》及《職業安全衛生作守則》等，並以行為導向管理推動職安文化。CIMPOR與OYAK CEMENT也於綜合管理系統政策(Integrated Management System Policy)中強調對員工職業安全衛生管理的重視。 Professio...`
- ID `10037` true=`between_2_and_5_years` pred=`N/A` text=`誠信經營是公司治理內部控制機制重要的一環。研華會在事前辨識各項法令規章，並與內部相關單位溝通、衡量公司相關規則之制定與落實，以求符合法規。誠信經營中之法令遵循、反貪腐與反競爭概念與社會責任與公司商譽有重大關聯，為研華永續經營重點之一。 Professional ESG sustainability report analysis assistant. Extract text from a scanned page of a co...`
- ID `10046` true=`between_2_and_5_years` pred=`N/A` text=`為因應未來溫室氣體排放費用開徵及碳價格將持續升高，永續委員會定義智邦科技碳管理策略第一步為設定短中期減量及長期淨零排放目標，減量的方向優先進行組織減量，後透過購買綠電憑證及其他除碳手段進行剩餘排放抵換。 Professional ESG sustainability report analysis assistant. Extract text from a scanned page of a corporate ESG repo...`
- ID `10056` true=`between_2_and_5_years` pred=`N/A` text=`台泥旗下達和航運所有水泥船皆優先自主導入岸電系統，優於IMO規定 達和航運積極響應國際海事組織(IMO)減排策略 目標2030年減碳40% 2025年啟用環保水泥船「達循輪」，導入智能船管系統、封閉式裝卸技術，相較能源效率設計指數第一階段(EEDI Phase I)預估減碳23.7%。旗下散裝貨輪在現成船能源效率指數(EEXI)與營運碳強度指標(CII)方面皆優於IMO規範，CII評級持續保持在目標C級以上，86%船隻更達到最優等...`
- ID `10146` true=`between_2_and_5_years` pred=`N/A` text=`我們遵循保證作業的國際最佳實務，包括國際審計與保證標準委員會頒布的《國際保證作業標準》（ISAE）3000（修訂版）—非屬歷史財務資訊審計與核閱的保證作業》，執行了數據保證查驗作業。為確保保證程序的一致性，我們依據 DNV 的保證方法學 VeriSustain 執行工作，僅應用與本次活動特定目的的相關的部分。此方法學確保遵循倫理要求，並要求規劃與執行保證作業以達到預期保證等級。 Professional ESG Sustainab...`
- ID `10187` true=`between_2_and_5_years` pred=`N/A` text=`我們已建置完善的端到端資訊管理系統, 涵蓋從產品設計與開發、生產製造、採購與交貨至供應商管理的全流程。透過即時市場監控與回饋機制, 我們能快速響應市場變化, 做出最佳決策, 確保產品準時交付且符合質量與數量要求。主要生產基地分布於中國大陸的深圳、東莞、成都、武漢、嘉善, 以及越南河南, 同時在全球設有業務行銷與物流倉儲據點, 技術支援網絡隨時待命, 以便為來自亞洲、北美、南美及歐洲等地的客戶提供高效服務。為積極響應國際品牌客戶對永...`
- ID `10217` true=`between_2_and_5_years` pred=`N/A` text=`在緯創的戰略合作夥伴關係中，供應商扮演著至關重要的角色。我們深知，與供應商的合作不僅是實現業務成功的基石，也是落實公司永續發展目標的關鍵要素。因此，我們將永續責任採購列為六大永續發展策略之一，將永續發展的理念融入採購管理中，並從風險管理、競爭優勢和成本優化三大驅動力出發，遵循永續採購指南 (ISO 20400)，同時依循 RBA 行為準則，以確保供應商在環境、社會和治理方面，持續提升績效。 Professional ESG Sus...`
- ID `10226` true=`between_2_and_5_years` pred=`N/A` text=`和泰集團自 2022 年啟動「原夢代表隊」公益計畫，攜手集團內各事業體，共同整合資源，長期支持新竹縣尖石鄉嘉興國小與五峰鄉桃山國小的泰雅族兒童合唱團。此計畫旨在幫助這些擁有音樂天賦的孩子，在成長與學習的過程中，接觸多元職業與環境，拓展視野並提升對未來職業的想像。 Professional ESG Sustainability Report Analysis Assistant. Extract all text from the ...`

## evidence_status

### Per-Label Metrics

| Label | Precision | Recall | F1 | Support |
|---|---:|---:|---:|---:|
| Yes | 0.925000 | 0.847328 | 0.884462 | 131 |
| No | 0.483871 | 0.576923 | 0.526316 | 26 |
| N/A | 0.877551 | 1.000000 | 0.934783 | 43 |

### Confusion Matrix

Rows are truth labels; columns are predicted labels.

| Truth \ Pred | Yes | No | N/A |
|---|---:|---:|---:|
| Yes | 111 | 16 | 4 |
| No | 9 | 15 | 2 |
| N/A | 0 | 0 | 43 |

### Largest Gaps

- `Yes` -> `No`: 16 rows
- `No` -> `Yes`: 9 rows
- `Yes` -> `N/A`: 4 rows
- `No` -> `N/A`: 2 rows

### Example Mismatches

- ID `10003` true=`Yes` pred=`No` text=`III. 產品危害物質減免 (HSF) 短、中、長期目標設定 **1. 2024 年 目標和實績** * 已達標 * 詳述於 "產品各階段危害物質減免風險管理目標與成效" **2. 短期目標 2025~2026 年** * 監控 PFAS 中有害物質管制要求 * 減少 RoHS 豁免零件之使用，往 Lead Free 持續前進。 **3. 中長期目標 2026~2027 年** * 優化綠色管理系統審查作業提升效率。 Profes...`
- ID `10057` true=`Yes` pred=`No` text=`中華電信持續以 360 度全方位視角推動數位包容行動，多年來持續投入企業資源，普及電信基礎建設，確保全民均享基本通訊權益。我們發揮在資通訊領域的專業與核心優勢，致力於縮小數位落差，開拓數位時代下的多元可能。以「縮短數位落差」及「創造數位機會」兩大社會投資主軸，投注心力推動「企業志工」參與在地社區服務，積極賦能當地社區，藉助數位科技創造更多機會。 Professional ESG Sustainability Report Anal...`
- ID `10090` true=`Yes` pred=`No` text=`呼應萬海的企業精神與經營理念，企業營運以人為本，從內部到外部建立與利害關係人的信任關係。對內透過培養全體員工永續意識、視員工的需求提供多元職涯發展與生活照護，高度尊重人權以建立與員工之間的互信；對外網羅優秀的人才，為專業人才提供可發揮所能的舞台。透過全方位的安全管理，確保在營運過程中達到人安、航安、貨安，打造領先業界的高度安全性，以維持穩健的經營與競爭力。此外，萬海與合作夥伴攜手合作，共同發揮社會影響力，持續關注海洋生態與水資源議...`
- ID `10217` true=`Yes` pred=`No` text=`在緯創的戰略合作夥伴關係中，供應商扮演著至關重要的角色。我們深知，與供應商的合作不僅是實現業務成功的基石，也是落實公司永續發展目標的關鍵要素。因此，我們將永續責任採購列為六大永續發展策略之一，將永續發展的理念融入採購管理中，並從風險管理、競爭優勢和成本優化三大驅動力出發，遵循永續採購指南 (ISO 20400)，同時依循 RBA 行為準則，以確保供應商在環境、社會和治理方面，持續提升績效。 Professional ESG Sus...`
- ID `10303` true=`Yes` pred=`No` text=`企業價值觀是形塑企業文化的基石，也是推動永續發展的核心動能。中華電信致力於推動公司治理的四大價值觀，望將其內化為全體同仁的日常行為準則，引領全員朝共同目標邁進。我們堅信，價值觀的實踐不僅能凝聚團隊向心力、提升營運效率，更是驅動企業持續續創新與永續成長的關鍵力量，為公司開創長期穩健且具韌性的發展基礎。 Professional ESG Sustainability Report Analysis Assistant. Extract...`
- ID `10360` true=`Yes` pred=`No` text=`TSMC ESG AWARD 為台積公司推動永續文化的核心平台，鼓勵同仁提出連結公司 ESG 五大方向的新創好點子，並表彰組織的永續實績，以永續力促進創新力，創造美好改變。 Professional ESG Sustainability Report Analysis Assistant. Extract all text from the provided image of a corporate ESG report page...`
- ID `10442` true=`Yes` pred=`No` text=`服務本身就是人與人的交流，透過暖心的問好、精準的回應，提升服務的溫度及專業。另一方面，提供多元諮詢管道供客戶使用，並以完備處理流程及公平、合理、有效之原則，妥適處理客戶的寶貴意見，方能使服務的品質不斷提升、符合客戶之期待。 Professional ESG Sustainability Report Analysis Assistant. Two scanned pages (142 and 143) from a corpora...`
- ID `10466` true=`Yes` pred=`No` text=`馬來西亞廠 (WYMY) 為第一個取得 GBI (Green Building Index) 綠色建築 Gold 等級認證之營運據點。將持續在全球各地落實綠色建築標準，強化環保與節能策略。推動自然保育與永續發展，以促進環保、公益及企業責任交流，實現人與環境共好及身心平衡。 Professional ESG Sustainability Report Analysis Assistant. Extract all text from...`

## evidence_quality

### Per-Label Metrics

| Label | Precision | Recall | F1 | Support |
|---|---:|---:|---:|---:|
| Clear | 1.000000 | 0.122642 | 0.218487 | 106 |
| Not Clear | 0.000000 | 0.000000 | 0.000000 | 25 |
| Misleading | 0.000000 | 0.000000 | 0.000000 | 0 |
| N/A | 0.402439 | 0.956522 | 0.566524 | 69 |

### Confusion Matrix

Rows are truth labels; columns are predicted labels.

| Truth \ Pred | Clear | Not Clear | Misleading | N/A |
|---|---:|---:|---:|---:|
| Clear | 13 | 11 | 6 | 76 |
| Not Clear | 0 | 0 | 3 | 22 |
| Misleading | 0 | 0 | 0 | 0 |
| N/A | 0 | 1 | 2 | 66 |

### Largest Gaps

- `Clear` -> `N/A`: 76 rows
- `Not Clear` -> `N/A`: 22 rows
- `Clear` -> `Not Clear`: 11 rows
- `Clear` -> `Misleading`: 6 rows
- `Not Clear` -> `Misleading`: 3 rows
- `N/A` -> `Misleading`: 2 rows
- `N/A` -> `Not Clear`: 1 rows

### Example Mismatches

- ID `10004` true=`Clear` pred=`N/A` text=`面對這些全球與國內政策的推動，富邦人壽秉持永續經營理念，積極透過永續金融的投資力量，引導被投資公司與企業進行永續轉型，除非資金明確用於綠能轉型計畫，不再新增投資燃煤比重超過 50% 的電廠。同時，針對燃料煤開採、運輸業、燃料煤發電及非典型油氣產業，制定嚴格的准入與撤資標準，積極引導資金流向低碳與可再生能源領域，展現對環境永續的堅定承諾，並連續 4 年榮獲「台灣永續投資典範機構獎 – 機構影響力 (壽險組)」殊榮，在責任投資與推動企...`
- ID `10023` true=`Clear` pred=`N/A` text=`台泥致力打造安全工作環境，訂有《職業安全衛生管理相關內部控制政策》，適用於員工、派駐外包工作者及承攬商，實現零工傷願景。現行安全管理規章包含《職業安全衛生管理規章》、《職業安全衛生管理計畫》及《職業安全衛生作守則》等，並以行為導向管理推動職安文化。CIMPOR與OYAK CEMENT也於綜合管理系統政策(Integrated Management System Policy)中強調對員工職業安全衛生管理的重視。 Professio...`
- ID `10035` true=`Clear` pred=`N/A` text=`本集團以獨立超然之精神執行稽核業務，隸屬於董事會，協助董事會及高階管理階層審查與評估風險管理是否有效運作，包含評估第一道及第二道防線監控之有效性，並適時提出改進建議。內部稽核單位建立及執行集團內部稽核制度，查核與評估內部控制之有效性，並定期向審計委員會及董事會報告。對本公司每年至少辦理 1 次一般業務查核。 Professional ESG Sustainability Report Analysis Assistant. Ext...`
- ID `10039` true=`Clear` pred=`N/A` text=`聯電集團除持續提升能源效率外，亦規劃多元能源使用，積極設置廠內再生能源，更將太陽能系統列為新建廠房標準設計建置項目，發電量連續 5 年增長。2024 年原規劃設置太陽光電 500kW 計畫調整，整併於 2025 年設置合計約 900kW。至 2024 年止，聯電集團已安裝峰值發電容量超過 14,000 瓩 (kWp) 之太陽光電系統，預估每年發電量達 15,000 MWh。惟太陽光電主要受氣候等因素影響，例如 2024 年台灣地區...`
- ID `10046` true=`Clear` pred=`N/A` text=`為因應未來溫室氣體排放費用開徵及碳價格將持續升高，永續委員會定義智邦科技碳管理策略第一步為設定短中期減量及長期淨零排放目標，減量的方向優先進行組織減量，後透過購買綠電憑證及其他除碳手段進行剩餘排放抵換。 Professional ESG sustainability report analysis assistant. Extract text from a scanned page of a corporate ESG repo...`
- ID `10056` true=`Clear` pred=`N/A` text=`台泥旗下達和航運所有水泥船皆優先自主導入岸電系統，優於IMO規定 達和航運積極響應國際海事組織(IMO)減排策略 目標2030年減碳40% 2025年啟用環保水泥船「達循輪」，導入智能船管系統、封閉式裝卸技術，相較能源效率設計指數第一階段(EEDI Phase I)預估減碳23.7%。旗下散裝貨輪在現成船能源效率指數(EEXI)與營運碳強度指標(CII)方面皆優於IMO規範，CII評級持續保持在目標C級以上，86%船隻更達到最優等...`
- ID `10072` true=`Clear` pred=`N/A` text=`投入光電及儲能案場 加入「富邦能源綠能投資平台」，在2024年加入「富邦能源綠能投資平台」，借重泓德能源的技術與經驗，投資380MW光電案場以及開發354 MW儲能案場，助力台灣再生能源儲能未來。 Professional ESG Sustainability Report Analysis Assistant. Extract text from a scanned page of an ESG report. * Full t...`
- ID `10116` true=`Clear` pred=`N/A` text=`鴻海致力於推動員工穩定留任政策，2030年達成間接員工年度整體留任率90%以上，同步強化間接員工中高績效人才之專屬發展機制與福利制度，設定該族群人員之留任率達95%。員工是公司最重要的無形資產之一。吸引合格且才華橫溢的員工以及留住和培養內部人才的能力，對於公司的成功至關重要。專注於吸引最優秀人才的公司不應忽視與公司共同成長、了解組織、使命和文化的內部人才。公司需要建立有序的內部職涯流動流程，以留住人才並降低外部招募成本。 Prof...`

## Evidence-Based Next Suggestions

- Focus first on `evidence_quality` because it has the lowest macro F1 in this report (0.1963).
- Inspect `evidence_quality` label `Not Clear`: recall is 0.0000 over support 25.
- Inspect `verification_timeline` label `within_2_years`: recall is 0.0000 over support 1.
- Inspect `verification_timeline` label `already`: recall is 0.0156 over support 64.
- Review `evidence_quality` confusion `Clear` -> `N/A` (76 rows) before adding new rules.
- Review `verification_timeline` confusion `between_2_and_5_years` -> `N/A` (33 rows) before adding new rules.
- Review `verification_timeline` confusion `already` -> `N/A` (30 rows) before adding new rules.

## Anti-Hallucination Note

The suggestions above are generated only from the prediction/truth comparison in this report. They are not proof of root cause; inspect the cited IDs and confusion pairs before changing code.
