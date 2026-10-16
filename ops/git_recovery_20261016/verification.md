# 최종 실행 검증 — 2026-10-16

## 재발 원인 및 이전 수정 정정
- Claude 전역 지침의 예시 명령이 승인 옵션 없는 과거 명령이었다. 저장소 지침만 변경하여 새 round 생성에 반영되지 않았다.
- CLI 0.163.0은 `--sandbox workspace-write --approve-for-me` 동시 지정을 거부한다. recovery.log에 실제 인자 충돌을 보존했다. 이전 git_permissions_DECISION.md의 승인 판단은 이 조합 오류를 놓쳤다.
- `--approve-for-me` 단독 사용이 workspace-write 및 자동 승인 검토를 설정한다. 이를 공통 단계 실행기에 고정했다. 샌드박스를 해제하지 않았다.
- Windows PowerShell 실행 정책은 해당 프로세스의 `-ExecutionPolicy Bypass`로만 처리한다. 시스템 전역 정책은 변경하지 않았다.

## 실제 복구
Codex가 공통 실행기로 시작한 새 세션에서 직접 승인 재실행을 통해 지정 결과만 각각 커밋하고 push했다.

| 결과 파일 | 복구 커밋 |
|---|---|
| round40/codex.md | d3a2f83 |
| round41/codex.md | 2a78cce |
| round42/codex.md | 9dd155d |
| round43/codex.md | 59f7d73 |

실행기 독립 검증 보고서 커밋은 a9c4699. 원격 main SHA a9c46997341e7806fb5c62ea0bfd03c5c197da69와 로컬 HEAD가 일치했다. 네 보고서의 작업 전후 SHA-256은 codex.md 표의 값과 모두 동일했다. PPT 및 연구 보고서 내용은 수정하지 않았다.

## 독립 검증 지적 및 보완
- 로그 전체의 느슨한 문자열 검사 → CLI 헤더 구간만 추출하고 sandbox 값 전체를 검사.
- 인계 검증을 worker에게만 위임 → HandoffFiles 필수, 레포 안 상대 경로 제한, 추적/미커밋 여부 및 로컬 HEAD=원격 branch 확인.
- 로그 신규 생성 경쟁/쓰기 오류 → CreateNew 배타 생성, UTF-8 StreamWriter, 쓰기 실패 종료 오류.
- 자동 승인 reviewer의 별도 헤더가 없다는 한계는 유지한다. CLI의 --approve-for-me로 선택하며 approval on-request 헤더만으로 모든 작업 자동 허용을 보장한다고 주장하지 않는다.

## 최종 실행 확인
- verification.log: 최신 공통 실행기로 새 Codex 세션 실제 실행, approval on-request 및 sandbox workspace-write 확인.
- Codex가 최신 실행기 보완을 직접 읽고 확인했으며 round40~43 보고서 모두 추적 중/변경 없음 및 원격 SHA 일치를 확인했다.
- 실행기 종료 코드 0, 마지막 출력: `VERIFIED_GIT_HANDOFF a9c46997341e7806fb5c62ea0bfd03c5c197da69 round43/codex.md`.
- 기존 로그 경로를 다시 지정하는 시험은 모델 실행 전 덮어쓰기 거부로 종료했다.
- 실제 헤더 허용, workspace-write-INVALID 거부, PowerShell 구문 검사 통과.
- 작업 중 1분마다 진행 안내 및 Git 커밋 상태 확인은 호출자가 수행했다.

## 지속 적용
- Invoke-CodexStage.ps1에 호출 방식 고정, round39~43 run.ps1은 공통 실행기로만 위임.
- 저장소 CLAUDE.md/AGENTS.md와 C:/Users/HeejinKim/.claude/CLAUDE.md 규칙 20을 동기화했다. 전역 지침 전체는 개인정보 포함 가능성을 고려해 저장소에 복사하지 않았다.
- 이미 실행 중인 세션에는 설정 변경이 소급 적용되지 않는다. 이번처럼 Git 인계만 새 세션으로 복구한다.
- 자동 승인 검토가 개별 명령을 거부하면 우회하지 않고 미완료와 사유를 보고한다.
