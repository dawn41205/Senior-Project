# Validation Evidence Report

- Generated: 2026-06-02 05:09:47
- Prediction file: `E:\project\test510\week14_runs\week14_2\LLM_pipeline_pred_week14_2.json`
- Truth file: `E:\project\test510\dataset\week14\week14_2\val_grouped.json`
- Input file: `E:\project\test510\week14_runs\week14_2\val_formal_input.json`
- Prediction rows: 200
- Truth rows: 200
- Weighted score: `0.568368`

## Score Summary

| Field | Weight | Macro F1 | Weighted component | Truth distribution | Prediction distribution |
|---|---:|---:|---:|---|---|
| promise_status | 0.20 | 0.977966 | 0.195593 | Yes=156, No=44 | Yes=157, No=43 |
| verification_timeline | 0.15 | 0.258143 | 0.038721 | already=74, N/A=44, more_than_5_years=41, between_2_and_5_years=40, within_2_years=1 | N/A=130, between_2_and_5_years=48, more_than_5_years=21, already=1 |
| evidence_status | 0.30 | 0.815562 | 0.244669 | Yes=136, N/A=44, No=20 | Yes=144, N/A=43, No=13 |
| evidence_quality | 0.35 | 0.255385 | 0.089385 | Clear=112, N/A=64, Not Clear=24 | N/A=161, Clear=18, Not Clear=16, Misleading=5 |

## promise_status

### Per-Label Metrics

| Label | Precision | Recall | F1 | Support |
|---|---:|---:|---:|---:|
| Yes | 0.987261 | 0.993590 | 0.990415 | 156 |
| No | 0.976744 | 0.954545 | 0.965517 | 44 |

### Confusion Matrix

Rows are truth labels; columns are predicted labels.

| Truth \ Pred | Yes | No |
|---|---:|---:|
| Yes | 155 | 1 |
| No | 2 | 42 |

### Largest Gaps

- `No` -> `Yes`: 2 rows
- `Yes` -> `No`: 1 rows

### Example Mismatches

- ID `10503` true=`No` pred=`Yes` text=`永康宿舍大樓空調冰水主機節能專案 年節省用電量 246,205 度 (KWh)；減少 0.8863 兆焦耳 (TJ) 之能源使用量；降低 121.63 噸 CO₂e 排放；年度節省費用 0.76 百萬元。 永康宿舍大樓汰換高耗能的 120RT 冰水機 ( 單位能耗 1.15KW/RT )，置換為永磁式 120RT 冰水機 ( 單機能耗 0.63KW/RT )。永康宿舍大樓改善後平均單位能耗較未加裝時約下降 45%。 [Local ...`
- ID `10748` true=`No` pred=`Yes` text=`本公司依據品質管理系統進行客戶意見回饋之管理與改善，若接獲客戶之申訴時，由 PM 或業務人員先行瞭解客戶之問題，並將其問題轉移至客戶服務單位 (customer service unit) 處理。由客戶服務單位判斷客訴案件之類型，協調相關責任單位在最迅速的時間內共同處理客戶問題直至問題解決，以保障客戶權益。 Professional ESG Sustainability Report Analysis Assistant. Ext...`
- ID `10457` true=`Yes` pred=`No` text=`\| 集團資訊策略委員會 \| 研議華南金融集團短、中、長期資訊策略及資訊發展相關重要議題。 \| • 每半年召開 1 次，惟得視業務需要隨時召開，2024 年共召開 2 次<br>• 平均出席率：98.15%(含委託出席為 100%) \| Professional ESG Sustainability Report Analysis Assistant. Two scanned pages (080 and 081) from a c...`

## verification_timeline

### Per-Label Metrics

| Label | Precision | Recall | F1 | Support |
|---|---:|---:|---:|---:|
| already | 1.000000 | 0.013514 | 0.026667 | 74 |
| within_2_years | 0.000000 | 0.000000 | 0.000000 | 1 |
| between_2_and_5_years | 0.291667 | 0.350000 | 0.318182 | 40 |
| more_than_5_years | 0.666667 | 0.341463 | 0.451613 | 41 |
| N/A | 0.330769 | 0.977273 | 0.494253 | 44 |

### Confusion Matrix

Rows are truth labels; columns are predicted labels.

