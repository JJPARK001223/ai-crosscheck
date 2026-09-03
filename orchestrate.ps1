<#
Claude Code + Codex 교차검증 오케스트레이터 (PowerShell, 외부 의존성 없음)

한 번 실행하면:
  PROBLEM.md 기록 -> 두 AI 독립 조사(blind, 병렬) -> 서로 교차검증
  -> DECISION.md 초안 -> 최종 판단은 사용자.

사용법:
  .\orchestrate.ps1 "이번에 풀 문제를 여기에"
  .\orchestrate.ps1            # PROBLEM.md에 이미 적어둔 경우

전제: claude, codex 둘 다 설치 + 로그인. 이 폴더가 git repo이고 origin(main) 연결됨.
git(pull/commit/push)은 전부 이 스크립트가 한다. AI는 파일만 쓴다.
이 파일은 UTF-8 BOM으로 저장해야 Windows PowerShell 5.1에서 한글이 안 깨진다.

ponytail: blind 무결성은 "phase1에서 상대 파일이 아직 없음(템플릿뿐)"으로만 보장.
AI가 규칙을 어기고 상대 파일을 억지로 읽으면 못 막는다 -> CLAUDE.md/AGENTS.md 규칙에 맡김.
#>
param([Parameter(ValueFromRemainingArguments = $true)] [string[]] $Question)

$ErrorActionPreference = 'Stop'
$repo = $PSScriptRoot
Set-Location $repo

$claudeTpl = "# Round 1 - Claude 독립 조사 결과`n`n(PROBLEM.md만 보고 조사. Codex 결과는 보지 말 것.)`n"
$codexTpl  = "# Round 1 - Codex 독립 조사 결과`n`n(PROBLEM.md만 보고 조사. Claude 결과는 보지 말 것.)`n"
$noGit = "파일 저장까지만 해라. git add/commit/push는 하지 마라 - 오케스트레이터가 처리한다."

function Need($cmd) {
  if (-not (Get-Command $cmd -ErrorAction SilentlyContinue)) { throw "'$cmd' 를 찾을 수 없다. 설치/PATH 확인." }
}

function Invoke-Git() {
  Write-Host "  git $args" -ForegroundColor DarkGray
  & git.exe @args
  if ($LASTEXITCODE -ne 0) { throw "git 실패: $args" }
}

function Sync-Repo($msg) {
  & git.exe add -A
  & git.exe diff --cached --quiet
  if ($LASTEXITCODE -ne 0) {
    Invoke-Git commit -m $msg
    Invoke-Git push origin main
  } else {
    Write-Host "  (변경 없음, 커밋 생략)" -ForegroundColor DarkGray
  }
}

function Invoke-Claude($prompt) {
  $out = & claude -p $prompt --permission-mode acceptEdits --disallowedTools Bash 2>&1 | Out-String
  [pscustomobject]@{ name = 'claude'; code = $LASTEXITCODE; text = $out }
}

function Show-Result($r) {
  $tail = $r.text.Trim()
  if ($tail.Length -gt 800) { $tail = '...' + $tail.Substring($tail.Length - 800) }
  Write-Host "`n--- $($r.name) (exit $($r.code)) ---`n$tail`n" -ForegroundColor Cyan
  if ($r.code -ne 0) { throw "$($r.name) 실패. 위 출력 확인." }
}

# claude(foreground) + codex(background job) 동시 실행 -> blind 보장
function Invoke-Pair($claudePrompt, $codexPrompt) {
  $codexExe = (Get-Command codex).Source
  $job = Start-Job -ScriptBlock {
    param($repo, $prompt, $exe)
    Set-Location $repo
    $last = Join-Path $repo '.codex_last.txt'
    '' | & $exe exec -C $repo -s workspace-write --skip-git-repo-check --ephemeral -o $last $prompt 2>&1 | Out-Null
    $code = $LASTEXITCODE
    $text = if (Test-Path $last) { Get-Content $last -Raw -Encoding UTF8 } else { '(출력 없음)' }
    Remove-Item $last -Force -ErrorAction SilentlyContinue
    [pscustomobject]@{ name = 'codex'; code = $code; text = "$text" }
  } -ArgumentList $repo, $codexPrompt, $codexExe

  $c = Invoke-Claude $claudePrompt
  $x = Receive-Job -Job $job -Wait -AutoRemoveJob

  Show-Result $c
  Show-Result $x
}

