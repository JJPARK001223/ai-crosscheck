# 문제 (Round 3)

## 배경
사용자(재료공학/파괴역학 석사생)의 **대학원 졸업논문 주제**: Kwon 등의 논문
(2021 *J. Pressure Vessel Technol.*; 2024 *Materials* 17,569)이 제시한 "응력 +
응력구배 조건" 기반 **취성재료** 파괴기준(w_f 유도 — 순수 탄성변형에너지밀도
U=σ_l²/2E 와 LEFM 균열끝단 특이장 σ_l~K/√r 에 기반)을, **연성(ductile) 금속재료로
확장**하는 것.

현재 상태:
- 확장 방법론 **미정**. 선배/지도교수 지시는 "실험데이터가 있으니 연성으로
  확장해봐라"는 큰 방향만 있음.
- 실험데이터는 있음(구체적 재료·데이터 종류는 아직 학생이 정하지 못함/미공유).

## 이전 세션에서 Claude가 학생에게 이미 설명한 이론적 걸림돌 (재검증 불필요, 전제로 사용)
- 연성재료는 파괴에너지의 대부분이 소성일에서 나옴 — Orowan(1948) 확장 Griffith
  이론: w_f = 2γ_s + γ_p, γ_p ≫ γ_s.
- 균열끝단 응력장이 LEFM 특이장(1/√r)이 아니라 **HRR장**(Hutchinson 1968,
  *J. Mech. Phys. Solids* 16, 13–31; Rice & Rosengren 1968, 같은 저널 16, 1–12)을
  따름: σ_ij ~ r^(-1/(n+1)).
- Small-scale yielding 조건 하에서 J = K²/E' (Rice, 1968, *J. Appl. Mech.* 35,
  379–386) 이 성립 — K와 J를 잇는 다리.

## 조사 요청
문헌상 확립된 "취성/탄성 기반 파괴기준을 연성/탄소성 재료로 확장"하는 방법론들을
폭넓게 조사하고, 각각을 **이 논문의 "응력(σ_l) + 응력구배(dσ_l/ds)" 결합 조건
구조**와 결합 가능성 관점에서 비교 평가할 것. 최소 아래 후보를 검토(추가 발견 시
포함):

1. **J-적분/HRR장 기반 재유도** — K, σ_l, ds 등을 J, HRR 변수로 치환
2. **국소접근법(local approach to fracture)** — Weibull stress (Beremin model),
   RKR(Ritchie-Knott-Rice) 모델
3. **손상역학 모델** — GTN(Gurson-Tvergaard-Needleman), Johnson-Cook 파손모델
4. **Essential Work of Fracture (EWF)** 접근
5. **Cohesive Zone Model (CZM)**
6. 기타 문헌에 실제 유사 사례가 있다면 포함 — 특히 **"응력 + 응력구배(stress
   gradient)" 개념을 연성/탄소성 재료 파괴기준에 실제로 적용한 선행연구**가
   존재하는지 (예: critical distance theory / Theory of Critical Distances,
   TCD — Taylor 등의 연구가 이와 개념적으로 유사할 수 있음, 확인 필요)

## 원하는 결과물
각 방법론에 대해:
- 핵심 아이디어 1~2문장
- 대표 문헌(저자, 연도, 저널) — **실제 존재 확인된 것만**, 불확실하면 "확인
  불가"라고 명시. 추측/창작 절대 금지.
- 이 논문의 구조(σ_l 응력 + dσ_l/ds 응력구배 결합 조건)와 결합 가능성 —
  높음/중간/낮음 + 이유
- 필요한 실험 데이터 종류(예: J-R curve, 인장 응력-변형률 곡선, DIC 변형장,
  노치 시편 파괴하중 등)

마지막에 **"지도교수 면담 전 학생이 검토할 후보 3개"**를 근거와 함께 추천할 것.
