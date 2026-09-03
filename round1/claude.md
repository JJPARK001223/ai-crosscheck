# Round 1 — Claude 독립 분석

(PROBLEM.md만 보고 작성. Codex 결과는 보지 않음.)

## 문제

항복강도와 인장강도의 정의 차이를 2-3문장으로 답하라.

## 답 (2-3문장)

항복강도(yield strength, σ_y)는 재료가 탄성 거동을 벗어나 영구적인 소성변형을 일으키기 시작하는 응력이며, 많은 금속에서 탄성-소성 천이가 점진적이라 통상 0.2% 오프셋 항복강도(proof stress)로 규정한다. 인장강도(ultimate tensile strength, UTS)는 인장시험 중 재료가 견디는 최대 공칭응력, 즉 최대 하중을 초기 단면적으로 나눈 값으로, 이 지점 이후 네킹(necking)이 시작되어 공칭 응력-변형률 곡선에서 응력이 감소한다. 즉 항복강도는 "영구변형 개시" 기준(대부분의 구조 설계 한계), 인장강도는 공칭 곡선상의 "최대 하중 지지 능력" 기준이며 연성 금속에서는 항상 UTS ≥ σ_y 이다.

## 근거

- **항복강도 / 0.2% 오프셋 정의**: G. E. Dieter, *Mechanical Metallurgy*, 3rd ed., McGraw-Hill, 1986, pp. 275–279 — 탄성한계가 불명확할 때 offset method(보통 ε = 0.002)로 항복강도를 정의.
- **오프셋 항복강도 시험 규격**: ASTM E8/E8M-22, *Standard Test Methods for Tension Testing of Metallic Materials*; ISO 6892-1:2019 — "yield strength (offset method), R_p0.2" 및 "tensile strength, R_m = 최대 힘 / 초기 단면적" 을 명시적으로 규정.
- **인장강도(UTS)와 네킹**: W. D. Callister & D. G. Rethwisch, *Materials Science and Engineering: An Introduction*, 10th ed., Wiley, 2018, Ch. 6 — UTS는 공칭 응력-변형률 곡선의 최대점이며, 그 지점에서 네킹이 개시되고 이후 공칭응력이 감소.
- **UTS ≥ σ_y 및 설계 관점**: N. E. Dowling, *Mechanical Behavior of Materials*, 4th ed., Pearson, 2013, Ch. 4 — 항복강도는 소성변형 개시 기준으로 대부분의 정적 설계에서 허용응력 산정 근거.

## 불확실 / 유의점

- "인장강도"는 공칭(engineering) 응력 기준의 최대점이다. 진응력(true stress) 기준으로는 파단 시점까지 단조 증가하므로 "최대점"이라는 표현이 성립하지 않는다 — 이 답은 공칭 곡선 기준.
- 취성 재료(주철, 세라믹 등)나 뚜렷한 항복점을 보이는 저탄소강(upper/lower yield point)은 0.2% 오프셋이 아니라 다른 방식으로 항복을 정의할 수 있다. 위 답은 일반적인 연성 금속 기준.
- 규격 문서의 조항 번호·연도는 최신 개정판에서 달라질 수 있어 직접 대조가 필요하다(오프라인 작성).

## 상태

Codex 독립 결과 미도착. `round1/codex.md` 준비되면 교차검증 후 `DECISION.md` 갱신 예정. 현재는 Claude 단독 초안 상태.
