# Validation Evidence Report

- Generated: 2026-05-25 04:18:44
- Prediction file: `E:\project\test510\week13_runs\week13_1\LLM_pipeline_pred_week13_1.json`
- Truth file: `E:\project\test510\dataset\week13\week13_1\val_grouped.json`
- Input file: `E:\project\test510\week13_runs\week13_1\val_formal_input.json`
- Prediction rows: 200
- Truth rows: 200
- Weighted score: `0.554533`

## Score Summary

| Field | Weight | Macro F1 | Weighted component | Truth distribution | Prediction distribution |
|---|---:|---:|---:|---|---|
| promise_status | 0.20 | 0.746048 | 0.149210 | Yes=167, No=33 | Yes=164, No=36 |
| verification_timeline | 0.15 | 0.546126 | 0.081919 | already=88, between_2_and_5_years=39, more_than_5_years=39, N/A=33, within_2_years=1 | already=106, N/A=37, more_than_5_years=29, between_2_and_5_years=26, within_2_years=2 |
| evidence_status | 0.30 | 0.560210 | 0.168063 | Yes=148, N/A=33, No=19 | Yes=147, N/A=51, No=2 |
| evidence_quality | 0.35 | 0.443834 | 0.155342 | Clear=122, N/A=52, Not Clear=26 | Clear=126, N/A=55, Not Clear=19 |

## promise_status

### Per-Label Metrics

| Label | Precision | Recall | F1 | Support |
|---|---:|---:|---:|---:|
| Yes | 0.920732 | 0.904192 | 0.912387 | 167 |
| No | 0.555556 | 0.606061 | 0.579710 | 33 |

### Confusion Matrix

Rows are truth labels; columns are predicted labels.

| Truth \ Pred | Yes | No |
|---|---:|---:|
| Yes | 151 | 16 |
| No | 13 | 20 |

### Largest Gaps

- `Yes` -> `No`: 16 rows
- `No` -> `Yes`: 13 rows

### Example Mismatches

