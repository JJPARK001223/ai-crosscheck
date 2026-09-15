# Round1: Codex 연구계획서 독립 사실검증

검증일: 2026-09-15. 대상: `PROBLEM.md`의 ‘검증해야 할 항목 목록’ 11개.

## 검증 범위와 독립성

- 저장소의 조사 입력은 지정된 `PROBLEM.md`만 읽었다. `round1/claude.md`와 다른 검증 결과는 열지 않았다. 원본 연구계획서 PDF도 열지 않았으므로, 아래 판정은 PROBLEM.md에 옮겨진 텍스트 기준이다.
- **Blind 제한:** PROBLEM.md의 ‘주의’ 문장에 9번 항목에 관한 다른 검증자의 결론이 이미 포함되어 있었다. 따라서 9번에 대해 사전 결론을 전혀 보지 않은 완전한 blind 검증이었다고 주장할 수 없다. 해당 결론을 증거로 사용하지 않고, 아래에 명시한 논문 본문을 직접 대조했다.
- 웹 검색과 원문 텍스트 열람은 가능했다. PMC HTML 직접 접속은 브라우저 확인 화면에 막혔다. PMC 검색 색인에 노출된 원문, 동일 논문의 PDF 추출 본문, 출판사가 제공한 ResearchGate 원문을 대조했다. **PDF 페이지 이미지 조회는 실패했고 연결 가능한 브라우저도 없었다.** 그래프의 점 좌표를 눈으로 확인하거나 숫자로 복원했다고 주장하지 않는다.
- 문헌에 적혀 있다는 사실과 그 주장을 독립 실험·해석으로 입증했다는 것은 구분한다. 이번 작업에서는 FEA를 실행하거나 실험을 재현하지 않았다. 확인하지 못한 부분은 ‘확인 불가’로 표시했다.

## 1. 참고문헌 [1]~[6] 서지사항

**판정: 불일치 — [5] 저자 표기, [6] 보고서 번호와 연도·출판형태의 조합을 정정해야 한다. [1]~[4]의 아래 기본 서지사항은 일치한다.**

