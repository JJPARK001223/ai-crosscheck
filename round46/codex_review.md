# round46 교차검증 — Version 8 반영 결과

검증일: 2026-10-16. 검증자: Codex. 대상 기준 커밋: `8987804286abdb067e071ff8e9514e3f67c221f3`.

## 판정

- 수정 24개 세부 확인점 중 23개는 원문과 일치한다. 나머지 1개(p54)는 `possibly`가 복원됐지만, 새로 보충한 원인 설명에서 극한응력 쪽 대비절이 생략됐다. 경미한 압축 보완을 권고한다. 반대 뜻으로 바뀐 새로운 오역은 확인하지 못했다.
- `class="orig"` 71개 전부를 대조했다(요청한 최소 20개를 초과). 178개 쪽 블록, 중복 제외 PDF 136쪽이다. 표시 범위 안의 빠진 쪽·순서 오류·다른 쪽 혼입·추출 본문 잘림은 없었다.
- 영어 블록은 문자 그대로의 무가공 전문은 아니다. 보고서 머리말 삭제, 공백 정리, 특정 비라틴 문자군의 `⟦수식⟧` 치환을 거쳤다. 이 처리 이외의 차이는 없었다. 수식·그림을 복원한 전문이라는 뜻으로 사용하면 안 된다.

## 자료와 검증 방법

1. 대상: `round46/claude_html_snapshot.html`의 109개 카드. SHA-256: `39c4a4aa8adc2f7209523d83c9f26ea9d82687e6224ea303ff4c950cd65e473d`.
2. 수정 목록: `round46/DECISION.md`의 공통·Claude만·Codex만 항목. 목록이 여러 수정을 한 묶음으로 적었으므로 아래에서는 문장·한정어별로 24개 확인점으로 분리했다. 아래 번호는 DECISION의 원래 이슈 번호가 아니다.
3. 원문: `J:\Desktop\XLPR\xLPR참고문헌\(ML16341B049)Welding residual stresses.pdf`, 187쪽. SHA-256: `0f33ee5838fba78edaef1ca87709a2b1a73d6b454f713749be7e2ba46645ff32`.
4. 보조 원문: `round43/txt/(ML16341B049)Welding residual stresses.txt`의 `=====PAGE n=====`. PDF를 PyMuPDF로 다시 직접 추출했으며, 대조한 136쪽 모두 기존 txt와 공백 정리 후 일치했다.
5. 기존 한국어 문장과의 비교: `round46/html_cards.txt`. p54의 원인 설명은 이 파일에 없고 현재 스냅샷에 보충된 문장임을 확인했다. 다른 AI의 보고서 결론을 검증 근거로 사용하지 않았다.
6. 영어 블록 검증: HTML 엔티티를 복원하고 태그를 제거한 뒤, 쪽별 문자열 전체를 원문과 비교했다. 줄바꿈을 포함한 연속 공백만 한 칸으로 정리했다. 각 블록의 PDF 쪽 번호 열이 summary의 시작–끝 범위와 정확히 일치하는지도 검사했다.
7. 그림 표기 관련 #26은 PDF 84쪽 전체 및 Figure 58 확대 이미지를 직접 확인했다. 이하 PDF 번호는 파일의 1부터 세는 물리 쪽 번호다. 웹 검색이나 외부 자료로 원문을 보충하지 않았다.

## 수정 24개 확인점

