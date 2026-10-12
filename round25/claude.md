# Round 25 — Claude 블라인드 조사: 저널별 Abstract 단어수 가이드라인 실제 검증

## 결론 먼저

**이전 분석(150~250단어 공통 추정치 적용)은 부정확했다.** 15편이 게재된
11개 서로 다른 저널 중, 공식 1차 출처(저널/출판사 자체 페이지)에서 숫자를
직접 확인한 곳은 **2곳뿐**이다(ASME, Springer Nature 일괄정책). 나머지는
출판사 사이트가 자동화 접근을 차단(HTTP 403)해 1차 출처를 직접 열람하지
못했고, 2차 출처(aggregator)만으로는 신뢰도가 낮아 "확인 불가"로 남긴다.
즉, 사용자가 지적한 대로 "전체 다 각 저널 가이드라인을 따른 것"이 아니었고,
재조사 후에도 11개 중 9개는 여전히 저널별 정확한 숫자를 1차 출처로
확인하지 못했다.

## 조사 방법 및 한계

- WebSearch + WebFetch로 각 저널의 공식 "Guide for Authors" / "Author
  Guidelines" 페이지를 직접 열람 시도.
- **Elsevier(sciencedirect.com, elsevier.com)와 MDPI, ACS(pubs.acs.org,
  publish.acs.org)는 자동화 접근을 차단함** — WebFetch 시 전부 HTTP 403
  또는 빈 콘텐츠(JS 렌더링) 반환. 직접 확인 불가.
- web.archive.org(Wayback Machine)도 이 세션에서는 fetch 자체가 차단됨.
- 따라서 아래 표에서 "확인 불가"로 표시한 저널은 **1차 출처를 직접 읽지
  못했다는 뜻**이며, 과거처럼 임의 추정치를 적용하지 않는다.

## 저널별 조사 결과

| 저널 | 출판사 | 확인된 숫자 | 신뢰도 | 출처 |
|---|---|---|---|---|
| Journal of Engineering for Gas Turbines and Power | ASME | **250단어 이내** | **높음(1차 출처 직접 확인)** | asme.org 공식 "Writing a Research Paper or Technical Brief" 페이지 원문: "An abstract (250 words maximum) should open the paper or brief." — ASME 저널 전체 공통 지침 |
| Topics in Catalysis | Springer Nature | **350단어 이내** | 중간(Springer Nature 전사 공통 정책 확인, Topics in Catalysis 저널 전용 페이지는 로그인 장벽으로 열람 불가) | support.springernature.com 공식 FAQ 원문: "the abstract of the manuscript should not exceed 350 words" |
| Processes | MDPI | 약 200단어 (추정) | **낮음(1차 출처 미확인, mdpi.com 403)** | 2차 출처(aggregator) 복수가 "MDPI 전체 공통 약 200단어"라고 보고하나, Processes 저널 페이지 자체는 직접 열람하지 못함 |
| Fuel | Elsevier | 약 200단어 (추정) | **낮음(1차 출처 미확인, sciencedirect.com 403)** | 2차 출처(manusights.com, 2026-06-18 갱신)만 확인. "2025년 Fuel 저자 가이드라인 기반"이라 주장하나 원문 대조 불가 |
| Energy | Elsevier | 약 200단어 (추정) | **낮음(1차 출처 미확인, sciencedirect.com 403)** | 2차 출처(manusights.com)만 확인, 원문 대조 불가 |
| ACS Omega | ACS | **불명(상충)** | **확인 불가** | 한 2차 출처는 "단어수 제한 없음(no abstract word limit)", 다른 2차 출처는 "150~250단어"라고 상충되게 보고. 공식 페이지(publish.acs.org)는 JS 렌더링이라 내용 비어있음. **판정 보류 권고** |
| International Journal of Engine Research | SAGE | 확인 불가 | - | journals.sagepub.com 공식 author-instructions 페이지를 특정하지 못함(IJER 저널코드 불명), 검색으로도 숫자 발견 못함 |
| Journal of the Energy Institute | Elsevier | 확인 불가 | - | sciencedirect.com 403으로 미확인, 검색으로도 숫자 발견 못함 |
| Case Studies in Thermal Engineering | Elsevier | 확인 불가 | - | sciencedirect.com 403. 검색에서는 "원고는 5페이지 이내"라는 분량 제한만 발견, 초록 단어수는 불명 |
| Applied Thermal Engineering | Elsevier | 확인 불가 | - | sciencedirect.com 403으로 미확인, 검색으로도 숫자 발견 못함 |
| Combustion and Flame | Elsevier | 확인 불가 | - | sciencedirect.com 403. 검색 결과는 "Combustion Institute Proceedings"(별개 간행물)의 지침과 혼동되는 자료만 발견, Combustion and Flame 저널 자체 수치는 불명 |

