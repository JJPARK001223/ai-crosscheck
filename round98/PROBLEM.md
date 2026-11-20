# round98 — 과학논문작성법 과제: Best/Worst 논문 선정 및 상세분석 교차검증

## 배경

사용자는 가솔린 엔진 SCI(E) 논문 15편(기존 평가 완료, round85~88에서 확정)을 대상으로 Best Paper 1편과
Worst Paper 1편을 선정하고, 두 논문의 평가 항목별 상세분석(Title/Authors, Abstract, Introduction,
Methodology, Results)을 Claude Code가 작성했다. Codex는 독립 검증자로서 다음을 확인한다.

## 원본 자료 위치 (읽기 전용)

- 15편 원본 PDF, 기존 평가표(CSV), 기존 종합 HTML: `J:\Desktop\수업과제\과학논문작성법 과제\`
- 15편 Introduction/Methodology/Results 상/중/하 등급 확정본(round85~88 교차검증 완료):
  `J:\Desktop\공학\ai-crosscheck\round85\input\evaluation_data.md`
- No.5(Best 후보) 원본 PDF: `J:\Desktop\수업과제\과학논문작성법 과제\Effect of the use of methanol, toluene and nitromethane mixtures as fuel additives in a gasoline engine on engine performance and exhaust emissions.pdf`
- No.1(Worst 후보) 원본 PDF: `J:\Desktop\수업과제\과학논문작성법 과제\A Comparison of Ethanol, Methanol, and Butanol Blending with Gasoline and Its Effect on Engine Performance and Emissions Using Engine Simulation.pdf`

## Claude의 1차 산출물 (round98/input/, 검증 대상)

- `paper_list.csv` — 15편 전체 내용평가 8축(상/중/하) 집계 + Title/Authors 총점(10점제)
- `evaluation_criteria.md` — 기존 평가기준 조사 및 "두 척도(숫자점수/범주형)를 합산하지 않는다"는 비교가능성 판단
- `best_paper_analysis.md` — No.5 Title/Abstract/Introduction/Methodology/Results/Conclusion 상세분석
- `worst_paper_analysis.md` — No.1 동일 구조 상세분석 (**0번 항목에 Claude가 스스로 발견한 불일치 포함**:
  evaluation_data.md의 No.1 Introduction 구체성="하" 등급 근거 문구 "선행연구의 정량적 결과 인용은 거의 없음"이
  원문과 완전히 일치하지는 않는다는 지적 — 원문 4~5쪽에 "29%", "42%", "25%–45%", "13%", "15%", "10.6%", "9.8%"
  수치를 포함한 선행연구 인용 3건이 존재함)
- `comparative_analysis.md` — No.5 vs No.1 항목별 비교
- `evidence_matrix.csv` — 위 분석의 원문 근거(페이지/절 번호) 정리

## 검증 항목 (전부 확인)

1. **Best/Worst 선정 근거 검증**: `paper_list.csv`의 15편 내용평가 8축 집계(상/중/하 개수)가 evaluation_data.md
   원본과 정확히 일치하는가? No.5·No.3·No.15가 8/8 상으로 동점이고, Abstract IMRaD 완결성에서 No.5만 "완전"
   이라 Best로 선정했다는 논리가 타당한가? No.1이 "하" 3개로 최다라 Worst로 선정됐다는 논리가 타당한가?
   (round85~88 확정본을 다시 뒤집지 않되, 집계·선정 논리 자체의 정합성만 검증)
2. **연료/엔진 종류 배제 원칙 준수 검증**: 사용자 지시("연료의 종류는 선정과 점수에서 완전히 제외한다")에 따라
   No.13·14·15(디젤·수소 엔진)가 후보에서 배제되지 않고 동일 기준으로 평가되었는가? 기존 9개 Title/Authors
   세부항목과 8개 내용평가 항목 중 실제로 연료 종류를 가점·감점 요인으로 쓰는 항목이 있는지 직접 재확인하라.
3. **원문 대조 검증 (가장 중요)**: `best_paper_analysis.md`와 `worst_paper_analysis.md`에 인용된 모든 직접
   인용문·페이지 번호·수치가 실제 원본 PDF와 정확히 일치하는지 두 PDF를 직접 열어 전수 대조하라.
4. **No.1 Introduction 불일치 재검증 (핵심 쟁점)**: `worst_paper_analysis.md` 0번 항목에서 Claude가 제기한
   의문 — "evaluation_data.md의 '선행연구의 정량적 결과 인용은 거의 없음'이라는 근거 문구가 원문과 정확히
   일치하는가?"를 원문을 직접 읽고 독립적으로 재검증하라. 실제로 수치를 포함한 선행연구 인용이 몇 건인지
   직접 세고, 이것이 "거의 없음"이라는 표현이 타당한지, 아니면 수정이 필요한지에 대한 독립적 판단을 제시하라.
   (주의: round85~88에서 이미 여러 차례 교차검증된 기존 등급 자체(하)를 뒤집으라는 요청이 아니다. 근거 문구의
   정확성만 판단하면 된다.)
5. **비교 가능성 판단 검증**: `evaluation_criteria.md`의 "Title/Authors 숫자점수와 내용평가 범주형 등급을
   합산하지 않는다"는 판단이 타당한지, 더 나은 비교 방법이 있는지 의견을 제시하라.
6. **AI 번역체 여부**: `best_paper_analysis.md`, `worst_paper_analysis.md`, `comparative_analysis.md`에
   "학술적 완성도를 제고한다", "다각적인 관점에서 고찰한다" 같은 어색한 번역체 표현이 있는지 확인하라.

## 결과 파일

`round98/codex.md`에 위 6개 항목 검증 결과를 작성하라. 형식은 자유. 문제를 발견하면 구체적으로
(어느 파일의 어느 문장, 원문의 어느 페이지와 비교해 무엇이 다른지) 적을 것. 끝나면 `round98/codex.md`만
git add/commit/push 하고 원격 반영까지 확인하라. 다른 파일은 건드리지 마라.