| 번호 | 구분 | 카드 | 확인한 현재 반영 | 원문 영어·위치 | 판정 |
|---|---|---|---|---|---|
| 1 | 공통 | p10 | 플랜트당 → SG 한 대마다 DMW 2개 | PDF 29 / 인쇄 14: “there are two nozzle-to-safe end DMWs on each SG” | 일치. SG 한 대가 단위이며 inlet·outlet 각 1개다. |
| 2 | 공통 | p32 | 압력용기 → 가압기(pressurizer) | PDF 67 / 52: “This result was for pressurizer safety and surge line examples but is assumed to apply for hot leg size.” | 일치. 고온관 적용도 가정으로 남겼다. |
| 3 | 공통 | p54 | 극한응력 기반 변동 추정이 더 잘 거동했다고 표현 | PDF 80 / 65: “estimates of material property variation using ultimate stress were much better behaved than those based on yield stress” | 일치. 원문은 변동 추정의 거동을 비교한다. |
| 4 | 공통 | p54 | 가공경화 원인 설명에 possibly 복원 | PDF 80 / 65: “possibly since yield stress values in the statistical database might be affected by work hardening in the tensile specimens used while ultimate stress would not.” | 부분 일치. 추정임은 복원됐지만 “while ultimate stress would not”가 한국어 설명에 없다. 아래 보완 표 참조. |
| 5 | 공통 | p54 | 곡선 개발에 절차를 적용한 뒤 시간 제약으로 더 진행하지 않음 | PDF 80 / 65: “This process was applied to develop material property stress strain curves for all materials presently included”; “due to time constraints … not to pursue this topic at this time.” | 일치. 이미 수행한 곡선 개발과 중단한 후속 진행을 구분했다. 물성 변동이 최종 xLPR 2.0에 미포함이라는 후속 문장도 맞다. |
| 6 | 공통 | p6 | 부분 원주 수리의 시작·종료 위치와 수리부 중앙 결과 가정 | PDF 18–19 / 3–4: “the start stop locations are typically at the same locations at the repair excavation sites”; “at the center point of the repairs, i.e., away from the start/stop.” | 일치. typically 및 시작·종료점에서 떨어진 위치라는 조건을 보존했다. |
| 7 | 공통 | p6 | 열원 기술과 입열·목표 온도 이력을 정밀 규정하지 않은 이유 | PDF 19 / 4: “only weakly sensitive to heat input”; “did not precisely define heat input models or target temperature-time profiles.” | 일치. 선행 연구 [1, 3]에 근거한 설명이고 대류·복사 조건도 맞다. |
| 8 | Claude만 | p15 | 웹포털 제공 예정 시제 | PDF 41 / 26: “These are currently available on Subversion and will be made available from the xLPR web portal” | 일치. 2016년 보고서의 현재/미래 표현을 구분한다. 현시점 실제 접속 여부는 확인 불가라고 명시했다. |
| 9 | Claude만 | p21 | FSWOL·OWOL 두 가지가 WOR 범주 | PDF 60 / 45: “full structural weld overlay (FSWOL) and optimized weld overlay (OWOL) which are grouped in the weld overlay repair (WOR) category” | 일치. MSIP·inlay까지 WOR라고 묶지 않는다. |
| 10 | Claude만 | p55 | 드물었던 이상치 사례라는 한정 | PDF 81 / 66: “For these cases, which were rare, the WRS distributions were weighted to reduce the influence of the outlier” | 일치. 드문 사례에 적용한 조치라는 조건을 복원했다. |
| 11 | Claude만 | p10 | 대표 치수 Figure 5와 모델 형상 Figure 7 구분 | PDF 31 / 16: “A sketch with representative dimensions … is shown in Figure 5.” Figure 7 캡션: “Steam Generator Nozzle Model Configurations” | 일치. 검정·빨강 치수 설명도 해당 원문과 맞다. |
| 12 | Claude만 | p43 | 일반화에 관한 결론을 Claude 해설로 표시 | 현재 문장 앞에 “(Claude 해설, 원문 문장 아님)”이 있다. PDF 73 / 58의 근거 문장은 “Axial WRS always increases at the ID”; “The ID stresses are high (near or above yield)”이다. | 해설 표시 반영 확인. 한국어 일반화 문장 자체는 원문 인용이 아니다. 기초 응력 거동은 원문과 맞다. |
| 13 | Codex만 | p4 | SIS = shop instruction sheet / 공장 작업지시서 | PDF 14 / xiii: “SIS shop instruction sheet”; PDF 29 / 14: “The Shop Instruction Sheet (SIS) … described the general weld process.” | 일치. |
| 14 | Codex만 | p6 | 용융부를 올바르게 모델링하는 것이 각 모델러에게 필수 | PDF 19 / 4: “The key is to model the weld fusion zone correctly, which was required for each modeler.” | 일치. 단순한 권장으로 약화하지 않았다. |
| 15 | Codex만 | p8 | LBB 범위의 후보는 일반적으로 surge line뿐 | PDF 21 / 6: “generally only the surge line would be a candidate for inclusion within the LBB scope.” | 일치. 이미 범위에 포함됐다는 확정 표현이 아니다. |
| 16 | Codex만 | p8 | wrought를 소성가공재로 표현 | PDF 21 / 6: “most WRS analyses to date have assumed wrought stainless steel materials.” | 일치. 주조재와 구분하며 단조재 하나로 한정하지 않는다. |
| 17 | Codex만 | p9 | 인용 쪽 범위 PDF 23–28로 수정 | PDF 23: SG·B&W 선정 설명, 24–25: B&W 설명 계속, 25–28: 업체 자료 및 Figure 4–6. 카드 메타와 orig 모두 23–28이다. | 범위 일치. |
| 18 | Codex만 | p9 | SG 용접은 자주 모델링된 대상이 아니었음 | PDF 23 / 8: “SG welds have not been frequently modeled.” | 일치. 한 번도 해석하지 않았다는 뜻이 아니다. |
| 19 | Codex만 | p18 | 폐쇄 용접의 영향에 probably 복원 | PDF 50 / 35: “probably due to the fact that the stainless steel closure weld is so close to the DMW nozzle weld that it dominates the axial WRS field.” | 일치. 이전 수리 해석과 다른 거동의 원인을 추정으로 표현한다. |
| 20 | Codex만 | p58 | 곱 가중 설명의 단정적 해석 삭제·영어 직접 인용 | PDF 83 / 68: “the resulting spread using the summation approach was slightly larger than using the product”; “the ratio in weight … was less important using the product approach. Therefore, the product procedure was used.” | 일치. 인용은 원문과 맞으며 less important의 수학적 의미를 확정하지 않는다. |
| 21 | Codex만 | p74 | 적분 0 유지 → 0에 가깝게 유지 | PDF 96 / 81: “In order to keep an integral close to zero, these high values at the ID are associated with low values when the WRS becomes negative.” | 일치. 정확히 0이라는 보장으로 바꾸지 않았다. |
| 22 | Codex만 | p74 | 가중 CDF가 초기 분포를 재현하리라는 기대 | PDF 97–98 / 82–83: “with inclusion of the weight for each realization (which should lead to the initial distribution).” | 일치. 재현 완료라는 단정을 제거했다. |
| 23 | Codex만 | p96 | 이하 → 4% 증분 위치보다 작은 쪽의 가장 가까운 점 | PDF 171 / C-4: “the point nearest to the 4% increment value but less than the increment value.” | 일치. less than의 엄격한 부등호 의미를 보존했다. 예시 분석·보간 미사용이라는 조건도 있다. |
| 24 | Codex만 | p109 #26 | 두 그래프에 confidence level: 99.%라고 표기 | PDF 84 / 69 Figure 58의 좌우 그래프 확대 지면에서 둘 다 “confidence level: 99.%” 확인. 같은 쪽 본문은 “99% confidence interval”과 “2.05 × … standard deviation”을 함께 쓴다. | 일치. 그림 문자 표기와 본문 통계 불일치를 구분한다. 정규분포에서 ±2.05σ의 포함률은 약 95.96%다. |

