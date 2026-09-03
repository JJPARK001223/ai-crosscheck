# Round 1 - Claude 초안

## 문제
연동 파이프라인 점검용 테스트: 항복강도와 인장강도의 정의 차이를 2-3문장으로만 답하라.

## 답 (2-3문장)

항복강도(yield strength)는 재료가 소성변형(영구변형)을 시작하는 응력으로, 명확한 항복점이 없는 금속에서는 통상 0.2% 오프셋 방법으로 규정한다. 인장강도(ultimate tensile strength, UTS)는 인장시험의 공칭 응력-변형률 곡선에서 도달하는 최대 공칭 응력으로, 이 지점 이후 네킹이 시작되어 하중이 감소한다. 즉 항복강도는 "탄성 거동의 끝(소성변형 개시)"을, 인장강도는 "공칭 곡선상 하중 지지 능력의 최대치"를 나타낸다.

## 근거

- **항복강도 / 0.2% 오프셋 정의**: ASTM E8/E8M *Standard Test Methods for Tension Testing of Metallic Materials* — "yield strength"를 offset method(일반적으로 0.2%), extension-under-load method 등으로 규정. 동일 정의가 ISO 6892-1에도 있으며 여기서는 비례한도가 없는 재료에 대해 규약항복강도 R_p0.2를 사용.
- **인장강도(UTS) 정의**: ASTM E8/E8M 및 표준 재료역학 교과서 — "tensile strength = maximum tensile stress that a material can withstand", 시험편 원단면적 기준 최대 하중 / 원단면적(engineering stress 기준).
- **교과서**:
  - Callister & Rethwisch, *Materials Science and Engineering: An Introduction* — yield strength(σ_y)는 0.2% strain offset로 정의, tensile strength(TS)는 engineering stress–strain 곡선의 최대점, 그 이후 necking 발생.
  - Dieter, *Mechanical Metallurgy* — UTS는 "the maximum load divided by the original cross-sectional area of the specimen"; 소성불안정(dP=0) 조건에서 necking 개시.
  - Dowling, *Mechanical Behavior of Materials* — 동일한 구분.

## 불확실성 / 주의점

- 문제는 "2-3문장"만 요구하므로 위 답 문단이 제출본이고 나머지는 근거 자료다.
- "정의 차이"의 범위 해석: 본 답은 표준 인장시험(단축, 준정적, 상온, 금속) 기준. 재료군(고분자, 세라믹, 취성재료)에 따라 항복 개념 자체가 불명확하거나 인장강도가 파단강도와 같아지는 경우가 있으나, 파이프라인 점검용 간단 테스트이므로 일반 금속 기준으로 한정했다.
- 항복강도 정의를 "0.2% offset"으로 특정할지, 더 일반적으로 "탄성→소성 전이 응력"으로 둘지는 맥락에 따라 다르다. 본 답은 둘 다 언급.
- 용어: "인장강도"는 UTS(극한인장강도)를 뜻하며 파단강도(fracture/breaking strength)와 구분된다. 연성 금속에서는 necking 때문에 공칭 파단응력 < UTS.
- 출처는 표준(ASTM E8, ISO 6892-1)과 표준 교과서로 신뢰도 높음. 특정 판/페이지 번호는 확인하지 않았다(정의 자체는 판과 무관하게 동일).

## Codex 검토 대기

Codex의 `round1/codex.md` 독립 결과가 아직 비어 있음 → 교차검증 미완료. Codex 결과가 준비되면 공통점/충돌/보완사항을 정리하고 그 뒤에 DECISION.md를 갱신한다.
