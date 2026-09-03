<#
ask.ps1 - "Claude 초안 -> Codex 검증 -> 최종답은 Codex가 작성" 모드

이 창(Claude)에 시킨 일을 Claude가 먼저 풀고, Codex가 검증한 뒤 최종 답을 낸다.
결과물(FINAL.md)의 최종 답은 Codex가 쓴 것이다.

사용법:
  .\ask.ps1 "질문 / 시킬 일"

전제: claude, codex 로그인 완료. 이 폴더가 git repo(origin main) 연결됨.
git(pull/commit/push)은 스크립트가, 파일 작성은 각 AI가 한다.

주의: 이 모드는 blind 교차검증이 아니다. Codex가 Claude 초안을 보고 검증/보완한다
(리뷰어 패턴). 완전 독립 배심원 방식을 원하면 orchestrate.ps1 을 써라.

이 파일은 UTF-8 BOM으로 저장해야 Windows PowerShell 5.1에서 한글이 안 깨진다.
#>
param([Parameter(ValueFromRemainingArguments = $true)] [string[]] $Question)

$ErrorActionPreference = 'Stop'
$repo = $PSScriptRoot
Set-Location $repo

function Need($c) { if (-not (Get-Command $c -ErrorAction SilentlyContinue)) { throw "'$c' 없음. 설치/PATH 확인." } }
function Invoke-Git() {
  Write-Host "  git $args" -ForegroundColor DarkGray
  & git.exe @args; if ($LASTEXITCODE -ne 0) { throw "git 실패: $args" }
}
function Sync-Repo($msg) {
  & git.exe add -A
  & git.exe diff --cached --quiet
  if ($LASTEXITCODE -ne 0) { Invoke-Git commit -m $msg; Invoke-Git push origin main }
  else { Write-Host "  (변경 없음)" -ForegroundColor DarkGray }
}

Need git.exe; Need claude; Need codex
$q = ($Question -join ' ').Trim()
if (-not $q) { throw "질문을 인자로 넣어라: .\ask.ps1 `"...`"" }

Write-Host "`n[1/4] git pull + 문제 기록" -ForegroundColor Green
Invoke-Git pull --ff-only origin main
Set-Content (Join-Path $repo 'PROBLEM.md') "# 이번에 풀 문제`n`n$q`n" -Encoding utf8
Set-Content (Join-Path $repo 'round1\claude.md') "# Round 1 - Claude 초안`n" -Encoding utf8
Remove-Item (Join-Path $repo 'FINAL.md') -Force -ErrorAction SilentlyContinue
Sync-Repo "ask: 문제 기록 - $q"

Write-Host "`n[2/4] Claude 초안 작성" -ForegroundColor Green
& claude -p "PROBLEM.md 를 읽고 네 분석/답을 round1/claude.md 에 써라. 중요한 주장에 근거(코드/실행결과/데이터/공식문서)를 붙이고, 불확실한 부분은 명시해라. 파일 저장까지만. git 은 건드리지 마라." `
  --permission-mode acceptEdits --disallowedTools Bash 2>&1 | Out-String | Write-Host
if ($LASTEXITCODE -ne 0) { throw "claude 실패" }
Sync-Repo "ask: Claude 초안"

Write-Host "`n[3/4] Codex 검증 + 최종답 작성" -ForegroundColor Green
# codex는 Start-Job 안에서 실행해야 stdin 문제(-File 실행 시 "Reading from stdin" 멈춤)를 피한다
$codexExe = (Get-Command codex).Source
$codexPrompt = "git pull 하지 말고 현재 파일 그대로 본다. PROBLEM.md 와 round1/claude.md(Claude 초안)를 읽어라. Claude 초안을 코드/실행/데이터/공식문서로 검증해라. 그런 다음 FINAL.md 를 새로 써라. FINAL.md 구성: '## 최종 답'(네가 검증해 확정한 답), '## Claude 초안에서 고친 점', '## 남은 불확실성 / 확인 필요'. 최종 답의 근거를 반드시 붙여라. 파일 저장까지만. git 은 건드리지 마라."
$job = Start-Job -ScriptBlock {
  param($repo, $prompt, $exe)
  Set-Location $repo
  $last = Join-Path $repo '.codex_last.txt'
  '' | & $exe exec -C $repo -s workspace-write --skip-git-repo-check --ephemeral -o $last $prompt 2>&1 | Out-Null
  $code = $LASTEXITCODE
  $text = if (Test-Path $last) { Get-Content $last -Raw -Encoding UTF8 } else { '(출력 없음)' }
  Remove-Item $last -Force -ErrorAction SilentlyContinue
  [pscustomobject]@{ code = $code; text = "$text" }
} -ArgumentList $repo, $codexPrompt, $codexExe
$cx = Receive-Job -Job $job -Wait -AutoRemoveJob
Write-Host $cx.text -ForegroundColor Cyan
if ($cx.code -ne 0) { throw "codex 실패 (exit $($cx.code))" }
Sync-Repo "ask: Codex 검증 + FINAL.md"

Write-Host "`n[4/4] 최종 결과 (Codex 작성)" -ForegroundColor Green
Write-Host ('=' * 60)
if (Test-Path (Join-Path $repo 'FINAL.md')) {
  Get-Content (Join-Path $repo 'FINAL.md') -Raw -Encoding UTF8
} else {
  Write-Host "FINAL.md 가 없다. Codex 출력(위 Cyan)을 확인해라." -ForegroundColor Red
}
Write-Host ('=' * 60)