## 새로 보충한 문장에서 확인한 압축

| 카드 id | 현재 HTML 문장 | 원문 영어 | 정정안 | 분류 |
|---|---|---|---|---|
| p54 | “이유는 인장시편의 가공경화가 항복응력에 영향을 줄 수 있기 때문일 ‘possibly’” | PDF 80 / 65: “possibly since yield stress values in the statistical database might be affected by work hardening in the tensile specimens used while ultimate stress would not.” | “통계 DB의 항복응력 값은 사용한 인장시편의 가공경화 영향을 받을 수 있지만 극한응력은 그렇지 않기 때문일 가능성이 있다.” | 경미한 압축. 새 원인 설명에 ultimate stress 쪽 대비가 없다. possibly의 복원 자체는 맞다. |

이 압축은 같은 카드의 orig 영어 블록에는 없다. 영어 원문을 열면 해당 대비절 전체를 읽을 수 있다. 이 점을 새로운 반대 의미의 오역이나 물성 변동 최종 포함 여부 오류로 확대하지 않는다. 지정 수정 및 확인 범위에서 그 밖의 새로운 오역·의미를 바꾸는 압축은 확인하지 못했다.

## orig 대조 결과와 해석상의 한계

쪽 순서 검사는 각 카드의 summary 범위와 `[PDF n / 인쇄 …]` 쪽 구분자를 기준으로 했다. 71개 모두 시작부터 끝까지 연속이고 중복 쪽이 없다. 카드 사이에 같은 PDF 쪽이 반복되는 것은 같은 쪽에 두 주제가 걸치는 경우이며, 해당 쪽의 텍스트 전체가 각각 일치한다.

