# Validation Evidence Report

- Generated: 2026-06-02 04:23:23
- Prediction file: `E:\project\test510\week14_runs\week14_1\LLM_pipeline_pred_week14_1.json`
- Truth file: `E:\project\test510\dataset\week14\week14_1\val_grouped.json`
- Input file: `E:\project\test510\week14_runs\week14_1\val_formal_input.json`
- Prediction rows: 200
- Truth rows: 200
- Weighted score: `0.433705`

## Score Summary

| Field | Weight | Macro F1 | Weighted component | Truth distribution | Prediction distribution |
|---|---:|---:|---:|---|---|
| promise_status | 0.20 | 0.888517 | 0.177703 | Yes=167, No=33 | Yes=155, No=45 |
| verification_timeline | 0.15 | 0.177223 | 0.026583 | already=88, between_2_and_5_years=39, more_than_5_years=39, N/A=33, within_2_years=1 | N/A=125, between_2_and_5_years=62, more_than_5_years=13 |
| evidence_status | 0.30 | 0.575726 | 0.172718 | Yes=148, N/A=33, No=19 | Yes=152, N/A=45, No=3 |
| evidence_quality | 0.35 | 0.161999 | 0.056700 | Clear=122, N/A=52, Not Clear=26 | N/A=160, Not Clear=25, Misleading=8, Clear=7 |

## promise_status

### Per-Label Metrics

| Label | Precision | Recall | F1 | Support |
|---|---:|---:|---:|---:|
| Yes | 0.993548 | 0.922156 | 0.956522 | 167 |
| No | 0.711111 | 0.969697 | 0.820513 | 33 |

### Confusion Matrix

Rows are truth labels; columns are predicted labels.

| Truth \ Pred | Yes | No |
|---|---:|---:|
| Yes | 154 | 13 |
| No | 1 | 32 |

### Largest Gaps

- `Yes` -> `No`: 13 rows
- `No` -> `Yes`: 1 rows

### Example Mismatches

