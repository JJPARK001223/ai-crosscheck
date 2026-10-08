# Round 24 — Codex 독립 검증

## 검증 범위와 판정 기준

- 블라인드 단계이므로 `round24/claude.md`는 열람하지 않았다.
- 확인한 원문은 Y. W. Kwon, “Revisiting Failure of Brittle Materials,” *Journal of Pressure Vessel Technology*, Vol. 143, 064503 (2021), DOI: 10.1115/1.4050989의 1–2쪽이다.
- 아래 인용문의 강조는 추가하지 않았으며, 기호는 PDF에 인쇄된 표기대로 옮겼다.
- “원문 대조 결과: 맞음”은 원문의 명시적 문장 또는 식으로 확인되는 경우에만 썼다. 원문보다 강한 해석은 별도 단서로 구분했다.

## 1. \(\sigma_l\)은 변수이고 \(\sigma_f, w_f\)는 재료 고유 상수인가

**원문 대조 결과: 틀림(문장 전체를 “원문이 그대로 명시했다”고 할 경우).** \(\sigma_l\)의 하중·위치 의존성과 \(w_f\)의 재료 상수 가정은 직접 확인되지만, \(\sigma_f\)에는 원문이 문자 그대로 “material constant”라고 명시한 문장이 없다. 또한 원문은 \(w_f\)를 “새 균열면 생성에 필요한 에너지”라고 직접 정의하지 않는다.

### \(\sigma_l\): 적용하중과 위치에 따라 정해지는 국소응력

식 (1) 직후 원문은 다음과 같이 정의한다.

> “where \(\sigma_l\) is the local stress resulting from the applied load and \(\sigma_f\) is the failure strength of the material.” (p. 1, Eq. (1) 직후)

따라서 \(\sigma_l\)은 “적용하중으로 생기는 국소응력”이다. 위치 의존성은 식 (2)의 \(|d\sigma_l/ds|\) 및 다음 문장에서 직접 확인된다.

> “...and \(s\) is the orientation from the local point to yield the smallest value of \(|d\sigma_l/ds|\). That is, \(s\) is the path of the failure direction.” (p. 1, Eq. (2) 직후)

또한 Case 2의 식 (4)는 \(\sigma_x=K/\sqrt{2\pi r}\), Case 3의 식 (9)는 \(\sigma_\theta\)를 \(r,\theta\)의 함수로 쓴다. 그러므로 결함이 있는 예제에서 국소응력은 명백한 위치 함수이며, \(K\) 또는 원격응력 \(\sigma_o\)를 통해 적용하중에도 의존한다.

### \(\sigma_f\): 재료의 파괴강도

원문은 위 인용처럼 \(\sigma_f\)를 “the failure strength of the material”로 정의한다. Case 1에서도 다음과 같이 재료의 인장시험으로 얻는 값임을 밝힌다.

> “Thus, the failure of the test coupon is governed only by the failure strength of the material. In other words, the failure occurs when the applied stress equals to the failure strength of the material, which is actually obtained from the test results of the dog-bone shape coupon.” (p. 1, Case 1)

따라서 이 논문 안에서 \(\sigma_f\)를 형상에 따라 변하는 국소응력과 구별되는 재료 파괴강도로 취급한다는 판정은 맞다. 다만 확인한 본문에는 \(\sigma_f\)를 정확히 “material constant” 또는 “geometry-independent”라고 부르는 문장은 없다. 따라서 HTML에서는 “원문이 \(\sigma_f\)를 재료의 파괴강도로 정의한다”고 쓰는 것이 가장 정확하고, “원문이 형상과 무관한 상수라고 명시했다”고 따옴표 수준으로 강화해서는 안 된다.

### \(w_f\): 원문이 명시한 재료 상수

요청한 직접 문장은 다음과 같다.

> “Here, \(|d\sigma_l/ds|\) is the absolute value of the stress gradient, \(E\) is the elastic modulus of the material, \(w_f\) is the critical value, **which is assumed to be a material constant**, and \(s\) is the orientation from the local point to yield the smallest value of \(|d\sigma_l/ds|\).” (p. 1, Eq. (2) 직후)

원문은 이어서 단위를 확인한다.

> “The units of \(w_f\) are Pa · m = N/m = J/m². Therefore, it has the value force per unit length or energy per unit area.” (p. 1, Eq. (3) 직후)

