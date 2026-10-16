# Claude Code + Codex 교차검증

사용자 안내문 J:\Desktop\AI\Claude Code + Codex 같이 쓰는 법 (초보자용).html에 따른다.
두 AI를 각각 실행하며 PowerShell 자동화 스크립트를 사용하지 않는다.

## 시작

Windows **명령 프롬프트(cmd)** 창 두 개를 연다.

Claude 창:

```bat
cd /d "J:\Desktop\공학\ai-crosscheck"
claude
```

Codex 창:

```bat
cd /d "J:\Desktop\공학\ai-crosscheck"
codex.cmd --sandbox workspace-write --ask-for-approval on-request
```

위 Codex 옵션은 설치된 CLI의 대화형 도움말에서 확인했다. Git 명령에 필요한 권한은 사용자가 승인한다. 명령 프롬프트와 codex.cmd를 사용하므로 codex.ps1의 PowerShell 실행 정책에 의존하지 않는다.

## 매번 진행하는 순서

1. 사용자가 이번 문제를 PROBLEM.md에 작성하고 두 AI에게 동일하게 준다. 기존 문제는 새 과제가 확정되기 전에 덮어쓰지 않는다.
2. Claude: **PROBLEM.md 읽고 독립 조사해서 roundN/claude.md에 정리해줘. Codex 결과는 보지 마.**
3. Codex: **PROBLEM.md 읽고 독립 조사해서 roundN/codex.md에 정리해줘. Claude 결과는 보지 마.**
4. 각 AI에게 **네 결과 파일만 커밋하고 푸시해줘.**라고 지시한다. GitHub Desktop으로 사용자가 처리해도 된다. 같은 저장소의 커밋 작업은 차례로 진행한다.
5. 독립 결과가 모두 확정된 후 Claude는 codex.md를, Codex는 claude.md를 검증한다. 더 맞는 점·틀린 점·놓친 점을 근거와 함께 claude_review.md / codex_review.md에 작성하고 각자 커밋·push한다.
6. 사용자가 공통 의견과 충돌을 보고 최종 결정하며 DECISION.md에 결정과 이유를 기록한다.

## 핵심

- Blind 단계에는 상대 답을 보지 않는다.
- 합의를 억지로 만들지 않는다. 충돌을 남긴다.
- 같은 결론도 실제 근거로 검증한다.
- 시작 시 pull, 결과 완료 시 지정 파일만 commit·push하고 원격 반영을 확인한다.
- 비밀번호·API 키·개인정보를 커밋하지 않는다.
- 연구 결과와 이전 기록은 보존했다. 과거 자동화 검증 기록은 현재 실행 지침이 아니다.