| Truth \ Pred | already | within_2_years | between_2_and_5_years | more_than_5_years | N/A |
|---|---:|---:|---:|---:|---:|
| already | 1 | 0 | 27 | 5 | 41 |
| within_2_years | 0 | 0 | 0 | 0 | 1 |
| between_2_and_5_years | 0 | 0 | 14 | 2 | 24 |
| more_than_5_years | 0 | 0 | 6 | 14 | 21 |
| N/A | 0 | 0 | 1 | 0 | 43 |

### Largest Gaps

- `already` -> `N/A`: 41 rows
- `already` -> `between_2_and_5_years`: 27 rows
- `between_2_and_5_years` -> `N/A`: 24 rows
- `more_than_5_years` -> `N/A`: 21 rows
- `more_than_5_years` -> `between_2_and_5_years`: 6 rows
- `already` -> `more_than_5_years`: 5 rows
- `between_2_and_5_years` -> `more_than_5_years`: 2 rows
- `N/A` -> `between_2_and_5_years`: 1 rows

### Example Mismatches

- ID `10035` true=`already` pred=`N/A` text=`本集團以獨立超然之精神執行稽核業務，隸屬於董事會，協助董事會及高階管理階層審查與評估風險管理是否有效運作，包含評估第一道及第二道防線監控之有效性，並適時提出改進建議。內部稽核單位建立及執行集團內部稽核制度，查核與評估內部控制之有效性，並定期向審計委員會及董事會報告。對本公司每年至少辦理 1 次一般業務查核。 Professional ESG Sustainability Report Analysis Assistant. Ext...`
- ID `10120` true=`already` pred=`N/A` text=`金控及轄下子公司之企業核心價值為「誠信、親切、專業、創新」，首重以「誠信」是公司治理及企業永續經營的根本，而本公司本於廉潔、透明及負責之經營理念，建構誠信經營之企業文化及健全發展，以建立良好商業運作模式與風險控管機制，創造永續發展之經營環境，爰參照「富邦金控誠信經營守則」制定「富邦人壽誠信經營守則」並經董事會決議通過，並於公司內部網站、法令遵循網站公告予內、外勤同仁知悉。 Professional ESG Sustainabili...`
- ID `10135` true=`already` pred=`N/A` text=`企業永續發展是瑞昱持續精進的核心理念與價值，瑞昱體認企業的永續經營運作和全球穩健多元發展密不可分，因此我們持續關注企業永續續相關之國際倡議，並發展及建置各項與國內外標準接軌之永續營運管理政策，同步實踐誠信經營、重視環境保護、推展 ESG 理念以及促進社會共榮，堅定實踐全球共好價值。我們關注企業永續發展議題及成果，呼應全球永續發展及回應內外部利害關係人的期待。透過系統性深化檢視各項重大永續議題，發展永續行動方針及短、中、長期目標，並...`
- ID `10144` true=`already` pred=`N/A` text=`在技術研發上，電源與散熱技術一直是資料中心客戶降低整體使用成本的關鍵，除投入研發資源於技術產品的創新設計，開發兼具節能、模組化的產品，亦透過高度系統整合及測試能力，提升附加價值以拉大差異化，為客戶提供綜合解決方案。作為 OCP (Open Compute Project，開放運算計畫) 的白金會員與解決方案供應商，亦積極導入 OCP 設計理念至全系列產品，協助資料中心享有效率、精簡及易於維護的優點，滿足其對運算效能、省電與簡易維護...`
- ID `10205` true=`already` pred=`N/A` text=`在社會參與上，我們長期與財團法人日月之光慈善事業基金會、財團法人日月光文教基金會、財團法人張姚宏影社會福利慈善事業基金會合作推動社區公益專案，串聯夥伴網路與資源，擴大專案效益與影響力。2024 年社區營造投入近新台幣 6,804 萬元，幫助約 13,276 位受益者，包括社區弱勢學生課後輔導 485 位及資助清寒家庭學童共 12,791 人次、合作公益機構 57 個等，日月光投控致力建構良好的學習與生活環境，點亮社會各個角落。 [...`
- ID `10224` true=`already` pred=`N/A` text=`光寶重視員工的身心平衡，鼓勵同仁自發性成立各式性質的休閒社團，並從辦法制度優化、各社群影音宣傳、以及每年盛大舉辦的社團成果展，積極推動社團文化及參與風氣，打造優質、和諧、平衡兼具的工作環境。 Professional ESG Sustainability Report Analysis Assistant. Extract all text from the provided image. Convert tables to Ma...`
- ID `10262` true=`already` pred=`N/A` text=`依據本公司供應商問卷調查自然相關風險分析結果，得出供應商依賴生態系統提供水資源、疾病控制；並對化石燃料與電力使用產生溫室氣體對自然環境產生較高衝擊，因此，本公司將專注供應商對水資源、空氣污染及疾病控制預防與管理情形，2024年將前揭預防與管理作為納入採購前的「廠商資料檢核表」檢核項目及「供應商分級評鑑」之評估指標項目，藉由「事前檢核」機制，加強供應商自然風險管理及「事後管理」機制，鼓勵供應商有更積極之自然風險管理作為。 Profe...`
- ID `10271` true=`already` pred=`N/A` text=`台光電子以資訊安全管理的三大原則「機密性、完整性、可用性」訂立《資訊安全管理辦法》，除了提供台光集團整體業務持續運作的資訊環境，並建置管理制度與標準程序，目的為達成符合相關法規要求，並免於遭受各種不當使用、洩漏、竄改、竊取、破壞等資安事故威脅，降低可能危害。 台光電子公司、台光（昆山）公司、中山台光公司、台光（黃石）公司均設有資通安全處理小組，由總經理擔任召集人，組員包含各部門主管及資通安全通報網聯絡人員。台灣觀音一廠已於 202...`