- ID `10045` true=`Yes` pred=`No` text=`藥華醫藥將其已使用於表彰企業之產品或服務的主要名稱、圖形標誌，及個別所使用過的場域，進行全面性盤點蒐集及各商業國際分類(International Class)，將尚未註冊保護但已進行商業使用的商標(Logo)，批次提交臺灣註冊商標申請案，藉以完整保護新藥相關的註冊商標，進而提升臺灣新藥產業在國際上的品牌形象。 Professional ESG Sustainability Report Analysis Assistant. E...`
- ID `10061` true=`Yes` pred=`No` text=`隔年度輪流舉行運動會與員工旅遊，提升員工身心健康與團隊凝聚力。員工交流活動：每季由不同部門舉辦創意慶生活動，每月舉辦「萬海好食光」提供精選下午茶促進交流，不定期在公司頂樓空中花園安排活動，讓同仁在美食與音樂的輕鬆氛圍中彼此交流。社團活動：目前全台灣計有 27 個各類社團，包含但不限於登山健行慢跑社、保齡球社、太極拳社、攝影社、手工藝社、拳擊社等，員工每年最多可參加兩個社團，每月每社團可補助新台幣 500 元活動經費。 Profes...`
- ID `10111` true=`Yes` pred=`No` text=`瑞昱全員活動除公司攜手職工福利委員會舉辦一年一度的尾牙旺年晚會活動外，在「瑞昱家庭日」活動上，我們邀請同仁帶著眷屬親友一同共襄盛舉參加包含五大活動主題的家庭日活動，包含：(1) 瑞昱鐵人三項與體育競賽活動、(2) 瑞昱同仁團隊趣味競賽分組活動、(3) 大螃蟹、小螃蟹遊樂設施體驗與親子闖關活動、(4) 瑞昱園遊會同樂活動，以及 (5) 全員齊聚與資深同仁頒獎活動，打造專屬螃蟹家族「團隊、創新、活力」氛圍之家庭日活動，共創螃蟹大家庭特...`
- ID `10216` true=`Yes` pred=`No` text=`2024 年船舶主因為巴拿馬運河限航及紅海危機，造成船舶需繞道，增加航程與時間使用較多的燃油，但本公司仍積極採取管控措施，熱值相較 2023 年僅增加約 7.93%，且 2024 年年度營業收入較 2023 年增加 58.37%，使能源使用強度較 2023 年減少 31.85%。 Professional ESG Sustainability Report Analysis Assistant. Extract text from...`
- ID `10248` true=`Yes` pred=`No` text=`每年盤點本公司之台灣子公司中租迪和、合迪、中租汽車、仲利國際、仲利越南等投融資數據(包含股權投資、公司債、一般企業授信及車貸)，2024年授信客戶，依據中租鑑別之五大高碳排產業分類，符合分析標的之企業總數共898家。本公司企業客戶的碳排放曝險以水泥工業及鋼鐵工業為主，在情境一當中國鍵曝險產業為鋼鐵工業；因本公司授信客戶主要位於台灣及中國大陸區域，在情境二及情境三之中中國因政策轉變，碳價開始快速成長，故本公司水泥工業曝險額度隨著碳價...`
- ID `10356` true=`Yes` pred=`No` text=`台塑工業 ( 寧波 ) 公司也致力於廢棄物管理並減量，主要透過末端處置進行。 Professional ESG Sustainability Report Analysis Assistant. Extract all text from a scanned image of an ESG report. Convert tables to Markdown format precisely. The user specifica...`
- ID `10426` true=`Yes` pred=`No` text=`報告揭露及品質管理流程 議合 包容性 確實與利害關係人溝通，收集合理期待 衝擊性 對台積公司組織營運、外部永續發展造成衝擊及利害關係人關注的 ESG 議題 重大性 鑑別與排序 ESG 議題，定義台積公司重大議題 回應性 制訂重大議題管理方針，透明揭露行動與績效 Professional ESG Sustainability Report Analysis Assistant. Extract text from the provi...`
- ID `10430` true=`Yes` pred=`No` text=`本公司自 1992 年公司成立時即與國際接軌並配合政府全面禁用海龍 (Halons)、CFC-11、CFC-12 等易破壞臭氧層物質。現況使用冷媒多為 R-134a、R-401a、R-410a；並且汽、柴油產品硫、苯含量嚴格遵照歐盟規範。 Professional ESG Sustainability Report Analysis Assistant. Extract all text from a scanned page i...`

## verification_timeline

### Per-Label Metrics

| Label | Precision | Recall | F1 | Support |
|---|---:|---:|---:|---:|
| already | 0.594340 | 0.715909 | 0.649485 | 88 |
| within_2_years | 0.500000 | 1.000000 | 0.666667 | 1 |
| between_2_and_5_years | 0.576923 | 0.384615 | 0.461538 | 39 |
| more_than_5_years | 0.413793 | 0.307692 | 0.352941 | 39 |
| N/A | 0.567568 | 0.636364 | 0.600000 | 33 |

### Confusion Matrix

Rows are truth labels; columns are predicted labels.

| Truth \ Pred | already | within_2_years | between_2_and_5_years | more_than_5_years | N/A |
|---|---:|---:|---:|---:|---:|
| already | 63 | 0 | 5 | 9 | 11 |
| within_2_years | 0 | 1 | 0 | 0 | 0 |
| between_2_and_5_years | 15 | 1 | 15 | 6 | 2 |
| more_than_5_years | 20 | 0 | 4 | 12 | 3 |
| N/A | 8 | 0 | 2 | 2 | 21 |

### Largest Gaps

- `more_than_5_years` -> `already`: 20 rows
- `between_2_and_5_years` -> `already`: 15 rows
- `already` -> `N/A`: 11 rows
- `already` -> `more_than_5_years`: 9 rows
- `N/A` -> `already`: 8 rows
- `between_2_and_5_years` -> `more_than_5_years`: 6 rows
- `already` -> `between_2_and_5_years`: 5 rows
- `more_than_5_years` -> `between_2_and_5_years`: 4 rows

### Example Mismatches

