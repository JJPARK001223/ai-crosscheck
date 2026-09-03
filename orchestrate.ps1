param([Parameter(ValueFromRemainingArguments = $true)] [string[]] $Question)

$ErrorActionPreference = 'Stop'
$repo = $PSScriptRoot
Set-Location $repo
$workerMark = '[CROSSCHECK_WORKER]'
$noGit = '파일만 저장하고 git 명령은 실행하지 마라. orchestrate.ps1을 다시 실행하지 마라.'

function Need([string]$Command) {
  if (-not (Get-Command $Command -ErrorAction SilentlyContinue)) {
    throw "'$Command' 명령을 찾을 수 없습니다. 설치와 로그인을 확인하세요."
  }
}

function Invoke-Git {
  & git.exe @args
  if ($LASTEXITCODE -ne 0) { throw "git 실패: $args" }
}

function Sync-Repo([string]$Message) {
  & git.exe add -A
  & git.exe diff --cached --quiet
  if ($LASTEXITCODE -ne 0) {
    Invoke-Git commit -m $Message
    Invoke-Git push origin main
  }
}

function Show-Monitor([string]$Phase, [datetime]$Started, [object[]]$Jobs, [string[]]$Files) {
  $elapsed = [int]((Get-Date) - $Started).TotalSeconds
  $states = ($Jobs | ForEach-Object { "$($_.Name)=$($_.State)" }) -join ', '
  Write-Host "[1분 점검] 단계=$Phase, 경과=${elapsed}초, $states" -ForegroundColor Yellow
  foreach ($file in $Files) {
    $path = Join-Path $repo $file
    if (Test-Path $path) {
      $item = Get-Item $path
      Write-Host "  $file : $($item.Length) bytes, 수정 $($item.LastWriteTime.ToString('HH:mm:ss'))"
    } else {
      Write-Host "  $file : 아직 없음"
    }
  }
}

function Wait-Workers([string]$Phase, [object[]]$Jobs, [string[]]$Files) {
  $started = Get-Date
  Show-Monitor $Phase $started $Jobs $Files
  while (@($Jobs | Where-Object State -eq 'Running').Count -gt 0) {
    Start-Sleep -Seconds 60
    $Jobs | ForEach-Object { Get-Job -Id $_.Id | Out-Null }
    Show-Monitor $Phase $started $Jobs $Files
  }

  $results = @($Jobs | Receive-Job -Wait)
  $Jobs | Remove-Job -Force
  foreach ($result in $results) {
    $tail = "$($result.text)".Trim()
    if ($tail.Length -gt 800) { $tail = '...' + $tail.Substring($tail.Length - 800) }
    Write-Host "`n--- $($result.name) (exit $($result.code)) ---`n$tail" -ForegroundColor Cyan
    if ($result.code -ne 0) { throw "$($result.name) 작업이 실패했습니다." }
  }
}

function Start-ClaudeWorker([string]$Name, [string]$Prompt) {
  Start-Job -Name $Name -ScriptBlock {
    param($Repo, $Prompt)
    Set-Location $Repo
    $out = & claude -p $Prompt --permission-mode acceptEdits --disallowedTools Bash 2>&1 | Out-String
    [pscustomobject]@{ name = 'Claude'; code = $LASTEXITCODE; text = $out }
  } -ArgumentList $repo, $Prompt
}

function Start-CodexWorker([string]$Name, [string]$Prompt) {
  $exe = (Get-Command codex.cmd -CommandType Application -ErrorAction Stop).Source
  Start-Job -Name $Name -ScriptBlock {
    param($Repo, $Prompt, $Exe)
    Set-Location $Repo
    $last = Join-Path $Repo '.codex_last.txt'
    & $Exe exec -C $Repo -s workspace-write --skip-git-repo-check --ephemeral -o $last $Prompt 2>&1 | Out-Null
    $code = $LASTEXITCODE
    $text = if (Test-Path $last) { Get-Content $last -Raw -Encoding UTF8 } else { '(출력 없음)' }
    Remove-Item $last -Force -ErrorAction SilentlyContinue
    [pscustomobject]@{ name = 'Codex'; code = $code; text = $text }
  } -ArgumentList $repo, $Prompt, $exe
}

function Require-Result([string]$RelativePath, [int]$MinimumLength = 80) {
  $path = Join-Path $repo $RelativePath
  if (-not (Test-Path $path)) { throw "필수 결과가 없습니다: $RelativePath" }
  $body = Get-Content $path -Raw -Encoding UTF8
  if ($body.Trim().Length -lt $MinimumLength) { throw "결과가 너무 짧습니다: $RelativePath" }
}

