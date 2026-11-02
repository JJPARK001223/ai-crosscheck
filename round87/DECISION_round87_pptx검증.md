# round87 — 중간평가.pptx 내용 검증 (사용자 결정 기록)

## 절차
1. `중간평가.pptx`(완성본) 텍스트를 python-pptx로 추출(`round87/input/pptx_text.md`)해 `round85/input/evaluation_data.md`(확정 정답)와 비교 자료로 고정.
2. Claude가 120개 등급·근거를 전수 대조해 `round87/claude.md` 작성(등급 120/120 일치, 왜곡 없음, 압축 9건 발견).
3. Codex가 블라인드로 동일 검증 수행(`round87/codex.md`) — 등급 120/120 일치 확인 + 5건(E1~E5) 수정 제안.
4. Claude가 evaluation_data.md로 E1~E5를 재검증(`round87/claude_review.md`).

## 결과
- **등급(상/중/하) 120개 전부 일치. 사실 왜곡 없음.** (두 AI 독립 확인)
- **실제 수정한 오류 2건** (Claude가 이번에 채운 부분의 실수):
  - No.3(슬라이드7) Introduction 연관성: "수소/메탄올/가솔린 혼합을 상세히" 범위가 압축되며 공백의 의미가 넓어짐 → 원문 범위 복원.
  - No.8(슬라이드12) Abstract 구체성: `CO2.24ppm`(공백 누락, CO2로 오독 가능) → `CO 2.24ppm`.
- **Codex가 추가로 지적한 3건(E1~E3)은 Claude의 작업 범위 밖**(No.1 전체·No.2 Abstract행은 사용자 본인이 이미 작성한 부분이며 Claude가 손댄 적 없음):
  - E1: `Abstact`(Abstract 오타) — 사용자 본인이 슬라이드5·6에 이미 그렇게 썼고, Claude는 나머지 13슬라이드를 채울 때 일관성을 위해 의도적으로 같은 표기를 따름.
  - E2: No.1 "3중"(원문은 "3가지") — 사용자 본인 작성.
  - E3: No.2 Abstract "COV 33% ~ 32%"(원문은 "COV ~33%·~32%") — 사용자 본인 작성.
- 그 외 9~15건의 "세부사항 압축"(저자명·보조 수치·장비 모델명 일부 생략)은 등급 근거에 영향 없음, 수정 불필요로 두 AI 합의.

## 적용된 수정
- `/tmp/midterm_unzip`에서 슬라이드7·12 XML 직접 수정 → 재압축 → `validate.py` 재검증(All validations PASSED) →
  `J:\Desktop\과학논문작성법 과제\중간평가.pptx` 덮어쓰기 완료(덮어쓰기 전 `중간평가_교차검증전_백업2.pptx`로 백업).

## 사용자 결정 필요 (아직 미확정)
- **E1 (Abstact → Abstract로 15곳 전부 통일할지)**: 사용자 본인이 슬라이드5·6에 이미 "Abstact"로 썼기 때문에, 전부 고치려면
  사용자 작성분까지 수정해야 함. 과제 제출용이면 통일해서 고치는 것을 권장하나, 최종 결정은 사용자가 내려야 함.
- E2, E3도 마찬가지로 사용자 본인 작성분 수정 여부는 사용자가 결정.

## 커밋
- claude.md, PROBLEM.md, input/: commit 5efcc38
- codex.md: Codex 자체 커밋(round87/codex_stage_A.log 참조), origin/main 반영 확인
- claude_review.md: commit 1301aa9
