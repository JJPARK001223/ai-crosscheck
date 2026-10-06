# Round 21 Codex 블라인드 검증

## 검증 범위와 방법

- `round21/claude.md`와 SVG 코드는 열지 않았다.
- 지정된 세 원문과 동일한 논문 PDF 본문, 식, 그림 캡션을 대조했다.
- 판정 대상은 사용자가 지정한 다섯 가지 물리적 사실에 한정했다.

## 판정 요약

| 항목 | 판정 | 핵심 결론 |
|---|---|---|
| 1. Case 2 중앙균열 | **원문과 일치** (단, `θ=0`은 해석적 주석) | 식 (4)는 일반 각도장의 식이 아니라 균열 끝에서 **균열 연장선**을 따라 쓰인 1차원 근사이다. |
| 2. Case 3 원공/Kirsch | **불일치** (위치의 `좌·우` 표현) | `θ=π/2`는 하중축에 수직인 반경 방향이며 `σ_θ(R,π/2)=3σ_o`가 맞다. 그러나 원문의 그림 방향에서는 그 두 점은 좌·우가 아니라 위·아래이다. |
| 3. Case 4 FE 검증 | **원문과 일치** (2496개는 1/4 모델) | 40 mm × 100 mm, 반지름 4종, 4절점 사각형 요소, 1/4 대칭 모델, 2496요소가 맞다. |
| 4. HCP 3PB | **불일치** (`pre-crack`으로 부르면) | 2003년 원 실험은 중앙 edge **notch** 시험이다. 2024년 논문은 이를 `crack`으로 재서술한다. 역산점은 `H=100 mm, a/H=0.1`이며 나머지는 5조합이다. |
| 5. 조건① AND 조건② | **원문과 일치** | 원문은 약한 부정 표현만 쓴 것이 아니라 초록과 본문에서 두 조건이 모두 충족되어야 한다고 명시한다. |

## 1. Case 2: 중앙균열 무한평판과 Irwin 근사

### 판정: **원문과 일치** — 다만 `θ=0`은 원문의 기호가 아니라 표준 국소좌표로 번역한 해석

Kwon의 Case 2는 중앙균열 길이를 `2a`로 두고, 식 (4)을

\[
\sigma_x=\frac{K}{\sqrt{2\pi r}}
\]

로 쓴다. 이어서 다음을 명시한다.

1. `σ_x`는 균열 방향에 수직이고 하중방향과 평행한 응력성분이다.
2. 균열은 수직 `y`축을 따라 진행한다.
3. 따라서 응력구배도 `|dσ_x/dy|`로 계산한다(식 (5)).

즉 식 (4)의 `r`은 임의의 `(r,θ)` 위치에서 각도 의존항을 생략한 일반식이 아니다. 논문의 후속 미분이 `r=y`인 균열 연장선 위에서 이루어지므로, **균열 끝 전방의 연장선 값**으로 사용되었다고 보아야 한다. 일반 Mode-I 근접장에서는 응력성분에 `θ` 의존성이 존재하므로 식 (4)을 모든 각도에서 성립하는 식처럼 그리면 틀린다.

다만 원문 Case 2는 극각 `θ`를 정의하지 않는다. 따라서 그림의 “`θ=0 방향(σₓ 평가선)`”은 “국소 극각의 0방향을 균열 연장방향으로 잡는다”는 표준 LEFM 관례를 추가한 **정당한 해석적 주석**이지, 원문에 그대로 적힌 표현은 아니다. 가장 엄밀한 라벨은 다음과 같다.

> 균열 연장선 (`θ=0`으로 정의), `σ_x` 평가 및 구배 방향

**근거:** Kwon, *Journal of Pressure Vessel Technology*, 143(6), 064503 (2021), “Case 2”, 식 (4)–(5), 논문 인쇄쪽 064503-2; Irwin (1957), 원문 참고문헌 [1].

## 2. Case 3: 무한평판 원공의 Kirsch 해

### 판정: **불일치** — `θ=π/2`와 `3σ_o`는 맞지만 원문 좌표에서 “좌·우”는 틀림

원문의 식 (9)은

\[
\sigma_\theta=\frac{\sigma_o}{2}
\left[1+\frac{R^2}{r^2}-\left(1+3\frac{R^4}{r^4}\right)\cos 2\theta\right]
\]

이고, 본문은 최대값이 `θ=π/2`에서 생겨

\[
\sigma_\theta(R,\pi/2)=3\sigma_o
\]

라고 명시한다. 또 `θ=π/2`에서 반경방향은 “vertical direction”이라고 직접 쓴다. 같은 논문의 좌표·하중 배치에서 인장은 수평방향이므로, 이 위치는 **하중축에 수직인 원공 경계의 위·아래 두 점**이다. 따라서 물리적으로 “하중축에 수직인 방향”은 맞지만, 이를 동시에 “원공의 좌·우”라고 쓰면 원문의 그림 방향과 맞지 않는다. 하중 화살표를 수직으로 회전해 새로 그린 그림이라면 좌·우가 될 수 있으나, 그 경우 좌표계도 함께 회전했음을 분명히 해야 한다.

