# round91 — Claude 1단계(blind) 결과: LEAK RATE PPT Eqn. 1~25 ↔ 원문 b047.pdf

기준: PDF 쪽 이미지(p28~34, 39, 45)와 `spec25_latex.py`. 단위 `[...]` 제거는 의도된 차이로 불일치에서 제외.

## 1. 식 일치 (25개 전부 일치)
| Eqn | 슬라이드 | PDF쪽(인쇄쪽) | 판정 |
|---|---|---|---|
| 1 | 5 | 28(17) | 일치 |
| 2 | 6 | 28(17) | 일치 (원문 `ṁ`는 `\dot{m}`) |
| 3 | 7 | 29(18) | 일치 |
| 4 | 8 | 29(18) | 일치 |
| 5 | 9 | 30(19) | 일치 |
| 6 | 10 | 30(19) | 일치 |
| 7 | 11 | 30(19) | 일치 (단위 [m²] 제거) |
| 8 | 12 | 30(19) | 일치 (단위 [m] 제거) |
| 9 | 13 | 31(20) | 일치 |
| 10 | 14 | 31(20) | 일치 |
| 11 | 15 | 31(20) | 일치 |
| 12 | 16 | 31(20) | 일치 |
| 13 | 17 | 32(21) | 일치 |
| 14 | 18 | 32(21) | 일치 |
| 15 | 19 | 33(22) | 일치 |
| 16 | 20 | 33(22) | 일치 |
| 17 | 21 | 33(22) | 일치 |
| 18 | 22 | 34(23) | 일치 |
| 19 | 23 | 34(23) | 일치 |
| 20 | 24 | 34(23) | 일치 |
| 21 | 25 | 39(28) | 일치 |
| 22 | 26 | 39(28) | 일치 (`;\ for` 조건 포함) |
| 23 | 27 | 39(28) | 일치 (단위 [kg/(m²−sec)] 제거) |
| 24 | 28 | 45(34) | 일치 |
| 25 | 29 | 45(34) | 일치 |

## 2. 정의 문구가 원문과 글자 단위로 다른 곳
| Eqn | 슬라이드 행 | 원문 | 비고 |
|---|---|---|---|
| 1 | N: "Empirical parameter" | "empirical parameter, see Eqs. (3)-(4)." | `see Eqs. (3)-(4)` 생략 |
| 1 | v_fg(c) 행 | 원문 기호는 `v_fg(c) = v_g(c) − v_f(c)` | 슬라이드는 `v_{fg(c)}`만 |
| 1 | 행 순서 | 원문: G_c, x_c, v_g(c), γ0, p_c, N, v_fg(c), x_E, dx_E/dp | 슬라이드는 p_c를 2번째에 둠 (순서만 다름) |
| 2 | Q, ṁ 행 | where 목록 없음. 본문 "volumetric flow rate, I"(원문 오탈자), "mass flow rate, ṁ" | 본문에서 가져온 문구. v_std 행만 원문 where 형식 |
| 5 | G_c 행 없음 | 원문 where 목록에 G_c 없음 | 의도된 생략 |
| 7 | D_h: "…of the crack entrance flow area (Equation 8)" | 본문 "the hydraulic diameter, D_h, of the crack entrance flow area is defined by [Eq. 8]" | "(Equation 8)" 슬라이드가 덧붙임 |
| 9 | A_o 행 | 원문 where "A_o"(소문자 o), 식에는 A_0 | 원문 표기 불일치. 슬라이드는 where대로 A_o |
| 11 | C_1, C_2: "C coefficients (defined below Equation 12)" | "The C coefficients are defined as:" | 문구 변형. C 계수 값(2, 1.14 / 3.39, −0.866)은 슬라이드에 없음 |
| 11 | D_h: "The hydraulic diameter ratio by Equation 19" | 원문 문장의 일부(어색한 원문 그대로) | 원문 그대로 |
| 12 | D_h/μ 행 | "The hydraulic diameter to effective surface roughness is limited by" | 슬라이드는 명사구로 줄임 |
| 14 | e_vloss: "Velocity head loss" | 원문 "The velocity head loss is defined as"(기호표 "velocity head loss") | 원문 문구 존재 확인 |
| 21 | Δp: "The required pressure loss (Equation 22)" | 본문 "the required pressure loss is [Eq. 22]" | "(Equation 22)" 덧붙임 |
| 22 | p_0, p_c 행 | 이 절에는 정의 없음 (Eqn. 3 where 목록 문구) | Eqn. 3 문구를 가져옴 |
| 23 | Q: "(Equation 21)" | 원문에 없음 | 덧붙임 |
| 24,25 | COV 행 | 원문 2.9절 "COV, defined as the ratio of the standard deviation of the leak rate to the mean leak rate" | 일치. 슬라이드에서 "rate" 한 단어가 줄바꿈 (레이아웃) |

## 3. 제목·쪽 표기
- 쪽 표기 p.17, 18, 19, 20, 21, 22, 23, 28, 34는 인쇄쪽과 일치.
- 제목 접두어 "Eqn. n — "은 원문에 없는 형식(HTML 카드 제목에 맞춘 것).
- Eqn. 24 제목 "280°C에서 COV와 평균 누설률 λ", Eqn. 25 "340°C…"는 원문 "280°C (Equation 24) and 340°C equations (Equation 25)"와 일치.

## 4. 원문 자체의 불일치 (교정하지 않음)
- Eqn. 9 where 목록 `A_o` vs 식 `A_0`.
- Eqn. 2 본문 "volumetric flow rate, I"(Q 대신 I).
- Eqn. 4 where `v_I(0)`로 인쇄되나 다른 식에서는 `v_l(0)` 형태 (글꼴상 l/I 구분 불가 — 확인 불가).
- Eqn. 23 `v_I(o)`(소문자 o) 본문 표기.
- Eqn. 12 본문 "the hydraulic diameter ratio by Equation 19": Eqn. 19는 D_h 정의식이고 비 D_h/μ는 Eqn. 12 — 원문 문장 자체가 어색.
- Figure 2는 C 계수 경계를 D_h/μ = 27.74로 표기하는데, 본문 식 11 아래 조건은 100. (원문 간 차이)

## 5. 레이아웃 (슬라이드 PNG 기준)
- 이전 라운드 렌더 확인에서 겹침·잘림 없음. Eqn. 24/25 COV 행의 "rate" 줄바꿈 잔여.
