# Validation Evidence Report

- Generated: 2026-05-25 11:39:05
- Prediction file: `E:\project\test510\week13_runs\week13_3\LLM_pipeline_pred_week13_3.json`
- Truth file: `E:\project\test510\dataset\week13\week13_3\val_grouped.json`
- Input file: `E:\project\test510\week13_runs\week13_3\val_formal_input.json`
- Prediction rows: 200
- Truth rows: 200
- Weighted score: `0.589792`

## Score Summary

| Field | Weight | Macro F1 | Weighted component | Truth distribution | Prediction distribution |
|---|---:|---:|---:|---|---|
| promise_status | 0.20 | 0.794872 | 0.158974 | Yes=164, No=36 | Yes=161, No=39 |
| verification_timeline | 0.15 | 0.381168 | 0.057175 | already=79, between_2_and_5_years=44, more_than_5_years=40, N/A=36, within_2_years=1 | already=92, more_than_5_years=44, N/A=39, between_2_and_5_years=18, within_2_years=7 |
| evidence_status | 0.30 | 0.711730 | 0.213519 | Yes=132, N/A=36, No=32 | Yes=138, N/A=50, No=12 |
| evidence_quality | 0.35 | 0.457496 | 0.160123 | Clear=111, N/A=68, Not Clear=21 | Clear=116, N/A=62, Not Clear=22 |

## promise_status

### Per-Label Metrics

| Label | Precision | Recall | F1 | Support |
|---|---:|---:|---:|---:|
| Yes | 0.931677 | 0.914634 | 0.923077 | 164 |
| No | 0.641026 | 0.694444 | 0.666667 | 36 |

### Confusion Matrix

Rows are truth labels; columns are predicted labels.

| Truth \ Pred | Yes | No |
|---|---:|---:|
| Yes | 150 | 14 |
| No | 11 | 25 |

### Largest Gaps

- `Yes` -> `No`: 14 rows
- `No` -> `Yes`: 11 rows

### Example Mismatches

