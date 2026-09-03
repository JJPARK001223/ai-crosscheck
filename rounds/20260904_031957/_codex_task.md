# Codex 작업 지시 (blind)

[CROSSCHECK_WORKER] 이 파일과 PROBLEM.md 만 근거로 독립 검증을 수행한다.

## 하지 말 것
- `round1/claude.md` 를 열거나 읽지 말 것 (blind 검증).

## 할 일
1. `PROBLEM.md` 를 읽는다. 선행연구 1(Kwon 2021, J. Pressure Vessel Technol.
   143, 064503, 3쪽)과 선행연구 3(Kwon·Markoff·DeFisher 2024, Materials 17, 569,
   19쪽)의 수식 유도 7개 항목이 적혀 있다.
2. 원문 PDF 를 직접 열어 식을 확인한다. 경로는 PROBLEM.md 안에 있다.
   - 선행연구 1: `J:\Desktop\선행연구 관련\[선행연구 1] Revisintg Failure of Brittle Materials (2021-12).pdf`
   - 선행연구 3: `J:\Desktop\선행연구 관련\[선행연구 3] Unified Failure Criterion Based on Stress ans Stress Gradient Conditions (2024-01).pdf`
   - 선행연구 3 페이지 이미지: `J:\Desktop\공학\claude_code\2026_09_01_선행연구분석\images\paper3_page-01.png` ~ `paper3_page-19.png`
3. 7개 항목 **각각**에 대해 손으로 미분·대입하여 유도를 검증한다.
   대수 스텝을 전부 보이고, "유도 맞음" 또는 "어디가 느슨/틀림"을 명시한다.
   특히 항목 6(선행연구 3의 Y = K²/E 와 "임계 에너지방출률 동등" 주장, 선행연구 1의
   w_f = K²/(2πE) 와의 2π 차이)을 집중 분석한다.
4. 결과를 `round1/codex.md` 에 **한국어로** 작성한다. 결론만이 아니라 스텝을 보인다.
5. 완료 후: `git add round1/codex.md` → `git commit -m "round1: Codex blind verification"` → `git push origin main`
6. `AGENTS.md` 규칙을 따른다.