- **H**: 공백을 정리하고 PDF의 반복 머리말 `xLPR Models Subgroup Report—Welding Residual Stresses`를 제거하면 문자열 전체가 일치. 본문·각주·캡션·추출 가능한 그림 문자는 추가로 삭제되지 않았다.
- **F**: H 처리에 더해 연속 비라틴 문자군 U+0700–U+0FFF를 각각 `⟦수식⟧`로 바꾸면 문자열 전체가 일치. HTML을 재현한 비교 규칙이며, 이 문자군의 모든 문자가 실제 수식인지 의미상 인증한 것은 아니다.
- 178개 쪽 블록 중 H 142개, F 36개. 기존 txt와 PDF 재추출 사이의 불일치 0개. 위 처리로 설명되지 않는 잔여 차이 0개.
- 아래는 추출 텍스트의 **전문 대조** 기록이다. 수식의 시각적 정확성이나 PDF 그림의 모든 문자가 추출됐다는 판정은 아니다. 이미지 안 글자가 원래 추출되지 않으면 orig에도 없으며, 그 완전성은 #26 이외에는 확인 불가다.
- 각 orig 밑의 안내는 “머리말·쪽 번호 제거”라고 하지만 실제로 인쇄 쪽 번호(`1`, `2`, `A-1` 등)는 남아 있다. 예: p5의 PDF 16 블록은 `1 1 INTRODUCTION`으로 시작한다. 자료가 다른 쪽이라는 증거는 아니며, 안내 문구를 “반복 머리말 제거, 줄바꿈 정리, 인쇄 쪽 번호는 일부 남음”으로 정정하는 편이 정확하다.
- “그대로”는 위 전처리 조건을 붙여 이해해야 한다. 제목에 “PDF 추출 텍스트 — 머리말·공백 정리, 수식 문자 치환”이라고 명시하면 실제 처리와 일치한다. 이 표기 보완은 번역 오류와 별개다.