- ID `10111` true=`Yes` pred=`No` text=`瑞昱全員活動除公司攜手職工福利委員會舉辦一年一度的尾牙旺年晚會活動外，在「瑞昱家庭日」活動上，我們邀請同仁帶著眷屬親友一同共襄盛舉參加包含五大活動主題的家庭日活動，包含：(1) 瑞昱鐵人三項與體育競賽活動、(2) 瑞昱同仁團隊趣味競賽分組活動、(3) 大螃蟹、小螃蟹遊樂設施體驗與親子闖關活動、(4) 瑞昱園遊會同樂活動，以及 (5) 全員齊聚與資深同仁頒獎活動，打造專屬螃蟹家族「團隊、創新、活力」氛圍之家庭日活動，共創螃蟹大家庭特...`
- ID `10169` true=`Yes` pred=`No` text=`2024 年參考業界發生租賃廠房屋頂空調箱火災案例，本公司竹南廠會同房東辦理聯合演練，強化兩廠間的通報與應變能量。藉由演練過程中的 PDCA 循環，檢視公司間的通報聯繫、裝備支援、人員協調等救災流程，優化並擴大減災措施的成效。 Professional ESG Sustainability Report Analysis Assistant. Extract all text from the provided scanned p...`
- ID `10216` true=`Yes` pred=`No` text=`2024 年船舶主因為巴拿馬運河限航及紅海危機，造成船舶需繞道，增加航程與時間使用較多的燃油，但本公司仍積極採取管控措施，熱值相較 2023 年僅增加約 7.93%，且 2024 年年度營業收入較 2023 年增加 58.37%，使能源使用強度較 2023 年減少 31.85%。 Professional ESG Sustainability Report Analysis Assistant. Extract text from...`
- ID `10248` true=`Yes` pred=`No` text=`每年盤點本公司之台灣子公司中租迪和、合迪、中租汽車、仲利國際、仲利越南等投融資數據(包含股權投資、公司債、一般企業授信及車貸)，2024年授信客戶，依據中租鑑別之五大高碳排產業分類，符合分析標的之企業總數共898家。本公司企業客戶的碳排放曝險以水泥工業及鋼鐵工業為主，在情境一當中國鍵曝險產業為鋼鐵工業；因本公司授信客戶主要位於台灣及中國大陸區域，在情境二及情境三之中中國因政策轉變，碳價開始快速成長，故本公司水泥工業曝險額度隨著碳價...`
- ID `10311` true=`Yes` pred=`No` text=`為深化區域化策略合作，並降低製造與運輸過程對環境產生的二氧化碳排放，研華持續運用在地化採購策略，歷年採購均以當地供應商為優先選擇；研華全球營運據點涵蓋六大區域事業單位（RBU），考量目前主要製造基地集中於台灣及昆山，本報告書中關於採購策略與績效聚焦於台灣及昆山地區。整體而言，2024 年研華台灣在地採購金額為 109 億元，比率約 82%；研華昆山在地採購因部分電子、周邊原物料由研華台灣統購因素，在地採購比率約占總金額 43%*，...`
- ID `10378` true=`Yes` pred=`No` text=`光寶的離職率主要來自直接人員（含產線作業員及與生產相關協作人員），並以中國大陸員工為主。未來我們將透過數位智能發展整合智慧製造與自動化作業，以取代直接人員之自然流失人力，並提升人均產值，以降低人力流動所帶來的影響。請參見附錄 137 頁。 Professional ESG Sustainability Report Analysis Assistant. Extract text from a scanned page of an...`
- ID `10430` true=`Yes` pred=`No` text=`本公司自 1992 年公司成立時即與國際接軌並配合政府全面禁用海龍 (Halons)、CFC-11、CFC-12 等易破壞臭氧層物質。現況使用冷媒多為 R-134a、R-401a、R-410a；並且汽、柴油產品硫、苯含量嚴格遵照歐盟規範。 Professional ESG Sustainability Report Analysis Assistant. Extract all text from a scanned page i...`
- ID `10644` true=`Yes` pred=`No` text=`本公司內部績效評核分別以「董事會績效考核自評問卷」、「董事成員績效評估自評問卷」、「薪酬委員會績效考核自評問卷」與「審計委員會績效考核自評問卷」進行評估，滿分為 5 分 ( 非常同意 5 分；同意 4 分；普通 3 分；不同意 2 分；非常不同意 1 分)，2024 年董事會暨功能性委員會績效評估結果皆高於 4.5 分，整體績效俱佳，董事及功能性委員會對於各項評核指標運作多為非常認同，整體運作良好，符合公司治理要求。本公司外部評核...`

## verification_timeline

### Per-Label Metrics

| Label | Precision | Recall | F1 | Support |
|---|---:|---:|---:|---:|
| already | 0.000000 | 0.000000 | 0.000000 | 88 |
| within_2_years | 0.000000 | 0.000000 | 0.000000 | 1 |
| between_2_and_5_years | 0.193548 | 0.307692 | 0.237624 | 39 |
| more_than_5_years | 0.461538 | 0.153846 | 0.230769 | 39 |
| N/A | 0.264000 | 1.000000 | 0.417722 | 33 |

### Confusion Matrix

Rows are truth labels; columns are predicted labels.

| Truth \ Pred | already | within_2_years | between_2_and_5_years | more_than_5_years | N/A |
|---|---:|---:|---:|---:|---:|
| already | 0 | 0 | 35 | 5 | 48 |
| within_2_years | 0 | 0 | 0 | 0 | 1 |
| between_2_and_5_years | 0 | 0 | 12 | 2 | 25 |
| more_than_5_years | 0 | 0 | 15 | 6 | 18 |
| N/A | 0 | 0 | 0 | 0 | 33 |

### Largest Gaps

- `already` -> `N/A`: 48 rows
- `already` -> `between_2_and_5_years`: 35 rows
- `between_2_and_5_years` -> `N/A`: 25 rows
- `more_than_5_years` -> `N/A`: 18 rows
- `more_than_5_years` -> `between_2_and_5_years`: 15 rows
- `already` -> `more_than_5_years`: 5 rows
- `between_2_and_5_years` -> `more_than_5_years`: 2 rows
- `within_2_years` -> `N/A`: 1 rows

### Example Mismatches