## 15편 논문에 이를 적용한 재판정 (1차 출처로 확인된 것만 숫자 적용)

| No | 저널 | Abstract 단어수(Claude 전사 기준) | 적용 가능한 공식 기준 | 판정 |
|---|---|---|---|---|
| 1 | Processes | 231 | 확인 불가(200단어는 미검증 추정) | **판정 보류** |
| 2 | Case Studies in Thermal Engineering | 243 | 확인 불가 | **판정 보류** |
| 3 | Fuel | 380 | 확인 불가(200단어는 미검증 추정) | **판정 보류** (단, 380단어는 어떤 추정치를 적용해도 과다할 가능성이 높음 — 보수적으로만 언급) |
| 4 | Energy | 195 | 확인 불가 | **판정 보류** |
| 5 | Fuel | 252 | 확인 불가 | **판정 보류** |
| 6 | ACS Omega | 171 | 확인 불가(상충) | **판정 보류** |
| 7 | International Journal of Engine Research | 245 | 확인 불가 | **판정 보류** |
| 8 | Energy | 174 | 확인 불가 | **판정 보류** |
| 9 | Journal of the Energy Institute | 235 | 확인 불가 | **판정 보류** |
| 10 | Fuel | 204 | 확인 불가 | **판정 보류** |
| 11 | Journal of Engineering for Gas Turbines and Power | 208 | **250단어(1차 확인)** | **부합** |
| 12 | Topics in Catalysis | 220 | **350단어(Springer Nature 공통정책, 1차 확인)** | **부합** |
| 13 | Energy | 220 | 확인 불가 | **판정 보류** |
| 14 | Combustion and Flame | 388 | 확인 불가 | **판정 보류** |
| 15 | Applied Thermal Engineering | 190 | 확인 불가 | **판정 보류** |

## Codex에게 요청하는 것 (네트워크 차단 확인됨 — codex exec workspace-write 샌드박스에서
외부 curl 연결 실패를 직접 테스트로 확인함)

Codex는 웹 조사를 할 수 없으므로, 대신:
1. `pdftotext.exe`(경로:
   `J:\Desktop\공학\claude_code\tools\poppler\poppler-26.02.0\Library\bin\pdftotext.exe`)로
   `J:\Desktop\과학논문작성법 과제\*.pdf` 15개 파일의 1페이지를 텍스트로
   추출하고, 각 논문의 Abstract 단락만 분리해서 단어수를 독립적으로
   재계산한다(Claude의 수동 전사값과 비교하기 위함 — Codex는 Claude의 숫자를
   보지 않은 상태에서 계산할 것).
2. 위 표에서 Claude가 "확인 불가"로 남긴 9개 저널에 대해, Codex가 가진
   학습 지식 중 **확실히 기억하는 공식 수치가 있다면** 그것도 보고한다(단,
   추측이면 반드시 "추측"이라고 명시할 것 — 사용자가 추측성 정보에 민감함).