따라서 \(w_f\)를 “단위면적당 에너지 차원의 임계값이며 재료 상수로 가정된다”고 설명하는 것은 정확하다. 다만 원문은 이를 “균열면을 새로 만드는 데 필요한 에너지”라고 직접 정의하지 않고, “critical value” 및 “energy per unit area”라고만 쓴다. 그 이상의 단정은 원문 표현보다 강하다.

### HTML에 넣을 수 있는 검증된 문장

> \(\sigma_l\)은 적용하중이 만들어 내는 국소응력으로, 결함이 있으면 위치 \(s\) 또는 \((r,\theta)\)에 따라 달라진다. \(\sigma_f\)는 원문이 정의한 재료의 파괴강도이고, \(w_f\)는 원문이 명시적으로 재료 상수라고 가정한 응력구배 기준의 임계값이다.

## 2. 식 (1)만으로 부족하여 식 (2)가 필요한가

**원문 대조 결과: 맞음. 단, 원문의 명칭은 “응력구배 조건(stress-gradient condition)”이며 단순한 총에너지 또는 충격량 조건이 아니다.**

Introduction/「Failure of Brittle Materials」 도입부의 직접 근거는 다음과 같다.

> “In other words, for a material to fail under a given loading, the local stress exceeding the failure strength of the material is not enough to initiate the failure. The material surrounding the local point must provide a path for failure.” (p. 1)

> “If the stress gradient at the local point of potential failure is too steep, failure would not occur even though the local stress is much greater than the failure strength of the material.” (p. 1)

초록도 두 조건의 관계를 더 직접적으로 말한다.

> “The proposed criteria consist of two conditions, of which both must be satisfied for failure to occur.” (p. 1, Abstract)

> “Even if the stress at a local point far exceeds the failure strength of the material, failure will not initiate until the stress gradient condition is satisfied.” (p. 1, Abstract)

식 (2)의 물리량에 대한 원문의 설명은 다음과 같다.

> “The numerator of Eq. (2) is the strain energy density, and the denominator is the stress gradient per unit stress.” (p. 1)

따라서 “한 점의 \(\sigma_l\ge\sigma_f\)만으로는 충분하지 않고, 주변의 파괴 경로와 관련된 공간 응력구배 조건도 만족해야 한다”는 요약은 원문과 정확히 맞는다. 반면 식 (2)를 시간에 대한 에너지 축적, 충격량, 접촉시간 또는 단순히 ‘넓은 면적에 전달된 총에너지’로 바꾸어 설명하면 원문에서 벗어난다.

### HTML에 넣을 수 있는 검증된 문장

> 식 (1)은 후보 지점의 국소응력이 재료의 파괴강도에 도달했는지를 묻는다. 그러나 원문은 그 값이 훨씬 커도 공간 응력구배가 너무 가파르면 파괴가 시작되지 않을 수 있다고 명시한다. 따라서 파괴에는 식 (1)과 식 (2)가 모두 필요하다.

## 3. 비유 A와 B의 물리적 정확성

### 비유 A: 핀으로 살짝 찌르기 대 뭉툭한 손가락으로 눌러 멍들기

**원문 대조 결과: 틀림(현재 문구 그대로는 식 (1)–(2)의 설명으로 쓰기에 부적합).**

