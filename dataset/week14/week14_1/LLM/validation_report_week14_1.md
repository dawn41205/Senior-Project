# Validation Evidence Report

- Generated: 2026-06-02 23:54:43
- Prediction file: `E:\project\test510\week14_structured_full_rerun_fresh\week14_1\LLM_pipeline_pred_week14_1.json`
- Truth file: `E:\project\test510\dataset\week14\week14_1\val_grouped.json`
- Input file: `E:\project\test510\week14_structured_full_rerun_fresh\week14_1\val_formal_input.json`
- Prediction rows: 200
- Truth rows: 200
- Weighted score: `0.638775`

## Score Summary

| Field | Weight | Macro F1 | Weighted component | Truth distribution | Prediction distribution |
|---|---:|---:|---:|---|---|
| promise_status | 0.20 | 0.909744 | 0.181949 | Yes=167, No=33 | Yes=158, No=42 |
| verification_timeline | 0.15 | 0.577903 | 0.086686 | already=88, between_2_and_5_years=39, more_than_5_years=39, N/A=33, within_2_years=1 | already=83, N/A=43, between_2_and_5_years=41, more_than_5_years=29, within_2_years=4 |
| evidence_status | 0.30 | 0.680452 | 0.204136 | Yes=148, N/A=33, No=19 | Yes=154, N/A=42, No=4 |
| evidence_quality | 0.35 | 0.474302 | 0.166006 | Clear=122, N/A=52, Not Clear=26 | Clear=95, Not Clear=57, N/A=48 |

## promise_status

### Per-Label Metrics

| Label | Precision | Recall | F1 | Support |
|---|---:|---:|---:|---:|
| Yes | 0.993671 | 0.940120 | 0.966154 | 167 |
| No | 0.761905 | 0.969697 | 0.853333 | 33 |

### Confusion Matrix

Rows are truth labels; columns are predicted labels.

| Truth \ Pred | Yes | No |
|---|---:|---:|
| Yes | 157 | 10 |
| No | 1 | 32 |

### Largest Gaps

- `Yes` -> `No`: 10 rows
- `No` -> `Yes`: 1 rows

### Example Mismatches