권장 위치 표기는 방향에 독립적인 다음 문구이다.

> 하중축에 수직인 원공 경계의 두 점 (`θ=π/2, 3π/2`)

`θ=0`의 부호도 원문의 식 (9)에서 직접 확인할 수 있다.

\[
\sigma_\theta(R,0)=\sigma_o(1-2)=-\sigma_o
\]

따라서 인장을 양(+)으로 두면 `θ=0`의 원주응력은 **압축**이다. 이 부호는 본문 문장으로 따로 설명되지는 않지만, 원문 식 (9)의 직접 대입 결과이므로 확인불가가 아니다. 원공 자유경계에서 `σ_r(R,θ)=τ_{rθ}(R,θ)=0`인 것과 혼동하면 안 된다.

**근거:** Kwon (2021), “Case 3”, Fig. 3, 식 (8)–(11), 특히 식 (9)와 `θ=π/2` 최대응력 설명, 논문 인쇄쪽 064503-2; Kirsch (1898), 원문 참고문헌 [2].

## 3. Case 4: 유한평판 원공 FE 검증

### 판정: **원문과 일치** — 단, 2496개는 1/4 모델 메시의 요소 수

원문의 Case 4 서술과 대응은 다음과 같다.

- 평판 폭 40 mm, 길이 100 mm: 일치.
- 중앙 원공 반지름 0.25, 0.5, 1.0, 2.0 mm: 일치(4종).
- 두 대칭성을 이용한 1/4 모델: 일치.
- 등매개 사각형 요소, 모서리에 4개 절점: 일치. 따라서 “4절점 사각형 요소”가 정확하다.
- 요소 수 2496개: 일치하나, 문장 주어가 Fig. 4의 **1/4 모델 mesh**이므로 2496은 1/4 모델의 요소 수이다. 전체 평판으로 환산한 실제 모델 요소 수를 뜻하지 않는다.

비교 실험은 Sapora, Torabi, Etesam, Cornetti의 2018년 논문 참고문헌 [3]에서 가져왔고, Kwon의 Fig. 6 본문은 **polymethyl-methacrylate (PMMA)**와 **general-purpose polystyrene (GPPS)** 두 재료의 서로 다른 원공 크기 데이터를 비교했다고 명시한다. Sapora et al. 원문도 실험부에서 PMMA와 GPPS notched samples를 다룬다.

따라서 “총 2496개”라는 라벨은 모호하다. 그림에는 **“1/4 FE 모델: 2496개 4절점 사각형 요소”**라고 쓰는 것이 안전하다.

**근거:** Kwon (2021), “Case 4”, Fig. 4–6, 논문 인쇄쪽 064503-2–064503-3; Sapora, Torabi, Etesam & Cornetti, *Fatigue & Fracture of Engineering Materials & Structures*, 41(7), 1627–1636 (2018), DOI 10.1111/ffe.12801.

## 4. HCP 3점굽힘 시편

### 판정: **불일치** — 원 실험을 `pre-crack` 또는 실제 균열로 부르는 것은 부정확

#### 4.1 원 실험의 결함 형상

Karihaloo, Abdalla, Xiao의 원 논문은 제목이 “Size effect in concrete beams”이고, 실험체를 반복해서 **notched HCP beams**, **central edge notch**, **notch-to-depth ratio**로 부른다. 시험한 HCP 빔은 3점굽힘, span/depth = 4, 폭 100 mm이며, 노치비는 0.05, 0.10, 0.30, 0.50이다. 원문은 fatigue pre-cracking 등으로 만든 sharp pre-crack이라고 서술하지 않는다.

따라서 개략도의 시작 결함은 **노치(notch)**로 표시해야 한다. “사전균열(pre-crack)” 또는 단순히 실제 균열이라고 단정하면 원 실험의 제작·기하 정보를 바꾼다.

반면 Kwon et al. (2024)은 §4 제목을 “Hardened Cement Pastes with Cracks”로 두고, §4.1에서 각 시편이 깊이 `a`의 “crack”을 갖는다고 쓰며, §4.3에서도 “specimens with initial cracks”라고 지칭한다. 즉 **2024 논문의 재서술 용어는 crack**, **2003 원 실험의 용어와 형상은 notch**이다. 두 층위는 구분해야 한다.

#### 4.2 역산점과 나머지 조합 수

Kwon et al. (2024) §4.3은 재료 파괴값 `Y`의 역산점으로 정확히 다음 한 조합을 지정한다.

- `H = 100 mm`
- `a/H = 0.1`

Fig. 11에 사용된 시편군은 `H=50 mm`와 `H=100 mm`, 각각 `a/H=0.1, 0.3, 0.5`인 **총 6개 기하 조합**이다. 따라서 역산에 쓴 한 조합을 뺀 **나머지는 5개 조합**이다.

- `H=50 mm`: `a/H=0.1, 0.3, 0.5` (3개)
- `H=100 mm`: `a/H=0.1, 0.3, 0.5` 중 역산점 하나를 제외한 `0.3, 0.5` (2개)