1. **“압력 대 충격량”이라는 표제부터 식 (2)와 다르다.** 식 (2)는 정적 공간좌표 \(s\)에 대한 \(|d\sigma_l/ds|\)를 사용한다. 시간, 작용시간, 운동량 또는 충격량은 식에 없다.
2. **일상적 결과의 방향이 비유가 의도한 방향과 충돌한다.** 뾰족한 핀은 같은 힘에서 접촉면적이 작아 국소응력이 커지므로, 일반적으로 뭉툭한 손가락보다 피부 관통을 쉽게 만든다. “핀은 높은 국소응력에도 뚫지 못하지만 손가락은 더 낮은 응력으로 조직을 파괴한다”는 대비는 보편적 관찰과 반대이며, 논문의 두 조건을 입증하지도 않는다.
3. **서로 다른 손상모드를 비교한다.** 핀의 피부 관통/절단과 손가락 압박에 의한 멍은 동일한 ‘파괴 시작’을 비교하지 않는다. 인장·전단 파단과 혈관 손상/압궤를 섞으면 하나의 \(\sigma_f,w_f\)로 두 현상을 설명할 수 없다.
4. **식 (1)을 빠뜨릴 위험이 있다.** 손가락 쪽 응력이 “낮다”는 말이 \(\sigma_f\)보다 낮다는 뜻이면, 영역이 넓어도 식 (1)을 만족하지 않으므로 논문 기준에서는 파괴가 시작되지 않는다. 두 식은 대체관계가 아니라 모두 만족해야 하는 조건이다.
5. **핀으로 ‘살짝’ 찌르면 안 뚫릴 수 있다는 사실만으로는 식 (2)의 사례가 되지 않는다.** 그때 핀 끝의 실제 관련 등가응력이 피부의 해당 파괴강도 \(\sigma_f\)를 넘었는지 측정하지 않았기 때문이다. 식 (1)의 성립을 확인하지 않은 채 “식 (1)은 만족했지만 식 (2)가 실패했다”고 단정할 수 없다.

결론적으로 비유 A는 사용하지 않는 편이 정확하다. 굳이 살리려면 피부·핀·멍을 모두 버리고, “높지만 매우 좁은 응력 봉우리”와 “\(\sigma_f\) 이상을 유지하면서 공간적으로 완만한 응력 분포”라는 추상 도식으로 바꾸어야 한다.

### 비유 B: 칼끝 대 숟가락

**원문 대조 결과: 틀림(현재 문구 그대로는 부적합).**

1. 같은 힘이라면 칼날은 숟가락보다 큰 국소응력을 만들어 실제로 더 쉽게 절단하는 것이 보통이다. 따라서 “칼끝은 응력구배가 커서 못 자르지만 숟가락은 넓게 에너지가 쌓여 파괴한다”는 대표 대비로 사용할 수 없다.
2. 숟가락의 넓은 응력장이 식 (2)에 유리할 수 있어도, 국소응력이 \(\sigma_f\)에 못 미치면 식 (1)이 실패한다. 넓이 또는 총에너지가 식 (1)을 대신하지 않는다.
3. 칼날 접촉과 숟가락 접촉은 응력 상태, 접촉면적, 마찰 및 손상모드가 함께 달라진다. 그러므로 동일 재료의 고정된 \(\sigma_f,w_f\) 아래에서 ‘오직 응력구배만’ 비교하는 비유가 아니다.

“어떤 매우 작은 하중에서는 칼날 아래의 좁은 영역만 \(\sigma_f\)를 넘고 식 (2)는 아직 만족하지 않을 수 있다”는 제한된 가능성 자체는 논문의 문장과 양립한다. 그러나 같은 하중의 숟가락이 그보다 더 쉽게 파괴를 일으킨다는 결론은 따라오지 않는다. 따라서 현재 A·B 모두 최종 HTML의 중심 비유로 권하지 않는다.

## 4. 더 정확한 대안: 미세 흠집이 있는 유리판

**원문 대조 결과: 맞음(원문의 Case 2를 일상적인 유리 흠집 상황으로 옮긴 비유).**

### 제안 문구

> 미세한 균열형 흠집이 있는 유리판을 천천히 당긴다고 생각하자. 선형파괴역학 식에서는 흠집 끝에 가까울수록 \(\sigma_l(r)=K/\sqrt{2\pi r}\)가 매우 커지므로, 아주 작은 영역에서는 재료 파괴강도 \(\sigma_f\)를 넘을 수 있다. 그래도 흠집이 곧바로 달리기 시작하는 것은 아니다. 이 논문의 Case 2에서는 식 (2)의 값이 \(K^2/(2\pi E)\)가 되고, 이것이 재료 임계값 \(w_f\)에 도달해야 균열이 전파한다. 즉, ‘끝의 한 점이 매우 세다’와 ‘균열이 진행할 만큼 응력장이 갖추어졌다’는 별개의 조건이다.

직접 근거는 Case 2의 다음 문장과 식 (4), (6), (7)이다.

> “The stress at the crack tip is infinite such that the induced local stress exceeds the failure strength of the material. Then, the stress gradient is the dominating factor for the failure.” (p. 2, Case 2)