- ID `10031` true=`more_than_5_years` pred=`already` text=`近年全球暖化造成各地環境災害，國巨股份有限公司了解溫室氣體的排放將對環境造成傷害，基於關心生活，貢獻社會的精神，完成系統化的溫室氣體排放盤查與清冊建置，並制定內部文件化及查證程序等。期盼能達成能源節約、工業減廢、資源回收與再利用目標，共同為國內產業未來朝向低碳型經濟社會來努力。為有效管理本公司能源使用情況，防止浪費資源能源，並適時謀求提升使用效率，各廠均配合政府節能規定設定每年節電率 1%以上之目標，台灣廠區與中國廠區已於每年接受...`
- ID `10067` true=`more_than_5_years` pred=`already` text=`統一超商每年持續投入大量教育訓練資源，針對不同階層、部門設計規劃不同課程，包含新進人員訓練、階層別訓練、門市、後勤公開班、通識課程、及各單位專業訓練。2024 年教育訓練總費用投入共 86,888 仟元，平均每人訓練費用 9,459 元，相較去年人均訓練費用多 2,424 元；全公司教育訓練總時數為 134,624 小時，平均每人受訓時數為 14.66 小時（註）。2024 年因應同仁工作型態，除了持續開辦實體課程，也積極打造數位...`
- ID `10137` true=`more_than_5_years` pred=`already` text=`陽明海運岸勤人員每年定期施作績效考核及晉升作業，績效考核作業每年進行一次，並於每年初進行績效目標設定，年中進行期中面談，年末進行績效考核，以肯定從業人員貢獻，激發潛能，提昇個人工作與組織營運績效並配合公司經營理念與發展願景，經由職位升遷資格條件之規範，拔擢優秀人才，激勵員工士氣，提高生產力。受考核者須於期初時填寫「工作目標規劃」，內容包含當年度個人工作目標及個人發展計劃，至期中面談階段，主管與被考核者進行面談，以了解被考核者工作情...`
- ID `10175` true=`more_than_5_years` pred=`already` text=`「安全、服務、永續」是經營的核心價值，藉由運行安全架構，持續強化飛安與地安等安全範疇。定期報告營運狀況及產業前景，傳達經營理念與企業價值，將整年度經營重點載於年報，提供重要財務及業務資訊供投資人參考。訂有「風險管理政策與程序」，依重大性原則，將營運過程中可能面臨之經濟(含公司治理)、環境、社會與其他面向之風險，執行風險範疇確認、評估、管理及揭露，並每年定期向董事會報告運作情形。長期以來致力於資訊安全制度建立與法令規範遵循，設立專責...`
- ID `10185` true=`more_than_5_years` pred=`already` text=`緯創長期深耕外部創新，自 2010 年起積極參與新創圈活動與投資，與各類新創夥伴攜手合作：與時代基金會共同培育未來創業人才，攜手規劃 Wistron Lab@Garage+ 新創空間，並捐助支持 AAMA 台北搖籃計畫等，持續推動創新生態系的發展。 Professional ESG Sustainability Report Analysis Assistant. An image of a page from Wistron's...`
- ID `10210` true=`more_than_5_years` pred=`already` text=`永豐金控透過編撰並每年發行永續報告書 (Sustainability Report)，讓利害關係人與社會大眾瞭解永豐金控在環境 (E)、社會 (S)、治理 (G) 的具體作為，以及回應聯合國永續發展目標 (SDGs) 之承諾與行動，並藉此檢視永續策略的進展，期能攜手各方利害關係人推動企業、環境與社會之永續發展。本報告書於2025年7月發行，報導期間為2024年度 (2024年1月1日至12月31日)。中英文版皆可於永豐金控官網下載...`
- ID `10211` true=`more_than_5_years` pred=`already` text=`依國巨《薪資管理辦法》執行。國巨深信員工是企業的最重要資產，在提升公司營運、團隊與個人績效表現之前提下，每年會透過薪資調查，採取具市場競爭力的整體薪酬，對同仁薪資做出適當的調整，藉以吸引優秀人才加入國巨團隊，共同達成營運目標，與員工共享成果。員工薪資及報酬係依據其學經歷、專業知識技術、專業年資經驗及個人績效表現來決定，不因員工性別而有不同。營運之主要據點的新進員工亦不因其種族、宗教、政治立場、性別、婚姻狀況或隸屬工會之差異而在起薪...`
- ID `10255` true=`more_than_5_years` pred=`already` text=`和碩依據ISO 45001:2018職業安全衛生管理標準，建立適宜之職業安全衛生管理系統，並通過第三方公正單位驗證，全體員工皆涵蓋於此管理系統中，比例為100%。透過持續地稽核與持續確保員工有安全及健康的工作環境，並依據內部程序文件與法規辦理企業社會責任教育訓練，包括職業安全衛生相關教育訓練、企業社會責任稽核教育訓練以及企業社會責任管理系統介紹等實體與線上課程，內容包含作業安全衛生相關法規概要、作業前中後之自動檢查、標準作業程序、...`