## evidence_status

### Per-Label Metrics

| Label | Precision | Recall | F1 | Support |
|---|---:|---:|---:|---:|
| Yes | 0.909722 | 0.963235 | 0.935714 | 136 |
| No | 0.692308 | 0.450000 | 0.545455 | 20 |
| N/A | 0.976744 | 0.954545 | 0.965517 | 44 |

### Confusion Matrix

Rows are truth labels; columns are predicted labels.

| Truth \ Pred | Yes | No | N/A |
|---|---:|---:|---:|
| Yes | 131 | 4 | 1 |
| No | 11 | 9 | 0 |
| N/A | 2 | 0 | 42 |

### Largest Gaps

- `No` -> `Yes`: 11 rows
- `Yes` -> `No`: 4 rows
- `N/A` -> `Yes`: 2 rows
- `Yes` -> `N/A`: 1 rows

### Example Mismatches

- ID `10181` true=`No` pred=`Yes` text=`台新持續培養數位金融技能，除了藉由教育訓練提升現有員工的科技專業技能外，也積極招募外部數位科技人才，以快速提升整體數位技能。透過掌握金融科技發展趨勢，未來台新將積極布建數位金融生態環境，並且因應新世代趨勢進行科技人才培育，以更積極、穩健的腳步，落實企業永續經營。 Professional ESG Sustainability Report Analysis Assistant. Extract text from a scanne...`
- ID `10190` true=`No` pred=`Yes` text=`本公司屬實收資本額 50~100 億元之公司，配合金管會推動「上市櫃公司永續發展路徑圖」，分階段揭露溫室氣體盤查及確信資訊，個體公司（即母公司）應於第二階段適用本公司期程於 2026 年度完成盤查，2028 年度完成查證。本公司將配合金管會要求，不晚於對應時間內完成溫室氣體盤查及確信。 Professional ESG Sustainability Report Analysis Assistant. Extract text f...`
- ID `10227` true=`No` pred=`Yes` text=`鴻海已展示了有效鑑別和公平評估對利害關係者的過程，其中已刻一系對來自廣泛來源的環境、社會和治理主題，對於其營運活動所帶來的衝擊的過程。其鑑別評估已透過定性化和定量相結合的目標愈來達成，本查證可持續提請佐證管道，透過多元管道與利害關係人揭露重大主題進展與成果，並透過決策流程提升與各方的互信與合作，持續優化企業溝通競爭力。 Professional ESG Sustainability Report Analysis Assistan...`
- ID `10269` true=`No` pred=`Yes` text=`廣達致力於推動包裝材料創新與減量，積極消除不必要的包材使用與一次性塑膠。包裝設計優先考量可回收性、可再利用性與材料減量原則，並逐步導入再生材料。透過永續設計導向，降低整體包裝對環境的衝擊，實踐資源效率與產品全生命週期管理。 Professional ESG Sustainability Report Analysis Assistant. Scan of an ESG report page (Quanta Computer). ...`
- ID `10401` true=`No` pred=`Yes` text=`2024 年開始投入鄰近中壢廠的黃墘溪生態評估，規劃為期三年以恢復河川生態系統為目的之專案，並朝向生物多樣性淨正向影響 (NPI) 邁進。 Professional ESG Sustainability Report Analysis Assistant. Extract text from a scanned image of an ESG report. Convert tables to Markdown format. M...`
- ID `10422` true=`No` pred=`Yes` text=`持續進行工業入侵防禦系統 (Industrial IPS, Intrusion Prevention System) 擴大佈署，可依網路流量偵測與回應，提早發現並阻擋潛在的網路攻擊活動。提升端點設備的異常偵測及防護能力，包含應用程式白名單 (Application Whitelisting) 機制與端點偵測與回應 (EDR, Endpoint Detection and Response) 機制。建置資安協調、自動化與回應 (SO...`
- ID `10484` true=`No` pred=`Yes` text=`集團致力於推動可持續發展，積極導入可持續原材料的選擇與管理機制，依據以下幾項核心原則，持續優化產品設計與供應鏈管理： Professional ESG Sustainability Report Analysis Assistant. Extract text from a scanned page of a corporate ESG report. Complete extraction, precise Markdown t...`
- ID `10537` true=`No` pred=`Yes` text=`重大議題鑑別流程由永續發展中心統籌執行，整合內外部專業意見、產業趨勢及利害關係人關注重點，並透過跨部門合作進行系統性評估。最終辨識結果不僅反映於本報告書中，更落實於廣達ESG策略擬定、行動方案推進及管理績效追蹤機制，協助投資人、客戶、員工、供應商與營運所在地社區等利害關係人，全面掌握廣達在永續議題上的重視程度與具體作為。 Professional ESG Sustainability Report Analysis Assista...`

