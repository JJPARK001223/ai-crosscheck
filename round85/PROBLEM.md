# round85 — 가솔린 엔진 SCI 논문 15편 "4섹션 평가 종합 보고서" 작성 (Claude↔Codex 교차검증)

## 배경
사용자(서울과학기술대학교 신뢰성기반 기계설계연구실, 과학논문작성법 수업 과제)가 가솔린 엔진 출력 관련 SCI(E) 논문 15편에 대해
이미 Abstract / Introduction / Methodology / Results 네 섹션을 각각 "[섹션] 구체성"과 "논문과 [섹션]의 연관성" 두 기준(상/중/하)으로
평가 완료했다. 그 확정 결과와 근거 문장 전체가 `round85/input/evaluation_data.md`에 논문 15편 × 섹션 4개 = 총 60개 평가항목으로 정리되어 있다.

## 과제
`round85/input/evaluation_data.md`만을 근거로, 15편 논문에 대한 **종합 평가 보고서**를 작성하라.

### 반드시 지킬 제약
1. **입력 파일(evaluation_data.md)에 없는 새로운 평가·등급·수치는 절대 추가하지 말 것.** 새로 PDF를 읽거나 추측으로 등급을 바꾸지 않는다.
   이 라운드의 목적은 "이미 끝난 60개 평가"를 **종합·설명**하는 보고서를 쓰는 것이며, 재평가가 아니다.
2. 각 등급(상/중/하)마다 **왜 그렇게 평가되었는지**(evaluation_data.md에 적힌 근거 문장)를 보고서에 반드시 포함할 것.
3. 사실(이미 확정된 등급·근거)과 너의 해석(그 근거가 타당한지에 대한 판단)을 구분해서 쓸 것. "이미 확정된 자료에 근거해 타당하다고 판단한다 / 근거가 약하다고 생각한다" 식으로 명시.
4. 모르거나 input에 없는 내용은 "확인 불가"라고 쓸 것. 추측 금지.

### 보고서에 포함할 내용
- **논문별 요약**: No.1~15 각각에 대해 4섹션 등급을 표로 정리하고, 가장 특징적인 근거 1~2개를 요약.
- **섹션별 종합 경향**: Abstract/Introduction/Methodology/Results 각각에서 상/중/하 분포가 어떻게 다른지, 그리고 그 차이가 "왜" 발생했는지(evaluation_data.md의 근거에 기반해) 설명.
  (참고: 이미 확정된 경향 — Methodology·Results는 상 비율이 높고 Abstract는 하/중이 많다. 이 패턴이 evaluation_data.md의 근거들로 볼 때 타당한지 네 의견을 밝혀라.)
- **특이사례**: No.11(시뮬레이션 전체에서 실험적 정량검증 부족이 4섹션 전체에서 일관 지적됨), No.9(Introduction만 연관성 "중", Methodology·Results는 "상"으로 바뀌는 섹션간 불일치), No.13/14/15(가솔린이 아닌 디젤/수소 엔진 논문이지만 섹션 내부 품질은 높게 평가된 경우) 각각에 대해 evaluation_data.md의 근거를 인용하며 설명.
- **이 평가 체계 자체에 대한 네 의견**: "상/중/하" 2축 평가 기준(구체성, 연관성)이 15편을 구분하는 데 실제로 유효했는지, evaluation_data.md에 나타난 근거의 질(수치 밀도, 논리 연결)을 보고 판단하라.

### 출력
`round85/claude.md` (Claude 작성) / `round85/codex.md` (Codex 작성) 각자 독립적으로 작성한다. **서로의 결과 파일을 보지 않고** 작성할 것(blind).
형식은 자유(마크다운), 단 위 "반드시 지킬 제약"과 "포함할 내용"은 전부 충족해야 한다.

## 이후 단계 (이 PROBLEM.md에 포함, 별도 지시 없이 순서대로 진행)
1. Claude: `round85/claude.md` 작성.
2. Codex: `round85/codex.md` 작성 (blind).
3. Claude: `round85/codex.md`를 읽고 검증 — 더 맞는 점, 틀린 점(evaluation_data.md 근거와 불일치하는 부분), 놓친 점을 `round85/claude_review.md`에 근거와 함께 작성.
4. Codex: `round85/claude.md`를 읽고 같은 방식으로 `round85/codex_review.md` 작성.
5. 최종 종합은 사용자에게 보고할 때 Claude가 "Codex 단독 의견 / Claude 단독 의견 / 공통 의견(Codex+Claude)" 세 챕터로 구성한다. 이 종합 자체는 PROBLEM.md의 범위를 벗어나는 새 평가를 추가하지 않고, claude.md/codex.md/두 review 파일에 이미 쓰인 내용만 재구성한다.

## Git
이 라운드는 보고서 작성 라운드이며, 각자 자신이 작성한 파일만 커밋한다. 커밋·push는 사용자 승인 후 진행한다(AGENTS.md 전역 규칙 #20).
