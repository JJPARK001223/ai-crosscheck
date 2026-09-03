# Round 1 - Claude 초안

## 문제
연동 파이프라인 점검용 테스트: 항복강도(yield strength)와 인장강도(tensile strength)의 정의 차이를 2-3문장으로만 답하라.

## 답 (2-3문장)

항복강도는 재료가 탄성 변형에서 영구적인 소성 변형으로 넘어가기 시작하는 응력으로, 항복점이 뚜렷하지 않은 금속에서는 통상 0.2% 잔류 변형에 해당하는 응력(offset yield strength, σ_0.2)으로 정의한다. 인장강도(정확히는 극한인장강도, ultimate tensile strength, UTS)는 공칭 응력-변형률 곡선에서 시편이 견디는 최대 공칭 응력으로, 이 지점 이후 국부 네킹이 시작되어 하중이 감소한다. 즉 항복강도는 "소성 변형이 시작되는" 응력이고 인장강도는 "시편이 버티는 최대" 응력이며, 연성 금속에서는 항상 인장강도 ≥ 항복강도이다.

## 근거

- **정의 (offset yield):** ASTM E8/E8M "Standard Test Methods for Tension Testing of Metallic Materials" — yield strength를 지정된 offset(관례적으로 0.2%)에서의 응력으로 규정. 상항복/하항복(upper/lower yield point)이 나타나는 저탄소강 등은 별도 정의 사용.
- **정의 (UTS):** ASTM E8/E8M — tensile strength = 최대 하중 / 원래 단면적. 공칭(engineering) 응력 기준 곡선의 최댓값.
- **교과서:**
  - Callister & Rethwisch, *Materials Science and Engineering: An Introduction*, Ch. 6 (Mechanical Properties of Metals): yield strength는 탄성-소성 전이, 0.2% offset 관례; tensile strength는 engineering stress-strain 곡선의 최대점, 이후 necking.
  - Dieter, *Mechanical Metallurgy*, Ch. 8–9: UTS 시점에서 dσ_true/dε = σ_true (Considère 조건) → 소성 불안정(diffuse necking) 개시.
- **부등식 근거:** 가공경화(strain hardening)로 인해 항복 이후에도 응력이 계속 증가하다가 네킹 전까지 최대에 도달하므로 UTS ≥ YS. 완전소성/가공경화 없는 이상재료에서만 등호.

## 불확실 / 주의 사항

- "인장강도"라는 용어는 문맥에 따라 (1) 극한인장강도(UTS), (2) 파단강도(fracture strength)와 혼용될 수 있음. 본 답변은 표준 관례에 따라 UTS로 해석함.
- offset 값 0.2%는 금속의 관례이며, 재료·규격에 따라 0.1%, 0.5% 등을 쓰기도 함(플라스틱은 ISO 527에서 다른 정의).
- 취성 재료(주철, 세라믹)는 뚜렷한 항복 없이 파단하므로 항복강도 개념이 잘 적용되지 않음.
- 이 문제는 파이프라인 점검용 테스트이므로 답 내용보다 "연동 절차가 정상 동작하는지"가 핵심 목적으로 보임.

## 상태

- Codex의 독립 결과(`round1/codex.md`)는 아직 비어 있음. 교차검증 미완료.
- Codex 결과가 준비되면 공통점/충돌/오류를 검증한 뒤 DECISION.md 갱신 예정.