- ID `10001` true=`Yes` pred=`No` text=`聯發科技除在「工作規則」中依照勞基法明確規定「員工在產假期間公司不得終止勞動契約」外，為支持同仁與其家人度過人生不同階段，自 2024 年起提供女性員工在分娩前後計有 12 週共 84 天的產假；男性員工則可於其配偶懷孕期間陪同產檢或生（流）產日及前後 15 日間請假陪伴，兩者合計共有 10 天陪產（檢）假可運用，陪產（檢）假期間工資照常給付。 Professional ESG Sustainability Report Anal...`
- ID `10033` true=`Yes` pred=`No` text=`為瞭解實體風險對本行據點資產之風險衝擊，針對本行各營運據點進行實體風險評估分析。本行以實體風險危害度 1~3 級 (24 小時內極端降雨頻率)、脆弱度 1~10 級 (淹水潛勢、坡地災害) 及暴露度 1~10 級 (暴險金額) 繪製風險敏感地圖，分別採用 RCP 8.5 及 RCP 2.6 作為風險衝擊之假設情境，進行本行據點資產在世紀中 (2036~2065) 的暴險分析，並提出對應之氣候風險管理策略。 Professional...`
- ID `10037` true=`Yes` pred=`No` text=`誠信經營是公司治理內部控制機制重要的一環。研華會在事前辨識各項法令規章，並與內部相關單位溝通、衡量公司相關規則之制定與落實，以求符合法規。誠信經營中之法令遵循、反貪腐與反競爭概念與社會責任與公司商譽有重大關聯，為研華永續經營重點之一。 Professional ESG sustainability report analysis assistant. Extract text from a scanned page of a co...`
- ID `10120` true=`Yes` pred=`No` text=`金控及轄下子公司之企業核心價值為「誠信、親切、專業、創新」，首重以「誠信」是公司治理及企業永續經營的根本，而本公司本於廉潔、透明及負責之經營理念，建構誠信經營之企業文化及健全發展，以建立良好商業運作模式與風險控管機制，創造永續發展之經營環境，爰參照「富邦金控誠信經營守則」制定「富邦人壽誠信經營守則」並經董事會決議通過，並於公司內部網站、法令遵循網站公告予內、外勤同仁知悉。 Professional ESG Sustainabili...`
- ID `10146` true=`Yes` pred=`No` text=`我們遵循保證作業的國際最佳實務，包括國際審計與保證標準委員會頒布的《國際保證作業標準》（ISAE）3000（修訂版）—非屬歷史財務資訊審計與核閱的保證作業》，執行了數據保證查驗作業。為確保保證程序的一致性，我們依據 DNV 的保證方法學 VeriSustain 執行工作，僅應用與本次活動特定目的的相關的部分。此方法學確保遵循倫理要求，並要求規劃與執行保證作業以達到預期保證等級。 Professional ESG Sustainab...`
- ID `10182` true=`Yes` pred=`No` text=`世芯電子之「公司治理實務守則」已明訂董事會成員組成應考量多元化，且不限制性別、年齡、國籍及文化，除應具備執行業務所必需之條件，為達到公司治理之理想目標，董事會整體應具備包括營運判斷能力、會計及財務分析能力、經營管理能力、危機處理能力、產業知識、國際市場觀、領導能力與決策能力等多元化專業背景。 Professional ESG Sustainability Report Analysis Assistant. OCR/Text ex...`
- ID `10244` true=`Yes` pred=`No` text=`導入產品永續性及生產 a. 減少材料使用 b. 採用回收材料 c. 模組化設計 d. 最佳運輸材積設計 e. 綠色生產製造 Professional ESG Sustainability Report Analysis Assistant. Extract text from a scanned image of a corporate ESG report. * Full text extraction. * Tables mu...`
- ID `10407` true=`Yes` pred=`No` text=`聯發科技提供具競爭力的薪酬福利、多元學習環境及具成就感的工作內容，吸引全球優秀人才。2024 年全球計畫招聘 1,440 人，共收到 21,680 份履歷，為預計招聘人數的 15 倍，聘用到任率約 85%，展現具吸引力的雇主品牌。 Professional ESG Sustainability Report Analysis Assistant. Extract text from a scanned page of an ESG...`

## verification_timeline

### Per-Label Metrics

| Label | Precision | Recall | F1 | Support |
|---|---:|---:|---:|---:|
| already | 0.543478 | 0.632911 | 0.584795 | 79 |
| within_2_years | 0.000000 | 0.000000 | 0.000000 | 1 |
| between_2_and_5_years | 0.388889 | 0.159091 | 0.225806 | 44 |
| more_than_5_years | 0.409091 | 0.450000 | 0.428571 | 40 |
| N/A | 0.641026 | 0.694444 | 0.666667 | 36 |

### Confusion Matrix

Rows are truth labels; columns are predicted labels.

| Truth \ Pred | already | within_2_years | between_2_and_5_years | more_than_5_years | N/A |
|---|---:|---:|---:|---:|---:|
| already | 50 | 1 | 7 | 14 | 7 |
| within_2_years | 1 | 0 | 0 | 0 | 0 |
| between_2_and_5_years | 18 | 3 | 7 | 10 | 6 |
| more_than_5_years | 15 | 3 | 3 | 18 | 1 |
| N/A | 8 | 0 | 1 | 2 | 25 |

### Largest Gaps

- `between_2_and_5_years` -> `already`: 18 rows
- `more_than_5_years` -> `already`: 15 rows
- `already` -> `more_than_5_years`: 14 rows
- `between_2_and_5_years` -> `more_than_5_years`: 10 rows
- `N/A` -> `already`: 8 rows
- `already` -> `N/A`: 7 rows
- `already` -> `between_2_and_5_years`: 7 rows
- `between_2_and_5_years` -> `N/A`: 6 rows

### Example Mismatches

