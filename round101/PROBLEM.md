# round101 — 신규 발표자료(paper_review_presentation_revised.html) 교차검증

## 배경

사용자 요청에 따라 기존 발표자료(`paper_review_project/html_presentation/paper_review_presentation.html`,
30페이지)를 PPT 원본 양식(`J:\Desktop\세미나 양식 (2025년 9월 기준).pptx`)에 맞춰 전면 재구성한
신규 파일 `paper_review_presentation_revised.html`(24페이지)을 제작했다. 기존 평가 결과·교차검증
기록(round85~100)은 그대로 유지하고, 발표 순서·설명 방식·표·디자인만 재구성했다. 기존 HTML 파일은
수정하지 않았다(별도 파일로 신규 제작).

## 최종 발표 순서 (고정)

1 표지 · 2 Contents · 3~4 평가기준(1~2) · 5~7 전체논문평가(1~3, No1-5/6-10/11-15) ·
8~15 Best Paper(소개·선정이유·Title/Authors·Abstract·Introduction·Methodology·Results·종합) ·
16~23 Worst Paper(동일 구조) · 24 질의응답(Q&A, 마지막 슬라이드).

## 원본 자료 (읽기 전용)

- 15편 PDF, 기존 CSV: `J:\Desktop\수업과제\과학논문작성법 과제\`
- 확정 등급 기록(round85~100 전부 반영된 최신본): `J:\Desktop\공학\ai-crosscheck\round85\input\evaluation_data.md`
- Title/Authors 점수 원본: `SCI논문15편_Title_Authors_분석표.csv`
- 15편 전체 집계·최신 등급: `round101/input/paper_list.csv` (source_inventory 사본, No.1 재심·No.11 Worst 확정 반영됨)
- 정식 논문 제목 대응표: `round101/input/paper_titles_full.md`
- 검증 대상 HTML: `round101/input/paper_review_presentation_revised.html`
- PPT 디자인 참조: `J:\Desktop\세미나 양식 (2025년 9월 기준).pptx`(python-pptx로 이미 확인된 치수: 4:3,
  제목 placeholder 상단 얇은 띠, 하단 "[n] Reference"+쪽번호, 감사합니다 슬라이드 44pt+20pt 등)

## 검증 항목 (전부 확인, 사용자가 명시한 15개 항목)

1. 전체 15편 논문 목록 정확성(번호·제목·저자·저널·연도)
2. 기존 평가 기준(Title/Authors 10점제 9항목, Abstract~Results 상/중/하 2축) 적용이 정확한가
3. 평가표의 각 항목별 점수·등급이 `evaluation_data.md`/`paper_list.csv`와 정확히 일치하는가
4. 평가표가 5편씩 정확히 3페이지(No.1-5/6-10/11-15)로 구성됐는가, 15편 누락·중복 없는가
5. Best Paper(No.5) 선정 근거가 원문과 일치하고 타당한가
6. Worst Paper(No.11) 선정 근거가 원문과 일치하고 타당한가(신규 동점해소 규칙 포함)
7. No.1 재심 결과(Introduction 구체성 하→중, 연관성 하→상)가 정확히 반영됐는가
8. 기존 동점해소 규칙("하 최다, 동률 시 상이 적은 쪽")이 올바르게 적용·설명됐는가
9. 논문 원문과 평가 의견(8-part: 평가기준/기존평가결과/실제확인내용/우수한점/부족한점/가점감점사유/원문근거/종합평가 또는 개선방향)이 일치하는가
10. 연료 종류에 대한 평가 편향이 없는가
11. AI 번역체 및 오탈자 여부
12. PPT 원본 디자인(4:3, 표지, 제목 위치·글꼴, 본문 글꼴, 배경·색상, 표 형태, 하단 Reference, 페이지 번호, 마지막 슬라이드) 반영 여부
13. HTML 슬라이드 기능(이전/다음, 키보드, 전체화면, 페이지 번호)
14. 표·글자·내용 잘림 여부, 불필요한 스크롤 여부
15. 발표 목차(Contents)와 실제 슬라이드 순서 일치 여부

## 결과 파일

`round101/codex.md`에 작성. 문제를 발견하면 구체적으로(어느 슬라이드의 어느 문장, 원문의 어느 페이지와
비교해 무엇이 다른지) 적을 것. 끝나면 `round101/codex.md`만 git add/commit/push 하고 원격 반영까지
확인하라. 다른 파일은 건드리지 마라.
