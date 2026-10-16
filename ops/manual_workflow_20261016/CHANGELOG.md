# 안내문 방식으로 복원 — 2026-10-16

## 사용자 결정
사용자가 PowerShell 자동화를 제거하고 `J:\Desktop\AI\Claude Code + Codex 같이 쓰는 법 (초보자용).html`대로 다시 구성하라고 명시했다. 이 결정에 따라 기존 자동 실행 방식을 폐기했다.

## 수행 내용
- 저장소의 모든 .ps1 파일 18개와 미추적 Invoke-CodexStage.cmd 1개를 저장소 밖으로 옮겼다. 영구 삭제 대신 복구 가능한 백업으로 보존했다.
- 백업: `J:\Desktop\AI\협업자동화_백업_20261016_172630`. moved_scripts.txt에 이동 목록이 있다.
- CLAUDE.md, AGENTS.md, README.md를 안내문의 독립 조사 → 각자 Git 인계 → 양방향 검증 → 사용자 최종 결정 방식으로 변경했다.
- Claude 전역 지침 C:/Users/HeejinKim/.claude/CLAUDE.md의 규칙 20도 같은 방식으로 변경하고 이전 실행기 호출 지침을 제거했다. 전역 파일 전체는 저장소에 복사하지 않았다.
- 새 스크립트, AI 자동 호출, 자동 승인 검토를 추가하지 않았다. Codex는 명령 프롬프트에서 대화형 on-request 승인 정책으로 실행하도록 안내했다.
- CLI의 대화형 도움말에서 --sandbox workspace-write 및 --ask-for-approval on-request 지원을 확인했다. exec의 --approve-for-me 방식과 구분한다.
- 사용자 연구 자료, PROBLEM.md와 기존 연구·검증 결과는 보존했다. 과거 자동화 기록은 이력이며 현재 실행 지침이 아니다.

## 사용
README.md의 두 창 시작 명령을 사용한다. Claude와 Codex가 상대 답을 보기 전에 각자의 독립 결과를 확정하고, 사용자가 각 창에 커밋 및 상호 검증을 지시한다. 필요한 Git 권한은 사용자에게 요청한다.

## 검증 범위
- 작업 트리에 .ps1 파일 및 Invoke-CodexStage.cmd가 남아 있지 않은지 확인한다.
- 저장소 규칙과 Claude 전역 규칙이 동일한 수동 협업 방식을 가리키는지 확인한다.
- 두 대화형 터미널은 이 작업에서 자동 실행하지 않았다. AI 자동 호출 금지라는 사용자 변경 방향을 따른다.
- 이번 설정 정리는 사용자 지시에 따라 Codex가 수행했다. 새 Claude 하위 세션을 호출해 검토받았다고 주장하지 않는다.