- ID `10040` true=`already` pred=`N/A` text=`拓展「蹲點・台灣」社會影響力。行動貼合大學 USR (大學社會責任) 計畫，鼓勵更多大學生養成社會人文關懷精神，共同為在地永續發展努力。至今已與全臺近六十間包含高中職與大專院校合作，近兩萬師生參與。 Professional ESG Sustainability Report Analysis Assistant. Extract text from a scanned page of an ESG report. Convert...`
- ID `10045` true=`already` pred=`N/A` text=`藥華醫藥將其已使用於表彰企業之產品或服務的主要名稱、圖形標誌，及個別所使用過的場域，進行全面性盤點蒐集及各商業國際分類(International Class)，將尚未註冊保護但已進行商業使用的商標(Logo)，批次提交臺灣註冊商標申請案，藉以完整保護新藥相關的註冊商標，進而提升臺灣新藥產業在國際上的品牌形象。 Professional ESG Sustainability Report Analysis Assistant. E...`
- ID `10102` true=`already` pred=`N/A` text=`為增進管理階層及一般員工在洗錢防制及打擊資恐方面之觀念，2024 年度金控董事在公司治理課程亦持續納入防制洗錢及打擊資恐教育訓練，針對集團洗錢防制專責主管 / 人員亦投入相當之教育訓練，總教育訓練時數達 647 小時；此外集團對金控及銀行、人壽、證券、投信、投顧、期貨、融資租賃等子公司之員工所提供之教育訓練方式，包含實體、線上 e-learning 及外部教育訓練課程，合計教育訓練時數為 41,571.44 小時，參加之員工人次為...`
- ID `10108` true=`already` pred=`N/A` text=`員工是台光電子的重要資產，而健康安全是員工的首要財富，為確保員工在一個健康及安全環境中工作及貫徹安全衛生政策，台光電子設置「職業安全衛生委員會」，委員會每三個月召開 1 次會議並針對職安法要求提出建議，共提出 11 項專案皆已於 2024 年底前完成結案： 職業安全衛生委員會勞方代表占總成員的 39%(比率優於法定人數三分之一以上)，其組成如下： (1) 職業安全衛生人員。 (2) 各部門之主管、監督、指揮人員。 (3) 與職業安...`
- ID `10111` true=`already` pred=`N/A` text=`瑞昱全員活動除公司攜手職工福利委員會舉辦一年一度的尾牙旺年晚會活動外，在「瑞昱家庭日」活動上，我們邀請同仁帶著眷屬親友一同共襄盛舉參加包含五大活動主題的家庭日活動，包含：(1) 瑞昱鐵人三項與體育競賽活動、(2) 瑞昱同仁團隊趣味競賽分組活動、(3) 大螃蟹、小螃蟹遊樂設施體驗與親子闖關活動、(4) 瑞昱園遊會同樂活動，以及 (5) 全員齊聚與資深同仁頒獎活動，打造專屬螃蟹家族「團隊、創新、活力」氛圍之家庭日活動，共創螃蟹大家庭特...`
- ID `10121` true=`already` pred=`N/A` text=`統一企業高度重視稅務治理，我們嚴格遵守所有稅務法規，並制定了具體的「稅務政策」和相關的稅務管理責任，以確保誠實申報納稅、評估和應對稅務風險、保持開放和誠實的溝通，以及提供資訊透明度。近三年支付之所得稅費用如下，另外，稅務政策可於公司網站 ( 公司政策項下之稅務政策 ) 下載 https://www.uni-president.com.tw/index.asp Professional ESG Sustainability Repo...`
- ID `10140` true=`already` pred=`N/A` text=`自 2024 第二季度起，研華秉持 ESG 理念，在環境面積極推動數位化以降低碳足跡，並有效運用雲端資源來提高能效。透過優化客服聊天機器人，導入 AI Agent 為客戶提供即時的產品資訊問答與多元服務。該年度由 AI Agent 協助之對話數量月增長率達 26.1%，對話滿意度亦提升 10%。 Professional ESG Sustainability Report Analysis Assistant. An image ...`
- ID `10159` true=`already` pred=`N/A` text=`近年各國政府對於改善空氣品質日趨重視，空氣污染物已然成為全球所關切的重要環境議題。大立光因應全球趨勢從設廠開始即著手空氣污染防制的規劃與執行，透過內部稽核及自我檢視，並配合確實的預防保養、訓練及操作，有效做好污染防治工作，並承諾持續改善污染及危害預防。 Professional ESG sustainability report analysis assistant. A scanned page from a corporate...`