| 카드 | PDF 쪽 범위 | 쪽 순서·누락·혼입 | 전체 텍스트 대조 |
|---|---|---|---|
| p2 | 5 | 이상 없음 | H |
| p5 | 16–17 | 이상 없음 | H |
| p6 | 18–19 | 이상 없음 | H |
| p7 | 19–20 | 이상 없음 | H |
| p8 | 20–22 | 이상 없음 | H |
| p9 | 23–28 | 이상 없음 | H |
| p10 | 29–31 | 이상 없음 | H |
| p11 | 31–34 | 이상 없음 | H |
| p12 | 34–36 | 이상 없음 | H |
| p13 | 36–37 | 이상 없음 | H |
| p14 | 37–39 | 이상 없음 | H |
| p15 | 40–41 | 이상 없음 | H |
| p16 | 42–43 | 이상 없음 | H |
| p17 | 44–46 | 이상 없음 | H |
| p18 | 46–51 | 이상 없음 | H |
| p19 | 51–54 | 이상 없음 | H |
| p20 | 54–59 | 이상 없음 | H |
| p21 | 60 | 이상 없음 | H |
| p22 | 61–63 | 이상 없음 | H |
| p32 | 67–69 | 이상 없음 | H |
| p42 | 71–72 | 이상 없음 | H |
| p43 | 73–78 | 이상 없음 | H |
| p53 | 79 | 이상 없음 | H |
| p54 | 80 | 이상 없음 | H |
| p55 | 81–82 | 이상 없음 | H+F |
| p56 | 82 | 이상 없음 | F |
| p57 | 83 | 이상 없음 | F |
| p58 | 83 | 이상 없음 | F |
| p59 | 83 | 이상 없음 | F |
| p60 | 84 | 이상 없음 | F |
| p61 | 84 | 이상 없음 | F |
| p62 | 84 | 이상 없음 | F |
| p63 | 85 | 이상 없음 | H |
| p64 | 86 | 이상 없음 | F |
| p65 | 86 | 이상 없음 | F |
| p66 | 87 | 이상 없음 | F |
| p67 | 87 | 이상 없음 | F |
| p68 | 88 | 이상 없음 | F |
| p69 | 87–88 | 이상 없음 | F |
| p70 | 88–91 | 이상 없음 | H+F |
| p71 | 91–93 | 이상 없음 | H+F |
| p72 | 94 | 이상 없음 | H |
| p73 | 94–95 | 이상 없음 | H |
| p74 | 95–100 | 이상 없음 | H+F |
| p81 | 130 | 이상 없음 | H |
| p82 | 131 | 이상 없음 | H |
| p84 | 136–138 | 이상 없음 | H |
| p85 | 138–141 | 이상 없음 | H |
| p86 | 141–143 | 이상 없음 | H |
| p87 | 143–146 | 이상 없음 | H |
| p88 | 146–149 | 이상 없음 | H |
| p89 | 149 | 이상 없음 | H |
| p90 | 148–149 | 이상 없음 | H |
| p91 | 150–155 | 이상 없음 | H |
| p92 | 156–159 | 이상 없음 | H |
| p93 | 160–163 | 이상 없음 | H |
| p94 | 164–167 | 이상 없음 | H |
| p95 | 168–169 | 이상 없음 | H |
| p96 | 169–173 | 이상 없음 | H+F |
| p97 | 173 | 이상 없음 | F |
| p98 | 173–178 | 이상 없음 | H+F |
| p99 | 179–180 | 이상 없음 | H |
| p100 | 180–183 | 이상 없음 | H+F |
| p101 | 181 | 이상 없음 | F |
| p102 | 181 | 이상 없음 | F |
| p103 | 182 | 이상 없음 | F |
| p104 | 182 | 이상 없음 | F |
| p105 | 182–183 | 이상 없음 | F |
| p106 | 183–185 | 이상 없음 | H+F |
| p107 | 185–187 | 이상 없음 | F |
| p108 | 186 | 이상 없음 | F |

## 확인 불가·범위 경계

- 109개 카드의 한국어 전 문장을 다시 전수 감사한 것은 아니다. 이번 판정은 지정 수정 24개 확인점과 orig 71개 전체의 원문 대조에 한정한다. 기존 문장 전체의 무오류는 확인 불가다.
- 부록 A PDF 150–155 및 부록 C PDF 181–187도 위 orig 검증에 포함했다. 다만 그 범위의 한국어 해설·수식을 모두 새로 검증한 것은 아니다.
- 브라우저의 펼침·스크롤 동작, 모바일·인쇄 화면에서의 잘림 여부는 확인 불가다. 확인한 잘림 없음은 HTML에 저장된 추출 문자열의 완전성을 뜻한다.
- 원문 웹포털의 현재 접근 가능 여부, 실제 xLPR 실행 구현, less important라는 문구의 정확한 수학적 의도는 확인 불가다. 문서 이상의 뜻을 추정하지 않았다.
- HTML 및 DECISION은 수정하지 않았다. 보고서의 지적 채택과 최종 결정은 사용자에게 남긴다.