> \(\sigma_x=K/\sqrt{2\pi r}\) (Eq. (4)); \(w_f=K^2/(2\pi E)\) (Eq. (6)); \(K_{IC}=\sqrt{2\pi E w_f}\) (Eq. (7)).

이 비유가 변수–상수 구조를 왜곡하지 않는 이유는 다음과 같다.

- 같은 유리와 같은 환경을 전제로 하면 \(\sigma_f\)는 그 재료의 파괴강도이고, \(w_f\)는 원문이 재료 상수로 가정한 임계값이다.
- 바뀌는 것은 적용하중에 따른 \(K\)와 흠집 끝으로부터의 거리 \(r\)이며, 그에 따라 국소응력 \(\sigma_l(r)\)이 바뀐다.
- 식 (1)과 식 (2)를 서로 대체하지 않는다. 이상화된 균열 끝의 큰 국소응력은 식 (1)의 필요성을, \(K^2/(2\pi E)\ge w_f\)는 별도의 식 (2) 필요성을 각각 보여 준다.

이 대안은 원문에 없는 피부 물성, 충격량 또는 서로 다른 손상모드를 끌어오지 않으므로 A·B보다 안전하다. 엄밀히는 새로운 독립 실험사례가 아니라 논문의 Case 2를 일상 소재인 ‘흠집 난 유리’로 번역한 설명이다.

## 5. Case 1 → 2 → 3에서 국소응력이 위치 함수가 되는 과정

**원문 대조 결과: 맞음. 단, Case 1의 원문은 \(\sigma_l=\sigma_o\)라는 식을 직접 쓰지 않고 “uniform”이라고 서술한다.**

- **Case 1 — 위치에 무관한 균일응력:** “the induced stress is uniform across the width of the test coupon around the midsection”이고 “the stress gradient is zero”이므로, 중앙부의 국소응력은 위치에 따라 변하지 않는 상수처럼 취급된다(p. 1, Case 1).
- **Case 2 — 균열 끝 거리 \(r\)의 함수:** 식 (4) \(\sigma_x(r)=K/\sqrt{2\pi r}\)이므로 균열 끝에 가까울수록 커지고, 원문은 균열 끝 응력이 무한대라고 서술한다(p. 2, Case 2).
- **Case 3 — 반지름 \(r\)과 각도 \(\theta\)의 함수:** 식 (9) \(\sigma_\theta(r,\theta)=\frac{\sigma_o}{2}[(1+R^2/r^2)-(1+3R^4/r^4)\cos2\theta]\)이므로 원공 주변에서 위치에 따라 달라진다. 원문은 최대가 \(\theta=\pi/2\), \(r=R\)에서 \(3\sigma_o\)이고, 그 방향의 응력구배가 \(7\sigma_o/R\)라고 계산한다(p. 2, Eqs. (9), (11)).

### HTML용 한 문장 요약

> Case 1에서는 중앙부 응력이 균일하여 구배가 0이지만, Case 2에서는 \(\sigma_l\propto r^{-1/2}\), Case 3에서는 \(\sigma_l=\sigma_l(r,\theta)\)가 되어 결함 주변의 명백한 위치 함수로 바뀐다.

## 최종 판정 요약

- 변수/상수 구분은 물리적 사용 방식으로는 대체로 맞지만, 세 기호에 관한 주장이 모두 원문에 그대로 명시됐다는 판정은 틀리다. 특히 \(w_f\)는 원문이 “material constant”라고 명시하지만, \(\sigma_f\)는 “failure strength of the material”로 정의될 뿐 같은 직설적 상수 문구가 없다.
- 식 (1)만으로 부족하고 식 (2)가 함께 필요하다는 설명은 원문이 명시적으로 뒷받침한다.
- 비유 A와 B는 현재 형태로는 모두 부적합하다. 핀/칼이 오히려 관통·절단을 쉽게 한다는 일상 경험과 충돌하고, 식 (2)를 충격량이나 넓은 면적의 총에너지로 오해하게 하며, 식 (1)이 여전히 필수라는 사실을 흐린다.
- 가장 안전한 비유는 원문의 Case 2를 일상 소재로 번역한 “미세 흠집이 있는 유리판”이다. 같은 재료의 \(\sigma_f,w_f\)는 고정하고, 하중과 위치에 따라 \(\sigma_l\)만 변하게 설명할 수 있다.
