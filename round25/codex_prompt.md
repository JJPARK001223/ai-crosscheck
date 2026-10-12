너는 Codex다. 이 repo(J:\Desktop\공학\ai-crosscheck)의 PROBLEM.md에 적힌
"Round 25" 문제를 읽고, round25/claude.md는 절대 열어보지 말고(blind 단계)
독립적으로 작업해라.

## 네트워크 제약 (이미 확인됨)
너의 실행 환경은 외부 네트워크 접근이 차단되어 있다(curl로 google.com 접속
실패 확인됨). 따라서 웹 조사는 하지 말고, 아래 두 가지만 수행해라.

## 작업 1: PDF에서 Abstract 단어수 독립 재계산
대상 PDF 15개: `J:\Desktop\과학논문작성법 과제\*.pdf` (전부 1페이지 상단에
Abstract가 있음).
- `pdftotext.exe` 경로:
  `J:\Desktop\공학\claude_code\tools\poppler\poppler-26.02.0\Library\bin\pdftotext.exe`
- 각 PDF의 1페이지를 텍스트로 추출(`pdftotext.exe -f 1 -l 1 <pdf> -`)하고,
  "Abstract"라는 제목 이후부터 "Keywords"/"1. Introduction" 직전까지의
  본문만 분리해서 단어수를 센다(공백 기준 단어 분리, 숫자·기호 포함해서
  센다).
- 15개 파일 각각의 (파일명, 추출된 Abstract 단어수)를 표로 정리해라.
- 주의: PDF 텍스트 추출은 하이픈 줄바꿈, 특수문자(λ, Nm, % 등) 깨짐이
  있을 수 있다. 깨진 경우 원본 PDF 레이아웃을 참고해서 보정하고, 보정
  내역을 명시해라.

## 작업 2: 11개 저널의 Abstract 단어수 공식 가이드라인 — 학습 지식 기반 회상
웹 조사 없이, 네가 사전학습 과정에서 알고 있는 범위 내에서만 아래 11개
저널의 공식 Abstract 단어수 제한을 안다면 적어라. 모르면 반드시
"모름"이라고 적어라. 추측이면 반드시 "추측(불확실)"이라고 표시해라. 확신이
없는데 숫자만 적는 것은 금지한다.
- Processes (MDPI)
- Case Studies in Thermal Engineering (Elsevier)
- Fuel (Elsevier)
- Energy (Elsevier)
- ACS Omega (ACS)
- International Journal of Engine Research (SAGE)
- Journal of the Energy Institute (Elsevier)
- Journal of Engineering for Gas Turbines and Power (ASME)
- Topics in Catalysis (Springer)
- Combustion and Flame (Elsevier)
- Applied Thermal Engineering (Elsevier)

## 출력
`round25/codex.md`에 한국어로 작업1 표 + 작업2 결과를 작성해라. 추측과
사실을 반드시 구분 표기. 작업이 끝나면 `git add round25/codex.md`,
`git commit`, `git push`까지 직접 실행해라.