## evidence_status

### Per-Label Metrics

| Label | Precision | Recall | F1 | Support |
|---|---:|---:|---:|---:|
| Yes | 0.897959 | 0.891892 | 0.894915 | 148 |
| No | 0.000000 | 0.000000 | 0.000000 | 19 |
| N/A | 0.647059 | 1.000000 | 0.785714 | 33 |

### Confusion Matrix

Rows are truth labels; columns are predicted labels.

| Truth \ Pred | Yes | No | N/A |
|---|---:|---:|---:|
| Yes | 132 | 2 | 14 |
| No | 15 | 0 | 4 |
| N/A | 0 | 0 | 33 |

### Largest Gaps

- `No` -> `Yes`: 15 rows
- `Yes` -> `N/A`: 14 rows
- `No` -> `N/A`: 4 rows
- `Yes` -> `No`: 2 rows

### Example Mismatches

- ID `10200` true=`No` pred=`Yes` text=`聯電在 2003 年成立「企業資訊安全委員會」，由總經理擔任主席，並由數位功能組織吳宗賢資深副總經理擔任督導暨資訊安全長，公司內各單位（包含法務、人力資源、研發、工程、生產等）主管均為委員會成員。另成立「企業安全處」專責公司資訊安全及實體安全規劃與相關的稽核事項，亦主導此委員會運行。企業資訊安全委員會負責執行資安管理規劃，建置、維護管理體系，統籌相關政策制定、執行，以及風險管理與遵循度查核。透過每半年管理審查會議，審核資安風險分析...`
- ID `10282` true=`No` pred=`Yes` text=`緯穎科技以「釋放數位能量，點燃永續創新」為願景，致力於推動各種類數位願景的同時，以創新實現永續。我們從「環境友善營運」、「員工與企業共善共榮」、「永續供應鏈」及「綠色創新」等四個面向，制定長期目標，並進一步將 ESG 績效連結薪酬制度，以深化永續管理，並推動永續發展與核心商業領域的對外倡議，透過參與及對話，深化公司在永續創新的影響力；同時積極參與社會關懷與環境保育等公益活動，與弱勢團體及當地社區等利害關係人議合，希望透過緯穎科技的...`
- ID `10297` true=`No` pred=`Yes` text=`有感於河川水資源珍貴，合庫銀行持續響應並簽署天下雜誌發起的「淡水河公約」，落實資源回收及廢棄物減量措施，加強對供應商宣導環境永續概念及提高綠色採購比率，承諾為河川健康減塑減廢，為推動臺灣水域的永續發展盡一份心力。 Professional ESG Sustainability Report Analysis Assistant. A scanned page from a corporate ESG report (Taiwan ...`
- ID `10329` true=`No` pred=`Yes` text=`視障咖啡師雖然眼睛看不見，但卻能放大大身體的其它感官，完全的輔助工作運行，這也證明了視障咖啡師已具備信心及能力於企業場域穩定工作。智邦已逐步建立適合身障者的工作流程模組，提升工作環境友善與作業的流暢度，我們不僅期望將此經驗與技術培植有需求的社福團體，亦期盼邀請更多企業共同響應。期待更多企業能看見、欣賞與支持，提供一個穩定的工作機會給身障朋友，共同推動身障者的工作平權。 Professional ESG Sustainability...`
- ID `10549` true=`No` pred=`Yes` text=`台塑推動永續投資轉型，聚焦高值化、綠色轉型及數位創新為核心，致力於開發新技術新產品，朝電子／半導體、綠能環保及醫療保健三大全球發展趨勢邁進，導入 AI 技術，強化競爭力，實現創新與永續的成長動能。 Professional ESG Sustainability Report Analysis Assistant. Extract all text from the provided image. Convert tabular d...`
- ID `10550` true=`No` pred=`Yes` text=`智邦科技除了致力於網通產品設計、開發外，我們也帶領著同仁透過志工活動關懷社會！作為一個負責任的企業，我們深知自己不僅是商業價值的創造者，更是社會的一份子，志工活動並不是一場形式化的公益，而是我們對這片土地深厚的承諾。「智邦有愛，社會無礙」，智邦將持續關注社會需求，透過更多元的方式實現我們的企業社會責任，期盼用我們的力量能夠創造更多的美好。 Professional ESG Sustainability Report Analysi...`
- ID `10555` true=`No` pred=`Yes` text=`監理壓力增加：各國政府和國際組織提高對金融機構之監理要求，如全球報告倡議組織 (GRI) 發布「GRI 101: 生物多樣性 2024」，並於 2026/1/1 正式生效，促使金融機構採取自然行動；國際永續發展標準委員會 (ISSB) 已經著手制定揭露標準草案 (IFRS S3)，將自然相關揭露納入框架中；自然相關財務揭露工作小組 (TNFD) 已於 2023 年 9 月發布指引，強調企業需揭露自然相關風險和機會，及對生物多樣性影...`
- ID `10637` true=`No` pred=`Yes` text=`合庫除為員工提供基礎就職訓練、語言課程，及強制性、合規性或基本之職業健康與安全培訓外，近年更規劃員工發展計畫，期能強化員工專業技能，藉此提高整體營運績效。 Professional ESG Sustainability Report Analysis Assistant. Extract text from a scanned image of an ESG report page. Convert tabular data in...`