function Reset-Round {
  $round = Join-Path $repo 'round1'
  if (Test-Path $round) {
    $hasWork = Get-ChildItem $round -File -ErrorAction SilentlyContinue | Where-Object Length -gt 80
    if ($hasWork) {
      $archive = Join-Path $repo ("rounds\" + (Get-Date -Format 'yyyyMMdd_HHmmss'))
      New-Item -ItemType Directory -Force -Path $archive | Out-Null
      Get-ChildItem $round -File | ForEach-Object { Move-Item $_.FullName $archive }
    }
  }
  New-Item -ItemType Directory -Force -Path $round | Out-Null
  Set-Content (Join-Path $round 'claude.md') "# Claude 독립 조사 결과`n" -Encoding UTF8
  Set-Content (Join-Path $round 'codex.md') "# Codex 독립 조사 결과`n" -Encoding UTF8
  Remove-Item (Join-Path $round 'claude_review.md') -Force -ErrorAction SilentlyContinue
  Remove-Item (Join-Path $round 'codex_review.md') -Force -ErrorAction SilentlyContinue
  Remove-Item (Join-Path $repo 'FINAL.md') -Force -ErrorAction SilentlyContinue
}

Need git.exe
Need claude
Need codex

$questionText = ($Question -join ' ').Trim()
Invoke-Git pull --ff-only origin main
if ($questionText) {
  Set-Content (Join-Path $repo 'PROBLEM.md') "# 이번에 풀 문제`n`n$questionText`n" -Encoding UTF8
}
$problem = Get-Content (Join-Path $repo 'PROBLEM.md') -Raw -Encoding UTF8
if (-not $problem.Trim()) { throw '질문 또는 PROBLEM.md 내용이 필요합니다.' }

Reset-Round
Sync-Repo '교차검증 작업 시작'

Write-Host '[1/3] Claude와 Codex 독립 조사' -ForegroundColor Green
$blindJobs = @(
  Start-ClaudeWorker 'blind-claude' "$workerMark PROBLEM.md만 읽고 독립적으로 조사하여 round1/claude.md에 근거와 함께 작성하라. round1/codex.md는 읽지 마라. $noGit"
  Start-CodexWorker 'blind-codex' "$workerMark PROBLEM.md만 읽고 독립적으로 조사하여 round1/codex.md에 근거와 함께 작성하라. round1/claude.md는 읽지 마라. $noGit"
)
Wait-Workers '독립 조사' $blindJobs @('round1/claude.md','round1/codex.md')
Require-Result 'round1/claude.md'
Require-Result 'round1/codex.md'
Sync-Repo 'round1 독립 조사 완료'

Write-Host '[2/3] 상호 교차검증' -ForegroundColor Green
$reviewJobs = @(
  Start-ClaudeWorker 'review-claude' "$workerMark round1/codex.md와 round1/claude.md를 대조하고 공통점, 충돌, Codex의 오류, Claude가 놓친 점을 round1/claude_review.md에 기록하라. 근거를 직접 확인하라. $noGit"
  Start-CodexWorker 'review-codex' "$workerMark round1/claude.md와 round1/codex.md를 대조하고 공통점, 충돌, Claude의 오류, Codex가 놓친 점을 round1/codex_review.md에 기록하라. 가능한 것은 실행으로 검증하라. $noGit"
)
Wait-Workers '교차검증' $reviewJobs @('round1/claude_review.md','round1/codex_review.md')
Require-Result 'round1/claude_review.md'
Require-Result 'round1/codex_review.md'
Sync-Repo 'round1 교차검증 완료'

Write-Host '[3/3] Claude Code 최종 종합' -ForegroundColor Green
$finalPrompt = "$workerMark PROBLEM.md와 round1의 네 결과 파일을 모두 읽고 직접 판단하라. DECISION.md에는 공통 의견, 핵심 충돌, 판단 근거를 기록하고, 사용자에게 전달할 최종 답변을 FINAL.md에 완결된 형태로 작성하라. 최종 답변의 작성자는 Claude Code임을 첫 줄에 표시하라. $noGit"
$finalJobs = @(Start-ClaudeWorker 'final-claude' $finalPrompt)
Wait-Workers 'Claude 최종 종합' $finalJobs @('DECISION.md','FINAL.md')
Require-Result 'DECISION.md'
Require-Result 'FINAL.md'
Sync-Repo 'Claude Code 최종 답변 완료'

Write-Host "`n===== Claude Code 최종 답변 =====" -ForegroundColor Green
Get-Content (Join-Path $repo 'FINAL.md') -Raw -Encoding UTF8