- ID `10111` true=`Yes` pred=`No` text=`瑞昱全員活動除公司攜手職工福利委員會舉辦一年一度的尾牙旺年晚會活動外，在「瑞昱家庭日」活動上，我們邀請同仁帶著眷屬親友一同共襄盛舉參加包含五大活動主題的家庭日活動，包含：(1) 瑞昱鐵人三項與體育競賽活動、(2) 瑞昱同仁團隊趣味競賽分組活動、(3) 大螃蟹、小螃蟹遊樂設施體驗與親子闖關活動、(4) 瑞昱園遊會同樂活動，以及 (5) 全員齊聚與資深同仁頒獎活動，打造專屬螃蟹家族「團隊、創新、活力」氛圍之家庭日活動，共創螃蟹大家庭特...`
- ID `10216` true=`Yes` pred=`No` text=`2024 年船舶主因為巴拿馬運河限航及紅海危機，造成船舶需繞道，增加航程與時間使用較多的燃油，但本公司仍積極採取管控措施，熱值相較 2023 年僅增加約 7.93%，且 2024 年年度營業收入較 2023 年增加 58.37%，使能源使用強度較 2023 年減少 31.85%。 Professional ESG Sustainability Report Analysis Assistant. Extract text from...`
- ID `10248` true=`Yes` pred=`No` text=`每年盤點本公司之台灣子公司中租迪和、合迪、中租汽車、仲利國際、仲利越南等投融資數據(包含股權投資、公司債、一般企業授信及車貸)，2024年授信客戶，依據中租鑑別之五大高碳排產業分類，符合分析標的之企業總數共898家。本公司企業客戶的碳排放曝險以水泥工業及鋼鐵工業為主，在情境一當中國鍵曝險產業為鋼鐵工業；因本公司授信客戶主要位於台灣及中國大陸區域，在情境二及情境三之中中國因政策轉變，碳價開始快速成長，故本公司水泥工業曝險額度隨著碳價...`
- ID `10356` true=`Yes` pred=`No` text=`台塑工業 ( 寧波 ) 公司也致力於廢棄物管理並減量，主要透過末端處置進行。 Professional ESG Sustainability Report Analysis Assistant. Extract all text from a scanned image of an ESG report. Convert tables to Markdown format precisely. The user specifica...`
- ID `10426` true=`Yes` pred=`No` text=`報告揭露及品質管理流程 議合 包容性 確實與利害關係人溝通，收集合理期待 衝擊性 對台積公司組織營運、外部永續發展造成衝擊及利害關係人關注的 ESG 議題 重大性 鑑別與排序 ESG 議題，定義台積公司重大議題 回應性 制訂重大議題管理方針，透明揭露行動與績效 Professional ESG Sustainability Report Analysis Assistant. Extract text from the provi...`
- ID `10430` true=`Yes` pred=`No` text=`本公司自 1992 年公司成立時即與國際接軌並配合政府全面禁用海龍 (Halons)、CFC-11、CFC-12 等易破壞臭氧層物質。現況使用冷媒多為 R-134a、R-401a、R-410a；並且汽、柴油產品硫、苯含量嚴格遵照歐盟規範。 Professional ESG Sustainability Report Analysis Assistant. Extract all text from a scanned page i...`
- ID `10715` true=`Yes` pred=`No` text=`本行風險管理組織架構係以董事會為最高決策單位，且每年需接受至少 6 小時數之風險課程，包括防制洗錢、反貪腐、資訊安全等風險管控議題。其下設置風險管理委員會統籌全行風險管理，並於總經理下設風險管理處，2024 年由協理陳嘉鴻擔任單位主管，負責建立全行性風險管理機制，獨立行使全行風險管理之職權；各權責單位視其規模及重要性、複雜度設置風險管理人員，負責執行各權責單位之風險管理。此外，總經理下另設置授信審議委員會及投資審議委員會分別負責授...`
- ID `10866` true=`Yes` pred=`No` text=`利害關係人意義與議合目的： 維持良好的互動是營運上的重點，制定年度目標時，將其納入評估考量因素，作為營運要點規劃，以達成廠鄉一家親的願景 Professional ESG Sustainability Report Analysis Assistant. Extract text from the provided image. Convert tables into Markdown format. Pay special at...`

## verification_timeline

### Per-Label Metrics

| Label | Precision | Recall | F1 | Support |
|---|---:|---:|---:|---:|
| already | 0.710843 | 0.670455 | 0.690058 | 88 |
| within_2_years | 0.250000 | 1.000000 | 0.400000 | 1 |
| between_2_and_5_years | 0.560976 | 0.589744 | 0.575000 | 39 |
| more_than_5_years | 0.448276 | 0.333333 | 0.382353 | 39 |
| N/A | 0.744186 | 0.969697 | 0.842105 | 33 |

### Confusion Matrix

Rows are truth labels; columns are predicted labels.

| Truth \ Pred | already | within_2_years | between_2_and_5_years | more_than_5_years | N/A |
|---|---:|---:|---:|---:|---:|
| already | 59 | 0 | 13 | 10 | 6 |
| within_2_years | 0 | 1 | 0 | 0 | 0 |
| between_2_and_5_years | 5 | 1 | 23 | 6 | 4 |
| more_than_5_years | 18 | 2 | 5 | 13 | 1 |
| N/A | 1 | 0 | 0 | 0 | 32 |

### Largest Gaps

- `more_than_5_years` -> `already`: 18 rows
- `already` -> `between_2_and_5_years`: 13 rows
- `already` -> `more_than_5_years`: 10 rows
- `between_2_and_5_years` -> `more_than_5_years`: 6 rows
- `already` -> `N/A`: 6 rows
- `between_2_and_5_years` -> `already`: 5 rows
- `more_than_5_years` -> `between_2_and_5_years`: 5 rows
- `between_2_and_5_years` -> `N/A`: 4 rows

### Example Mismatches