## evidence_quality

### Per-Label Metrics

| Label | Precision | Recall | F1 | Support |
|---|---:|---:|---:|---:|
| Clear | 0.944444 | 0.151786 | 0.261538 | 112 |
| Not Clear | 0.250000 | 0.166667 | 0.200000 | 24 |
| Misleading | 0.000000 | 0.000000 | 0.000000 | 0 |
| N/A | 0.391304 | 0.984375 | 0.560000 | 64 |

### Confusion Matrix

Rows are truth labels; columns are predicted labels.

| Truth \ Pred | Clear | Not Clear | Misleading | N/A |
|---|---:|---:|---:|---:|
| Clear | 17 | 12 | 3 | 80 |
| Not Clear | 1 | 4 | 1 | 18 |
| Misleading | 0 | 0 | 0 | 0 |
| N/A | 0 | 0 | 1 | 63 |

### Largest Gaps

- `Clear` -> `N/A`: 80 rows
- `Not Clear` -> `N/A`: 18 rows
- `Clear` -> `Not Clear`: 12 rows
- `Clear` -> `Misleading`: 3 rows
- `Not Clear` -> `Clear`: 1 rows
- `N/A` -> `Misleading`: 1 rows
- `Not Clear` -> `Misleading`: 1 rows

### Example Mismatches