참고로 Karihaloo et al. (2003)의 HCP 전체 Table 1에는 이보다 더 많은 12개 조합이 있다. `a/H=0.05`군은 높이 75, 150, 300 mm이고, `a/H=0.10, 0.30, 0.50`군은 각 높이 50, 100, 200 mm이다. Kwon et al. Fig. 11은 그 전체를 사용한 것이 아니라 높이 50 mm와 100 mm의 6개 조합만 제시한다. 그러므로 “나머지 시편”의 기준을 2024년 역산·예측 그림으로 잡으면 답은 5개이고, 2003년 원 실험 전체로 확대하면 답이 달라진다.

**근거:** Kwon, Markoff & DeFisher, *Materials*, 17(3), 569 (2024), §4.1 “Description of Specimens”, §4.3 “Results”, Fig. 8 및 Fig. 11, 논문 PDF 7–8쪽, DOI 10.3390/ma17030569; Karihaloo, Abdalla & Xiao, *Engineering Fracture Mechanics*, 70(7–8), 979–993 (2003), §“Notched HCP and HSC beams”, Table 1, DOI 10.1016/S0013-7944(02)00161-3.

## 5. 조건① ∧ 조건②의 AND 논리

### 판정: **원문과 일치** — 원문은 명시적인 동시 충족 조건을 제시함

Kwon (2021)은 초록에서 제안 기준이 두 조건으로 이루어지고 **둘 다 파괴 발생을 위해 만족되어야 한다**고 명시한다. Case 3에서도 식 (12)와 식 (13)을 제시한 직후 “the following conditions are both satisfied”일 때 파괴한다고 쓴다. 따라서 AND 로직은 후대의 해석이 아니라 원문의 직접 진술이다.

결론부에는 “한 조건만 만족하면 파괴가 시작되지 않을 수도 있다(`may not initiate`)”라는 다소 약한 문장도 있다. 그러나 이것만 따로 떼어 원문의 논리 강도로 삼으면 안 된다. 초록과 본문의 명시적 필요조건 진술을 함께 보면 원 저자가 제안한 판정 규칙은 분명히

\[
\text{파괴 판정}=\text{조건①}\land\text{조건②}
\]

이다. 다만 이는 저자가 **제안한 criterion 내부에서의 파괴 판정 규칙**이라는 의미이며, 자연법칙으로서 두 조건이 엄밀한 필요충분조건임이 보편적으로 증명되었다는 뜻으로 확장해서는 안 된다.

**근거:** Kwon (2021), Abstract, “Failure of Brittle Materials”, Case 3의 식 (12)–(13) 직전 문장, Conclusions, 논문 인쇄쪽 064503-1–064503-3.

## 그림 라벨에 반영할 최소 수정 권고

1. Case 2: `θ=0 방향`만 쓰지 말고 **“균열 연장선(θ=0으로 정의), σx 평가선”**으로 쓴다.
2. Case 3: **“좌·우”를 삭제**하고 “하중축에 수직인 원공 경계의 두 점”으로 쓴다. 원문과 같은 수평하중 그림이면 실제 위치는 위·아래이다.
3. Case 4: **“1/4 FE 모델, 2496개 4절점 사각형 요소”**로 범위를 명시한다.
4. HCP 3PB: 시작 결함 라벨은 **“중앙 edge notch, 깊이 a”**로 하고, 필요하면 “Kwon et al. (2024)은 crack으로 지칭”이라는 주석을 단다.
5. AND 도식은 유지하되 “Kwon (2021)이 제안한 판정 규칙”임을 캡션에서 한정한다.

## 참고문헌

1. Kwon, Y. W., “Revisiting Failure of Brittle Materials,” *Journal of Pressure Vessel Technology*, 143(6), 064503, 2021. DOI: 10.1115/1.4050989.
2. Kwon, Y. W., Markoff, E. K., and DeFisher, S., “Unified Failure Criterion Based on Stress and Stress Gradient Conditions,” *Materials*, 17(3), 569, 2024. DOI: 10.3390/ma17030569.
3. Sapora, A., Torabi, A. R., Etesam, S., and Cornetti, P., “Finite Fracture Mechanics Crack Initiation from a Circular Hole,” *Fatigue & Fracture of Engineering Materials & Structures*, 41(7), 1627–1636, 2018. DOI: 10.1111/ffe.12801.
4. Karihaloo, B. L., Abdalla, H. M., and Xiao, Q. Z., “Size Effect in Concrete Beams,” *Engineering Fracture Mechanics*, 70(7–8), 979–993, 2003. DOI: 10.1016/S0013-7944(02)00161-3.
5. Irwin, G. R., “Analysis of Stresses and Strains Near the End of a Crack Traversing a Plate,” *Journal of Applied Mechanics*, 24, 361–364, 1957.
6. Kirsch, G., “Die Theorie der Elastizität und die Bedürfnisse der Festigkeitslehre,” *Zeitschrift des Vereines Deutscher Ingenieure*, 42, 797–807, 1898.
