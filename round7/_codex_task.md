[CROSSCHECK_WORKER] Round 7 — 선행연구 1·3 참고문헌 + 윤석준 세미나자료 한국어 읽기자료 blind 검증

역할: 너는 교차검증 작업자다. Claude 의 초안(`round7/읽기자료_참고문헌_윤석준.html`)을 원 PDF 및 기존 확정 지식과 대조해 검증한다.

절대 규칙:
- Claude 의 다른 파일(claude.md 류)은 없다. 초안 HTML 자체가 검증 대상이다.
- 원 PDF 는 `J:\Desktop\선행연구 관련\` 폴더에 있다. 직접 열어 대조하라(pdftotext, 또는 가능한 도구).
  - Irwin_1957_Analysis_of_Stresses_and_Strains.pdf
  - Fatigue Fract...2018 - Sapora...circular hole.pdf
  - Fatigue Fract...2020 - Braun...notched.pdf
  - Strain - 2007 - Daniel - Failure of Composite Materials.pdf
  - podgórski-1985-general-failure-criterion-for-isotropic-media.pdf
  - 1-s2.0-S0013794415000661-main.pdf  (Han 2015)
  - 1-s2.0-S1359835X12000978-main.pdf  (Camanho 2012)
  - pvt_144_05_051506.pdf  (Kwon et al. 2022, PVT 144)
  - polymers-14-02481.pdf  (Kwon 2022, Polymers 14)
  - 20240122_윤석준_Displacement-controlled stress intensity factor solution 진행상황.pdf
  - 20250912_윤석준_[Speciment level] Compact tension test #3.pdf
- 선행연구 1·3 원문 번역: `J:\Desktop\공학\claude_code\2026_09_01_선행연구분석\선행연구1_원문번역_영한대역_*.html` 및 `선행연구3_원문번역_영한대역_*.html`
- 기존 확정: `J:\Desktop\공학\ai-crosscheck\DECISION_round1_*.md ~ DECISION_round6_*.md`, `DISCUSSION.md`

검증 항목: `round7/PROBLEM.md` 의 1~8 항목을 그대로 따른다.
1. 논문 식별(저자·연도·저널·권·페이지·제목·DOI, 선1/선3 참고문헌 번호 매핑)
2. 내용 충실도(초록·방법·핵심식·결론 대조, 왜곡·과장·창작·누락)
3. 수식 정확성(PROBLEM.md 3번 목록의 각 식을 원문과 대조)
4. 시각화 정확성(SVG 그림들의 물리적 타당성)
5. 선1·선3와의 연결 정확성(각 문헌의 역할 서술)
6. 윤석준 자료 취급(참고문헌 아님 명시, 별도 챕터, 미완성 연구 전달)
7. round1~6 정합성(2π, w_f=재료상수, FE 방법)
8. 읽기자료 완성도

출력: `J:\Desktop\공학\ai-crosscheck\round7\codex.md` 에 항목별 판정(정확 / 부분 정정 필요 / 틀림 / 확인 불가) + 근거(원문 페이지·문장) + 구체적 수정 지점(챕터 번호·문단). 한국어로.

작성 후 커밋:
  cd "J:\Desktop\공학\ai-crosscheck"
  rm -f .git/index.lock
  git add round7/codex.md
  git commit -m "round7: Codex blind 검증 (참고문헌+윤석준 읽기자료)"
  git push origin main
푸시가 권한 문제로 실패하면 커밋까지만 하고 종료하라(Claude 가 이어받는다).