- ID `10012` true=`Clear` pred=`N/A` text=`萬海要求所有供應商遵守雙方企業社會責任政策內容，並積極與供應商合作投入供應鏈永續管理，確保安全的工作環境、有尊嚴的勞工關係、誠信經營及促進環境保護。在 2024 年的隨機抽查中，共評鑑 325 家供應商，雖有零星個案發生品質或效率不佳之問題，但廠商均已於要求期限內完成改善，最終所有抽查之供應商皆通過評鑑。萬海將持續落實現行標準，並依循法規與國際公約的變化調整管理措施，推動所有新舊供應商簽署承諾書及永續評鑑表，以深化供應鏈的永續發展...`
- ID `10018` true=`Clear` pred=`N/A` text=`供應鏈是日月光投控成為一家具有影響力公司的重要夥伴，積極與供應商共同規劃與推動五大低碳管理方針，涵蓋低碳選商永續策略、完善供應鏈碳資訊、推動材料與機台低碳轉型、導入上游低碳運輸與建立低碳供應鏈等，並透過日月光環保永續基金會舉辦低碳節能永續獎，攜手供應商夥伴一同實現 2050 年淨零排放承諾。 更進一步，日月光在行之有年的供應商評比中，除了品質與交期的評核外，首度納入 10% 的永續績效，同時日月光投控與供應商組成低碳供應聯盟，正式...`
- ID `10021` true=`Clear` pred=`N/A` text=`自 2005 年起陸續展開溫室氣體盤查作業，並通過第三方 ISO 14064 查證，以追蹤各營運據點之溫室氣體排放情況，持續積極尋求各項減碳與低碳方案。同時逐步導入子公司盤查作業。2024 年溫室氣體相較前一年度下降 3.2%，並首次進行內部盤查子公司溫室氣體作業。 Professional ESG Sustainability Report Analysis Assistant. Extract text from the pr...`
- ID `10025` true=`Clear` pred=`N/A` text=`為避免因作業、活動或服務及設施等危害，造成同仁安全健康或公司財務損失，藉由建構 ISO 45001 安全衛生管理系統，持續推動安全衛生危害鑑別、風險機會評估，並採取適當預防措施或執行必要之控制方法，將風險控制在可接受的程度之下。 Professional ESG Sustainability Report Analysis Assistant. Extract text from the provided image. Preci...`
- ID `10035` true=`Clear` pred=`N/A` text=`本集團以獨立超然之精神執行稽核業務，隸屬於董事會，協助董事會及高階管理階層審查與評估風險管理是否有效運作，包含評估第一道及第二道防線監控之有效性，並適時提出改進建議。內部稽核單位建立及執行集團內部稽核制度，查核與評估內部控制之有效性，並定期向審計委員會及董事會報告。對本公司每年至少辦理 1 次一般業務查核。 Professional ESG Sustainability Report Analysis Assistant. Ext...`
- ID `10092` true=`Clear` pred=`N/A` text=`麥寮、台西鄉子弟獎助學金 活動簡介 為鼓勵麥寮、台西鄉優秀子弟認真向學，本公司贊助獎助學金，於每年3月及10月間放就讀高中、大學子弟申請 活動成果 ■ 自 2004 年起，獎助學金已持續發放 21 年 ■ 2024 年共 2,071 位優秀子弟獲頒獎助學金，累計金額約 570.4 萬元 利害關係人回饋 麥寮鄉單親的外配母親獨自撫養 2 名女兒，領到台塑獎助學金時表示：「感謝台塑幫助我們家孩子上學！」外配母親因學歷及專長受限，只能靠...`
- ID `10106` true=`Clear` pred=`N/A` text=`全氟 / 多氟烷基物質 (Per / Poly fluoroalkyl substances, PFAS) 為一類化學性質穩定的合成物質，具備防水、防油、及摩擦力小的特性，廣泛應用於許多產品的製造過程。然而，由於 PFAS 於環境中不易分解，且對人體可能造成危害，因此越來越多的國家和地區開始對其採取管制。聯電集團分別於 2015 年與 2016 年完成 PFOS 與 PFOA 的替代，並於 2017 年領先業界完成 PFOA 相關...`
- ID `10120` true=`Clear` pred=`N/A` text=`金控及轄下子公司之企業核心價值為「誠信、親切、專業、創新」，首重以「誠信」是公司治理及企業永續經營的根本，而本公司本於廉潔、透明及負責之經營理念，建構誠信經營之企業文化及健全發展，以建立良好商業運作模式與風險控管機制，創造永續發展之經營環境，爰參照「富邦金控誠信經營守則」制定「富邦人壽誠信經營守則」並經董事會決議通過，並於公司內部網站、法令遵循網站公告予內、外勤同仁知悉。 Professional ESG Sustainabili...`

## Evidence-Based Next Suggestions

- Focus first on `evidence_quality` because it has the lowest macro F1 in this report (0.2554).
- Inspect `verification_timeline` label `within_2_years`: recall is 0.0000 over support 1.
- Inspect `verification_timeline` label `already`: recall is 0.0135 over support 74.
- Inspect `evidence_quality` label `Clear`: recall is 0.1518 over support 112.
- Review `evidence_quality` confusion `Clear` -> `N/A` (80 rows) before adding new rules.
- Review `verification_timeline` confusion `already` -> `N/A` (41 rows) before adding new rules.
- Review `verification_timeline` confusion `already` -> `between_2_and_5_years` (27 rows) before adding new rules.

## Anti-Hallucination Note

The suggestions above are generated only from the prediction/truth comparison in this report. They are not proof of root cause; inspect the cited IDs and confusion pairs before changing code.
