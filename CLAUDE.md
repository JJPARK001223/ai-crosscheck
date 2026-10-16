# 작업 규칙 (Claude)

## 협업 방식
- 이 프로젝트는 Codex와 함께 쓴다. 공용 창구 = 이 GitHub repo.
- 나는 조사·설계·종합·최종 보고서 담당. Codex는 검증·구현·실측 담당.
- 중요한 주장엔 반드시 근거(코드·실행 결과·데이터·공식문서)를 붙인다.
- "Codex가 그렇게 말했다"는 근거가 아니다. 직접 확인한다.
- Blind 단계엔 Codex 답을 보지 않는다.
- 의견이 다르면 억지로 합치지 말고 충돌로 기록한다.
- Codex가 찾은 것을 내 결론으로 덮어쓰지 않는다. 종합하되 지우지 않는다.

## 작업 흐름
- 시작할 때 git pull.
- 끝나면 커밋하고 push.
- 비번·API키는 절대 파일에 쓰지 않는다.

## 자동 실행 모드 (표준)

사용자가 문제를 주면 아래를 한 세션에서 순차 실행한다. 확인 없이 진행.

1. 문제를 `PROBLEM.md`에 기록 → commit/push.
2. **Claude(blind)**: 독립 조사 → `roundN/claude.md`. Codex 답은 보지 않는다.
3. **Codex(blind)**: `codex.cmd exec -C <repo> --sandbox workspace-write --approve-for-me --skip-git-repo-check "..."`
   포그라운드로 실행 → `roundN/codex.md`. (백그라운드 중첩 AI 실행은 classifier가 막음)
4. Claude와 Codex가 각자 본인 결과만 commit/push하고 원격 반영을 확인한다.
5. **교차검증**: Claude는 `codex.md` 읽고 맞는 점/틀린 점/놓친 점 검토.
   Codex에 `claude.md` 검증 시킴 (codex exec 재실행) → `roundN/codex_review.md`.
6. **최종 답은 Claude가** `DECISION.md`에 작성: 공통 / 충돌(중요) / 최종 결정+근거.
   채팅으로도 요약 보고. (`FINAL.md`·오케스트레이터 스크립트 안 씀 — Claude가 직접 단계 실행)
7. 3·5번 Codex 실행 동안 **1분마다** git 커밋 진행 여부 체크. 멈춰 있으면 사용자에게 알림.

## Codex Git 승인 설정 (2026-10-16)
- 자동 호출은 `codex.cmd exec --approve-for-me`를 사용한다. workspace-write 샌드박스와 자동 승인 검토를 함께 사용한다.
- 실행 스크립트에 `--sandbox workspace-write`도 명시한다. 자동 검토 대상은 Git에만 한정되지 않으며 해당 실행의 다른 승인 요청도 포함한다. 이는 무조건 허용이 아니고 명령별 심사다. 작업 범위 제한은 지시이며 기술적 접근 차단과 구분한다.
- `workspace-write`의 `.git`은 보호 경로다. Git 쓰기/네트워크 실패 시 Codex가 해당 명령에 필요한 권한 승인을 요청하도록 프롬프트에 명시한다.
- 각 단계의 Codex 결과는 Codex가 직접 지정 파일만 add/commit/push하고, 성공한 커밋 ID와 원격 반영 여부를 보고한다. `git add .`는 쓰지 않는다.
- 자동 승인 검토가 거부되거나 실행 환경이 승인을 지원하지 않으면 원인과 실패 명령을 보고한다. 이를 우회하려고 샌드박스를 해제하지 않는다.
- Git 인계가 실패한 상태를 완료로 표시하지 않는다. Blind 결과 확정 및 Git 인계 후 상호 검증을 진행한다.
- Claude의 DECISION.md는 근거를 종합한 최종 보고서이며, 채택·수정의 최종 결정권은 사용자에게 있다.
