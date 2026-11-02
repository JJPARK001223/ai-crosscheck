# round88 — 최종 3자 대조: 중간평가.pptx ↔ evaluation_data.md ↔ HTML 보고서

## 배경
- `round87`에서 `중간평가.pptx`의 15편 평가표를 `evaluation_data.md`와 대조해 2건의 실제 오류(E4, E5)를 찾아 수정했다.
- 그 후 사용자 요청으로 `Abstact`→`Abstract`(15곳), No.1 "3중"→"3종"(2곳), No.2 Abstract "COV 33% ~ 32%"→"COV ~33%·~32%"
  표기를 전부 통일했고, 제목 폰트(18pt), 표지 이름/날짜(박준재, 2026.11.02)도 수정했다.
- 같은 `evaluation_data.md`를 기반으로 별도 산출물인 HTML 보고서(`SCI논문15편_교차검증_종합보고서.html`, Artifact)의
  PART 1(논문별 평가표)도 만들어져 있다.

**이번 라운드의 목적**: pptx(최종본)·HTML 보고서·evaluation_data.md(원 정답) 세 가지가 전부 "15편 × 4섹션 × 2기준 = 120개
등급과 그 근거"에서 서로 어긋나지 않는지 최종 확인한다. 등급 자체를 재평가하지 않는다.

## 입력 자료 (고정)
- `round88/input/evaluation_data.md` — round85 확정 정답(변경 없음, round87과 동일 파일).
- `round88/input/pptx_text_final.md` — 모든 수정이 끝난 현재 `중간평가.pptx`를 python-pptx로 추출한 전체 텍스트.
- `round88/input/html_tables.md` — HTML 보고서 PART 1(15편 평가표)에서 등급·근거만 추출한 텍스트.

## 검사 항목
1. **3자 등급 일치**: 120개 등급(상/중/하)이 evaluation_data.md·pptx·HTML 세 곳 모두에서 동일한가.
2. **pptx 자체의 최근 수정 반영 확인**: `Abstact`가 전부 `Abstract`로 바뀌었는지(15곳), No.1 "3중"이 "3종"으로
   바뀌었는지(2곳), No.2 Abstract가 "COV ~33%·~32%" 형태인지, round87에서 고친 E4(No.3 Introduction 연관성)·
   E5(No.8 Abstract "CO 2.24ppm") 문구가 그대로 남아있는지.
3. **HTML과 pptx 간 근거 문장 차이**: 두 산출물의 설명 문장이 서로 다른 경우(둘 다 정답과 모순되지 않더라도) 목록화.
   어느 쪽이 더 정답에 충실한지도 표시.
4. **표지 정보**: pptx 슬라이드1의 이름·날짜가 정상적으로 들어있는지(플레이스홀더로 되돌아가지 않았는지).
5. **구조 무결성**: pptx가 20슬라이드(표지1+목차3+15편+마무리1) 구조를 유지하는지, 깨진 문자가 없는지.

## 절차
1. Claude가 `round88/claude.md`에 독립적으로 1~5 전부 확인해 작성(Codex 결과를 보기 전).
2. Codex가 `round88/codex.md`에 블라인드로 동일 검증.
3. Claude가 `round88/claude_review.md`에서 codex.md를 재검증.
4. 필요하면 pptx를 추가 수정하고 `DECISION_round88.md`에 최종 결론 기록.