- ID `10031` true=`more_than_5_years` pred=`already` text=`近年全球暖化造成各地環境災害，國巨股份有限公司了解溫室氣體的排放將對環境造成傷害，基於關心生活，貢獻社會的精神，完成系統化的溫室氣體排放盤查與清冊建置，並制定內部文件化及查證程序等。期盼能達成能源節約、工業減廢、資源回收與再利用目標，共同為國內產業未來朝向低碳型經濟社會來努力。為有效管理本公司能源使用情況，防止浪費資源能源，並適時謀求提升使用效率，各廠均配合政府節能規定設定每年節電率 1%以上之目標，台灣廠區與中國廠區已於每年接受...`
- ID `10061` true=`more_than_5_years` pred=`already` text=`隔年度輪流舉行運動會與員工旅遊，提升員工身心健康與團隊凝聚力。員工交流活動：每季由不同部門舉辦創意慶生活動，每月舉辦「萬海好食光」提供精選下午茶促進交流，不定期在公司頂樓空中花園安排活動，讓同仁在美食與音樂的輕鬆氛圍中彼此交流。社團活動：目前全台灣計有 27 個各類社團，包含但不限於登山健行慢跑社、保齡球社、太極拳社、攝影社、手工藝社、拳擊社等，員工每年最多可參加兩個社團，每月每社團可補助新台幣 500 元活動經費。 Profes...`
- ID `10067` true=`more_than_5_years` pred=`already` text=`統一超商每年持續投入大量教育訓練資源，針對不同階層、部門設計規劃不同課程，包含新進人員訓練、階層別訓練、門市、後勤公開班、通識課程、及各單位專業訓練。2024 年教育訓練總費用投入共 86,888 仟元，平均每人訓練費用 9,459 元，相較去年人均訓練費用多 2,424 元；全公司教育訓練總時數為 134,624 小時，平均每人受訓時數為 14.66 小時（註）。2024 年因應同仁工作型態，除了持續開辦實體課程，也積極打造數位...`
- ID `10137` true=`more_than_5_years` pred=`already` text=`陽明海運岸勤人員每年定期施作績效考核及晉升作業，績效考核作業每年進行一次，並於每年初進行績效目標設定，年中進行期中面談，年末進行績效考核，以肯定從業人員貢獻，激發潛能，提昇個人工作與組織營運績效並配合公司經營理念與發展願景，經由職位升遷資格條件之規範，拔擢優秀人才，激勵員工士氣，提高生產力。受考核者須於期初時填寫「工作目標規劃」，內容包含當年度個人工作目標及個人發展計劃，至期中面談階段，主管與被考核者進行面談，以了解被考核者工作情...`
- ID `10175` true=`more_than_5_years` pred=`already` text=`「安全、服務、永續」是經營的核心價值，藉由運行安全架構，持續強化飛安與地安等安全範疇。定期報告營運狀況及產業前景，傳達經營理念與企業價值，將整年度經營重點載於年報，提供重要財務及業務資訊供投資人參考。訂有「風險管理政策與程序」，依重大性原則，將營運過程中可能面臨之經濟(含公司治理)、環境、社會與其他面向之風險，執行風險範疇確認、評估、管理及揭露，並每年定期向董事會報告運作情形。長期以來致力於資訊安全制度建立與法令規範遵循，設立專責...`
- ID `10185` true=`more_than_5_years` pred=`already` text=`緯創長期深耕外部創新，自 2010 年起積極參與新創圈活動與投資，與各類新創夥伴攜手合作：與時代基金會共同培育未來創業人才，攜手規劃 Wistron Lab@Garage+ 新創空間，並捐助支持 AAMA 台北搖籃計畫等，持續推動創新生態系的發展。 Professional ESG Sustainability Report Analysis Assistant. An image of a page from Wistron's...`
- ID `10199` true=`more_than_5_years` pred=`already` text=`為落實供應商管理政策，合庫督促供應商遵守相關勞動法規及遵循國際人權公約，彙整潛在及可能發生之人權議題，定期對供應商辦理人權盡職調查，包括避免或減少加班或過長的工作時間、設定最長的工作時間、確保男女同工同酬等強迫勞動與性別平等等議題，以掌握風險發生之頻率與影響程度，並針對潛在人權風險議題擬訂減緩措施，作為未來供應商管理政策精進之參考。 Professional ESG Sustainability Report Analysis A...`
- ID `10210` true=`more_than_5_years` pred=`already` text=`永豐金控透過編撰並每年發行永續報告書 (Sustainability Report)，讓利害關係人與社會大眾瞭解永豐金控在環境 (E)、社會 (S)、治理 (G) 的具體作為，以及回應聯合國永續發展目標 (SDGs) 之承諾與行動，並藉此檢視永續策略的進展，期能攜手各方利害關係人推動企業、環境與社會之永續發展。本報告書於2025年7月發行，報導期間為2024年度 (2024年1月1日至12月31日)。中英文版皆可於永豐金控官網下載...`