- ID `10062` true=`between_2_and_5_years` pred=`already` text=`中鋼承諾所有產品及其包裝所使用或包含之金屬沒有來自剛果 ( 金 ) 及其周邊國家，以及這些國家內任何武裝力量控制區之衝突礦產；透過加強供應鏈管理，有效甄別和追溯原料來源。針對料源投資作業，凡具有衝突疑慮之礦產，即不列入投資評估考慮。中鋼於設備及物料採購時亦關注來源國家之人權狀況，據以做可能之調整，並於投標須知 / 合約條款規定不得行賄、不得侵權、進入中鋼廠區須遵守環安衛規定等行為準則。 Professional ESG Susta...`
- ID `10181` true=`between_2_and_5_years` pred=`already` text=`台新持續培養數位金融技能，除了藉由教育訓練提升現有員工的科技專業技能外，也積極招募外部數位科技人才，以快速提升整體數位技能。透過掌握金融科技發展趨勢，未來台新將積極布建數位金融生態環境，並且因應新世代趨勢進行科技人才培育，以更積極、穩健的腳步，落實企業永續經營。 Professional ESG Sustainability Report Analysis Assistant. Extract text from a scanne...`
- ID `10237` true=`between_2_and_5_years` pred=`already` text=`為了評估氣候變遷對公司業務、策略和財務規劃的影響，我們採取了三個階段的氣候風險與機會辨識流程。通過此流程，我們收斂了統一企業面臨的五項重大風險和一項重大機會，詳細方法請參考 2020 年統一企業社會責任報告書。我們進一步針對環境法規相關資訊量化對統一企業的財務影響，並就相應議題進一步檢視與調整關鍵氣候風險與機會的議題因應與管理現況。2024 年，我們將持續依據最新的環境變化與政策趨勢，追蹤並優化氣候風險與機會管理措施，確保相關策略...`
- ID `10356` true=`between_2_and_5_years` pred=`already` text=`台塑工業 ( 寧波 ) 公司也致力於廢棄物管理並減量，主要透過末端處置進行。 Professional ESG Sustainability Report Analysis Assistant. Extract all text from a scanned image of an ESG report. Convert tables to Markdown format precisely. The user specifica...`
- ID `10413` true=`between_2_and_5_years` pred=`already` text=`積極回應氣候變遷帶來的風險，把握轉型低碳經濟過程中獲得的機會，有效資源配置提升企業競爭力及營運韌性。 Professional ESG Sustainability Report Analysis Assistant. Extract text from a scanned page of a corporate ESG report. Maintain structure, convert tables to Markdown,...`
- ID `10470` true=`between_2_and_5_years` pred=`already` text=`為了確保貨物運送能安全地送達世界各地，陽明海運嚴格遵守各項國際公約，如「國際海上人命安全公約」(SOLAS)、「防止船舶污染國際公約」(MARPOL)、「國際貨櫃安全公約」(International Convention for Safe Containers)、「國際海運危險品章程」(IMDG CODE) 等規定，並配合各國港口貨品及危險品的法律規範來安排與運輸貨品。除遵守公約及法規外，本公司於運輸過程導入 WNI 專業氣象導...`
- ID `10507` true=`between_2_and_5_years` pred=`already` text=`本年度報告書呈現統一超商在永續發展方面的觀點與具體作法，說明 2024 年公司治理、經濟、環境及社會面向的相關成果與未來規劃。同時，透過重大性評估流程（請參閱實踐永續管理章節），篩選出統一超商適用之重大主題，期望透過不同管道之揭露、溝通及回饋，為所有利害關係人創造最大共益，邁向最卓越零售商之目標。 Professional ESG Sustainability Report Analysis Assistant. A scanne...`
- ID `10522` true=`between_2_and_5_years` pred=`already` text=`聯電與中國信託銀行簽訂永續發展表現連結貸款 (Sustainability Linked Loan)。貸款架構通過金融機構的審核，並遵循國際資本市場協會制定的《永續發展表現連結貸款原則》，連結聯電數個具指標性的永續關鍵績效目標結合。透過與金融機構的合作，共同實現「與環境共生」的永續願景。 Professional ESG Sustainability Report Analysis Assistant. A scanned pag...`

