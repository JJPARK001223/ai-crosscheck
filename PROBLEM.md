# Round 28 — EPRI "Crack Growth and Coalescence" 수식 정리 블라인드 교차검증

## 대상 문서 (이 문서 한 편만 사용)
`J:\Desktop\XLPR\xLPR참고문헌\(ML16341B051)Crack growth and coalescence.pdf`
EPRI, xLPR Models Subgroup Report — Crack Growth and Coalescence, xLPR-MSGR-CGR Ver.1.0 (2016), 126쪽.
(원문 인쇄 쪽번호 = PDF 쪽번호 − 1)

## 사용자 요청 (박준재)
1. crack growth 장의 각 조건(재료/메커니즘)마다 이 수식을 왜 쓰고 어떤 식으로 썼는지 정리
2. 각 수식의 의미와 하첨자 정리
3. 어느 상황일 때 어떤 수식을 넣어 쓰는지(적용 조건) 정리
4. 원문에 나온 순서대로 정리
5. 이 논문에 나온 내용만 사용 (외부 지식 추가 금지)
6. 누가 봐도 5초 안에 이해되게 (식마다 한 줄 요약)

## 범위
수식 번호가 붙은 식 전부 (§2.2 PWSCC, §2.3 피로, §2.4 시간적분, §3.2.1.3 모듈 식, §6.2 개정식)와
§4 합체 모델의 규칙. 수식은 원문 그대로(상수, 지수, 부등호 조건 포함) 옮기고,
의미·왜 쓰나·언제 쓰나·하첨자 풀이·대표 값을 각 식별로 표기한다.

## 저작권 주의
원문 문장을 길게 베끼지 말고 자기 말로 쓴다. 수식과 수치는 그대로 옮겨도 된다.

## 블라인드 규칙
Claude와 Codex는 서로의 결과를 보지 않는다. Codex는 `XLPR_균열성장_수식정리.html`,
`J:\Desktop\XLPR\2026_10_13_XLPR모델분석\교차검증\`, 다른 라운드의 claude 파일을 읽지 않는다.

## 산출물
- `round28/claude.md` (Claude), `round28/codex.md` (Codex), `round28/codex_review.md`, `DECISION.md` (Claude 최종)