## evidence_status

### Per-Label Metrics

| Label | Precision | Recall | F1 | Support |
|---|---:|---:|---:|---:|
| Yes | 0.894737 | 0.918919 | 0.906667 | 148 |
| No | 0.000000 | 0.000000 | 0.000000 | 19 |
| N/A | 0.711111 | 0.969697 | 0.820513 | 33 |

### Confusion Matrix

Rows are truth labels; columns are predicted labels.

| Truth \ Pred | Yes | No | N/A |
|---|---:|---:|---:|
| Yes | 136 | 3 | 9 |
| No | 15 | 0 | 4 |
| N/A | 1 | 0 | 32 |

### Largest Gaps

- `No` -> `Yes`: 15 rows
- `Yes` -> `N/A`: 9 rows
- `No` -> `N/A`: 4 rows
- `Yes` -> `No`: 3 rows
- `N/A` -> `Yes`: 1 rows

### Example Mismatches

- ID `10200` true=`No` pred=`Yes` text=`聯電在 2003 年成立「企業資訊安全委員會」，由總經理擔任主席，並由數位功能組織吳宗賢資深副總經理擔任督導暨資訊安全長，公司內各單位（包含法務、人力資源、研發、工程、生產等）主管均為委員會成員。另成立「企業安全處」專責公司資訊安全及實體安全規劃與相關的稽核事項，亦主導此委員會運行。企業資訊安全委員會負責執行資安管理規劃，建置、維護管理體系，統籌相關政策制定、執行，以及風險管理與遵循度查核。透過每半年管理審查會議，審核資安風險分析...`
- ID `10282` true=`No` pred=`Yes` text=`緯穎科技以「釋放數位能量，點燃永續創新」為願景，致力於推動各種類數位願景的同時，以創新實現永續。我們從「環境友善營運」、「員工與企業共善共榮」、「永續供應鏈」及「綠色創新」等四個面向，制定長期目標，並進一步將 ESG 績效連結薪酬制度，以深化永續管理，並推動永續發展與核心商業領域的對外倡議，透過參與及對話，深化公司在永續創新的影響力；同時積極參與社會關懷與環境保育等公益活動，與弱勢團體及當地社區等利害關係人議合，希望透過緯穎科技的...`
- ID `10297` true=`No` pred=`Yes` text=`有感於河川水資源珍貴，合庫銀行持續響應並簽署天下雜誌發起的「淡水河公約」，落實資源回收及廢棄物減量措施，加強對供應商宣導環境永續概念及提高綠色採購比率，承諾為河川健康減塑減廢，為推動臺灣水域的永續發展盡一份心力。 Professional ESG Sustainability Report Analysis Assistant. A scanned page from a corporate ESG report (Taiwan ...`
- ID `10329` true=`No` pred=`Yes` text=`視障咖啡師雖然眼睛看不見，但卻能放大大身體的其它感官，完全的輔助工作運行，這也證明了視障咖啡師已具備信心及能力於企業場域穩定工作。智邦已逐步建立適合身障者的工作流程模組，提升工作環境友善與作業的流暢度，我們不僅期望將此經驗與技術培植有需求的社福團體，亦期盼邀請更多企業共同響應。期待更多企業能看見、欣賞與支持，提供一個穩定的工作機會給身障朋友，共同推動身障者的工作平權。 Professional ESG Sustainability...`
- ID `10426` true=`No` pred=`Yes` text=`報告揭露及品質管理流程 議合 包容性 確實與利害關係人溝通，收集合理期待 衝擊性 對台積公司組織營運、外部永續發展造成衝擊及利害關係人關注的 ESG 議題 重大性 鑑別與排序 ESG 議題，定義台積公司重大議題 回應性 制訂重大議題管理方針，透明揭露行動與績效 Professional ESG Sustainability Report Analysis Assistant. Extract text from the provi...`
- ID `10549` true=`No` pred=`Yes` text=`台塑推動永續投資轉型，聚焦高值化、綠色轉型及數位創新為核心，致力於開發新技術新產品，朝電子／半導體、綠能環保及醫療保健三大全球發展趨勢邁進，導入 AI 技術，強化競爭力，實現創新與永續的成長動能。 Professional ESG Sustainability Report Analysis Assistant. Extract all text from the provided image. Convert tabular d...`
- ID `10550` true=`No` pred=`Yes` text=`智邦科技除了致力於網通產品設計、開發外，我們也帶領著同仁透過志工活動關懷社會！作為一個負責任的企業，我們深知自己不僅是商業價值的創造者，更是社會的一份子，志工活動並不是一場形式化的公益，而是我們對這片土地深厚的承諾。「智邦有愛，社會無礙」，智邦將持續關注社會需求，透過更多元的方式實現我們的企業社會責任，期盼用我們的力量能夠創造更多的美好。 Professional ESG Sustainability Report Analysi...`
- ID `10555` true=`No` pred=`Yes` text=`監理壓力增加：各國政府和國際組織提高對金融機構之監理要求，如全球報告倡議組織 (GRI) 發布「GRI 101: 生物多樣性 2024」，並於 2026/1/1 正式生效，促使金融機構採取自然行動；國際永續發展標準委員會 (ISSB) 已經著手制定揭露標準草案 (IFRS S3)，將自然相關揭露納入框架中；自然相關財務揭露工作小組 (TNFD) 已於 2023 年 9 月發布指引，強調企業需揭露自然相關風險和機會，及對生物多樣性影...`

