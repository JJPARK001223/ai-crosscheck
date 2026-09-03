# 작업 규칙 (Claude)

## 자동 교차검증 작업자 규칙
- 프롬프트에 `[CROSSCHECK_WORKER]`가 있으면 `ask.ps1`이나 `orchestrate.ps1`을 실행하지 말고 지정된 단계와 파일만 수행한다.
- 최종 종합 단계에서는 양쪽 독립 결과와 검토 결과를 직접 판단하여 `DECISION.md`와 사용자용 `FINAL.md`를 작성한다.
- 독립 조사 단계의 blind 원칙과 근거 확인 원칙은 자동 실행 중에도 그대로 지킨다.

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
3. **Codex(blind)**: `codex exec -C <repo> -s workspace-write --skip-git-repo-check "..."`
   포그라운드로 실행 → `roundN/codex.md`. (백그라운드 중첩 AI 실행은 classifier가 막음)
4. commit/push.
5. **교차검증**: Claude는 `codex.md` 읽고 맞는 점/틀린 점/놓친 점 검토.
   Codex에 `claude.md` 검증 시킴 (codex exec 재실행).
6. **최종 답은 Claude가** `DECISION.md`에 작성: 공통 / 충돌(중요) / 최종 결정+근거.
   채팅으로도 요약 보고.
7. 3·5번 Codex 실행 동안 **1분마다** git 커밋 진행 여부 체크. 멈춰 있으면 사용자에게 알림.
