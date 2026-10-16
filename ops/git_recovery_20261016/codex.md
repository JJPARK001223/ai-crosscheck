# Git 인계 복구 및 실행기 독립 검증 (2026-10-16)

## 범위와 방법

사용자가 지정한 round40~43의 codex.md를 내용 수정 없이 각각 커밋했다. 연구 내용, Claude 조사 결과, DECISION.md는 읽거나 재검토하지 않았다. Invoke-CodexStage.ps1, CLAUDE.md, AGENTS.md만 실행기/지침 검증 대상으로 읽었다. 하위 AI, Invoke-CodexStage.ps1, ask.ps1, orchestrate.ps1, 라운드 실행기는 실행하지 않았다. CLI는 버전과 도움말만 호출했다.

근거는 아래의 로컬 코드, PowerShell 구문 분석 및 정규식 재현, 실제 Git 명령 결과다. 실행기 전체의 실제 세션 실행 검증은 이번 작업의 하위 AI 실행 금지 때문에 수행하지 않았다.

## Git 복구 확인 결과

- 최초 git status 및 git diff --cached --name-only: 기존 스테이징 없음. 다른 작업의 수정/삭제/미추적 파일이 다수 존재했으며 그대로 보존했다.
- git fetch origin: 일반 실행은 `.git/FETCH_HEAD: Permission denied`; 동일 명령을 require_escalated로 재실행하여 종료 코드 0.
- fetch 직후 현재 브랜치 main. HEAD와 origin/main은 모두 `b48517e511439e31de07518972a0cd11b1f92e4e`. 따라서 자동 병합 없이 진행했다. pull/reset/stash/clean은 실행하지 않았다.
- git ls-files에 지정 네 파일이 없었고, git status는 네 파일 모두 `??`였다.
- 각 git add와 git commit의 일반 실행은 `.git/index.lock: Permission denied`; 각 명령을 그대로 require_escalated로 재실행하여 모두 성공했다. 매 커밋 직전 git diff --cached --name-only가 지정 한 파일뿐임을 확인했다.
- 네 커밋의 파일 목록과 커밋 본문을 git log로 재확인했다. 모두 요청한 Co-Authored-By 푸터를 포함한다.

| 파일 | 커밋 SHA |
|---|---|
| round40/codex.md | d3a2f832301a5ebf9fb90e5dca998f34a19f55a2 |
| round41/codex.md | 2a78cced293f0d6e0150fcd8becea8a5e450056d |
| round42/codex.md | 9dd155d99c63922d2dbb04618c7f1bcccaf1c1d4 |
| round43/codex.md | 59f7d737ade8d1b158e86ec01ae05a8396c1399c |

아래 SHA-256은 최초 커밋 전과 네 커밋 후 Get-FileHash로 비교하여 모두 동일했다. Git은 add 시 LF→CRLF 경고를 출력했으나 이 시점의 작업 파일 바이트는 바뀌지 않았다. Git 저장 시 줄바꿈 정규화와 작업 파일 바이트 동일성은 별개의 검사다.

| 파일 | 작업 전후 SHA-256 |
|---|---|
| round40/codex.md | 3D81FEB53E424073D0D236DB84C640BFAC6E1AAD5F38067330214E4587E3817B |
| round41/codex.md | 2C7630E3F8CF98AEBD41516A6275A681FFD71E5B2D590506C65EED5F58DEE41F |
| round42/codex.md | FFA027C1BCEBE016DE312F4C7B805CDD677E8942937DE6D6510ABF65B09D5E3C |
| round43/codex.md | B037611D04962B3F22F4DD7C6E025E555AC386F3F496F9E5F122FCAA95656AAC |

이 보고서 커밋과 push 이후의 최종 HEAD/원격 SHA 비교 및 최종 파일 해시 재확인 결과는 최종 채팅에 보고한다. 이 문서 작성 시점에는 아직 최종 push 전이다.

## 실행기에서 확인한 사항

검사 환경: Windows PowerShell `5.1.26100.9444`, `codex-cli 0.163.0`. PowerShell Parser.ParseFile의 오류 수는 0이었다. CLI 도움말/버전 호출은 종료 코드 0이었지만 Codex 임시 arg0 디렉터리 정리와 PATH 별칭 생성에 액세스 거부 경고가 있었다. 이 경고로 본 실행기의 성공 여부를 판단할 수는 없다.

1. **명령 구성은 현재 지침과 일치한다.** 실행기 33~35행은 exec, -C, --approve-for-me, --skip-git-repo-check, --add-dir, stdin용 `-`를 전달한다. --sandbox를 함께 전달하지 않는다. 로컬 `codex.cmd exec --help`는 --approve-for-me가 workspace-write와 자동 검토를 사용한다고 설명하며, --add-dir는 추가 쓰기 가능 디렉터리를 지정한다고 설명한다. 이 검증에서는 --sandbox 병용 충돌을 실제 재실행하지 않았으므로 해당 충돌의 독립 실측 완료로 표시하지 않는다.

2. **정책 검사가 작업 종료 후에만 수행된다.** 39행의 CLI 파이프라인이 끝난 뒤 45~47행에서 로그를 검사한다. 잘못된 정책을 검출해도 실행 전 차단하는 구조는 아니다. CLI 인자가 정책을 설정하는 부분과 로그로 사후 확인하는 부분을 구분해야 한다.

