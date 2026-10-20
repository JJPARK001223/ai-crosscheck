# round49 Claude 독립 검증 — 2026_10_17.pptx vs B049 원문

(원문 근거는 인쇄쪽 기준. PDF쪽 = 인쇄쪽+15. 식 슬라이드는 Fig.29~31(PDF 61~63)만 지면 확인, 나머지 식 슬라이드는 Codex 결과와 교차 확인 예정)

## 내용 불일치 (원문 근거 있음)
| 슬라이드 | 문제 | 원문 근거 | 수정 |
|---|---|---|---|
| 5 | "비드당 약 2~30 요소" | p.5 "roughly 20-30 elements per bead" | 20~30 |
| 7 | "A580노즐" | p.8 "A508 nozzle" | A508 |
| 11 | 열물성 위치 "Fig.69-97" | p.21 "Figure 96, Figure 97" | Fig.96-97 |
| 11 | "각기 다른 DB를 쓰면 결과값에 대한 신뢰도가 없으므로" | p.21 "To remove this as a source of modeling uncertainty, a common set…" | 원문 문장으로 |
| 16 | "WRS 분포는 … 가깝다는 사실임" ("지배됨" 누락) | p.31 "dominated by the fact that" | "…사실에 지배됨" |
| 19 | 규칙2 "압축으로 변화" | p.45 "change to compression (or reduction from tension to lower tension)" | 괄호 내용 추가 |
| 19 | 규칙4 "ID 부근에서 최소 200MPa로 감소" | p.45 "decrease at least 200 MPa near ID" | "최소 200 MPa 감소" |
| 24 | 슬라이드 22(SG baseline) 내용 그대로 복제. 23은 SG 15% repair | p.46 Fig.30 "axial stresses will actually decrease near the ID since the repair WRS field is tensile" | 24를 SG 15% repair(Fig.30, p.47)로 교체 |
| 41 | MSIP(Fig.38)인데 "서비스 중 weld overlay 후…" (FSWOL 문구 복사) | p.52 MSIP rules [39-41] | 43과 같은 MSIP 문구 |
| 39 | "(fig.27)" | p.52 "(Figure 27 of [40])" — 참고문헌 [40]의 그림 | "[40]의 Figure 27"로 |
| 58~75 | "ID응력이 항복 근처까지 증가" | p.58 "high (near or above yield)" | "항복 근처 또는 그 이상" |
| 75 | 제목·사용대상 "15% repair", Fig.55 | p.63 Fig.55 "pump nozzle, 50% repair case" | 50% repair |
| 21·23·…·74 기호표 | u 설명 "(R/t)" | 규칙식은 x/t (p.46~) | "(x/t)" |
| 21·23·…·74 기호표 | "DMW (이중 금속용접)" | dissimilar metal weld | 이종금속용접 |
| 92 | 행렬 둘째 인수 "1+ρ²" | p.72 "√(1−ρ²)" | 1−ρ² |
| 82 | 평균 식 좌변 "u_k" | p.68 "μ_k" | μ_k |
| 88 | "Z3" | p.71 "z3" | z3 |
| 87 | "모든 점의 Param2가 같음" (깨진 기호) | p.69 "unique standard deviation" | σ(표준편차) 또는 "표준편차" |
| 78·79·81·85·87·90·93·94 | "식 5-1/5-3/5-4/5-5/6-1/6-3" 인용 | 원문 식에는 번호 없음 | 원문 문구로 대체 |
| 2, 76~87 | 목차에 5장(WRS SAMPLING AND UNCERTAINTY CHARACTERIZATION) 없음, 76~87 푸터가 4장 제목(SENSITIVITY AND UNCERTAINTY STUDIES) | p.66 "5 WRS SAMPLING AND UNCERTAINTY CHARACTERIZATION" | 푸터·목차 수정 |
| 7, 30~75, 77, 22… | 쪽 표기 혼용: p.8·p.66·p.86은 인쇄쪽, p.64~78은 PDF쪽(Fig.33=인쇄 49쪽) | 예: Fig.33 인쇄 p.49 | 한 기준으로 통일 |

## 원문에 없는 해설 (낮음)
- 22 등 FSWOL/MSIP 슬라이드 "케이스마다 새 FE 해석 없이 만들기 위해" — 원문은 "rules based on estimates made from the literature"(p.45).
- 77 "실측으로 이상치를 판정할 절차가 아니라 …가정" — 원문은 "would not be appropriate to reject completely one profile…".
- 85 "군집한 방향으로 더 가깝게 추정하기 위함".

## 오탈자
1 "2026.10.??" / 3 "꼐산"→계산 / 4 "Xlpr"→xLPR / 5 "페쇄"→폐쇄, "nonliner"→nonlinear / 7 "SG노블"→SG노즐, "가저이"→가정이 / 9 "VS Summer"→VC Summer, "공자에서"→공장에서 / 10 "Aooly"→Alloy, "Mpa"→MPa / 12 "맟게"→맞게 / 14 "취함해", "국비"→국부 / 15 "패쇄"→폐쇄 / 17 "transitaion"→transition / 18 "VC Sumer"→Summer, "bridg"→bridge, "pig.26d"→fig.26d, "Tsurga"→Tsuruga, "Accptance"→Acceptance / 19 "overla로"→overlay로, "sugar line"→surge line / 26 "SWOL(WOR)"→FSWOL(WOR) / 47 "baselline" / 13~75 푸터 "MODE LING"→MODELING(62곳) / 76~87 "UNCERATAINTY"→UNCERTAINTY / 82·83 "weighte"→weighted / 86·87 "umique", "applie"→unique, applied / 89 "사관된"→상관된, "분표"→분포 / 97 "맟추려고"→맞추려고 / 기호표 "Mpa"→MPa (76·82·84·86 등).