## evidence_quality

### Per-Label Metrics

| Label | Precision | Recall | F1 | Support |
|---|---:|---:|---:|---:|
| Clear | 0.714286 | 0.040984 | 0.077519 | 122 |
| Not Clear | 0.120000 | 0.115385 | 0.117647 | 26 |
| Misleading | 0.000000 | 0.000000 | 0.000000 | 0 |
| N/A | 0.300000 | 0.923077 | 0.452830 | 52 |

### Confusion Matrix

Rows are truth labels; columns are predicted labels.

| Truth \ Pred | Clear | Not Clear | Misleading | N/A |
|---|---:|---:|---:|---:|
| Clear | 5 | 20 | 7 | 90 |
| Not Clear | 0 | 3 | 1 | 22 |
| Misleading | 0 | 0 | 0 | 0 |
| N/A | 2 | 2 | 0 | 48 |

### Largest Gaps

- `Clear` -> `N/A`: 90 rows
- `Not Clear` -> `N/A`: 22 rows
- `Clear` -> `Not Clear`: 20 rows
- `Clear` -> `Misleading`: 7 rows
- `N/A` -> `Not Clear`: 2 rows
- `N/A` -> `Clear`: 2 rows
- `Not Clear` -> `Misleading`: 1 rows

### Example Mismatches