3. **로그 검사에 재현 가능한 오탐 통과가 있다.** 46행은 로그 전체에서 sandbox 접두부만 찾고 끝 경계를 검사하지 않는다. 아래 입력 모두 현행 정규식 판단에서 통과(True)했다. 두 번째는 잘못된 값도 통과함을, 세 번째는 서로 다른 위치의 줄을 조합하여 통과함을 보여준다. 실제 세션이 이런 로그를 생성했다고 주장하는 것이 아니라 검사식의 판별 한계를 재현한 것이다.

```text
approval: on-request
sandbox: workspace-write
=> True (정상 대조군)

approval: on-request
sandbox: workspace-write-INVALID
=> True

approval: on-request
sandbox: danger-full-access
agent output:
sandbox: workspace-write
=> True
```

재현에는 아래 현행 조건의 부정을 사용했다. 메모리 문자열만 검사했으며 실행기나 AI는 호출하지 않았다.

```powershell
-not ($probeLog -match '(?m)^approval:\s*never\s*$' -or
      $probeLog -notmatch '(?m)^approval:\s*on-request\s*$' -or
      $probeLog -notmatch '(?m)^sandbox:\s*workspace-write')
```

4. **자동 reviewer 선택을 독립 확인하지 않는다.** 46행은 approval과 sandbox만 검사하며 approvals_reviewer는 검사하지 않는다. 공식 OpenAI 문서도 on-request 정책만 바꾸는 것으로 reviewer가 선택되지는 않는다고 구분한다. 현행 CLI 인자 --approve-for-me 자체는 자동 검토를 요청하지만, 이 로그 검사만으로 실제 reviewer 선택까지 입증했다고 할 수 없다. 출처: OpenAI, *Auto-review*, 공식 기술문서, 2026-10-16 조회, https://learn.chatgpt.com/docs/sandboxing/auto-review (Select automatic review).

5. **Git 인계 완료는 CLI 종료 코드와 별도다.** 실행기 43~49행은 LASTEXITCODE와 정책 문자열만 검사한다. git status, 스테이징 목록, commit SHA, ls-remote 비교, 파일 해시 검사는 없다. worker가 실패를 보고하고 정상 종료하는 경우를 실행기가 별도로 판별하는 코드도 없다. 따라서 지침의 원격 확인 의무는 worker/호출자가 수행해야 하며 실행기 종료 코드 0만으로 대체할 수 없다.

6. **지정 결과 파일 제한과 blind 제한은 지시다.** guard 28~31행은 금지사항을 프롬프트로 전달한다. 파일별 읽기/쓰기 차단을 설치하지 않는다. 기본 AdditionalDirectory는 XLPR이며 --add-dir로 전달된다(5, 34행). 이는 지정 결과 경로보다 넓은 추가 쓰기 범위다. CLAUDE.md와 AGENTS.md는 작업 지시와 기술적 접근 차단을 구분하고 있어 이 점은 문서와 일치한다.

7. **로그 보존 검사는 비원자적이다.** 22행은 기존 경로를 Test-Path로 검사하고, 40행은 AppendAllText로 연다. 배타적 신규 생성/잠금이 없어 검사 이후의 동시 생성까지 방지하는 구조는 아니다. 또한 38행은 ErrorActionPreference를 Continue로 설정하고, 로그 쓰기 오류를 별도 누적하여 최종 실패로 만드는 코드가 없다. 정상 CLI 실행과 완전한 로그 저장을 각각 입증하는 구조는 아니다. 실제 로그 유실이나 동시 충돌은 이번에 재현하지 않았다.

8. **1분 주기 감시와 제한시간이 실행기에는 없다.** 39행은 동기 파이프라인이며 별도 타이머/timeout/진행 감시 코드가 없다. CLAUDE.md의 1분마다 Git 커밋 진행 여부 확인은 외부 호출자의 의무다. 커밋 부재만으로 프로세스 중단 여부를 판정할 근거는 이 실행기에 없다.

## 지침 검토와 검증 한계

디스크의 AGENTS.md와 CLAUDE.md는 --approve-for-me와 --sandbox를 병용하지 않도록 일치한다. 사용자 메시지에 인용된 이전 AGENTS.md에는 --sandbox 명시 문장도 있지만, 이번 작업의 최신 개별 지시는 실행기 실행을 금지하므로 이를 호출하지 않았다. 일반적인 시작 시 git pull 규칙도 이번의 명시적 fetch/동일 SHA 확인 및 pull 금지 지시보다 우선하지 않는다.

현재 세션의 실제 Git 승인 재실행 성공은 확인했다. 그러나 이 사실은 검토한 스크립트를 통해 새 세션을 시작했을 때의 종단간 동작을 검증한 결과가 아니다. Windows -ExecutionPolicy Bypass 명령, 네트워크 차단의 승인 재실행, 승인 거부/미지원 처리, CLI 비정상 종료, 디스크 쓰기 실패, 실행 중 1분 감시, --sandbox 병용 충돌은 이번에 실제 재현하지 않았다. 관련 문구를 검증 완료 사실로 확대하지 않는다.

검증 대상 파일 SHA-256(읽은 로컬 버전 식별용):

| 파일 | SHA-256 |
|---|---|
| Invoke-CodexStage.ps1 | D73AA727E01041E274344A330F4FF151BB467EDE1A49BBD57E8982331A2AABC5 |
| CLAUDE.md | A12A92DFCEC93D51E8E2D22AF4401F5D12814E9AD6FB5779BF4DB048689BAC12 |
| AGENTS.md | 4AC13D9E0D371320E2FF87BEAD1C0CC7E3557DE81EC1D59E2CF785661E4AFEE6 |

실행기와 지침 파일의 수정은 이번 승인 범위에 없으므로 수행하지 않았다.