## evidence_status

### Per-Label Metrics

| Label | Precision | Recall | F1 | Support |
|---|---:|---:|---:|---:|
| Yes | 0.909091 | 0.945946 | 0.927152 | 148 |
| No | 0.750000 | 0.157895 | 0.260870 | 19 |
| N/A | 0.761905 | 0.969697 | 0.853333 | 33 |

### Confusion Matrix

Rows are truth labels; columns are predicted labels.

| Truth \ Pred | Yes | No | N/A |
|---|---:|---:|---:|
| Yes | 140 | 1 | 7 |
| No | 13 | 3 | 3 |
| N/A | 1 | 0 | 32 |

### Largest Gaps

- `No` -> `Yes`: 13 rows
- `Yes` -> `N/A`: 7 rows
- `No` -> `N/A`: 3 rows
- `Yes` -> `No`: 1 rows
- `N/A` -> `Yes`: 1 rows

### Example Mismatches

- ID `10200` true=`No` pred=`Yes` text=`聯電在 2003 年成立「企業資訊安全委員會」，由總經理擔任主席，並由數位功能組織吳宗賢資深副總經理擔任督導暨資訊安全長，公司內各單位（包含法務、人力資源、研發、工程、生產等）主管均為委員會成員。另成立「企業安全處」專責公司資訊安全及實體安全規劃與相關的稽核事項，亦主導此委員會運行。企業資訊安全委員會負責執行資安管理規劃，建置、維護管理體系，統籌相關政策制定、執行，以及風險管理與遵循度查核。透過每半年管理審查會議，審核資安風險分析...`
- ID `10282` true=`No` pred=`Yes` text=`緯穎科技以「釋放數位能量，點燃永續創新」為願景，致力於推動各種類數位願景的同時，以創新實現永續。我們從「環境友善營運」、「員工與企業共善共榮」、「永續供應鏈」及「綠色創新」等四個面向，制定長期目標，並進一步將 ESG 績效連結薪酬制度，以深化永續管理，並推動永續發展與核心商業領域的對外倡議，透過參與及對話，深化公司在永續創新的影響力；同時積極參與社會關懷與環境保育等公益活動，與弱勢團體及當地社區等利害關係人議合，希望透過緯穎科技的...`
- ID `10297` true=`No` pred=`Yes` text=`有感於河川水資源珍貴，合庫銀行持續響應並簽署天下雜誌發起的「淡水河公約」，落實資源回收及廢棄物減量措施，加強對供應商宣導環境永續概念及提高綠色採購比率，承諾為河川健康減塑減廢，為推動臺灣水域的永續發展盡一份心力。 Professional ESG Sustainability Report Analysis Assistant. A scanned page from a corporate ESG report (Taiwan ...`
- ID `10549` true=`No` pred=`Yes` text=`台塑推動永續投資轉型，聚焦高值化、綠色轉型及數位創新為核心，致力於開發新技術新產品，朝電子／半導體、綠能環保及醫療保健三大全球發展趨勢邁進，導入 AI 技術，強化競爭力，實現創新與永續的成長動能。 Professional ESG Sustainability Report Analysis Assistant. Extract all text from the provided image. Convert tabular d...`
- ID `10555` true=`No` pred=`Yes` text=`監理壓力增加：各國政府和國際組織提高對金融機構之監理要求，如全球報告倡議組織 (GRI) 發布「GRI 101: 生物多樣性 2024」，並於 2026/1/1 正式生效，促使金融機構採取自然行動；國際永續發展標準委員會 (ISSB) 已經著手制定揭露標準草案 (IFRS S3)，將自然相關揭露納入框架中；自然相關財務揭露工作小組 (TNFD) 已於 2023 年 9 月發布指引，強調企業需揭露自然相關風險和機會，及對生物多樣性影...`
- ID `10637` true=`No` pred=`Yes` text=`合庫除為員工提供基礎就職訓練、語言課程，及強制性、合規性或基本之職業健康與安全培訓外，近年更規劃員工發展計畫，期能強化員工專業技能，藉此提高整體營運績效。 Professional ESG Sustainability Report Analysis Assistant. Extract text from a scanned image of an ESG report page. Convert tabular data in...`
- ID `10644` true=`No` pred=`Yes` text=`本公司內部績效評核分別以「董事會績效考核自評問卷」、「董事成員績效評估自評問卷」、「薪酬委員會績效考核自評問卷」與「審計委員會績效考核自評問卷」進行評估，滿分為 5 分 ( 非常同意 5 分；同意 4 分；普通 3 分；不同意 2 分；非常不同意 1 分)，2024 年董事會暨功能性委員會績效評估結果皆高於 4.5 分，整體績效俱佳，董事及功能性委員會對於各項評核指標運作多為非常認同，整體運作良好，符合公司治理要求。本公司外部評核...`
- ID `10698` true=`No` pred=`Yes` text=`展望未來，聯發科技將持續以「全球觀」、「創新」、「人才」、「公司治理」、「綠色營運」及「在地實踐」六大面向推展永續作為，同時以加入 SBTi 科學基礎減量目標倡議，並成立 TCFD 小組等實際行動，加大對全球氣候變遷風險的因應力道。此外，我們將逐步導入 IFRS 國際財務報導準則，以確保公司的營運狀況與永續績效執行成效能完整揭露，並與國際永續報導準則接軌。 Professional ESG Sustainability Repor...`