## evidence_status

### Per-Label Metrics

| Label | Precision | Recall | F1 | Support |
|---|---:|---:|---:|---:|
| Yes | 0.869565 | 0.909091 | 0.888889 | 132 |
| No | 0.750000 | 0.281250 | 0.409091 | 32 |
| N/A | 0.720000 | 1.000000 | 0.837209 | 36 |

### Confusion Matrix

Rows are truth labels; columns are predicted labels.

| Truth \ Pred | Yes | No | N/A |
|---|---:|---:|---:|
| Yes | 120 | 3 | 9 |
| No | 18 | 9 | 5 |
| N/A | 0 | 0 | 36 |

### Largest Gaps

- `No` -> `Yes`: 18 rows
- `Yes` -> `N/A`: 9 rows
- `No` -> `N/A`: 5 rows
- `Yes` -> `No`: 3 rows

### Example Mismatches

- ID `10081` true=`No` pred=`Yes` text=`麥寮社教 ESG 永續發展示範園區致力於打造完整的生活機能與公共設施，融合教育、文化與生活，提升居民生活品質，成為地方特色與現代化社教的標竿，突破鄉鎮格局。園區同時作為社區休憩據點，結合戶外休閒、展覽表演及藝文活動，提供舒適的生活場域，促進親子交流，並營造友善的都市環境。 Professional ESG Sustainability Report Analysis Assistant. Extract all text from...`
- ID `10091` true=`No` pred=`Yes` text=`本公司依據人權風險評估結果，訂定相對應之減緩與補償措施，並定期追蹤執行結果。2024 年之人權關注議題中無高風險項目，故針對中風險項目設定預防與減緩措施。 Professional ESG Sustainability Report Analysis Assistant. An image of a page from a corporate ESG report (Yang Ming Marine Transport Corp....`
- ID `10118` true=`No` pred=`Yes` text=`本屆競賽冠軍團隊——廣太綠能，擁有微水力發電技術，與其高度應用潛力。於競賽提案規劃將微水力發電模組導入至日月光廠區的中水回收系統，運用既有管線的高低差進行發電，供應廠區內部用電。未來該技術亦可擴大應用，有助於推動綠電在地化發展，強化我國再生能源產業的韌性與自主性。 Professional ESG Sustainability Report Analysis Assistant. Extract all text from a s...`
- ID `10181` true=`No` pred=`Yes` text=`台新持續培養數位金融技能，除了藉由教育訓練提升現有員工的科技專業技能外，也積極招募外部數位科技人才，以快速提升整體數位技能。透過掌握金融科技發展趨勢，未來台新將積極布建數位金融生態環境，並且因應新世代趨勢進行科技人才培育，以更積極、穩健的腳步，落實企業永續經營。 Professional ESG Sustainability Report Analysis Assistant. Extract text from a scanne...`
- ID `10188` true=`No` pred=`Yes` text=`展望未來，富邦人壽將持續以「正向力量 豐富生命」的品牌精神為指引，深化「低碳、數位、激勵、影響」四大策略推動，積極實現永續願景。作為臺灣保險業的領導品牌，富邦人壽將持續發揮金融影響力，以創新思維與具體行動，為臺灣的永續發展注入更多正向動能。我們相信，唯有將 ESG 理念深植於企業文化，並以實際行動展現永續承諾，才能真正實現經濟、環境和社會的均衡發展，共同打造更美好的永續未來。 Professional ESG Sustainabi...`
- ID `10253` true=`No` pred=`Yes` text=`本公司對利害關係人建立相應之議合方式與管道，傾聽意見與回饋，每年亦定期向董事會陳報與利害關係人之溝通實績。 Professional ESG Sustainability Report Analysis Assistant. Extract text from a scanned page of an ESG report. Convert tables to Markdown format. Maintain precision...`
- ID `10282` true=`No` pred=`Yes` text=`緯穎科技以「釋放數位能量，點燃永續創新」為願景，致力於推動各種類數位願景的同時，以創新實現永續。我們從「環境友善營運」、「員工與企業共善共榮」、「永續供應鏈」及「綠色創新」等四個面向，制定長期目標，並進一步將 ESG 績效連結薪酬制度，以深化永續管理，並推動永續發展與核心商業領域的對外倡議，透過參與及對話，深化公司在永續創新的影響力；同時積極參與社會關懷與環境保育等公益活動，與弱勢團體及當地社區等利害關係人議合，希望透過緯穎科技的...`
- ID `10373` true=`No` pred=`Yes` text=`過去四年，AI 為全世界帶來巨大的改變，時至今日依然還在持續演進中，相信在人類的進步史中 AI 必然成為一股很重要的推力。我們一直思考的事是，公司怎麼運用自身的強項再創造出更高效率、低耗能的架構，讓 AI 運算中心基礎建設可以兼顧永續與韌性。現在智邦創新基地，已開發出散熱、光傳輸、AI 運算中心組網方式等等相關先進技術，希望能與全球各地頂尖合作夥伴分享，並共同努力加速創新技術的發展。 Professional ESG sustai...`

