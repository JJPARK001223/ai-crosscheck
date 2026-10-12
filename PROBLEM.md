# Round 25 — SCI 논문 15편 Abstract 분석표의 "저널 가이드라인 부합여부" 검증

## 배경

사용자(박준재, 과학논문작성법 과목 과제: 가솔린 엔진 출력 관련 SCIE 논문
15편의 Abstract 분석)가 Claude에게 Abstract 평가 기준 중 "저널 가이드라인
부합여부" 열을 채워 달라고 요청했다. Claude는 1차로 "공학계열 저널 공통
관행상 약 150~250단어"라는 **단일 추정치**를 15편 전체에 동일하게 적용했고,
이것이 개별 저널의 실제 Guide for Authors를 전수 확인한 것이 아니라는 점을
스스로 고지했다.

사용자가 이를 지적했다: "각 저널의 기준으로 평가기준을 작성해야지, 지금
전체 다 각 저널들의 가이드라인을 따른거야? 다시 확인해봐 혹시 모르니까
codex랑 검증해서 끝나고 알려줘."

## 이번 라운드에서 검증해야 할 것

1. **15편 논문이 게재된 11개 서로 다른 저널 각각의 실제 공식 Author
   Guidelines/Guide for Authors에 Abstract 분량(단어수) 규정이 있는지,
   있다면 정확히 몇 단어인지** 1차 출처(저널 공식 홈페이지)를 찾아 확인한다.
   - Processes (MDPI)
   - Case Studies in Thermal Engineering (Elsevier)
   - Fuel (Elsevier)
   - Energy (Elsevier)
   - ACS Omega (American Chemical Society)
   - International Journal of Engine Research (SAGE)
   - Journal of the Energy Institute (Elsevier)
   - Journal of Engineering for Gas Turbines and Power (ASME)
   - Topics in Catalysis (Springer)
   - Combustion and Flame (Elsevier)
   - Applied Thermal Engineering (Elsevier)
2. **각 논문의 실제 Abstract 단어수가 정확한지** PDF 원문에서 독립적으로
   재검증한다 (이전에 Claude가 수동 전사 후 `wc -w`로 계산한 값:
   No.1=231, No.2=243, No.3=380, No.4=195, No.5=252, No.6=171, No.7=245,
   No.8=174, No.9=235, No.10=204, No.11=208, No.12=220, No.13=220,
   No.14=388, No.15=190 — 이 값이 PDF 원문과 정확히 일치하는지 재확인).
3. 1·2번 결과를 종합해, 15편 각각에 대해 "해당 저널의 실제 규정" 기준으로
   부합/미부합을 다시 판정한다. 저널에 명시적 단어수 규정이 없는 경우
   "규정 없음(상한 미설정)"으로 별도 표기하고, 이전처럼 150~250단어 공통
   추정치를 임의로 적용하지 않는다.

## 참고
- 15편 PDF 원문 위치: `J:\Desktop\과학논문작성법 과제\*.pdf`
- 기존 분석표: `J:\Desktop\과학논문작성법 과제\SCI논문15편_Abstract_분석표.csv`
- 기존 평가기준 문서: `J:\Desktop\과학논문작성법 과제\평가기준_설명.md`
- Codex 실행 환경은 네트워크 접근이 차단되어 있음(확인됨: workspace-write
  샌드박스에서 외부 curl 연결 실패). 따라서 1번(웹 조사)은 Claude가 전담하고,
  Codex는 2번(PDF 원문에서 Abstract 텍스트를 직접 추출해 단어수 독립
  재계산 — `pdftotext.exe` 사용 가능, 경로:
  `J:\Desktop\공학\claude_code\tools\poppler\poppler-26.02.0\Library\bin\pdftotext.exe`)을
  담당한다. Claude가 찾은 저널별 규정 숫자를 Codex에게 전달한 후
  3번(판정)을 Codex가 독립적으로 재계산해 Claude의 판정과 대조한다.

## 출력
`round25/claude.md`, `round25/codex.md`에 각자 조사/계산 결과를 근거(출처
URL, 추출 텍스트 등)와 함께 작성. 추측 금지, 확인된 것만 기술. 작업 끝나면
git add, commit, push까지.
