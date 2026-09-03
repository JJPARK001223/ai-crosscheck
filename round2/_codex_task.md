# Codex 작업 지시 (blind)

[CROSSCHECK_WORKER] 이 파일과 `PROBLEM.md` 만 근거로 독립 검증을 수행한다.

## 하지 말 것
- `round2/claude.md` 를 열거나 읽지 말 것 (blind 검증).

## 할 일
`PROBLEM.md`에 적힌 1~4번 주장을 각각 독립적으로 검증한다. 웹 접근이 가능하면
직접 검색/조회해서 확인하고, 접근이 안 되면 "확인 불가"라고 명확히 밝힐 것
(추측·창작 금지 — 근거 없는 주장을 사실처럼 쓰지 말 것).

특히 아래를 중점 확인:
1. Karihaloo, Abdalla, Xiao (2003), *Engineering Fracture Mechanics* 70, 979-993,
   "Size effect in concrete beams" — 서지사항 정확성, Kwon et al. (2024) Materials
   17,569 (PMC10856633) 참고문헌 39번과의 연결, 시편 크기(H=50~400mm, W=100mm 고정)
   및 노치비(α=0.05/0.10/0.30) 기술의 정확성.
2. Bažant & Estenssoro (1979), Int. J. Solids Structures 15, 405-426,
   "Surface singularity and crack propagation" — 서지사항, 내용(균열끝단-자유표면
   교차부 3D 코너 특이점) 정확성.
3. ASTM E399 SENB 시편 표준 비율 B(두께):W(깊이):S(스팬) = 0.5:1:4 가 맞는지,
   고정 규격인지 권장값(허용범위 있음)인지.
4. "균열끝단 폭 방향이 자유표면과 만나는 코너 영향구간 크기는 리가먼트(H-a)에
   비례 → H≫W면 코너영향이 crack front 전체 잠식, W≫H면 국소적이지만 보이론
   가정이 깨질 위험 → W/H≈1이 무난"이라는 논리가 문헌적으로 뒷받침되는지,
   아니면 근거 없는 일반화인지.

## 결과물
1~4번 각각 "사실 확인됨 / 부분적으로 맞음(정정 필요) / 확인 불가 / 틀림"으로
판정하고 근거(실제 조회한 출처, 접근 가능했던 범위)를 명시. 마지막에 "H=100mm
채택 근거로 이 인용들을 발표자료에 써도 되는지"에 대한 권고 포함.

결과를 `round2/codex.md` 에 **한국어로** 작성한다.

완료 후: `git add round2/codex.md` → `git commit -m "round2: Codex blind verification"`
→ `git push origin main`. `AGENTS.md` 규칙을 따른다.