## evidence_quality

### Per-Label Metrics

| Label | Precision | Recall | F1 | Support |
|---|---:|---:|---:|---:|
| Clear | 0.810345 | 0.846847 | 0.828194 | 111 |
| Not Clear | 0.227273 | 0.238095 | 0.232558 | 21 |
| Misleading | 0.000000 | 0.000000 | 0.000000 | 0 |
| N/A | 0.806452 | 0.735294 | 0.769231 | 68 |

### Confusion Matrix

Rows are truth labels; columns are predicted labels.

| Truth \ Pred | Clear | Not Clear | Misleading | N/A |
|---|---:|---:|---:|---:|
| Clear | 94 | 10 | 0 | 7 |
| Not Clear | 11 | 5 | 0 | 5 |
| Misleading | 0 | 0 | 0 | 0 |
| N/A | 11 | 7 | 0 | 50 |

### Largest Gaps

- `Not Clear` -> `Clear`: 11 rows
- `N/A` -> `Clear`: 11 rows
- `Clear` -> `Not Clear`: 10 rows
- `Clear` -> `N/A`: 7 rows
- `N/A` -> `Not Clear`: 7 rows
- `Not Clear` -> `N/A`: 5 rows

### Example Mismatches

- ID `10020` true=`Not Clear` pred=`Clear` text=`鴻海堅持長期永續發展的承諾，明確訂定ESG目標，推動並落實行動策略，積極因應外部日益加劇的永續風險與機遇。我們聚焦於綠色智能、循環經濟、幸福發展、共贏共榮、鴻傳永續、海納治理六大核心策略，持續深化ESG數位智能管理平台與治理基礎，系統推進行動方案，實踐責任經營，創造永續價值。《行為準則》是鴻海規範全球廠區與員工商業行為的核心依據，也是處理與各類利益相關方關係的基本準則。如當地法律與本準則有所差異或衝突，我們將依法從事，同時遵循更高...`
- ID `10042` true=`Not Clear` pred=`Clear` text=`面對氣候變遷所帶來的挑戰，長榮航空訂定「公共事務參與倡議守則」與「環境及能源政策」，並承諾 2050 年淨零碳排放的目標。透過訂定淨零路徑、推動減緩與調適行動方案與參與氣候相關行業協會組織等，期許為全球社會帶來正面的改變和影響。此外，長榮航空針對行業協會參與建立審查與監督機制，管理範疇涵蓋本公司全球營運據點，以確保氣候相關公共事務參與符合永續發展政策、環境及能源政策與「巴黎協定」，並期望協會的運行與我們關注之商業核心本業、氣候變遷...`
- ID `10062` true=`Not Clear` pred=`Clear` text=`中鋼承諾所有產品及其包裝所使用或包含之金屬沒有來自剛果 ( 金 ) 及其周邊國家，以及這些國家內任何武裝力量控制區之衝突礦產；透過加強供應鏈管理，有效甄別和追溯原料來源。針對料源投資作業，凡具有衝突疑慮之礦產，即不列入投資評估考慮。中鋼於設備及物料採購時亦關注來源國家之人權狀況，據以做可能之調整，並於投標須知 / 合約條款規定不得行賄、不得侵權、進入中鋼廠區須遵守環安衛規定等行為準則。 Professional ESG Susta...`
- ID `10237` true=`Not Clear` pred=`Clear` text=`為了評估氣候變遷對公司業務、策略和財務規劃的影響，我們採取了三個階段的氣候風險與機會辨識流程。通過此流程，我們收斂了統一企業面臨的五項重大風險和一項重大機會，詳細方法請參考 2020 年統一企業社會責任報告書。我們進一步針對環境法規相關資訊量化對統一企業的財務影響，並就相應議題進一步檢視與調整關鍵氣候風險與機會的議題因應與管理現況。2024 年，我們將持續依據最新的環境變化與政策趨勢，追蹤並優化氣候風險與機會管理措施，確保相關策略...`
- ID `10292` true=`Not Clear` pred=`Clear` text=`在餐損管理策略，除透過大數據分析輔以專業人員經驗精準預測旅客報到率，藉以調整各航線減量訂餐比率，持續降低餐損。此外藉由 CM (Amadeus Altéa Departure Control Customer Management) 追蹤轉機旅客搭乘之前段航班 NO SHOW 人數與班機狀態，以推算該班旅客報到情形並調整餐數、降低餐損。全球訂餐人員定期實施年度訓練，持續訓練提升人員控餐技巧，搭配公司推行網路報到及早掌握旅客報到人數...`
- ID `10507` true=`Not Clear` pred=`Clear` text=`本年度報告書呈現統一超商在永續發展方面的觀點與具體作法，說明 2024 年公司治理、經濟、環境及社會面向的相關成果與未來規劃。同時，透過重大性評估流程（請參閱實踐永續管理章節），篩選出統一超商適用之重大主題，期望透過不同管道之揭露、溝通及回饋，為所有利害關係人創造最大共益，邁向最卓越零售商之目標。 Professional ESG Sustainability Report Analysis Assistant. A scanne...`
- ID `10522` true=`Not Clear` pred=`Clear` text=`聯電與中國信託銀行簽訂永續發展表現連結貸款 (Sustainability Linked Loan)。貸款架構通過金融機構的審核，並遵循國際資本市場協會制定的《永續發展表現連結貸款原則》，連結聯電數個具指標性的永續關鍵績效目標結合。透過與金融機構的合作，共同實現「與環境共生」的永續願景。 Professional ESG Sustainability Report Analysis Assistant. A scanned pag...`
- ID `10641` true=`Not Clear` pred=`Clear` text=`為讓旅客享受賓至如歸的飛行旅程，長榮航空定期更新機上餐飲內容、使用在地食材及當季新鮮食材，持續並擴大與國際知名主廚聯手推出新穎潮流餐點，搭配各式酒類與飲品，創新與突破旅客的航餐體驗。 Professional ESG Sustainability Report Analysis Assistant. Extract text from a scanned page of a corporate ESG report. Conver...`

## Evidence-Based Next Suggestions

- Focus first on `verification_timeline` because it has the lowest macro F1 in this report (0.3812).
- Inspect `verification_timeline` label `within_2_years`: recall is 0.0000 over support 1.
- Inspect `verification_timeline` label `between_2_and_5_years`: recall is 0.1591 over support 44.
- Inspect `evidence_quality` label `Not Clear`: recall is 0.2381 over support 21.
- Review `verification_timeline` confusion `between_2_and_5_years` -> `already` (18 rows) before adding new rules.
- Review `evidence_status` confusion `No` -> `Yes` (18 rows) before adding new rules.
- Review `verification_timeline` confusion `more_than_5_years` -> `already` (15 rows) before adding new rules.

## Anti-Hallucination Note

The suggestions above are generated only from the prediction/truth comparison in this report. They are not proof of root cause; inspect the cited IDs and confusion pairs before changing code.
