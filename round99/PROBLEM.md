# round99 — No.1 Introduction 등급 재심 검증 + Worst Paper 재선정 검증

## 배경

round98에서 Claude·Codex 둘 다 No.1(Processes, 2021)의 Introduction 등급(하/하) 근거문구
"선행연구의 정량적 결과 인용은 거의 없음"이 원문과 정확히 일치하지 않음을 확인했다(실제로는 문헌
[27,28,39,41,44] 기반 정량 서술 4대목·수치 8개 존재). round98의 Codex는 "근거문구만 고치고 등급은
유지"를 권고했으나, 별도로 수행된 2차 독립 검증(`paper_review_project/codex_review/`)은 더 강하게
"등급 자체가 무너졌으므로 재채점 전에는 No.1을 Worst로 확정할 수 없다"고 판단했다. **사용자가 공식
재심을 결정**했다.

Claude는 다음과 같이 1차 재심했다(`round99/input/evaluation_data.md`에 반영):
- No.1 Introduction 구체성: 하 → **중**
- No.1 Introduction 연관성: 하 → **중**
- 근거: 위 4대목·8개 수치 확인 + No.4의 Introduction 연관성(중)과의 등급 일관성(No.4도 "일반배경 중심,
  구체적 연결 약함"이지만 중으로 평가됨)

이 재심으로 15편 내용평가 집계가 바뀐다:
- No.1: 상2/중3/하3 → **상2/중5/하1**
- No.4: 상4/중2/하2 (변경 없음)
- No.11: 상2/중4/하2 (변경 없음)

"하" 최다 논문이 더 이상 No.1(1개)이 아니라 No.4·No.11(각 2개로 동률)이 된다. Claude는 "상" 개수가
적은 쪽(No.11, 상2 vs No.4 상4)과 evaluation_data.md의 기존 특이사항 기록("No.11은 4섹션 전체에서
일관되게 시뮬레이션/수식 위주·물리적 실험 검증 부족이 지적된 유일한 논문")을 근거로 **새 Worst = No.11**
로 잠정 변경했다.

## 검증 요청

1. **No.1 Introduction 재심(하→중, 구체성·연관성 둘 다)이 타당한가?** `round99/input/evaluation_data.md`의
   No.1 Introduction 항목(새 근거문구 포함)을 원문(`J:\Desktop\수업과제\과학논문작성법 과제\A Comparison of
   Ethanol, Methanol, and Butanol Blending with Gasoline and Its Effect on Engine Performance and Emissions
   Using Engine Simulation.pdf`)과 직접 대조해 중이 적절한지, 아니면 하 유지 또는 상 승격이 더 타당한지
   독립 판단하라. 비교 기준으로 evaluation_data.md의 다른 "중"·"하" 등급 사례(No.4, No.8, No.12 등)와의
   일관성도 확인하라.
2. **No.11이 새 Worst로 타당한가?** No.4(상4/중2/하2)와 No.11(상2/중4/하2)이 "하" 개수로 동률일 때,
   "상" 개수가 적은 쪽을 택하는 동점 해소 기준이 타당한지, 그리고 No.11의 기존 "4섹션 전체 일관된 약점"
   특이사항 기록을 가중치로 쓰는 것이 타당한지 검토하라.
3. **15편 전체 재집계**: round99/input/evaluation_data.md의 120개 등급(No.1 Introduction 2개만 변경,
   나머지 118개는 round85~88에서 이미 확정)을 처음부터 다시 세어 전체 집계표를 독립 작성하라.

## 결과 파일

`round99/codex.md`에 작성. 형식 자유. 끝나면 `round99/codex.md`만 git add/commit/push 하고 원격 반영까지
확인하라. 다른 파일(특히 round99/input/evaluation_data.md 등 Claude의 1차 재심 결과)은 건드리지 마라.