## evidence_quality

### Per-Label Metrics

| Label | Precision | Recall | F1 | Support |
|---|---:|---:|---:|---:|
| Clear | 0.785714 | 0.811475 | 0.798387 | 122 |
| Not Clear | 0.315789 | 0.230769 | 0.266667 | 26 |
| Misleading | 0.000000 | 0.000000 | 0.000000 | 0 |
| N/A | 0.690909 | 0.730769 | 0.710280 | 52 |

### Confusion Matrix

Rows are truth labels; columns are predicted labels.

| Truth \ Pred | Clear | Not Clear | Misleading | N/A |
|---|---:|---:|---:|---:|
| Clear | 99 | 11 | 0 | 12 |
| Not Clear | 15 | 6 | 0 | 5 |
| Misleading | 0 | 0 | 0 | 0 |
| N/A | 12 | 2 | 0 | 38 |

### Largest Gaps

- `Not Clear` -> `Clear`: 15 rows
- `Clear` -> `N/A`: 12 rows
- `N/A` -> `Clear`: 12 rows
- `Clear` -> `Not Clear`: 11 rows
- `Not Clear` -> `N/A`: 5 rows
- `N/A` -> `Not Clear`: 2 rows

### Example Mismatches

- ID `10071` true=`Not Clear` pred=`Clear` text=`身為新時代科技電信公司，我們體認人才是維繫核心競爭力的關鍵，將員工視為永續成長的夥伴，建構多元共融平等文化之工作環境，邁向區域及世界級的成功，開創永續發展未來。人力資源政策結合公司「Open Possible 能所不能」的核心精神，依此展開選用育留方案。 Professional ESG Sustainability Report Analysis Assistant. Extract text from a scanned pa...`
- ID `10159` true=`Not Clear` pred=`Clear` text=`近年各國政府對於改善空氣品質日趨重視，空氣污染物已然成為全球所關切的重要環境議題。大立光因應全球趨勢從設廠開始即著手空氣污染防制的規劃與執行，透過內部稽核及自我檢視，並配合確實的預防保養、訓練及操作，有效做好污染防治工作，並承諾持續改善污染及危害預防。 Professional ESG sustainability report analysis assistant. A scanned page from a corporate...`
- ID `10210` true=`Not Clear` pred=`Clear` text=`永豐金控透過編撰並每年發行永續報告書 (Sustainability Report)，讓利害關係人與社會大眾瞭解永豐金控在環境 (E)、社會 (S)、治理 (G) 的具體作為，以及回應聯合國永續發展目標 (SDGs) 之承諾與行動，並藉此檢視永續策略的進展，期能攜手各方利害關係人推動企業、環境與社會之永續發展。本報告書於2025年7月發行，報導期間為2024年度 (2024年1月1日至12月31日)。中英文版皆可於永豐金控官網下載...`
- ID `10236` true=`Not Clear` pred=`Clear` text=`合作超過一甲子的日本豐田汽車、精工打造 TOYOTA、HINO 國產化的國瑞汽車、緊密團結且共識堅強的經銷商團隊，以及提供高品質及高配合度的供應商，是和泰汽車成立迄今超過 70 個年頭以來最值得信賴的夥伴。在我們攜手合作之下，共同創造了使員工、股東與顧客驚艷與感動的最佳服務。未來，和泰汽車將持續投入熱情與資源，持續與我們的經銷商及供應商共同努力，再創更多佳績。 Professional ESG Sustainability Rep...`
- ID `10290` true=`Not Clear` pred=`Clear` text=`隨著永續發展成為企業長期競爭力的關鍵要素，廣達持續深化多元面向之永續管理，從員工照顧、社會參與、技術創新，到供應鏈韌性強化與地緣政治調適，積極建構應對全球變局的能力。我們相信，企業的永續實踐與財務表現相輔相成，2024年不僅創下歷年營收與獲利新高，更展現了以永續驅動創新、以創新實現永續的堅定承諾。 Professional ESG Sustainability Report Analysis Assistant. Extract ...`
- ID `10319` true=`Not Clear` pred=`Clear` text=`統一超商為呼應減塑趨勢、回應外部關係人對於包裝包材議題之期待，我們持續關注《全球塑膠公約》，2024 年進行第四次談判後雖未有進展，但統一超商已提前布局，設有減塑小組主責管理，並採取積極行動，確保依循環境部的減塑法規，與消費者及供應商共同逐步減少塑膠用量，針對自有品牌商品包裝包材設定完整管理政策，目標於 2030 年前，自有商品包裝及物料於較 2019 年減少 30% 原生塑膠使用量，自有商品包裝及物料 50% 轉換為環保材質。統...`
- ID `10366` true=`Not Clear` pred=`Clear` text=`國巨集團深知人才全球化趨勢，將更著重於跨國人才培育，多數公司藉由海外輸入優秀人才，國巨集團則是希望由本地輸出優秀人力到海外分公司。國巨未來人才發展策略將是透過招募、留才、培育，達到歷練不同功能別職務、跨國及跨文化的管理能力。 Professional ESG Sustainability Report Analysis Assistant. Extract text from a scanned page of an ESG re...`
- ID `10495` true=`Not Clear` pred=`Clear` text=`2018 年起本集團於內部推動《誠信經營守則承諾書》，承諾除遵守商業行為相關法令外，本集團員工於從事商業行為之過程中，不得做出任何不誠信行為，並應克盡善良管理人之注意義務，督促公司避免做出不誠信行為，確保誠信經營文化之落實。 Professional ESG Sustainability Report Analysis Assistant. Two scanned pages (086 and 087) from a corpor...`

## Evidence-Based Next Suggestions

- Focus first on `evidence_quality` because it has the lowest macro F1 in this report (0.4438).
- Inspect `evidence_status` label `No`: recall is 0.0000 over support 19.
- Inspect `evidence_quality` label `Not Clear`: recall is 0.2308 over support 26.
- Inspect `verification_timeline` label `more_than_5_years`: recall is 0.3077 over support 39.
- Review `verification_timeline` confusion `more_than_5_years` -> `already` (20 rows) before adding new rules.
- Review `promise_status` confusion `Yes` -> `No` (16 rows) before adding new rules.
- Review `verification_timeline` confusion `between_2_and_5_years` -> `already` (15 rows) before adding new rules.

## Anti-Hallucination Note

The suggestions above are generated only from the prediction/truth comparison in this report. They are not proof of root cause; inspect the cited IDs and confusion pairs before changing code.
