# Round 3 — Codex blind 독립 검증

작성일: 2026-09-09. 작업 지시: `round3/_codex_task.md`, 문제 정의: `PROBLEM.md`.
`round3/claude.md` 및 다른 라운드의 조사 결과는 읽지 않았다. 이 문서는 독립 조사이며 최종 공동 결론이나 `DECISION.md`를 대신하지 않는다.

## 1. 핵심 발견과 확인 범위

**가장 먼저 연구 범위를 수정·명확화할 필요가 있다.** Kwon, Markoff, DeFisher(2024), *Materials* 17(3), 569의 제3절은 이미 연성 5000계 알루미늄의 원공·슬릿 시편을 다룬다. 원공 시편에 실측 인장곡선을 넣은 탄소성 유한요소해석을 사용했고, 소성변형으로 응력구배가 작아져 응력 조건이 파괴를 지배한다고 설명한다. 따라서 “이 기준을 연성 금속에 처음 적용”하는 것 자체는 신규성이 아니다. 다만 이 사례가 **응력구배 조건의 독립적인 예측력이나 안정 연성 균열 성장의 J–R 곡선까지 검증한 것은 아니다**. 후자는 본 조사에서의 검증 범위 판단이다. [Kwon 등, 2024, 원문 제2·3절](https://pmc.ncbi.nlm.nih.gov/articles/PMC10856633/)

**TCD와 RKR는 모두 실제 존재한다.** TCD에는 대규모 소성변형 및 연성 균열 전파를 동반하는 금속 노치 시편의 파괴하중 예측 사례가 있다. 그러나 그 사실과 “진행 중인 균열의 전체 성장 저항곡선을 예측했다”는 주장은 다르다. RKR는 탄소성 응력장과 특성거리를 결합한 **벽개파괴** 모델이다. 소성영역을 고려한다는 이유만으로 미세공동 성장·합체에 의한 연성파괴 모델로 분류하면 안 된다. 근거는 §3.2와 §3.7에 제시한다.

웹 검색·열람을 실제 수행했다. 출판사 페이지, 저자 원문 및 대학·학술기관 저장소를 우선 사용했다. 검색엔진의 인용논문 소개나 자동 요약을 해당 논문 본문으로 취급하지 않았다. 아래에서 “원문 확인”과 “초록/공개 발췌 확인”을 구분한다. 유료 본문·원자료를 확보하지 못한 문헌의 수치 재현은 **확인 불가**이다. 학생의 재료·시험 원자료도 제공되지 않아 실험 재분석이나 FE 재현은 수행하지 않았다.

## 2. 결합 가능성을 판단하는 기준

평가의 “높음/중간/낮음”은 **기존의 응력 + 공간 응력구배 구조를 보존하며 확장할 수 있는 정도**에 관한 본 검토의 판단이다. 문헌에서 Kwon 모델과의 결합이 이미 입증됐다는 뜻이 아니다. 필요한 실험 목록도 해당 판단을 시험하기 위한 제안이다.

2021년 Kwon 원문에서 응력구배는 절댓값이며, 원래 에너지형 지표는 다음 구조다.

\[
g=|d\sigma_l/ds|,\qquad
\ell_g=\frac{\sigma_l}{g},\qquad
\mathcal F_e=\frac{\sigma_l^2}{2E}\ell_g
=\frac{\sigma_l^3}{2Eg}.
\]

응력 조건과 \(\mathcal F_e\ge w_f\)를 함께 적용한다. 여기서 \(\ell_g\)는 응력장으로부터 계산되는 **국소 길이**로, 처음부터 일정한 재료 임계거리인 것은 아니다. \(g=0\)에서는 나눗셈을 직접 계산하지 말고 \(\sigma_l^3\ge 2Ew_fg\) 형태 및 별도의 응력 조건으로 다뤄야 한다. [Y. W. Kwon, 2021, *Journal of Pressure Vessel Technology* 143(6), 064503, “Revisiting Failure of Brittle Materials”, DOI 10.1115/1.4050989; 저자 공개 원문 식 (2)–(3)](https://www.researchgate.net/publication/351141697_Revisiting_Failure_of_Brittle_Materials)

다음은 **위 식과 문제에서 주어진 HRR 지수로 수행한 독립 대수 검증**이며, 검증된 신규 파괴법칙이 아니다. 고정된 각도에서 \(s=r\), \(\sigma_l=A r^{-p}\), \(p=1/(n+1)\)라 놓으면

\[
g=p\sigma_l/r,\qquad \ell_g=r/p,\qquad
\mathcal F_e=\frac{A^2}{2Ep}r^{1-2p}
\propto r^{(n-1)/(n+1)}.
\]

따라서 LEFM의 \(p=1/2\)에서는 평가거리 의존성이 소거되지만, 일반적인 HRR의 \(n>1\)에서는 그렇지 않다. **응력장만 HRR로 바꾸고 탄성 에너지밀도와 원래 임계값 해석을 유지하는 단순 치환은 성립하지 않는다.** \(n\)은 여기서 \(\varepsilon_p\propto\sigma^n\)의 지수이다. \(\sigma\propto\varepsilon_p^N\)의 지수를 쓰는 문헌에서는 \(N=1/n\)임에 주의한다.

JavaScript로 지수와 거리비를 직접 계산했다. 동일한 A, E에서 평가거리 r을 10배 바꿀 때의 비는 다음과 같다.

| n | 지수 (n−1)/(n+1) | 기존 지표 F_e(10r)/F_e(r) |
|---|---:|---:|
| 1 | 0 | 1.000000 |
| 3 | 0.5 | 3.162278 |
| 5 | 0.666667 | 4.641589 |
| 10 | 0.818182 | 6.579332 |

재현식: `for (const n of [1,3,5,10]) console.log(n, 10**((n-1)/(n+1)));`. Python 실행은 설치/경로 문제로 실패했고, 위 값은 JavaScript 실행 결과다. 이 계산은 수학적 치환 검증이며 실제 금속의 파괴하중 예측 결과가 아니다.

변형이론의 HRR장에서는 응력×변형률 및 일밀도가 \(r^{-1}\)의 차수를 가지므로, 일밀도와 \(\ell_g\)를 결합하면 거리 차수의 상쇄를 검토할 수 있다. 그러나 단조 비례하중의 일밀도와 실제 소성 소산·손상 에너지는 같은 개념이 아니며, 차원·차수 일치만으로 보편적 파괴조건이 입증되지 않는다. [Rice & Rosengren, 1968, *JMPS* 16(1), 1–12](https://www.sciencedirect.com/science/article/pii/0022509668900136), [Rice, 1968, *Journal of Applied Mechanics* 35, 379–386](https://esag.harvard.edu/rice/015_Rice_PathIndepInt_JAM68.pdf)

## 3. 후보별 비교

### 3.1 J-적분/HRR장 기반 재유도

**핵심:** J로 탄소성 균열끝단 장의 강도를 나타내고, HRR 응력·변형률 분포를 이용해 국소 지표를 다시 유도한다. J/HRR는 그 자체로 공동 합체나 균열 성장의 파괴조건이 아니므로 임계조건과 저항곡선이 별도로 필요하다.

**대표 문헌과 확인 수준:**

- J. R. Rice(1968), “A Path Independent Integral and the Approximate Analysis of Strain Concentration by Notches and Cracks”, *Journal of Applied Mechanics* 35, 379–386. [저자 대학 원문](https://esag.harvard.edu/rice/015_Rice_PathIndepInt_JAM68.pdf): 탄성/변형이론 탄소성체의 경로독립 적분 정의 확인.
- J. R. Rice, G. F. Rosengren(1968), “Plane strain deformation near a crack tip in a power-law hardening material”, *Journal of the Mechanics and Physics of Solids* 16(1), 1–12, DOI 10.1016/0022-5096(68)90013-6. [출판사 초록](https://www.sciencedirect.com/science/article/pii/0022509668900136): 멱법칙 경화, 평면변형률, 응력×변형률의 역거리 특이성 확인.

**결합 가능성: 높음(재유도 구조), 적용에는 조건 필요.** §2처럼 응력과 구배를 모두 계산할 수 있다. 하지만 J를 K 자리로 넣는 단순 대체가 아니라 에너지밀도, 유효응력, 경로 s, 길이, 임계량의 정의를 함께 재검토해야 한다. 일반 증분소성·제하를 동반하는 성장균열에서 원래 J의 경로독립성을 무조건 가정하지 않는다. 먼저 정지 균열의 개시를 다루고 J 지배 영역과 유한변형·둔화 영역을 구분하는 편이 검증 범위를 명확히 한다.

**필요 데이터:** E, ν, 항복응력 및 진응력–진소성변형률 경화곡선; 예비균열 CT 또는 SE(B)의 하중–변위, 균열길이·증분 Δa, J–R 또는 개시 J; 두께·a/W; DIC 또는 CTOD를 통한 변형 검증. 경화곡선은 목줄어듦 이후까지 무비판적으로 공칭값을 환산하면 안 되며 필요한 구간을 역해석으로 보완한다. FE에서는 평가거리·구속도·메시 변화에 대한 응력구배 민감도를 별도로 확인한다.

### 3.2 RKR 국소 벽개파괴 모델

**핵심:** 탄소성 균열끝단 앞에서 인장응력이 임계값을 넘는 영역이 특성거리만큼 확보되어야 벽개파괴가 일어난다는 접근이다. 극한의 한 점 응력만 보는 조건과 구별된다.

**대표 문헌:** R. O. Ritchie, J. F. Knott, J. R. Rice(1973), “On the Relationship between Critical Tensile Stress and Fracture Toughness in Mild Steel”, *Journal of the Mechanics and Physics of Solids* **21(6), 395–410**, DOI **10.1016/0022-5096(73)90008-2**. [LBNL에 공개된 원문 PDF](https://www2.lbl.gov/ritchie/Library/PDF/1973_Ritchie_JMechPhysSolids_OnTheRelationship.pdf).

**직접 확인:** 고질소 연강의 평면변형률 벽개파괴를 대상으로 하며, 탄소성 응력분포와 특성거리 조건을 사용한다. 원문 초록은 임계 인장응력을 넘는 거리와 결정립 크기의 약 두 배를 연결한다. 이 수치를 모든 금속의 보편 상수로 사용할 근거는 없다. PDF 텍스트 추출에는 σ_f가 σ_y로 잘못 읽히는 부분이 있어 기호는 임계 벽개응력 σ_c로 구별한다.

**결합 가능성: 중간.** 유한한 거리에서 응력이 유지되어야 한다는 점에서 응력구배와 가깝다. 그러나 거리 전체의 임계응력 조건을 한 점의 1차 미분으로 바꾸는 것은 별도 근사이며, RKR가 명시적 응력구배 방정식을 제시한 것은 아니다. 순수 연성 tearing을 대상으로 하면 직접 적합성은 낮다. 벽개와 연성파괴가 경쟁하는 재료라면 비교 모델로 의미가 있다.

**필요 데이터:** 온도별 인장 경화곡선, 예비균열/노치 파괴시험, 파면의 벽개 여부, 결정립 크기·분포, 노치반경과 구속도 변화. 학생 재료가 상온에서 딤플 파괴만 보인다면 RKR를 주 모델로 채택할 근거가 부족하다.

### 3.3 Beremin/Weibull stress

**핵심:** 국소 응력장과 취약영역의 체적 효과를 Weibull 통계로 묶어 벽개파괴 확률을 예측한다. 단일 최대응력 대신 높은 응력을 받는 영역의 크기와 확률적 산포를 반영한다.

**대표 문헌:** F. M. Beremin 등(1983), “A local criterion for cleavage fracture of a nuclear pressure vessel steel”, *Metallurgical Transactions A* **14, 2277–2287**, DOI **10.1007/BF02663302**. [출판사 서지·초록](https://link.springer.com/article/10.1007/BF02663302): A508 class 3 강, 여러 노치 시편, 소성변형 효과 및 Weibull 파괴확률 확인. 유료 원문 전체는 확인 불가.

**결합 가능성: 낮음.** 원래 구조는 체적을 통한 통계적 집계이므로 국소 미분 조건과 직접 대응하지 않는다. 구배가 다른 응력장은 간접적으로 체적 적분에 영향을 주지만 이것이 독립적인 응력구배 조건을 뜻하지 않는다. 별도 구배 인자를 추가하면 통계 모수와 길이의 식별 문제가 늘어난다는 것이 본 검토의 판단이다. 특히 Weibull stress만으로 공동 성장형 연성파괴를 설명했다고 주장해서는 안 된다.

**필요 데이터:** 동일 조건의 반복 파괴시험과 산포, 시편 체적·두께·노치형상, 온도별 경화곡선, FE 국소응력장, 파면 분석. 평균 파괴하중 몇 개만으로 확률모델의 신뢰성을 검증하기 어렵다.

### 3.4 GTN 손상모델

**핵심:** 공동 체적분율이 항복·소성유동과 결합하고 공동의 핵생성·성장·합체를 통해 내하력이 감소하는 연성파괴를 모델링한다. 탄성 균열 특이장에 파괴에너지를 대입하는 대신 재료 내부 손상의 진화를 계산한다.

**대표 문헌:** V. Tvergaard, A. Needleman(1984), “Analysis of the cup-cone fracture in a round tensile bar”, *Acta Metallurgica* **32(1), 157–169**, DOI **10.1016/0001-6160(84)90213-X**. [출판사 초록](https://www.sciencedirect.com/science/article/pii/000161608490213X): 탄소성 구성식, 공동 핵생성·성장·합체, 원형 인장봉의 cup–cone 파괴 계산 확인. 원류 자료로 A. L. Gurson의 “Continuum Theory of Ductile Rupture by Void Nucleation and Growth. Part I. Yield Criteria and Flow Rules for Porous Ductile Media”는 [Brown University 기술보고서 No.39, 1975, 원자료](https://digital.library.unt.edu/ark:/67531/metadc1448204/m1/1/)도 확인했다. 1975 보고서와 1977년 저널 출판을 혼동하지 않는다.

**결합 가능성: 중간(검증·손상 결합), 직접 치환은 낮음.** 손상 FE로 얻은 응력과 구배를 Kwon형 개시조건과 비교할 수 있다. 다만 GTN의 손상진화와 추가 구배조건이 각각 무엇을 결정하는지 정해야 한다. 같은 파괴하중에 둘을 중복 보정한 뒤 예측력이 향상됐다고 평가하는 것은 유효한 독립 검증이 아니다. 연화·국소화 문제에서는 메시와 물리적 길이의 구별도 검증 과제이다.

**필요 데이터:** 평활·여러 반경의 노치 인장시험, 하중–변위와 단면수축, SEM 파면·개재물/공동 관찰, 초기 공동분율 및 핵생성·합체에 대한 자료, 균열성장 시험. 전단 파괴가 중요하면 전단시험도 필요하며 기본 공동성장 모델의 적용 범위를 별도로 검토한다. 미세조직 모수 없이 하나의 인장곡선만으로 모든 모수를 유일하게 정했다고 볼 수 없다.

### 3.5 Johnson–Cook 파손모델

**핵심:** 응력삼축도·변형률속도·온도에 따른 파단변형률과 누적 소성변형을 이용해 파손을 판정하는 경험적 모델이다. 유동응력용 Johnson–Cook 구성식과 파손모델은 구별해야 한다.

**대표 문헌:** G. R. Johnson, W. H. Cook(1985), “Fracture characteristics of three metals subjected to various strains, strain rates, temperatures and pressures”, *Engineering Fracture Mechanics* **21(1), 31–48**, DOI **10.1016/0013-7944(85)90052-9**. [출판사 초록](https://www.sciencedirect.com/science/article/pii/0013794485900529): OFHC 구리·Armco 철·4340강, 노치 인장·비틀림·Hopkinson 시험 및 누적손상 모델 확인. 원문 전체 수식·모수표 재현은 확인 불가.

**결합 가능성: 낮음.** 파단변형률과 하중 이력이 중심이며 명시적 공간 응력구배는 기본 입력이 아니다. 구배를 추가한다면 새로운 모수와 독립 데이터가 필요하다. 정적 파괴 연구라면 속도·온도 의존성을 모두 보정하는 작업보다 응력상태와 공간효과를 분리하는 편이 목적에 맞는다는 판단이다.

**필요 데이터:** 여러 노치반경의 인장 및 전단/비틀림 파단변형률, FE 삼축도 이력, 온도·속도 효과까지 주장할 경우 해당 범위의 시험. 기본 모델로 다양한 전단·인장 상태를 예측할 때의 한계는 별도 시험으로 확인해야 한다.

### 3.6 Essential Work of Fracture(EWF)

**핵심:** 얇은 연성 시편의 총 파괴일을 균열끝단 과정영역의 essential work와 외부 소성영역의 일로 나누어 해석한다. 여러 리가먼트 길이의 시험 결과를 외삽하여 주어진 두께에서의 essential work를 구한다.

**대표 문헌:** B. Cotterell, J. K. Reddel(1977), “The essential work of plane stress ductile fracture”, *International Journal of Fracture* **13, 267–277**, DOI **10.1007/BF00040143**. [출판사 초록·서지](https://link.springer.com/article/10.1007/BF00040143): 두께에 대한 조건과 리가먼트 길이 외삽 확인. 원문 전체 확인 불가.

**결합 가능성: 낮음(국소 구배식), 에너지 검증에는 중간.** EWF는 전역적인 일 분리·측정 접근으로 자체적인 응력구배 법칙을 주지 않는다. EWF의 면적당 일과 Kwon의 w_f가 단위가 같다는 이유로 같은 재료상수라고 놓을 수 없다. 과정영역 정의와 바깥 소성일의 중복 여부를 먼저 확인해야 한다.

**필요 데이터:** 동일 두께에서 리가먼트 길이를 달리한 깊은 양측 노치 인장 시편, 완전 분리까지의 하중–변위, 정확한 리가먼트·두께, 반복시험, 소성영역과 균열개시 관찰. 리가먼트 소성화와 변형형태의 상사성, 길이별 외삽의 안정성을 확인해야 하므로 임의 형상의 단일 파괴시험을 EWF라고 부르면 안 된다.

### 3.7 Theory of Critical Distances(TCD) — 우선 검토 대상

**핵심:** 균열/노치 끝단의 한 점 최대응력 대신 특성거리에서의 응력(Point Method)이나 유한 구간 평균응력(Line Method)으로 파괴를 판정한다. 유한한 거리 또는 평균 구간을 사용해 탄성 특이점의 무한응력만으로 파괴가 결정되는 문제를 피한다.

**대표 문헌 및 실재 확인:**

- D. Taylor(2008), “The theory of critical distances”, *Engineering Fracture Mechanics* **75(7), 1696–1705**, DOI **10.1016/j.engfracmech.2007.04.007**. [출판사 초록](https://www.sciencedirect.com/science/article/pii/S0013794407002172): 프레임워크의 명칭·범위 확인. DOI에 2007이 있어도 권호 출판연도는 2008이다.
- D. Taylor(2005), “The Theory of Critical Distances Applied to the Prediction of Brittle Fracture in Metallic Materials”, *Structural Durability & Health Monitoring* **1(2), 145–154**, DOI **10.3970/sdhm.2005.001.145**. [출판사 초록](https://www.techscience.com/sdhm/v1n2/34948): PM/LM, 불안정 파괴 개시, 미시기구가 cleavage 또는 ductile tearing인 사례를 명시한다. 제목의 brittle과 미시적 ductile tearing을 동일한 분류축으로 혼동하지 않는다.
- L. Susmel, D. Taylor(2008), “On the use of the Theory of Critical Distances to predict static failures in ductile metallic materials containing different geometrical features”, *Engineering Fracture Mechanics* **75(15), 4410–4421**, DOI **10.1016/j.engfracmech.2008.04.018**. [출판사 초록·Discussion/Conclusions 발췌](https://www.sciencedirect.com/science/article/abs/pii/S0013794408001082), [저자 소속 대학 저장소](https://sfera.unife.it/handle/11392/531386).

**연성 적용을 어디까지 확인했는가:** 마지막 논문은 냉간압연 저탄소강의 노치 시편을 인장·3점굽힘으로 시험한다. 큰 소성영역 및 연성 균열전파 기구를 동반하는 정적 파괴하중을 탄성 TCD와 탄소성 해석으로 예측한 사례가 확인된다. 저자는 탄성 해석 예측 오차 약 15%를 보고하지만 원자료로 독립 재계산하지는 못했다. **안정적으로 성장하는 균열의 전 과정, Δa별 저항곡선, 이동 균열끝단의 길이 진화법칙까지 TCD로 검증한 사례인지는 공개 발췌로 확인 불가**이다. 따라서 “연성 전파를 동반한 파괴 사례가 없다”도 틀리고, “TCD가 연성 성장균열 문제를 이미 일반적으로 해결했다”도 근거가 부족하다.

**결합 가능성: 높음(공간 응력분포와 길이), 동일 이론은 아님.** 본 검토의 수학적 비교로, 매끄러운 응력장에서는 \(\sigma(s+L)=\sigma(s)+L\sigma'(s)+O(L^2)\)이므로 유한거리 응력은 구배와 연결된다. 그러나 특이점 r=0에서는 이 Taylor 전개를 쓸 수 없고, TCD의 재료길이 L과 \(\ell_g=\sigma/g\)도 자동으로 같지 않다. 따라서 동일 시편에서 TCD와 Kwon형 조건을 나란히 검증하는 것이 “이미 등가”라고 선언하는 것보다 근거가 명확하다.

**필요 데이터:** 평활 인장곡선, 여러 노치반경·리가먼트·두께에서의 개시/최대하중, 파면과 균열개시 위치, DIC, 가능하면 파괴인성. 재료길이와 임계응력을 함께 보정한 시편은 검증 세트에서 분리한다. 성장까지 주장하려면 Δa–하중–변위 및 J–R를 추가해야 한다.

### 3.8 Cohesive Zone Model(CZM)

**핵심:** 균열면의 traction–separation 법칙으로 분리를 표현하고, 주변 금속은 탄소성체로 해석한다. 계면의 최대 견인력과 분리일, 주변 소성변형의 조합으로 균열 개시와 성장 저항을 계산한다.

**대표 문헌:** V. Tvergaard, J. W. Hutchinson(1992), “The relation between crack growth resistance and fracture process parameters in elastic-plastic solids”, *Journal of the Mechanics and Physics of Solids* **40(6), 1377–1397**, DOI **10.1016/0022-5096(92)90020-3**. [저자 대학 원문 PDF](https://groups.seas.harvard.edu/hutchinson/papers/TvergaardHutch1992.pdf): 탄소성체에서 개시 및 후속 성장 저항, 최대 견인력·분리일을 이용하는 모델 확인.

**결합 가능성: 중간.** 응력기준을 cohesive 손상 개시와 대응시키고 구배/길이의 역할을 과정영역과 비교할 여지는 있다. 그러나 기존 CZM이 응력구배를 독립 파괴조건으로 요구하는 것은 아니다. Kwon형 기준의 연성 성장 확장안을 검증할 기준 모델로 특히 적합하다. 분리일과 전체 J–R에 포함된 주변 소성일을 동일시하면 에너지를 중복 계산할 수 있다.

**필요 데이터:** 진응력–진소성변형률, 하중–CMOD/CTOD, 균열길이 이력·J–R, 시편 두께와 구속도, 개시 위치. 견인력 최대값과 분리일을 한 개의 최고하중만으로 동시에 식별하지 말고 곡선·균열성장 데이터를 함께 사용한다. 균열경로를 미리 지정할 경우 경로예측 능력과 성장저항 예측 능력도 구분한다.

### 3.9 추가 발견: Equivalent Material Concept(EMC)

**핵심:** 연성 재료의 변형에너지밀도와 등가인 가상의 취성재료를 정의하여 취성 노치 파괴기준을 적용한다. 원래 탄성 기준의 형식을 상당 부분 보존하려는 방법이라는 점에서 이번 문제와 직접 관련된다.

**대표 문헌:** A. R. Torabi(2012), “Estimation of tensile load-bearing capacity of ductile metallic materials weakened by a V-notch: The equivalent material concept”, *Materials Science and Engineering: A* **536, 249–255**, DOI **10.1016/j.msea.2012.01.007**. [출판사 초록·본문 발췌](https://www.sciencedirect.com/science/article/pii/S092150931200010X): 동일 E의 가상 취성재료, 에너지밀도 등가, 인성 동일 가정, 평균응력 기준과의 결합 및 연성강 노치 하중 비교 확인.

**결합 가능성: 중간.** 가상 강도와 탄성장을 사용하여 기존 형태를 보존할 수 있지만 이것이 실제 탄소성 응력구배를 재현한다는 보장은 없다. 특히 가상/실제 재료 인성의 동일성은 가정이며 일반적인 연성 금속의 대규모 항복과 성장곡선에 자동 적용할 수 없다. Kwon 기준과 결합된 선행 검증은 이번 조사에서 확인 불가이다.

**필요 데이터:** 인장 파단까지의 에너지 평가에 충분한 곡선, E, 유효한 인성 자료, 여러 V/U 노치 파괴하중, 소성변형 범위. 보정에 쓰지 않은 노치·두께·하중형태로 이전성을 확인한다.

## 4. 비교표와 검증 설계상의 쟁점

| 방법 | Kwon형 구조와 결합 | 직접 입증된 주요 역할 | 이번 연구에서의 용도 |
|---|---|---|---|
| J/HRR | 높음 | 탄소성 정지 균열의 장 기술 | 지표의 이론적 재유도 |
| RKR | 중간 | 탄소성장과 거리에 의한 벽개파괴 | 길이 개념 비교, 벽개 경쟁 시 사용 |
| Beremin | 낮음 | 벽개확률·산포·체적효과 | 확률적 벽개가 연구 대상일 때 |
| GTN | 중간 | 공동 진화에 의한 연성파괴 | 손상 기구 검증과 수치 비교 |
| Johnson–Cook | 낮음 | 하중이력에 따른 경험적 누적파손 | 속도·온도 데이터가 충분할 때 |
| EWF | 낮음 | 얇은 시편의 파괴일 분리 | 에너지 측정의 보조 경로 |
| TCD | 높음 | 거리/평균응력 기반 노치 파괴하중 | 기존 기준과 직접 비교 |
| CZM | 중간 | 탄소성 균열 개시·성장 저항 | 성장 단계의 기준 모델 |
| EMC | 중간 | 등가 취성재료로 연성 노치 내하력 평가 | 형식 보존형 대안 |

위 등급은 문헌의 성능 순위가 아니라 §2의 목적별 평가이다. 표의 검증 범위는 각 절의 출처를 따른다.

### 명시적 응력구배 선행연구에 대한 답

직접 확인된 명시적 “응력 + 응력구배”의 연성 금속 적용은 **Kwon 등(2024)의 알루미늄 사례 자체**이다. TCD/RKR는 응력의 공간적 유지 범위·길이를 고려하는 관련 선행이지만 동일한 미분 결합조건은 아니다. 이번 검색 범위에서는 Kwon과 독립적인 저자군이 **동일한 미분조건으로 안정 연성 균열 성장 전 과정을 검증한 논문**은 확인 불가였다. 이는 부재의 증명이 아니다. strain-gradient plasticity나 gradient damage라는 명칭만으로 stress-gradient 파괴기준의 선행이라고 세지 않았다.

### 현재 데이터로 구별해야 할 것

1. **최대하중, 균열개시, 최종분리, 안정성장**을 별도 관측량으로 정의한다. 한 시점의 적합으로 나머지를 입증할 수 없다.
2. 응력구배 조건이 늘 자동 만족되는 데이터만 있으면 구배 임계값의 예측력을 식별하기 어렵다. 서로 다른 공간 응력분포를 갖는 노치반경·하중형태를 포함하고, 두 조건 중 무엇이 지배하는지 하중 증가에 따라 기록한다.
3. 실제 3D 탄소성장의 삼축도·경화·구속도 효과를 하나의 응력스칼라와 1차 구배만으로 충분히 나타내는지는 실험 과제이다. 보정과 검증 시편을 분리하고 다른 두께·a/W로 이전성을 확인한다.
4. FE의 미분은 메시·응력 외삽·경로에 민감할 수 있다. s의 방향, 현재/기준 좌표계, 평가거리, 응력 추출법을 고정하고 수렴성 검증을 수행해야 한다. 특이점의 첫 요소 값만을 재료상수로 해석하지 않는다.

이 항목들은 문헌에서 확보한 방법들을 학생 데이터에 적용하기 위한 **검증 설계 제안**이다. 실제 자료가 없으므로 어느 모델의 오차가 더 작을지는 현재 판단할 수 없다.

## 5. 실행 기록

- 시작 시 `git pull` 실행: `error: cannot open '.git/FETCH_HEAD': Permission denied`로 실패. 최신 원격 상태를 가져왔다고 주장할 수 없다.
- 작업 시작 시 `git status --short`에서 기존 `round1/codex.md` 수정이 보였다. 해당 파일의 내용은 읽거나 수정하지 않았다.
- 검색한 주요 구문: `Kwon Materials 2024 17 569 fracture stress gradient`, `Ritchie Knott Rice 1973`, `Taylor theory critical distances ductile crack growth`, `Susmel Taylor static failures ductile metallic geometrical 2008 critical distances`, `stress gradient ductile fracture criterion`, 각 후보의 원 논문 제목.
- 웹 접근 자체는 성공했으나 일부 DOI/출판사 열기는 오류를 반환했다. 재검색 또는 저자 공개본으로 확인 가능한 부분만 사용했다. “초록 확인”은 전체 본문·원자료 검증을 의미하지 않는다.
- `git diff --check -- round3/codex.md`: 공백 오류 없음. LF→CRLF 변환 예고만 출력.
- `git add round3/codex.md` 및 `git commit -m "round3: Codex blind verification"`: 모두 `.git/index.lock` 생성 권한 거부로 실패. 이번 결과의 스테이징·커밋은 생성되지 않았다.
- `git push origin main`: GitHub 443 포트 연결 실패로 종료. 푸시는 완료되지 않았다. 웹 검색 도구의 인터넷 접근과 셸 Git의 네트워크 접근은 별개였다.
- 현재 환경은 `.git` 쓰기 제한과 셸 네트워크 제한이 있고 권한 상승도 허용되지 않아 우회하지 않았다. 결과 파일은 작업 폴더에 저장했다.

## 6. 지도교수 면담 전 학생이 검토할 후보 3개

**1. TCD와 탄소성 Kwon형 기준의 비교·확장.** 원래 관심인 응력의 공간분포와 길이에 가장 직접적으로 연결되며, Susmel–Taylor(2008)의 연성강 노치 사례가 실제 존재한다. 보유 데이터가 노치별 파괴하중과 인장곡선이라면 우선 비교할 후보이다. Kwon 등의 기존 연성 적용과 무엇이 다른지, 구배 조건이 실제 지배하는 데이터를 확보할 수 있는지가 연구 질문이어야 한다. [Susmel & Taylor, 2008, *EFM* 75, 4410–4421](https://www.sciencedirect.com/science/article/abs/pii/S0013794408001082)

**2. J/HRR 기반의 에너지–구배 지표 재유도.** §2의 독립 계산에서 단순 치환의 평가거리 문제가 명확하게 드러난다. 따라서 이론적 확장을 원한다면 에너지 정의와 길이의 역할을 다시 유도하는 근거가 있다. 예비균열 시편의 개시 데이터와 경화곡선으로 시작하고, J 지배성 확인 후 성장 문제로 범위를 넓히는 방안을 검토한다. [Rice & Rosengren, 1968, *JMPS* 16, 1–12](https://www.sciencedirect.com/science/article/pii/0022509668900136)

**3. 탄소성 CZM을 기준으로 한 균열 성장 검증.** 목표가 실제 ductile growing crack이라면 개시뿐 아니라 성장 저항까지 다룬 원문이 있고, 강도·분리일·주변 소성일을 구분할 수 있다는 근거가 있다. J–R·CMOD·Δa 이력이 있을 때 우선 검토하며, Kwon형 조건은 우선 개시 예측에 사용하고 성장에 필요한 별도 법칙을 명확히 한다. [Tvergaard & Hutchinson, 1992, *JMPS* 40, 1377–1397](https://groups.seas.harvard.edu/hutchinson/papers/TvergaardHutch1992.pdf)

세 후보의 최종 선택은 아직 할 수 없다. 면담에는 재료·두께·파면 기구·시험 형상·인장곡선·균열길이 이력의 실제 보유 여부를 정리해 가져가야 한다. 미세공동 자료가 풍부하면 GTN의 우선순위가 높아지고, 얇은 판의 여러 리가먼트 시험만 있으면 EWF를 보조 축으로 삼을 수 있다. 이는 데이터 조건에 따른 후보 조정이며 공동 최종 결론이 아니다.