function Reset-Round() {
  $cf = Join-Path $repo 'round1\claude.md'
  $cur = if (Test-Path $cf) { Get-Content $cf -Raw -Encoding UTF8 } else { '' }
  if ($cur.Trim() -and $cur.Trim() -ne $claudeTpl.Trim()) {
    $stamp = Get-Date -Format 'yyyyMMdd_HHmmss'
    $dest = Join-Path $repo "rounds\$stamp"
    New-Item -ItemType Directory -Force -Path $dest | Out-Null
    Get-ChildItem (Join-Path $repo 'round1') -Filter *.md |
      ForEach-Object { Move-Item $_.FullName (Join-Path $dest $_.Name) }
    Write-Host "이전 라운드 -> rounds\$stamp" -ForegroundColor Yellow
  }
  New-Item -ItemType Directory -Force -Path (Join-Path $repo 'round1') | Out-Null
  Set-Content (Join-Path $repo 'round1\claude.md') $claudeTpl -Encoding utf8
  Set-Content (Join-Path $repo 'round1\codex.md')  $codexTpl  -Encoding utf8
  foreach ($s in 'claude_review.md', 'codex_review.md') {
    Remove-Item (Join-Path $repo "round1\$s") -Force -ErrorAction SilentlyContinue
  }
}

# ---------------- main ----------------
Need git.exe; Need claude; Need codex
$q = ($Question -join ' ').Trim()

Write-Host "`n[0/4] git pull" -ForegroundColor Green
Invoke-Git pull --ff-only origin main

$problemPath = Join-Path $repo 'PROBLEM.md'
if ($q) { Set-Content $problemPath "# 이번에 풀 문제`n`n$q`n" -Encoding utf8 }
$body = ((Get-Content $problemPath -Raw -Encoding UTF8) -replace '#.*이번에 풀 문제', '').Trim()
if (-not $body) { throw "PROBLEM.md가 비어있고 인자도 없다. 문제를 넣어라." }
Write-Host "문제: $body" -ForegroundColor White

Reset-Round
Sync-Repo "라운드 시작: PROBLEM.md 갱신"

Write-Host "`n[1/4] 독립 조사 (blind, 병렬)" -ForegroundColor Green
Invoke-Pair `
  "round1/claude.md 에 PROBLEM.md에 대한 너의 독립 분석을 써라. round1/codex.md 는 읽지 마라. 중요한 주장에 근거(코드/실행결과/데이터/공식문서)를 붙여라. $noGit" `
  "round1/codex.md 에 PROBLEM.md에 대한 너의 독립 분석을 써라. round1/claude.md 는 읽지 마라. 최대한 많이 찾고 코드/실행으로 실제 확인해라. $noGit"
Sync-Repo "round1: 독립 조사"

Write-Host "`n[2/4] 교차검증" -ForegroundColor Green
Invoke-Pair `
  "round1/codex.md 를 읽고 너의 round1/claude.md 와 대조해라. 공통점 / 충돌(가장 중요) / Codex가 더 맞는 점 / 틀린 점 / 네가 놓친 점을 round1/claude_review.md 에 써라. 네 답이 틀렸으면 round1/claude.md 도 고쳐라. $noGit" `
  "round1/claude.md 를 읽고 너의 round1/codex.md 와 대조해라. 공통점 / 충돌 / Claude가 더 맞는 점 / 틀린 점 / 네가 놓친 점을 round1/codex_review.md 에 써라. 코드/실행으로 검증해라. $noGit"
Sync-Repo "round1: 교차검증"

Write-Host "`n[3/4] DECISION.md 초안 (Claude)" -ForegroundColor Green
$d = Invoke-Claude "round1/ 의 claude.md, codex.md, claude_review.md, codex_review.md 4개를 모두 읽고 DECISION.md 를 갱신해라: ## 공통 의견 / ## 충돌 (제일 중요) / ## 권고안 (근거 포함). '## 내 최종 결정 + 이유' 항목은 제목만 두고 내용은 비워서 사용자가 채우게 남겨라. $noGit"
Show-Result $d
Sync-Repo "DECISION.md 초안"

Write-Host "`n[4/4] 완료." -ForegroundColor Green
Write-Host ('=' * 60)
Get-Content (Join-Path $repo 'DECISION.md') -Raw -Encoding UTF8
Write-Host ('=' * 60)
Write-Host "`n충돌 항목을 보고 DECISION.md 의 '내 최종 결정'을 직접 채워라." -ForegroundColor Yellow