| 번호 | 대조한 서지사항 / 권장 표기 | 판정 및 근거 |
|---|---|---|
| [1] | Kwon, Y. W. (2021). Revisiting Failure of Brittle Materials. *Journal of Pressure Vessel Technology*, **143(6)**, **064503**. DOI: **10.1115/1.4050989**. | **일치.** [저자 공개 원문](https://www.researchgate.net/publication/351141697_Revisiting_Failure_of_Brittle_Materials)의 첫 페이지와 머리말·꼬리말, DOI 대조. 064503은 논문번호이다. |
| [2] | Kwon, Y. W., Markoff, E. K., & DeFisher, S. (2024). Unified Failure Criterion Based on Stress and Stress Gradient Conditions. *Materials*, **17(3)**, **569**. DOI: **10.3390/ma17030569**. | **일치.** [PMC 서지 및 원문](https://pmc.ncbi.nlm.nih.gov/articles/PMC10856633/). 569는 논문번호이다. |
| [3] | Karihaloo, B. L., Abdalla, H. M., & Xiao, Q. Z. (2003). Size effect in concrete beams. *Engineering Fracture Mechanics*, **70(7-8)**, **979-993**. DOI: **10.1016/S0013-7944(02)00161-3**. | **일치.** [Elsevier 출판사 서지·초록](https://www.sciencedirect.com/science/article/abs/pii/S0013794402001613). 전체 실험 원문을 확보한 것은 아니다. |
| [4] | Hutchinson, J. W. (1968). Singular behaviour at the end of a tensile crack in a hardening material. *Journal of the Mechanics and Physics of Solids*, **16(1)**, **13-31**. DOI: **10.1016/0022-5096(68)90014-8**. | **일치.** [Elsevier 출판사 서지·초록](https://www.sciencedirect.com/science/article/pii/0022509668900148). |
| [5] | Rice, J. R., & **Rosengren, G. F.** (1968). Plane strain deformation near a crack tip in a power-law hardening material. *Journal of the Mechanics and Physics of Solids*, **16(1)**, **1-12**. DOI: **10.1016/0022-5096(68)90013-6**. | **불일치: GF0166 → G. F.** [Elsevier 출판사 저자·서지](https://www.sciencedirect.com/science/article/pii/0022509668900136). 나머지 저널·권호·쪽·연도는 일치. |
| [6] | Rice, J. R. (1968). A Path Independent Integral and the Approximate Analysis of Strain Concentration by Notches and Cracks. *Journal of Applied Mechanics*, **35(2)**, **379-386**. DOI: **10.1115/1.3601206**. | **불일치: 학술지판을 인용한다면 이 표기로 교체.** [저자 소장 학술지 원문](https://esag.harvard.edu/rice/015_Rice_PathIndepInt_JAM68.pdf), [저자 논문목록 15번](https://esag.harvard.edu/rice/RicePubs.html), [INL 공식 문서의 권호·DOI](https://malamute.inl.gov/modules/solid_mechanics/FractureIntegrals.html). |

**[6]의 보고서 자체는 실재한다.** [Brown University 보고서 표지](https://esag.harvard.edu/rice/015B_Rice_PathIndepInt_BrownUnivRept67.pdf)에 **ARPA SD-86, Report E39, May 1967**이 표시되어 있다. 따라서 보고서를 인용하려면 기관·보고서번호와 함께 **1967년**으로 적어야 한다. ‘기술보고서는 없고 학술지 논문만 있다’고 정정하면 오히려 틀린다. 저자 논문목록도 1968년 학술지판과 그 바탕이 된 1967년 보고서를 구분한다.

`GF0166`가 실제 저자명과 다르다는 것은 확인했지만, 그 문자열이 생긴 원인이 OCR인지 문헌관리 프로그램인지까지는 **확인 불가**이다. 참고문헌에 DOI가 빠져 있다는 사실 자체를 잘못된 인용으로 판정하지는 않으며, 위 DOI는 식별을 위해 보완했다.

## 2. 식 (4)의 형태와 통합기준으로서의 완결성

**판정: 일치 — 원문 식의 전사 기준. 단독 파괴조건으로 제시하면 불완전하다.**

Kwon 등(2024), §2의 식 (2)는 다음과 같다. [원문 PDF, p.2](https://pdfs.semanticscholar.org/1bfc/fa7f59c018aba971ca6433b1f81c184c300a.pdf#page=2)

\[
\sigma_e\geq\left(2EY\frac{d\sigma_e}{ds}\right)^{1/3}.
\]

지수·계수·변수는 일치한다. 원문 식 (1)의 \(\sigma_e\geq\sigma_f\)도 동시에 만족해야 한다.

**정정 제안:** 식 (4)의 이름을 ‘응력구배 조건’으로 쓰고, 응력 조건을 함께 제시한다.

### 부호 문제: 직접 미분에 의한 검토

기울기를 부호 있는 도함수로 구현하면 문제가 생긴다. 균열에서 바깥쪽으로 증가하는 좌표에 대해 \(\sigma_e=A/\sqrt{s}\), \(A>0\)라 놓으면

\[
\frac{d\sigma_e}{ds}=-\frac{A}{2s^{3/2}}<0.
\]

\(E,Y>0\)일 때 우변의 실수 세제곱근은 음수가 되어, 양의 인장응력은 이 부등식을 자동으로 만족한다. 이는 유효한 응력구배 제한이 되지 못한다. **이 결과는 식을 직접 미분한 검증이며, 저자의 의도를 추측한 것이 아니다.**

Kwon(2021), p.1 식 (2)-(3)은 응력구배의 **절댓값**을 명시한다. [저자 원문](https://www.researchgate.net/publication/351141697_Revisiting_Failure_of_Brittle_Materials)

따라서 재현 구현에서는 \(g=|d\sigma_e/ds|\)를 별도로 정의해 \(\sigma_e\geq(2EYg)^{1/3}\)로 사용하는지, 다른 양의 구배 정의를 사용하는지 명시해야 한다. 이를 2024년 인쇄식 그대로라고 표시해서는 안 된다. 해당 논문의 실제 계산 코드에서 부호를 어떻게 처리했는지는 **확인 불가**이다.

## 3. 유효응력 정의

**판정: 일치.** 등방 취성·준취성의 최대수직응력, 등방 연성의 최대전단응력 또는 팔면체전단응력이라는 구분은 §2와 같다. [Kwon 등, *Materials*, 2024, §2](https://pmc.ncbi.nlm.nih.gov/articles/PMC10856633/)

정정은 필수적이지 않다. 다만 실제 구현에서는 선택한 유효응력과 강도·재료상수의 정의를 통일해야 한다. 이 정의 문장만으로 특정 연성파괴 모델의 보편적 타당성이 증명되는 것은 아니다.

## 4. 검증 재료·시편 목록

**판정: 일치 — ‘초기 균열 없음’이라는 의미에서.** HCP는 균열 시편(§4), PLA와 적층 유리섬유 복합재는 **원공 시편**(§5-6)이다. [Kwon 등, *Materials*, 2024, §4-6](https://pmc.ncbi.nlm.nih.gov/articles/PMC10856633/)

**정정 제안:** ‘균열이 없는’을 ‘초기 균열 대신 원공을 가진’으로 바꾸면 무결함 시편으로 오해할 여지가 줄어든다. ‘3D프린팅’이 유리섬유 복합재의 제작법까지 수식하지 않도록 문장을 구분한다.

## 5. 5000계열 알루미늄 시편 제원

**판정: 불일치 — 슬릿 길이.**

원공 지름 **1-18 mm**는 일치한다. 슬릿은 **4 mm 또는 6 mm**이며, **6 mm**에 폭 방향 기준 **0°·15°·30°·45°**를 적용했다. **4.6 mm가 아니다.** [Kwon 등, *Materials*, 2024, §3.1, p.3](https://pdfs.semanticscholar.org/1bfc/fa7f59c018aba971ca6433b1f81c184c300a.pdf#page=3)

**정정 제안:** 길이와 각도의 적용 대상을 위와 같이 분리한다. 원본 PDF를 보지 않았으므로 `4.6`이 원본 오기인지 PROBLEM.md 전사 오류인지는 **확인 불가**이다.

## 6. 공칭파괴응력 220-230 MPa

**판정: 불일치 — 보고값 전체의 범위로는 부정확하다.**

Table 1의 원공별 평균값은 다음과 같다. [Kwon 등, *Materials*, 2024, Table 1, p.5](https://pdfs.semanticscholar.org/1bfc/fa7f59c018aba971ca6433b1f81c184c300a.pdf#page=5)

| 지름(mm) | 0 | 1 | 2 | 3 | 6 | 9 | 12 | 15 | 18 |
|---|---|---|---|---|---|---|---|---|---|
| 평균(MPa) | 228 | 237 | 236 | 228 | 236 | 219 | 227 | 228 | 230 |

최솟값·최댓값을 직접 비교하면 **219-237 MPa**이다. **‘약 230 MPa 수준(원공별 평균 219-237 MPa)’**으로 정정한다. 이는 평균들의 범위이며 개별 시험값 전체의 범위나 신뢰구간이 아니다.

최소단면 기준이라는 설명과 거의 일정하다는 경향은 §3.2와 일치한다. 슬릿의 정확한 수치는 Figure 7을 판독하지 못해 **확인 불가**이다. 원공 표의 범위를 슬릿의 확인된 범위처럼 옮겨 쓰지 않는다.

## 7. 탄소성·탄성 응력구배 비교 방향

**판정: 일치.** §3.2는 연성 알루미늄의 구배가 취성재료 탄성해석보다 **최소 한 자릿수 작다**고 서술한다. 응력 조건 지배라는 해석도 일치한다. [Kwon 등, *Materials*, 2024, §3.2, p.5](https://pdfs.semanticscholar.org/1bfc/fa7f59c018aba971ca6433b1f81c184c300a.pdf#page=5)

‘최소 한 자릿수’는 대략 10배 이상 작다는 뜻이다. 이번 검증으로 확인한 것은 **논문의 비교 방향과 서술**이다. 실제 구배 수치쌍이나 FEA 결과를 직접 확보해 10배를 재계산한 것은 아니므로, 그 정량 재현은 **확인 불가**이다. 모든 연성 금속에 동일하게 적용되는 배율로 일반화해서는 안 된다.

## 8. HCP 3점굽힘 제원과 조건 조합

**판정: 확인 불가 — 일부 제원은 일치하지만, 요청한 전체 조합을 모두 확인하지 못했다.**

§4.1의 **W=100 mm, L/H=4, E=20.8 GPa**는 일치한다. Figure 11 추출 범례에는 **H=0.05 m·0.1 m**가 있다. [Kwon 등, *Materials*, 2024, §4.1 및 Figure 11, pp.6-8](https://pdfs.semanticscholar.org/1bfc/fa7f59c018aba971ca6433b1f81c184c300a.pdf#page=6)

확인 제한은 다음과 같다.

- **a/H=0.1·0.3·0.5와 두 깊이의 전체 조합: 확인 불가.** Figure 11의 축 눈금·범례 추출만으로 모든 데이터 점이 각 조합에 실제 존재한다고 단정하지 않았다. 아래 9번에서 본문으로 확인한 두 조건만 별도로 확정한다.
- 원문은 **L을 length**로 설명한다. 이를 계획서처럼 ‘지지점 사이 스팬’으로 정확히 동일시할 수 있는지는 도면을 판독하지 못해 **확인 불가**이다. 재현 모델에서는 전체 길이와 지지점 간격을 별도 기호로 구분해야 한다.
- **Karihaloo 등(2003)의 전체 원자료와의 직접 일치: 확인 불가.** 해당 출판사 서지·초록은 확인했지만 실험 표·도면 전체는 확보하지 못했다. Kwon 등(2024)의 재인용 내용을 2003년 원자료까지 확인한 것으로 표현하지 않는다.

**정정 제안:** 확인된 제원을 우선 사용하되, 전체 조합과 스팬의 정의는 Figure 8·11 및 2003년 실험 표·도면을 확보한 뒤 확정한다.

## 9. 보정 조건 및 불일치 조건

**판정: 불일치 — 보정 조건은 맞고, 불일치 조건은 틀리다.**

- 보정: **a/H=0.1, H=100 mm**.
- 불일치: **a/H=0.3, H=100 mm**.
- 원문은 추가 정보 부족으로 차이의 원인을 조사하지 못했다고 설명한다.

근거: [Kwon 등, *Materials*, 2024, §4.3의 Figure 11 설명, p.8](https://pdfs.semanticscholar.org/1bfc/fa7f59c018aba971ca6433b1f81c184c300a.pdf#page=8).

**정정 제안:** 연구내용의 불일치 조건에서 **0.1 → 0.3**으로 바꾼다. 그 원인이 모델·메시·경계조건 때문이라는 판단은 **확인 불가**이다. 이를 앞으로 점검할 후보로 제시하는 것은 가능하지만 이미 밝혀진 원인처럼 써서는 안 된다. 보정 데이터와의 정확한 일치는 독립 예측의 정확도 검증과 구분한다.

## 10. 식 (1)~(3)의 개념적 타당성

**판정: 불일치 — 식 (3). 식 (1)·(2)는 전제조건을 명시하면 타당하다.**

### 식 (1): 일치, 다만 응력 성분·방향과 근사 범위를 명시

Kwon(2021), Case 2의 식 (4)는 중앙균열 선단 앞 인장응력의 특이항을 \(K/\sqrt{2\pi r}\)로 쓴다. [저자 원문, p.2](https://www.researchgate.net/publication/351141697_Revisiting_Failure_of_Brittle_Materials)

이 식은 전체 응력텐서나 모든 각도에서의 응력장을 완전히 적은 것이 아니다. Mode I 균열 정면의 열림방향 응력 성분을 예로 들면

\[
\sigma_{nn}(r,0)\sim\frac{K_I}{\sqrt{2\pi r}}\qquad(r\to0)
\]

로 쓰는 것이 명확하다. 일반 각도에서는 각도함수가 필요하다. 근거: Rice, J. R. (1968), *Mathematical Analysis in the Mechanics of Fracture*, in *Fracture: An Advanced Treatise*, Vol.2, pp.191-311, 특히 [p.216 식 (78)](https://esag.harvard.edu/rice/018_Rice_MathAnalMechFract_68.pdf).

### 식 (2): 일치, 무한평판·단일 원공·원방 단축인장 조건

Kwon(2021), Case 3의 식 (9)와 그 직후 설명에서 원공 경계 최대 원주응력은 \(3\sigma_o\)이다. [원문, p.2](https://www.researchgate.net/publication/351141697_Revisiting_Failure_of_Brittle_Materials)

그 식에서 원공 반지름을 \(R\), 원공 중심 기준 반경을 \(r\)라 두고 \(r=R\)를 대입하면

\[
\sigma_{\theta\theta}(R,\theta)=\sigma_o(1-2\cos2\theta),\qquad
\max_\theta\sigma_{\theta\theta}=3\sigma_o.
\]

따라서 원방응력을 분모로 정의한 \(K_t=3\)이다. 유한 폭, 순단면 공칭응력 기준, 소성변형까지 이 숫자를 그대로 일반화할 수는 없다.

### 식 (3): 불일치, 차원 검산으로 확정

연구계획서 식 (3)은 \(\sigma_{\theta,\max}=3\sigma_oK/\sqrt{2\pi r}\)이다. 통상적인 응력확대계수 정의에서는

\[
[K]=[\text{응력}]\sqrt{[\text{길이}]},\quad
\left[\frac{K}{\sqrt{2\pi r}}\right]=[\text{응력}],\quad
\left[3\sigma_o\frac{K}{\sqrt{2\pi r}}\right]=[\text{응력}]^2.
\]

좌변은 응력이고 우변은 응력의 제곱이므로 성립하지 않는다. **삭제하고 균열 해와 원공 해를 별개의 식으로 제시한다.** 원공 가장자리에 추가 균열이 있는 별도 문제를 뜻한다면 그 형상과 해당 응력확대계수 해를 따로 정의해야 한다. 현재 텍스트에는 그런 정의가 없다.

### 재현 시 추가로 구분할 K의 정규화

Kwon 등(2024)의 §2는 \(\sigma_e=K/\sqrt{s}\)와 \(Y=K^2/E\)를 사용한다. [원문 식 (3)-(4), p.2](https://pdfs.semanticscholar.org/1bfc/fa7f59c018aba971ca6433b1f81c184c300a.pdf#page=2)

같은 물리적 응력장에 대해 표준 \(K_I/\sqrt{2\pi s}\)와 이 표현을 비교하면, 곡선맞춤 계수를 \(A\)로 구별할 때 **\(A=K_I/\sqrt{2\pi}\)**이다. 직접 대입하면

\[
Y=\frac{A^2}{E}=\frac{K_I^2}{2\pi E}.
\]

따라서 표준 3점굽힘 공식의 \(K_I\)와 곡선맞춤 계수 \(A\)를 구별하지 않으면 상수 환산에 \(2\pi\) 차이가 발생한다. 이 관계는 Kwon(2021)의 식 (6)과도 대조된다. 이는 두 표현을 직접 비교한 대수적 검토이며, 2024년 저자의 계산 코드가 실제로 어떤 정규화를 썼는지는 **확인 불가**이다.

### ‘슬릿에는 특이응력장이 없다’는 일반화

**확인 불가: 해당 알루미늄 슬릿 끝의 실제 반지름·단면 형상을 이번 자료에서 확정하지 못했다.** 이상적인 날카로운 균열과 유한 곡률반경의 매끈한 노치는 구분해야 한다. ‘슬릿’이라는 명칭만으로 비특이성을 보장할 수 없다. Rice(1968) 원문은 둥근 끝의 노치와 그 극한인 균열을 구분한다. [*Journal of Applied Mechanics*, 35, 379-386, Fig.1 및 본문](https://esag.harvard.edu/rice/015_Rice_PathIndepInt_JAM68.pdf)

정정 제안: ‘원공 및 끝단 형상을 확인한 슬릿 주변의 응력·응력구배를 산출한다’로 고치고, 실제 끝단 반지름과 메시 수렴 조건을 기재한다.

## 11. HRR장·J-적분의 저자와 연도

**판정: 일치.** HRR장에 **Hutchinson(1968), Rice & Rosengren(1968)**, J-적분의 학술지 논문에 **Rice(1968)**를 붙인 것은 해당 문헌과 부합한다.

- Hutchinson, J. W., *Journal of the Mechanics and Physics of Solids* **16(1)**, 13-31 (1968): [출판사 원문 서지·초록](https://www.sciencedirect.com/science/article/pii/0022509668900148).
- Rice, J. R., & Rosengren, G. F., 같은 저널 **16(1)**, 1-12 (1968): [출판사 원문 서지·초록](https://www.sciencedirect.com/science/article/pii/0022509668900136).
- Rice, J. R., *Journal of Applied Mechanics* **35(2)**, 379-386 (1968): [저자 소장 학술지 원문](https://esag.harvard.edu/rice/015_Rice_PathIndepInt_JAM68.pdf).

**정정 제안:** 본문의 세 연도는 유지하고, [5]의 이름과 [6]의 출판형태를 1번처럼 정정한다. E39 보고서를 선택해 인용한다면 그 보고서의 연도는 1967년으로 바꾼다.

적용 범위에 관해서는 주의가 필요하다. Rice(1968) 원문은 변형이론으로 다루는 탄소성체와 일반적인 증분 소성론을 구분한다. 이 고전 논문들의 인용만으로 임의의 하중 이력·언로딩·대규모 소성 조건에서 같은 경로독립성이나 균열끝장 지배가 자동 보장된다고 확장할 수 없다. 이번 판정은 저자·연도와 해당 고전 문헌의 대응에 대한 것이다.

## 작업 기록

- 시작 시 `git pull`을 실행했으나 `.git/FETCH_HEAD: Permission denied`로 실패했다. 따라서 원격 최신 상태와 동기화되었다고 주장하지 않는다.
- 저장 후 번호 1-11과 판정 11개를 확인했으며, 줄 끝 공백과 문자 대체 오류는 없었다.
- 요청한 파일만 `git add`했으나 `.git/index.lock: Permission denied`로 실패했다. 요청한 메시지 `Round1: Codex blind fact-check of 연구계획서`로 해당 파일만 커밋하는 명령도 실행했지만, 파일이 Git에 등록되지 않아 pathspec 오류로 실패했다. **파일 저장은 완료했으나 커밋·푸시는 완료하지 못했다.** 현재 환경의 `.git` 쓰기 제한을 우회하지 않았다.
- 이 파일은 독립 검증 기록이다. 다른 검증자의 결과와 합의하거나 최종 결론을 종합한 문서가 아니다.
