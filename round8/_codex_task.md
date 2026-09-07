# Codex 검증 과업 — Round 8

## 배경
Claude가 `round8/이론흐름_발표목차.html` 초안을 만들었다(선행연구 1·3 이론의 시간 흐름 정리 + 발표자료 목차).
너는 이 초안을 **원 PDF·번역본·기존 DECISION에 직접 대조**하여 blind 검증한다. Claude의 판단을 신뢰하지 말고 1차 자료로 확인할 것.

## 읽을 자료
- 검증 대상: `round8/이론흐름_발표목차.html`, `round8/PROBLEM.md`
- 원 PDF: `J:\Desktop\선행연구 관련\` — 특히
  - `pvt_143_06_064503.pdf` 또는 선1 번역본 (Kwon 2021, 선행연구 1)
  - `pvt_144_05_051506.pdf` (Kwon·Diaz-Colon·DeFisher 2022, "선행연구 2")
  - `polymers-14-02481.pdf` (Kwon 2022 Polymers)
  - `1-s2.0-S...` Irwin 1957, Sapora 2018 등
- 번역본: `J:\Desktop\공학\claude_code\2026_09_01_선행연구분석\선행연구{1,3}_원문번역_영한대역_*.html`
- 기존 판정: `DISCUSSION.md`, `DECISION_round1_수식검증.md`, `DECISION_round3_*` (round3 폴더), `DECISION_round7_참고문헌읽기자료검증.md`
- `session_context.md`: `J:\Desktop\공학\claude_code\메모리\session_context.md`

## 검증 항목 (PROBLEM.md §Codex 검증 요청 A~E)
A. **계보/연대**: 논문 4편 시간 순서, 인용번호 매핑([34]=선1, [35]=선2 PVT144, [36]=Polymers, [37]=Schmeier 2023 ≠ Kwon 계보), 각 논문이 *새로 더한 것*의 서술이 원 PDF와 맞는가. 특히 선2(PVT144)에서 "σ ∝ R^{-1/3}" 관계와 κ_fail 표기가 실제 그 논문에 있는가. Polymers가 κ_fail = K_Ic²/(2πE)를 식으로 명시하는가.
B. **기호 유래**: σ_l/σ_e, σ_f, w_f/κ_fail/Y, s, E, K/K_I/K_IC, G 의 정의·단위·출처 설명 정확성. w_f=κ_fail=Y 가 같은 물리량이라는 주장.
C. **식 재검토**: 선1 식(1)~(7), 선3 식(1)~(4) 유도 재확인(2π 상쇄, r/s 소거). 초안에 새 수식 오류 없는가. "Y=G_c/2π(평면응력)" 및 "예측 시 상쇄되어 무해" 서술의 정확성.
D. **목차 설명 노트**: (2-2) 응력구배조건 설명, (3-1) "노치" 정의, (4-1) "왜 시멘트 페이스트 예제인가" 5개 근거 — 원문·기존 DECISION과 정합하는가. 과장·비약·근거 없는 단정 없는가. 특히 "치수효과를 설명하는지 본다"가 Kwon 논문의 실제 서술인지 아니면 Claude의 해석인지.
E. **SVG/그림 캡션**의 물리 서술 오류. 표 1·2 의 분류 오류.

## 출력
`round8/codex.md` 에:
1. 전체 판정 (이상 없음 / 부분 정정 필요 / 중대 오류)
2. 항목별(A~E) 확인 결과 — "원문 p.○ 에서 확인" 식으로 근거 명시
3. 정정 필요 목록 — 번호, 무엇을, 무슨 근거로
4. 판정 보류/불가 항목

## Git
작업 후:
```
cd "J:/Desktop/공학/ai-crosscheck"
git add round8/codex.md
git commit -m "round8: Codex blind 검증 (이론 흐름 + 발표 목차)"
git push
```
push 실패 시(`.git/index.lock` 등) 커밋만 하고 그 사실을 codex.md 끝에 적을 것. Claude가 수동 push 한다.
