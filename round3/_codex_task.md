# Codex 작업 지시 (blind)

[CROSSCHECK_WORKER] 이 파일과 `PROBLEM.md` 만 근거로 독립 조사를 수행한다.

## 하지 말 것
- `round3/claude.md` 를 열거나 읽지 말 것 (blind 검증).

## 할 일
`PROBLEM.md`에 적힌 후보 방법론들(J-적분/HRR장, 국소접근법 Weibull stress/RKR,
GTN/Johnson-Cook 손상모델, EWF, CZM, 기타)을 독립적으로 조사한다. 웹 접근이
가능하면 직접 검색해서 서지사항·핵심 내용을 확인하고, 접근이 안 되면 "확인
불가"라고 명확히 밝힐 것 (추측·창작 금지).

각 방법론에 대해:
1. 핵심 아이디어 1~2문장
2. 대표 문헌(저자, 연도, 저널) — 실제 존재 확인된 것만
3. Kwon 등 논문의 "응력(σ_l) + 응력구배(dσ_l/ds) 결합 조건" 구조와 결합
   가능성 — 높음/중간/낮음 + 이유
4. 필요한 실험 데이터 종류

특히 중점적으로 확인할 것:
- "Theory of Critical Distances"(Taylor 등)라는 프레임워크가 실제로 존재하며,
  균열/노치 문제에서 "임계거리(critical distance)" 개념으로 응력 특이장을
  다루는지, 그리고 연성 균열 성장(ductile growing crack)에도 적용된 사례가
  문헌에 있는지.
- RKR(Ritchie-Knott-Rice, 1973) 모델이 실제로 존재하며, 강(steel)의 벽개파괴를
  "탄소성 균열끝단 응력장 + 임계거리" 조합으로 설명하는지 (서지사항: J. Mech.
  Phys. Solids 21(6), 395-410, 1973로 알려져 있음 — 직접 확인할 것).

## 결과물
마지막에 "지도교수 면담 전 학생이 검토할 후보 3개"를 근거와 함께 추천.

결과를 `round3/codex.md` 에 **한국어로** 작성한다.

완료 후: `git add round3/codex.md` → `git commit -m "round3: Codex blind verification"`
→ `git push origin main`. `AGENTS.md` 규칙을 따른다.
