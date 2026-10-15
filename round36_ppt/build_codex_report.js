const fs = require('fs');
const path = require('path');
const ppt = fs.readFileSync('round36_ppt/ppt_dump.txt','utf8');
const root = 'J:/Desktop/XLPR';
const dir = fs.readdirSync(root).find(x=>x.startsWith('2026_10_13_XLPR') && fs.existsSync(path.join(root,x,'cgr_text.txt')));
const raw = fs.readFileSync(path.join(root,dir,'cgr_text.txt'),'utf8');
const pages = {};
for (const m of raw.matchAll(/=====PAGE\s+(\d+)=====([\s\S]*?)(?======PAGE|$)/g)) pages[+m[1]-1]=m[2];
const slides={};
for(const m of ppt.matchAll(/===== SLIDE (\d+) =====([\s\S]*?)(?====== SLIDE|$)/g)) slides[+m[1]]=m[2].trim();
// 열: 슬라이드 | 원문 그대로 인용할 PPT 행의 검색 문자열 | 인쇄 쪽 | 절 | 영어 직접 인용 | 문제 유형: 설명 | 최소 교체안
const data = `
2|MOUDLE|68|3 제목|CRACK GROWTH RATE MODULE|오탈자: MOUDLE 철자 오류.|CRACK GROWTH RATE MODULE
3|기본값임|18|1.2|The foundation of the PWSCC growth model is a module|의미 변경: foundation(기반)을 기본값(default)으로 바꾸었다.|PWSCC 성장 모델의 기반은 환경·하중변수와 불확실성을 포함해 성장 속도를 예측하는 모듈임.
3|권장 매개변수를|18|1.2|The Crack Growth Subgroup has provided model parameter recommendations for PWSCC|일치|
3|다른 재료|18|1.2|does not occur or occurs at substantially reduced rate relative to Alloy 600 in normal PWR environments.|일치|
3|같은 방식의|18|1.2|Like the PWSCC growth model, the foundation of the fatigue growth model is a module|일치|
3|세 가지 하위|18|1.2|Ni-based alloys, austenitic SS, and ferritic steels.|일치|
3|CGW는|18|1.2|CGR predictions for PWSCC and fatigue mechanisms are|오탈자: CGW → CGR.|PWSCC와 피로의 CGR 예측은 합산되어 프레임워크의 균열 성장 예측에 사용됨.
4|규칙 기반|19|1.2|This module uses rule-based criteria to simulate coalescence of|일치|
4|응력확대계수 증폭|19|1.2|including crack tip interaction that can lead to intensified stress intensity factors and plastic|일치|
4|매개변수는 실험|19|1.2|coalescence model parameters and has validated them against laboratory studies and fracture|일치|
4|CGR 모듈은|19|1.3|The objective of the Crack Growth Module of xLPR 2.0 is to predict SCC and fatigue CGRs in|일치|
4|합체 모듈은|19|1.3|The objective of the Coalescence Module of xLPR 2.0 is to predict the combination of idealized|일치|
29|거듭법칙에|42|2.3.2.1, 식 2-14|Paris power-law exponent|일치|
29|코드 1~5|72|3.2.1.3|If the fatigue degradation mechanism is active and the material is a nickel-based alloy|일치|
29|temperature effect|42|2.3.2.1, 식 2-14 기호 정의|temperature effect|범위주의: 제공된 EPRI 문서의 해당 기호 정의에는 단위가 없다. PPT의 ‘원 자료’가 NUREG/CR-6721 자체를 뜻한다면 이 자료만으로 그 문서의 단위 표기 유무는 확인 불가.|제공된 EPRI 보고서 p.42의 기호 정의는 F_T를 temperature effect로 표기하며, 그 정의에는 단위를 적지 않음.
29|Alloy 690은|44|2.3.2.2|The roughly 60 tests available for Alloy 690 fatigue CGR in air were not sufficient to support|일치|
57|CGR |14|약어 목록|Crack Growth Rate|일치|
57|Meterial Group|71|3.2.1.2, 표 3-1|Material Groups Recognized by CGR Module|오탈자: Meterial → Material.|Material Group
57|Transient component|78|3.3.1|The number of active transient components that are|일치|
62|피로 메커니즘이|73|3.2.1.3, 식 3-3|where all variables with the subscript cstm are user-defined custom CGR model parameters.|일치|
62|재료코드 10|73|3.2.1.3|If the fatigue degradation mechanism is active and the material is in a custom material|일치|
62|상승 시간 효과|73|3.2.1.3, 식 3-3|Custom|수식확인: 이 행은 식 3-3의 상승시간 거듭제곱과 하중비 거듭제곱 구조와 일치. 수식은 추출 텍스트의 줄바꿈을 고려하여 판독함.|
62|5개 값은|77|3.3, 표 3-3|Custom model scaling constant|일치|
64|몇 가지 규칙|92|4.1|These conventions are a substitute for higher order fracture|일치|
64|균열간섭 (|92|4.1|resulting in accelerated growth;|일치|
64|ligament 붕괴|92|4.1|experiences high stresses to the point of fully plastic failure.|일치|
64|이미 성장 중인|92|4.1; p.19 각주 2|when two adjacent macro-cracks of engineering significance|일치|
64|같은 평면의|93|4.2|The conventions are generally applicable irrespective of material.|일치|
64|pairwise colescence|93|4.2.1|All coalescence conventions are based on pairwise|오탈자: colescence → coalescence.|모든 규칙은 두 균열 사이의 pairwise coalescence를 기준으로 함.
64|세 균열 이상|93|4.2.1|pairwise coalescence conventions are applied in series.|일치|
64|몬테카를로|93|4.2.1|of minor importance (due to the many other sources of significant uncertainty).|일치|
65|Prediction of|93|4.2.1.1 제목|Prediction of Imminent Coalescence|오탈자: lmminent의 첫 문자는 소문자 l이 아니라 대문자 I이며, Colescence → Coalescence.|Prediction of Imminent Coalescence
65|가장 짧은 ID|93|4.2.1.1|The prediction of coalescence is contingent on the length of the smallest ID ligament|일치|
65|이 길이가 어떤|93|4.2.1.1|coalescence is said to be imminent, resulting in the replacement of|일치|
65|ID/OD|100|4.3|same ID and OD length|범위주의: 내면/외면이라는 사용 맥락은 맞지만 이 구절은 약어의 영어 풀어쓰기를 정의하지 않는다. 제공 텍스트의 약어 목록에서 별도 확인 필요.|
65|ligament |92|4.1|the span of material separating two through-wall cracks|일치|
66|거리의 합|94|4.2.1.1|with a positive coalescence distance.|의미 변경 + 오탈자: 원문은 양의 합체거리로 모의한다고 하며 거리들을 더한다고 하지 않는다. collaps → collapse.|균열간섭과 ligament collapse는 각각 양의 coalescence distance로 모의할 수 있음. 균열간섭은 K·성장 계산에서, ligament collapse는 K·성장·안정성 계산에서 직접 다루지 않음.
66|기본값은 0|94|4.2.1.1|distance is set to zero by default.|일치|
66|3가지로|94|4.2.1.1|For two through-wall cracks|일치|
66|표와 같이|94|4.2.1.1|For the crack pair made up of one surface crack and one through-wall crack|일치|
66|거리기준 불확실성|98|4.2.2|Uncertainty in the coalescence prediction may be incorporated through the use of distributed|한정어 누락: 원문은 불확실성을 분포된 거리로 반영할 수 있다고 한다(may). 이 첫 문장의 권고로의 강화는 원문 표현과 다름. 개별 분포의 권고는 뒤에서 별도로 제시됨.|합체 예측 불확실성은 분포된 합체거리를 사용해 반영할 수 있음.
66|epistemic|98|4.2.2|It is recommended that these uncertainties be designated as epistemic|일치|
66|구현하지 않음(p.94)|94|4.2.1.1|this dependency is not implemented in the coalescence module for xLPR Version 2.0.|일치|
67|표면 + 표면 |94|4.2.1.1|Provided the second modeling convention, the best-|조건 누락: 0.5는 최대 깊이에 비례시키는 두 번째 규칙의 계수이다. 첫 번째는 사용자 지정 절대거리이므로 두 규칙에 공통인 계수로 적으면 안 됨.|두 convention: 사용자 지정 절대거리 / 최대 깊이×계수(권장). 두 번째 규칙의 best-fit 계수 0.5; ASME Section XI IWA-3000과 일관됨(p.94).
67|표면+표면(불확실성)|98|4.2.2|a triangular distribution is recommended with extremes at 0.0 and 0.75 and a mode at 0.5.|일치|
67|관통+관통 |94|4.2.1.1|depending on the sizes of the flaws involved.|조건 누락: 0~20 in은 해당 부품에서 결함 크기에 따라 가능한 거리라고 설명한다. 무조건적인 사용자 입력 허용범위가 아님.|ligament collapse 모의; 사용자 지정 거리. 대상 부품에서는 결함 크기에 따라 0~20 in의 거리가 가능(p.94).
67|관통 + 관통 (길이관계)|98|4.2.2|with crack length|한정어 누락: 원문의 roughly one-to-one(대략 1:1)이 표에서 단정적인 1:1로 쓰임.|합체거리와 균열 길이가 대략 1:1(p.98).
67|표면+관통|94|4.2.1.1|distance is set to zero by default.|일치|
68|물리적 기대와 논리적|94|4.2.1.2|These transitioning rules were developed based on physical expectations and logical|일치|
68|표의 규칙으로|94|4.2.1.2|The various conventions for modeling the|일치|
68|호의 중심|95|4.2.1.2|The center of the new crack is set to the center of the arc that circumscribes the ID lengths of the|일치|
68|두개의 ID 길이|95|4.2.1.2|the ID length is set such that the|의미 변경: 정하는 대상은 원래 두 균열 각각의 ID 길이가 아니라 합체 후 새 균열 하나의 ID 길이임.|표면+관통 합체 후 새 균열의 ID 길이는 새 균열 면적이 원래 두 균열 면적의 합과 같도록 정함. 이는 합체 직전·직후 안정성 예측의 연속성을 촉진함.
68|하용할|95|4.2.1.2|should result in acceptable leakage continuity|오탈자: 하용할 → 허용할. ‘가져올 것’은 should result in의 기대 표현에 대응함.|OD 길이 규칙은 물리적 기대와 일치하며 합체 직전·직후 허용할 만한 누설 연속성을 가져올 것으로 설명함(p.95).
68|재진입 구간|95|4.2.1.2|regains a roughly symmetric shape|일치|
69|유형 |94|4.2.1.2|the combination of cracks with dissimilar type results in a transitioning|일치|
69|깊이 |95|4.2.1.2|the maximum depth is recommended|일치|
69|중심 |95|4.2.1.2|The center of the new crack is set to the center of the arc|일치|
69|OD길이 |95|4.2.1.2|For two surface cracks, this length is zero.|일치|
69|ID길이 |95|4.2.1.2|area of the coalesced crack is equivalent to the sum of the areas of the original two cracks.|일치|
70|분포된 합체거리|98|4.2.2|This uncertainty may reflect variability in the complex processes that lead|의미 변경: ‘반영할 수 없음’은 원문의 may reflect와 정반대임. 나머지 분포거리 도입 및 epistemic 권고는 일치.|이 불확실성은 합체로 이어지는 복잡한 과정의 변동성과 모델 오차(예: 균열 길이에 대한 체계적 의존성의 부재)를 반영할 수 있음.
70|표면균열 |98|4.2.2|with a best-estimate of 0.5.|일치|
70|관통균열 |98|4.2.2 및 각주 35|Alternatively, the coalescence distance for through-wall cracks may be assumed to be deterministic for|일치|
70|convention 은 논리에|98|4.2.2; p.99 계속|The modeling conventions for type, location, ID length, and|의미 변경: 원문에서 큰 불확실성에 해당하지 않는다고 열거한 것은 type/location/ID length/OD length이며 depth는 제외됨. 깊이는 다음 문장에서 별도의 물리적 기대와 민감도 대상으로 설명함.|다른 규칙은 주어진 균열 쌍과 선택한 규칙에 대해 결정적임. type, location, ID length, OD length 규칙은 논리에 근거해 큰 불확실성이 있다고 보지 않음. 최대 깊이 규칙은 물리적 기대에 근거하며 실행별로 바꾸어 영향을 살필 수 있음(p.98~99).
71|개요  |99|4.2.3|the coalescence modeling conventions were generally validated.|오탈자: conventio → convention(복수 맥락에서는 conventions). 대체로 검증되었다는 한정어는 보존되어 있음.|합체 모델링 conventions은 논리적·물리적 기대를 반영하고 발전된 연구 결과를 수용하도록 개발되었으며, 발표된 연구를 통해 대체로 검증됨.
71|표면균열의 K|99|4.2.3|Experimental evidence suggests that the onset of the intensification of stress intensity factor|일치|
71|관통균열의 양|99|4.2.3|Higher order modeling suggests low likelihood of rapid tearing leading to ligament collapse|오탈자: 사사함 → 시사함. low likelihood 및 길이 의존성 개선 필요는 일치.|상위 수준 모델링은 ligament가 균열 길이보다 짧아질 때까지 급속한 찢김 가능성이 낮다고 시사함.
72|두 표면균열의 최대|99|4.2.3|This rapid growth is predicted with higher order analytical modeling and has been|일치|
72|합체 후 균열 유형|99|4.2.3 및 각주 37|there is not experimental data involving the coalescence of a surface crack and a through-wall|일치|
72|적용 범위 |99|4.2.3|This module validation applies for the full range of crack and component geometries expected|의미 변경: ‘적용 범위’ 행의 본문은 범위를 제시하지 않는다. 같은 쪽의 별도 검증 문장을 가져오면서 검증 대상인 location/ID length/OD length도 빠뜨림.|적용 범위: 이 모듈 검증은 xLPR Version 2.0에서 예상되는 균열·부품 형상의 전체 범위에 적용됨(p.99). 위치·ID 길이·OD 길이 규칙의 대체적 검증은 별도 행으로 표기.
73|가장 중요한 단순화|100|4.3, Convention-based modeling|use of simplified convention-based modeling in lieu of mechanistic or phenomenological|일치|
73|목표는 물리적|100|4.3|approximate physical coalescence in an|일치|
73|이런 모델링은|100|4.3|The model includes a|오탈자: ‘함께 흔히 쓰이는 모델은’에서 두 문장이 잘못 연결되어 확률론적 방법과 규칙 선택 설명의 관계가 흐려짐.|이런 모델링은 개별 결정론적 모의 결과가 주된 의미를 갖지 않는 확률론적 방법과 함께 흔히 쓰임. 모델은 단순화에 대한 민감도를 살필 수 있도록 여러 합체 규칙을 포함함.
73|균열을 반타원|100|4.3, Crack shape idealization|Crack shape idealization|오탈자: 이 문단 위 두 번째 소제목이 Convention-based modeling으로 중복되어 원문 소제목과 다름. 문단의 세 유형 설명은 일치.|두 번째 Convention-based modeling 소제목을 Crack shape idealization으로 교체.
73|이는 응력확대계수|100|4.3|approximation for Version 2 used to allow tractable development of analytical models|일치|
73|실제 PWSCC|100|4.3|provided parameters are selected appropriately.|일치|
73|모든 원주방향|100|4.3, Coplanar crack assumption|All circumferential cracks are assumed to be coplanar within|일치|
73|실제로는 축방향|100|4.3|realistically might remain offset axially and independent are combined.|일치|
73|보수성은|100|4.3|increase leakage rates significantly|일치|
73|겹침이 큰 경우|100|4.3|decrease leakage rates by approximately one half|일치|
74|적용할 때 축방향|101|4.3|Axial cracks are|일치|
74|실제로는 수직|101|4.3|the intersection of perpendicular|일치|
74|같은 평면의 축방향|101|4.3|A maximum of one axial|일치|
74|이종 용접|101|4.3|over a relatively|일치|
74|상위 수준 해석 예측|101|4.3|coalescence distance may be sensitive to crack length and|일치|
74|특히 균열 사이|101|4.3|especially for coalescence of very large cracks|일치|
74|이 체계적 변화|101|4.3|generally early coalescence for short-length cracks and generally late coalescence for|일치|
74|사용 가능한 검증|101|4.3|All validation data available|일치|
74|적용 대상 부품|101|4.3|the extension of flat plate data is reasonable.|일치|
74|pressurizer nozzle|101|4.3|the ID curvature may affect crack|일치|
75|시간 스텝마다|103|5.1|At each time discretization, the Framework may call the coalescence module to|일치|
75|활성 균열 쌍마다|103|5.1|whereby each pair of active cracks is assessed against coalescence criteria.|일치|
75|어떤 쌍이|103|5.1|an absorbed crack, which is effectively ignored|일치|
75|입력으로 줍니다|103|5.1; p.105, 5.2.1.1~2|the Framework provides information about the crack configuration, component geometry,|일치|
75|요구사항을 함께|105|5.2.1.2|guarantees that pairwise coalescence will only occur between adjacent cracks.|일치|
75|원주방향 같은|104|5.1|The scope of the coalescence module is limited to coplanar circumferential cracks.|일치|
75|간 스텝은|111|5.3.2|the one month time|오탈자: 간 스텝 → 시간 스텝. 기본값 1개월 및 세 균열 이상 합체가 드물다는 서술은 일치.|시간 스텝은 xLPR 2.0 기본값이 1개월이며, 세 균열 이상이 같은 스텝에 합체하는 일은 드물다고 봄.
76|일반적으로|105|5.2.1.3; p.106 계속|the leftmost tip|일치|
76|oalescence distance는|106|5.2.1.3|The coalescence distance depends on|오탈자: oalescence → coalescence.|coalescence distance는 두 균열의 종류와 형상에 따라 달라짐.
76|구간 1에서|106|5.2.1.3|The crack that initiated in subunit 1 is the first crack designated as|일치|
76|어떤 균열이|106|5.2.1.3|beginning immediately clockwise of|일치|
76|현재 “Crack A”가|106|5.2.1.3|the crack immediately clockwise of the current|일치|
76|조건을 만족하면|106|5.2.1.3|receives updated attributes corresponding|일치|
76|두 번 이상|106|5.2.1.3|depending on directionality of the iterative procedure.|일치|
76|두 균열까지만|111|5.3.2|Coalescence of three or more cracks can|일치|
77|Coalescence direction |110|5.3.2|clockwise (1) or counter-clockwise direction (2).|일치|
77|Surface crack coalescence distance rule |111|5.3.2|absolute distance (1) or as a ratio of the maximum|일치|
77|Surface crack coalescence distance rule modifier |111|5.3.2|triangular distribution with extremes at 0.0 and 0.75 and a mode at 0.5|일치|
77|Through-wall crack coalescence distance rule modifier |111|5.3.2|a uniform distribution between zero|일치|
77|Coalescence depth rule |111|5.3.2|maximum (1), minimum (2), or average (3)|일치|
78|몇 개의 입력|110|5.3.2|parameter inputs fully define the behavior of the coalescence module|일치|
78|아래 표의|111|5.3.2|should be sampled from a distribution roughly|일치|
78|입력 단위는|109|5.3|This range is different from the range over which model validation was|일치|
78|열 수 0~200|109|5.3, 표 5-1|Number of cracks represented|오탈자: 열 수 → 균열 수. 나머지 0~200, 중심각 범위, 반길이 m, 거리계수의 단위·비음수 조건은 일치.|균열 수 0~200, 균열 중심 0 이상 2π rad 미만. ID·OD 입력은 반길이(m), 거리 규칙 1의 계수는 m, 규칙 2의 계수는 무차원, 관통균열 합체거리는 m이며 거리계수는 0 이상임.
78|열 유형 코드|110|5.3.1|any positive integer corresponds to a|오탈자: 열 유형 → 균열 유형. 유형·방향 코드의 값과 의미는 일치.|균열 유형 코드는 0=미발생, −1=표면, −2=천이, −3=이상화 관통, 양의 정수=흡수됨. 균열 방향은 원주 1, 축 2.
78|두 표면균열은|106|5.2.1.4|If both cracks are through-wall cracks, the coalescence distance is set to a user-defined|일치|
79|흡수된 균열은|107|5.2.1.5|positive integers designate absorbed|일치|
79|그 값은|107|5.2.1.5, 각주 39|initiation time index of the crack with|일치|
79|관여하지 않은|107|5.2.1.6|Cracks not involved in coalescence do not have their attributes updated|일치|
79|돌려주는 인수가|108|5.2.1.6|which output was found to be out of range.|일치|
79|한 번의 호출에서|108|5.2.1.6|the error flag is set to 301.|일치|
79|균열별 벡터|108|5.2.1.6|the order corresponding to crack initiation times.|일치|
79|0은 정상|111|5.3.3; p.109, 5.3|Error codes 101 through 115 communicate an input that is out of its range of verification.|일치|
79|201과 210|112|5.3.3|Error codes 201 and 210 communicate that a calculated output of the coalescence module|일치|
79|301은|112|5.3.3; p.111 시작|If it occurs frequently, the run should be repeated with the|일치|
80|실행중 메모리|108|5.2.1.7|The coalescence module memory does not exceed 30 kB during runtime.|일치|
82|LPR 2.0은|118|6.1.1; p.117 시작|material properties that exists at weld material interfaces|오탈자: LPR → xLPR.|xLPR 2.0은 용접 경계의 복잡한 물성 변화(모재 HAZ, 용접금속 희석 영역)를 모델링하지 않음.
82|용접금속 안에|118|6.1.1|immediately after the crack tip extends into the base|일치|
82|배관 맞대기|118|6.1.1|plant PWSCC experience for piping butt weld|일치|
82|발생 민감도와|118|6.1.1|no precise value is recommended for this correlation.|일치|
82|이 상관은|118|6.1.1|it tends to result in relatively high CGRs for the|일치|
83|Alloy 600 /|118|6.1.2|it may be useful to develop CGR models for other materials and other|일치|
83|현제 구현된|118|6.1.2|alternative model forms may be required.|오탈자: 현제 → 현재. 식 3-1 및 대안 형식의 가능성은 일치.|이런 모델이 현재 구현된 식 3-1 형태에 들어가길 바라지만 다른 형태가 필요할 수도 있음.
83|Alloy 600 다음으로|118|6.1.2|There are efforts underway within the EPRI Expert Panel on PWSCC|일치|
83|더 다양한|118|6.1.2|it may be required to implement SCC CGR models for BWR environments.|일치|
83|스테인리스의 IGSCC|118|6.1.2|IGSCC CGR models for SS have been developed from laboratory data and could be|일치|
85|현재 xLPR|119|6.2.3|irrespective of material.|일치|
85|피로CGR 모델의|119|6.2.4|In some cases, these alternative predictions were not|일치|
85|데이더|119|6.2.4|additional laboratory fatigue CGR data|오탈자: 데이더 → 데이터.|모델 개발과 독립적인 실험 피로 CGR 데이터가 더 필요함.
85|또한 가동중|119|6.2.4|verified to be advancing by fatigue were left in service for one or more cycles|일치|
86|부품 형상2.0|120|6.3.1|represented by three material groups, each an annular shape, adjacent to one another.|오탈자: ‘향후 개선 대상으로 부품 형상2.0의 기본은’은 소제목과 본문이 잘못 연결됨. 세 환형 재료 그룹 및 네 번째 그룹 설명은 일치.|xLPR 2.0은 단순화된 균열·부품 형상에 의존함. 부품 형상: 현재 기본은 인접한 세 환형 재료 그룹으로 나타낸 이종금속 용접이며 overlay/onlay는 네 번째 그룹으로 모델링할 수 있음.
86|이후 두께|120|6.3.1|through-wall|일치|
86|비대칭 균열 성장|120|6.3.1|does not include initiation, growth, coalescence, or|일치|
86|비동일평면 균열과|120|6.3.1|A coordinated effort between the Computational Framework and Models Groups would be required|일치|
86|K-solution 모듈은|120|6.3.2; p.121 계속|the K-solutions modules do not account for the interaction of|일치|
86|이 둘을|120|6.3.2; p.121 계속|is simulated by the coalescence module using simple modeling conventions.|일치|
87|파괴역학 기반|120|6.3.2; p.121 계속|More precise predictions would be achieved using fracture mechanics based solutions|일치|
87|최근 검증 연구|120|6.3.2; p.121 계속|the secondary determinant for|일치|
87|축방향과 원주방향|121|6.3.2|The interaction of axial and circumferential cracks is ignored|일치|
87|교 균열의|121|6.3.2|the effects of the intersection of orthogonal cracks|오탈자: 교 균열 → 직교 균열.|직교 균열의 교차 효과를 넣을 수 있지만 혼합 방향 균열의 처리는 다른 모듈에 더 큰 과제일 수 있음.
87|미세균열(micro|121|6.3.2|commonly considered to be part of the initiation process.|일치|
`.trim();
let records=data.split('\n').map(l=>{let [n,key,page,sec,quote,problem,fix]=l.split('|');return {n:+n,key,page:+page,sec,quote,problem,fix};});
const norm=s=>s.replace(/-\s*\r?\n\s*/g,'-').replace(/\s+/g,' ').trim();
const update=(n,key,changes)=>Object.assign(records.find(r=>r.n===n&&r.key===key),changes);
update(67,'관통 + 관통 (길이관계)',{quote:'the coalescence distance has a roughly one-to-one relationship',problem:'일치',fix:''});
update(65,'ID/OD',{page:14,sec:'약어 목록(인쇄 p.xiv)',quote:'ID Inner Diameter',problem:'일치',fix:'',extra:'“OD Outer Diameter” (인쇄 p.xiv, 약어 목록).'});
update(29,'temperature effect',{problem:'일치',fix:'',extra:'해당 판정은 제공된 EPRI 보고서 p.42의 기호 정의에 한함. 인용된 별도 NUREG 보고서 자체를 조사한 결과가 아님.'});
update(62,'상승 시간 효과',{quote:'where all variables with the subscript cstm are user-defined custom CGR model parameters.',problem:'수식확인: 일치. 원문 이미지 pages/p074.png(인쇄 p.73)의 식 3-3도 직접 확인함.',extra:'식 3-3: da/dN = C_cstm τ_R^(p_cstm) [ΔK/(1−a_cstm R)^(b_cstm)]^(m_cstm). 상승시간과 하중비가 거듭제곱 형태로 들어감.'});
update(77,'Surface crack coalescence distance rule ',{key:'Surface crack coalescence distance rule |'});
update(79,'한 번의 호출에서',{key:'301이 되며'});
const replacements=[
[3,'권장 매개변수를','The Crack Growth Subgroup has provided model parameter recommendations for PWSCC CGR predictions in Alloy 600 and its associated weld metals (Alloys 82, 182, and 1321) in normal PWR environments.'],
[3,'세 가지 하위','Distinct submodels have been developed for fatigue CGR predictions in three different material classes: Ni-based alloys, austenitic SS, and ferritic steels.'],
[3,'CGW는','CGR predictions for PWSCC and fatigue mechanisms are summed and utilized by the xLPR Framework to yield predictions for crack growth.'],
[4,'규칙 기반','This module uses rule-based criteria to simulate coalescence of coplanar circumferential cracks of engineering significance based on their type, geometry, and location.'],
[4,'응력확대계수 증폭','This simulation is intended to account for mechanisms that lead to crack extension on a time-scale significantly faster than that predicted for PWSCC and fatigue growth of a single crack, including crack tip interaction that can lead to intensified stress intensity factors and plastic collapse of a ligament separating two cracks.'],
[4,'매개변수는 실험','The Crack Growth Subgroup has provided general coalescence model parameters and has validated them against laboratory studies and fracture mechanics modeling.'],
[4,'CGR 모듈은','The objective of the Crack Growth Module of xLPR 2.0 is to predict SCC and fatigue CGRs in normal PWR primary water environment of materials commonly located in PWR primary piping systems, including dissimilar metal welds and similar metal welds.'],
[4,'합체 모듈은','The objective of the Coalescence Module of xLPR 2.0 is to predict the combination of idealized cracks of the types modeled within the xLPR 2.0 framework.'],
[29,'Alloy 690은','The roughly 60 tests available for Alloy 690 fatigue CGR in air were not sufficient to support estimation of the Paris power-law model or the load ratio effect. However, the temperature effect was re-estimated for Alloy 690.'],
[57,'Transient component','The number of active transient components that are treated independently in the calculation of fatigue CGR.'],
[64,'몇 가지 규칙','These conventions are a substitute for higher order fracture mechanics calculations that are not amenable to the xLPR probabilistic framework or that were not made a priority for Version 2.0 of xLPR.'],
[64,'균열간섭 (','Crack interaction, whereby stress intensity experienced at crack front locations are amplified due to local stress fields radiating from a nearby crack, resulting in accelerated growth;'],
[64,'ligament 붕괴','Ligament collapse, whereby the span of material separating two through-wall cracks experiences high stresses to the point of fully plastic failure.'],
[64,'pairwise colescence','All coalescence conventions are based on pairwise coalescence between only two cracks.'],
[64,'세 균열 이상','For rare instances of more than two cracks coalescing at the same time at the same location, pairwise coalescence conventions are applied in series.'],
[65,'이 길이가 어떤','When this ligament length becomes less than some value—termed the coalescence distance—coalescence is said to be imminent, resulting in the replacement of the two original cracks with a single coalesced crack in the xLPR Framework.'],
[66,'표와 같이','For the crack pair made up of one surface crack and one through-wall crack, the coalescence distance is set to zero by default.'],
[67,'표면 + 표면 ','Provided the second modeling convention, the best-fit scaling factor is half (0.5) of the maximum depth of the cracks involved in coalescence.'],
[68,'표의 규칙으로','The crack resulting from the coalescence of two original cracks requires updated geometrical attributes including type, depth, length, and location.'],
[68,'두개의 ID 길이','For the coalescence of one through-wall crack and one surface crack, the ID length is set such that the area of the coalesced crack is equivalent to the sum of the areas of the original two cracks. This promotes continuity of the component stability prediction immediately before and after coalescence.'],
[70,'분포된 합체거리','This uncertainty may reflect variability in the complex processes that lead to coalescence as well as model error (e.g., the lack of a systematic dependency with respect to crack length).'],
[70,'convention 은 논리에','The modeling conventions for type, location, ID length, and OD length are logically rooted and are therefore not considered subject to significant uncertainties.'],
[72,'적용 범위 ','This module validation applies for the full range of crack and component geometries expected within xLPR Version 2.0.'],
[73,'이런 모델링은','This type of modeling is often used in association with probabilistic methods where the result of any single deterministic simulation is not of primary significance. The model includes a range of different conventions, or rules, for coalescence so that the sensitivity to these simplifications can be explored.'],
[74,'적용할 때 축방향','Axial cracks are neglected when applying coalescence rules.'],
[74,'실제로는 수직','In reality, the intersection of perpendicular cracks may result in crack blunting that arrests one of the cracks. Therefore, this is a conservative assumption relative to probability of leakage and stability.'],
[74,'같은 평면의 축방향','Coplanar axial cracks are not modeled in Version 2.0 of xLPR. A maximum of one axial crack of engineering significance is modeled at each circumferential discretization of the component.'],
[74,'이종 용접','For dissimilar weld modeling, this is consistent with the expectation that weld residual stresses will peak (and therefore initiation will be most likely) over a relatively narrow axial extent.'],
[74,'상위 수준 해석 예측','Higher order analytical predictions suggest that coalescence distance may be sensitive to crack length and component thickness, especially for coalescence of very large cracks where the ligament stress between the cracks is substantially elevated relative to the intact condition.'],
[74,'사용 가능한 검증','All validation data available concern coalescence of cracks in flat plate geometries.'],
[74,'pressurizer nozzle','For smaller radius components, such as pressurizer nozzles, or for particularly large cracks, the ID curvature may affect crack interaction and susceptibility to ligament collapse.'],
[75,'어떤 쌍이','The iterative procedure continues until no pair of active cracks satisfies coalescence criteria, at which point the coalescence module returns control to the calling entity.'],
[76,'oalescence distance는','The coalescence distance depends on the crack types and geometries of “Crack A” and “Crack B”.'],
[76,'구간 1에서','The crack that initiated in subunit 1 is the first crack designated as “Crack A”.'],
[76,'어떤 균열이','Each time a crack is designated as “Crack A”, each other crack is iteratively designated as “Crack B”, beginning immediately clockwise of “Crack A” and proceeding in the clockwise direction.'],
[76,'현재 “Crack A”가','If the current “Crack A” does not satisfy the coalescence criteria with any other crack, the crack immediately clockwise of the current “Crack A” is designated as the new “Crack A”.'],
[78,'열 유형 코드','0 corresponds to a crack that has not yet initiated; -1 corresponds to a surface crack; -2 corresponds to a transitioning crack; -3 corresponds to an idealized through-wall crack; and any positive integer corresponds to a crack that was previously absorbed by coalescence.'],
[79,'그 값은','Specifically, absorbed cracks are given a crack type equal to the initiation time index of the crack with which it coalesces (i.e., “Crack A”).'],
[79,'301이 되며','If the number of pairwise coalescences exceeds one during a single call to the coalescence module, the error flag is set to 301.'],
[79,'균열별 벡터','All vector array outputs containing crack-specific attributes are reordered and returned with the order corresponding to crack initiation times.'],
[82,'용접금속 안에','immediately after the crack tip extends into the base metal, growth would be predicted with the base metal model.'],
[82,'이 상관은','This correlation can be important for assessing plant risks because it tends to result in relatively high CGRs for the earliest initiating cracks.'],
[83,'Alloy 600 다음으로','There are efforts underway within the EPRI Expert Panel on PWSCC Growth to develop such models.'],
[83,'스테인리스의 IGSCC','IGSCC CGR models for SS have been developed from laboratory data and could be implemented.'],
[85,'현재 xLPR','The current xLPR model uses the same fatigue stress intensity factor range threshold model, irrespective of material.'],
[85,'피로CGR 모델의','The validation performed for the fatigue CGR models was based predominantly on alternative equation or software predictions. In some cases, these alternative predictions were not independent from the development efforts underlying the xLPR fatigue CGR models.'],
[86,'이후 두께','It is expected that later versions of xLPR will introduce more complicated geometries, e.g., to allow for through-wall material gradients.'],
[86,'비동일평면 균열과','A coordinated effort between the Computational Framework and Models Groups would be required to introduce treatment for subsurface flaws.'],
[87,'교 균열의','Coalescence modeling could be updated to account for the effects of the intersection of orthogonal cracks; however, the treatment of mixed orientation cracks is likely more of a challenge for other modules.'],
[87,'미세균열(micro','It is not applicable to simulation of micro-fissure coalescence, a step commonly considered to be part of the initiation process.']
];
for(const [n,key,quote]of replacements)update(n,key,{quote});
// 복합 문장과 표 행은 필요한 추가 근거를 같은 기록에 붙인다.
const ranges=[
[2,'MOUDLE',19,'This report is organized as follows:','Section 7 provides a list of references cited in this report.'],
[3,'다른 재료',18,'Model parameters appropriate for other materials','normal PWR environments.'],
[29,'거듭법칙에',42,'da =C f F F','where:'],
[29,'코드 1~5',42,'Fatigue CGRs for nickel-based alloys are calculated as follows:','[Eqn. 2-14]'],
[29,'코드 1~5',72,'If the fatigue degradation mechanism is active and the material is a nickel-based alloy','Section 2.3.2.'],
[62,'5개 값은',77,'Custom model scaling constant','3.3.1 Physical Inputs'],
[64,'이미 성장 중인',92,'It is emphasized that the coalescence model','Hence, the distinct research area'],
[64,'이미 성장 중인',19,'As detailed later, the term','micro-sized fissures and defects.'],
[64,'같은 평면의',93,'Coalescence modeling conventions are applicable','irrespective of material.'],
[66,'3가지로',94,'Two conventions have been selected','the coalescence distance is set to zero by default.'],
[67,'관통+관통 ',94,'Through-wall crack coalescence','depending on the sizes of the flaws involved.'],
[68,'물리적 기대와 논리적',94,'These transitioning rules','Framework.'],
[68,'하용할',95,'This convention is consistent with physical expectations and should result','immediately before and after coalescence.'],
[68,'재진입 구간',95,'the maximum depth is recommended','regains a roughly symmetric shape'],
[69,'유형 ',94,'Regarding crack type after coalescence','results in a transitioning crack.'],
[69,'깊이 ',95,'Consistent with physical expectations','the maximum depth is recommended'],
[69,'OD길이 ',95,'The OD length of the new crack','the OD length of the original through-wall crack.'],
[69,'ID길이 ',95,'For two surface cracks or two through-wall cracks','immediately before and after coalescence.'],
[70,'분포된 합체거리',98,'Uncertainty in the coalescence prediction','more precise estimates.'],
[70,'표면균열 ',98,'For surface cracks, the ratio','a mode at 0.5.'],
[70,'관통균열 ',98,'The coalescence distance for through-wall cracks should','with crack length'],
[70,'convention 은 논리에',98,'The other coalescence modeling conventions','significant uncertainties.'],
[70,'convention 은 논리에',99,'of surface cracks is based on physical expectation','its influence on xLPR predictions.'],
[71,'표면균열의 K',99,'Experimental evidence suggests','validating the selected modeling convention.'],
[71,'관통균열의 양',99,'Higher order modeling suggests','account for length-dependency.'],
[72,'두 표면균열의 최대',99,'The maximum depth convention','observed experimentally.'],
[72,'합체 후 균열 유형',99,'While there is not experimental data','three crack type options in xLPR Version 2.0.'],
[72,'적용 범위 ',99,'The convention for establishing location','higher order modeling.'],
[73,'균열을 반타원',100,'Crack shape idealization:','or transitioning through-wall cracks.'],
[73,'실제 PWSCC',100,'In reality, of course, PWSCC and fatigue cracks','provided parameters are selected appropriately.'],
[73,'보수성은',100,'The conservatism of this approach','depending on the degree of axial offset.'],
[73,'겹침이 큰 경우',100,'For cracks with substantial','the effects of the coplanar assumption more rigorously.'],
[74,'이 체계적 변화',101,'This systematic variation','within the xLPR framework.'],
[75,'어떤 쌍이',103,'If any pair of cracks','calling entity.'],
[75,'입력으로 줍니다',105,'Prior to any other operations','first found to be out of range.'],
[75,'입력으로 줍니다',105,'All vector arrays corresponding','between adjacent cracks.'],
[75,'간 스텝은',111,'Coalescence of three or more cracks can','default in xLPR Version 2.0.'],
[76,'일반적으로',105,'In general, the crack coalescence criteria','the coalescence distance from the'],
[76,'일반적으로',106,'rightmost tip of','See Section 5.2.1.4.'],
[76,'두 번 이상',106,'The directionality of the iterative','depending on directionality of the iterative procedure.'],
[77,'Surface crack coalescence distance rule |',111,'Surface crack coalescence distance rule:','discussed in Section 4.2.'],
[77,'Surface crack coalescence distance rule modifier ',111,'Surface crack coalescence distance rule modifier:','maximum crack depth.'],
[77,'Through-wall crack coalescence distance rule modifier ',111,'Through-wall crack coalescence distance rule modifier:','and 20 inches.'],
[77,'Coalescence depth rule ',111,'Coalescence depth rule:','findings presented in Section 4.2.'],
[78,'입력 단위는',109,'Required unit:','model validation was performed.'],
[78,'열 수 0~200',109,'Number of cracks represented','Error flag'],
[78,'열 유형 코드',110,'Crack orientation:','Axial cracks are neglected'],
[78,'두 표면균열은',106,'If both cracks are surface cracks','distance is set to zero.'],
[79,'301이 되며',108,'If the number of pairwise coalescences','user or reviewers.'],
[79,'0은 정상',111,'The default error code is 0','Computational Framework.'],
[79,'201과 210',112,'Error codes 201 and 210','unknown error in the coalescence module.'],
[79,'301은',112,'Error code 301','there was no bias during the run.'],
[79,'301은',111,'In addition to the updated crack type','pairwise coalescences is returned.'],
[80,'실행중 메모리',108,'For a case with the existence','1000 times in less than 10 seconds.'],
[82,'LPR 2.0은',117,'The xLPR Version 2.0 program does not account','complex variation of'],
[82,'발생 민감도와',118,'Initiation-growth correlation:','help quantify this correlation.'],
[83,'Alloy 600 다음으로',118,'Alloy 690 and associated weld metals:','to develop such models.'],
[85,'현재 xLPR',119,'While this model has been validated','future revisions of the xLPR program.'],
[85,'또한 가동중',119,'Alternatively, review of in-service examination reports','estimation of fatigue CGR in field conditions.'],
[86,'부품 형상2.0',120,'Component geometry:','a fourth material group.'],
[86,'이후 두께',120,'Furthermore, geometries are expected','head penetration nozzles.'],
[86,'비대칭 균열 성장',120,'Asymmetric crack growth:','predictive fidelity of xLPR.'],
[86,'비대칭 균열 성장',120,'Subsurface flaws:','influence plant risks.'],
[86,'K-solution 모듈은',121,'Ligament collapse:','time of collapse.'],
[86,'이 둘을',121,'Instead, this collapse','time of collapse.'],
[87,'파괴역학 기반',121,'More precise predictions','simulation of ligament collapse.'],
[87,'파괴역학 기반',120,'Revisions to the simple modeling conventions','simulation of crack interaction.'],
[87,'최근 검증 연구',121,'Alternatively, recent validation work','roughly the same size).'],
[87,'미세균열(micro',121,'The simulation of micro-fissure coalescence','Initiation Subgroup.']
];
for(const [n,key,page,start,end]of ranges){
 const r=records.find(r=>r.n===n&&r.key===key);
 const p=norm(pages[page]);let a=p.indexOf(start),b=p.indexOf(end,a);
 if(!r||a<0||b<0)throw Error(`추가 근거 검색 실패 ${n} ${key} ${page} ${start}`);
 (r.more??=[]).push({page,quote:p.slice(a,b+end.length)});
}
const errors=[];
for(const r of records){
 const lines=slides[r.n].split(/\r?\n/).filter(l=>l.includes(r.key));
 if(lines.length!==1) errors.push(`PPT ${r.n}: ${r.key}: ${lines.length}`);
 r.ppt=lines.join(' / ').replace(/\u000b/g,' / ').trim();
 if(r.n===67&&r.key==='표면+관통')r.ppt+=' / | 기본값 0 | p.94';
 if(!norm(pages[r.page]||'').toLowerCase().includes(norm(r.quote).toLowerCase())) errors.push(`QUOTE ${r.n}, p${r.page}: ${r.quote}`);
}
fs.writeFileSync('round36_ppt/report_validation.txt',errors.join('\n'),'utf8');
if(errors.length){console.log(errors.join('\n'));process.exit(1);}
// 짧은 대조 키 대신 그 구절을 포함하는 원문 문장을 근거로 출력한다.
for(const r of records){
 if(r.quote.length>=90||r.n===57||r.key==='ID/OD'||r.n===2||r.n===65&&r.key==='Prediction of')continue;
 const p=norm(pages[r.page]);const at=p.toLowerCase().indexOf(r.quote.toLowerCase());
 const prev=p.lastIndexOf('. ',at);const end=p.indexOf('. ',at+r.quote.length);
 const start=prev<0?at:prev+2;
 if(end>=0&&end+1-start<1800)r.quote=p.slice(start,end+1);
}
let out=`# Round 36 — PPT 텍스트와 EPRI 원문 대조\n\n대상: round36_ppt/ppt_dump.txt의 90개 슬라이드. 근거: Kyle Schmitt, EPRI, *xLPR Models Subgroup Report—Crack Growth and Coalescence*, xLPR-MSGR-CGR Version 1.0, 2016-06-29. 모든 아래 영어 인용은 이 보고서의 제공된 cgr_text.txt에서 직접 확인했다. 외부 문헌의 원문 자체를 검증했다는 뜻은 아니다. 쪽은 인쇄 쪽이며 PAGE 마커 값에서 1을 뺀 값으로 대조했다. 표지·서명면 등 앞부분에는 본문 인쇄 쪽이 없으므로 해당 면은 PAGE 번호로 표시한다.\n\n본문 문장·표 행별 판정이다. 제목·내용 구분을 위한 소제목은 대응 절과 함께 확인하고 오류가 있을 때 별도 기록했다. 빈 틀은 요청에 따라 ‘내용 없음’만 적었다. PPT의 그림·수식 이미지는 텍스트 추출본에 담긴 문장과 별개로 검증하지 않았다. 작성자·소속·발표일·마지막 인사는 원문 과학 주장에 해당하지 않는다. ‘일치’는 해당 문장 내용의 대조 결과이며 슬라이드 전체 무오류 판정은 아니다.\n\n`;
const counts={};
for(let n=1;n<=90;n++){
 if(n===1){out+=`### [슬라이드 1] 제목 일치 / 발표 메타데이터 대조 대상 아님 — 확신도(CONFIRMED / PLAUSIBLE)\n- PPT 문구: “xLPR Crack Growth and Coalescence”; 작성자·소속·발표일.\n- 원문 근거: “Crack Growth and Coalescence” (서명면, PAGE 3, 절 없음).\n- 문제: 제목 일치. 발표자의 성명·소속·발표일은 이 보고서에서 확인 불가(PLAUSIBLE은 미검증 표지이며 사실 확인을 뜻하지 않음).\n\n`;continue;}
 if(n===90){out+=`### [슬라이드 90] 발표 마무리 — 확신도(PLAUSIBLE)\n- PPT 문구: “감사합니다”; “remsys.seoultech.ac.kr”.\n- 원문 근거: 해당 없음(발표 마무리 및 연구실 주소).\n- 문제: 원문 과학 내용 대조 대상 아님. 웹 주소의 유효성은 확인하지 않음.\n\n`;continue;}
 const rs=records.filter(r=>r.n===n);
 if(!rs.length){out+=`### [슬라이드 ${n}]\n내용 없음\n\n`;continue;}
 for(const r of rs){
 const special=r.problem.startsWith('범위주의');
 const match=r.problem==='일치'||r.problem.startsWith('수식확인');
 let label=match?'일치':special?'확인 한계':r.problem.split(':')[0];
 counts[label]=(counts[label]||0)+1;
 const printpage=r.page===14?'xiv':r.page;
 out+=`### [슬라이드 ${n}] ${label} — 확신도(${special?'PLAUSIBLE':'CONFIRMED'})\n- PPT 문구: “${r.ppt}”\n- 원문 근거(영어 인용 + 인쇄 쪽 + 절): “${r.quote}” (p.${printpage}, §${r.sec}).\n`;
 if(r.extra)out+=`- 추가 확인: ${r.extra}\n`;
 for(const e of r.more??[])out+=`- 추가 원문 근거: “${e.quote}” (p.${e.page}, 위 인용 절의 해당 문단).\n`;
 out+=`- 문제: ${match?(r.problem==='일치'?'일치':r.problem.slice(5)):r.problem}\n`;
 if(r.fix)out+=`- 최소 교체안: ${r.fix}\n`;
 out+='\n';
 }
}
out+='## 유형별 개수\n\n문장·표 행 기록 단위로 집계한다. 하나의 기록에 두 유형이 함께 있는 경우 복합 유형 한 건으로 표시하므로, 오탈자의 개별 철자 개수와 다르다. 같은 슬라이드의 반복 출현은 해당 기록에 묶었다.\n\n';
for(const [k,v]of Object.entries(counts))out+=`- ${k}: ${v}건\n`;
out+=`\n- 검토 기록 합계: ${records.length}건(표지·마무리 2건 별도).\n- 내용 없음: ${Array.from({length:90},(_,i)=>i+1).filter(n=>n!==1&&n!==90&&!records.some(r=>r.n===n)).length}개 슬라이드.\n- PPT에 명시된 인용 쪽 확인: 슬라이드 66 p.94; 67 p.94/p.98; 68 p.94/p.95; 70 p.98/p.98~99; 71 p.99; 72 p.99; 75 p.103; 79 p.109. 해당 쪽에서 관련 근거를 확인했다. 쪽 자체가 틀린 사례는 발견하지 못했으며, 72의 적용 범위 행은 쪽 오류가 아닌 내용·대상 오류로 기록했다.\n- 수치·단위 자체의 불일치: 발견하지 못함. 67의 0.5와 0~20 in은 조건 누락으로 별도 기록함.\n- 원문에 없는 내용 추가: 단독 유형 0건(66의 거리 합 표현은 의미 변경에 포함).\n\nGit 작업: 시작 시 git pull을 시도했으나 .git/FETCH_HEAD 쓰기 권한 거부로 실패했다. 커밋·푸시 결과는 아래 실행 기록으로 보완한다.\n\nROUND36 DONE\n`;
out=out.replace('쪽은 인쇄 쪽이며 PAGE 마커 값에서 1을 뺀 값으로 대조했다. 표지·서명면 등 앞부분에는 본문 인쇄 쪽이 없으므로 해당 면은 PAGE 번호로 표시한다.','본문 인쇄 쪽은 PAGE 마커 값에서 1을 뺀 값으로 대조했다. 약어 목록의 실제 인쇄 쪽은 xiv(PAGE 15)이다. 표지·서명면처럼 쪽번호가 없는 면은 PAGE 번호로 표시한다. 원문 인용의 1321은 Alloy 132 뒤에 각주 번호 1이 붙은 추출 표기이다. 영어 인용은 줄바꿈을 공백으로 정리하고 행말 분리 하이픈 뒤 줄바꿈을 연결했다.');
out=out.replace('Git 작업: 시작 시 git pull을 시도했으나 .git/FETCH_HEAD 쓰기 권한 거부로 실패했다. 커밋·푸시 결과는 아래 실행 기록으로 보완한다.','Git 작업: 시작 시 git pull을 시도했으나 .git/FETCH_HEAD 쓰기 권한 거부로 실패했다. 이 환경의 .git 쓰기 제한으로 git add/commit도 완료할 수 없었다. push 결과는 실행 후 기록한다.');
fs.writeFileSync('round36_ppt/codex_ppt.md',out,'utf8');
console.log(JSON.stringify({records:records.length,counts,bytes:Buffer.byteLength(out)},null,2));