## evidence_quality

### Per-Label Metrics

| Label | Precision | Recall | F1 | Support |
|---|---:|---:|---:|---:|
| Clear | 0.863158 | 0.672131 | 0.755760 | 122 |
| Not Clear | 0.263158 | 0.576923 | 0.361446 | 26 |
| Misleading | 0.000000 | 0.000000 | 0.000000 | 0 |
| N/A | 0.812500 | 0.750000 | 0.780000 | 52 |

### Confusion Matrix

Rows are truth labels; columns are predicted labels.

| Truth \ Pred | Clear | Not Clear | Misleading | N/A |
|---|---:|---:|---:|---:|
| Clear | 82 | 34 | 0 | 6 |
| Not Clear | 8 | 15 | 0 | 3 |
| Misleading | 0 | 0 | 0 | 0 |
| N/A | 5 | 8 | 0 | 39 |

### Largest Gaps

- `Clear` -> `Not Clear`: 34 rows
- `Not Clear` -> `Clear`: 8 rows
- `N/A` -> `Not Clear`: 8 rows
- `Clear` -> `N/A`: 6 rows
- `N/A` -> `Clear`: 5 rows
- `Not Clear` -> `N/A`: 3 rows

### Example Mismatches

- ID `10040` true=`Clear` pred=`Not Clear` text=`拓展「蹲點・台灣」社會影響力。行動貼合大學 USR (大學社會責任) 計畫，鼓勵更多大學生養成社會人文關懷精神，共同為在地永續發展努力。至今已與全臺近六十間包含高中職與大專院校合作，近兩萬師生參與。 Professional ESG Sustainability Report Analysis Assistant. Extract text from a scanned page of an ESG report. Convert...`
- ID `10056` true=`Clear` pred=`Not Clear` text=`台泥旗下達和航運所有水泥船皆優先自主導入岸電系統，優於IMO規定 達和航運積極響應國際海事組織(IMO)減排策略 目標2030年減碳40% 2025年啟用環保水泥船「達循輪」，導入智能船管系統、封閉式裝卸技術，相較能源效率設計指數第一階段(EEDI Phase I)預估減碳23.7%。旗下散裝貨輪在現成船能源效率指數(EEXI)與營運碳強度指標(CII)方面皆優於IMO規範，CII評級持續保持在目標C級以上，86%船隻更達到最優等...`
- ID `10060` true=`Clear` pred=`Not Clear` text=`本公司現任董事共11席，包含7位董事及4位獨立董事，年齡介於50至83歲間，包括3位女性，兼任公司員工之董事共3位，累積平均任期為7.91年。成員擁有生技、金融、教育及財務金融等產業之豐富經驗與專業，具備執行職務所需之知識、技能與素養，其中亦包括一位國家發展基金管理會代表，提升產業成長動能。4位獨立董事中，1名任期年資在5年以上，其經驗橫跨產、官、學三界，擁有傑出全球生技業生產與製造經驗，故繼續借重專業經驗，給與董事會監督並提供專...`
- ID `10061` true=`Clear` pred=`Not Clear` text=`隔年度輪流舉行運動會與員工旅遊，提升員工身心健康與團隊凝聚力。員工交流活動：每季由不同部門舉辦創意慶生活動，每月舉辦「萬海好食光」提供精選下午茶促進交流，不定期在公司頂樓空中花園安排活動，讓同仁在美食與音樂的輕鬆氛圍中彼此交流。社團活動：目前全台灣計有 27 個各類社團，包含但不限於登山健行慢跑社、保齡球社、太極拳社、攝影社、手工藝社、拳擊社等，員工每年最多可參加兩個社團，每月每社團可補助新台幣 500 元活動經費。 Profes...`
- ID `10079` true=`Clear` pred=`Not Clear` text=`台灣大於2022年制定「保護生物多樣性及零毀林宣言」，攜手關鍵價值鏈（包含一階供應商及非一階供應商），積極倡議，並與學研機構、保育單位或社區等利害關係人合作，維護自然生態系統與棲地，遏止生物多樣性喪失。在衝擊殘餘的情況下，以零淨損失(No Net Loss)原則進行最大補償，計畫於2050年實現生物多樣性淨正向衝擊(Net Positive Impact)與終止任何形式的毀林行為(No Gross Deforestation)，詳...`
- ID `10137` true=`Clear` pred=`Not Clear` text=`陽明海運岸勤人員每年定期施作績效考核及晉升作業，績效考核作業每年進行一次，並於每年初進行績效目標設定，年中進行期中面談，年末進行績效考核，以肯定從業人員貢獻，激發潛能，提昇個人工作與組織營運績效並配合公司經營理念與發展願景，經由職位升遷資格條件之規範，拔擢優秀人才，激勵員工士氣，提高生產力。受考核者須於期初時填寫「工作目標規劃」，內容包含當年度個人工作目標及個人發展計劃，至期中面談階段，主管與被考核者進行面談，以了解被考核者工作情...`
- ID `10199` true=`Clear` pred=`Not Clear` text=`為落實供應商管理政策，合庫督促供應商遵守相關勞動法規及遵循國際人權公約，彙整潛在及可能發生之人權議題，定期對供應商辦理人權盡職調查，包括避免或減少加班或過長的工作時間、設定最長的工作時間、確保男女同工同酬等強迫勞動與性別平等等議題，以掌握風險發生之頻率與影響程度，並針對潛在人權風險議題擬訂減緩措施，作為未來供應商管理政策精進之參考。 Professional ESG Sustainability Report Analysis A...`
- ID `10219` true=`Clear` pred=`Not Clear` text=`因應金管會法規，廣達於2024年底啟動IFRS永續資訊揭露準則導入計畫，進一步明確強化永續風險的治理，並隨導入計畫執行項目揭露。其中，永續風險以IFRS S1和S2永續揭露準則為標準，將環境、社會與治理（E、S、G）相關的風險和機會與財務評估結合，該風險內容經由特定之報告機制向董事會報告，以確保在營運策略或金融治理上能有效反應。 Professional ESG Sustainability Report Analysis Ass...`

## Evidence-Based Next Suggestions

- Focus first on `evidence_quality` because it has the lowest macro F1 in this report (0.4743).
- Inspect `evidence_status` label `No`: recall is 0.1579 over support 19.
- Inspect `verification_timeline` label `more_than_5_years`: recall is 0.3333 over support 39.
- Inspect `evidence_quality` label `Not Clear`: recall is 0.5769 over support 26.
- Review `evidence_quality` confusion `Clear` -> `Not Clear` (34 rows) before adding new rules.
- Review `verification_timeline` confusion `more_than_5_years` -> `already` (18 rows) before adding new rules.
- Review `verification_timeline` confusion `already` -> `between_2_and_5_years` (13 rows) before adding new rules.

## Anti-Hallucination Note

The suggestions above are generated only from the prediction/truth comparison in this report. They are not proof of root cause; inspect the cited IDs and confusion pairs before changing code.