- ID `10031` true=`Clear` pred=`N/A` text=`近年全球暖化造成各地環境災害，國巨股份有限公司了解溫室氣體的排放將對環境造成傷害，基於關心生活，貢獻社會的精神，完成系統化的溫室氣體排放盤查與清冊建置，並制定內部文件化及查證程序等。期盼能達成能源節約、工業減廢、資源回收與再利用目標，共同為國內產業未來朝向低碳型經濟社會來努力。為有效管理本公司能源使用情況，防止浪費資源能源，並適時謀求提升使用效率，各廠均配合政府節能規定設定每年節電率 1%以上之目標，台灣廠區與中國廠區已於每年接受...`
- ID `10040` true=`Clear` pred=`N/A` text=`拓展「蹲點・台灣」社會影響力。行動貼合大學 USR (大學社會責任) 計畫，鼓勵更多大學生養成社會人文關懷精神，共同為在地永續發展努力。至今已與全臺近六十間包含高中職與大專院校合作，近兩萬師生參與。 Professional ESG Sustainability Report Analysis Assistant. Extract text from a scanned page of an ESG report. Convert...`
- ID `10045` true=`Clear` pred=`N/A` text=`藥華醫藥將其已使用於表彰企業之產品或服務的主要名稱、圖形標誌，及個別所使用過的場域，進行全面性盤點蒐集及各商業國際分類(International Class)，將尚未註冊保護但已進行商業使用的商標(Logo)，批次提交臺灣註冊商標申請案，藉以完整保護新藥相關的註冊商標，進而提升臺灣新藥產業在國際上的品牌形象。 Professional ESG Sustainability Report Analysis Assistant. E...`
- ID `10056` true=`Clear` pred=`N/A` text=`台泥旗下達和航運所有水泥船皆優先自主導入岸電系統，優於IMO規定 達和航運積極響應國際海事組織(IMO)減排策略 目標2030年減碳40% 2025年啟用環保水泥船「達循輪」，導入智能船管系統、封閉式裝卸技術，相較能源效率設計指數第一階段(EEDI Phase I)預估減碳23.7%。旗下散裝貨輪在現成船能源效率指數(EEXI)與營運碳強度指標(CII)方面皆優於IMO規範，CII評級持續保持在目標C級以上，86%船隻更達到最優等...`
- ID `10061` true=`Clear` pred=`N/A` text=`隔年度輪流舉行運動會與員工旅遊，提升員工身心健康與團隊凝聚力。員工交流活動：每季由不同部門舉辦創意慶生活動，每月舉辦「萬海好食光」提供精選下午茶促進交流，不定期在公司頂樓空中花園安排活動，讓同仁在美食與音樂的輕鬆氛圍中彼此交流。社團活動：目前全台灣計有 27 個各類社團，包含但不限於登山健行慢跑社、保齡球社、太極拳社、攝影社、手工藝社、拳擊社等，員工每年最多可參加兩個社團，每月每社團可補助新台幣 500 元活動經費。 Profes...`
- ID `10089` true=`Clear` pred=`N/A` text=`為降低環境負擔衝擊，進而達到資源永續，合庫金控導入「ISO 14001 環境管理系統」，制定廢棄物管理措施，透過資源回收再利用、綠色採購及以租代買推動循環經濟，除了力行減量（Reduce）、回收（Recycle）、再利用（Reuse）的環保 3R 政策，提高廢棄物回收及再利用之效益外，同時訂定未來（自 2025 年起）集團廢棄物量（不可回收）目標，調整為每年廢棄物量（不可回收）較前一年度減少 1%，持續精進廢棄物減量目標，督促落實...`
- ID `10102` true=`Clear` pred=`N/A` text=`為增進管理階層及一般員工在洗錢防制及打擊資恐方面之觀念，2024 年度金控董事在公司治理課程亦持續納入防制洗錢及打擊資恐教育訓練，針對集團洗錢防制專責主管 / 人員亦投入相當之教育訓練，總教育訓練時數達 647 小時；此外集團對金控及銀行、人壽、證券、投信、投顧、期貨、融資租賃等子公司之員工所提供之教育訓練方式，包含實體、線上 e-learning 及外部教育訓練課程，合計教育訓練時數為 41,571.44 小時，參加之員工人次為...`
- ID `10108` true=`Clear` pred=`N/A` text=`員工是台光電子的重要資產，而健康安全是員工的首要財富，為確保員工在一個健康及安全環境中工作及貫徹安全衛生政策，台光電子設置「職業安全衛生委員會」，委員會每三個月召開 1 次會議並針對職安法要求提出建議，共提出 11 項專案皆已於 2024 年底前完成結案： 職業安全衛生委員會勞方代表占總成員的 39%(比率優於法定人數三分之一以上)，其組成如下： (1) 職業安全衛生人員。 (2) 各部門之主管、監督、指揮人員。 (3) 與職業安...`

## Evidence-Based Next Suggestions

- Focus first on `evidence_quality` because it has the lowest macro F1 in this report (0.1620).
- Inspect `verification_timeline` label `already`: recall is 0.0000 over support 88.
- Inspect `evidence_status` label `No`: recall is 0.0000 over support 19.
- Inspect `verification_timeline` label `within_2_years`: recall is 0.0000 over support 1.
- Review `evidence_quality` confusion `Clear` -> `N/A` (90 rows) before adding new rules.
- Review `verification_timeline` confusion `already` -> `N/A` (48 rows) before adding new rules.
- Review `verification_timeline` confusion `already` -> `between_2_and_5_years` (35 rows) before adding new rules.

## Anti-Hallucination Note

The suggestions above are generated only from the prediction/truth comparison in this report. They are not proof of root cause; inspect the cited IDs and confusion pairs before changing code.
