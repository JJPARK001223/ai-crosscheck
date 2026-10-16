[CmdletBinding()]
param(
    [Parameter(Mandatory = $true)][string]$PromptPath,
    [string]$LogPath,
    [string[]]$HandoffFiles = @(),
    [string[]]$AdditionalDirectory = @('J:\Desktop\XLPR')
)

$ErrorActionPreference = 'Stop'
$OutputEncoding = [Text.UTF8Encoding]::new($false)
[Console]::OutputEncoding = [Text.UTF8Encoding]::new($false)
$repoRoot = $PSScriptRoot
if ($HandoffFiles.Count -eq 0) { throw 'Specify HandoffFiles: assigned reports whose commit/push must be verified' }
foreach ($handoffPath in $HandoffFiles) {
    $handoffFullPath = [IO.Path]::GetFullPath((Join-Path $repoRoot $handoffPath))
    if ([IO.Path]::IsPathRooted($handoffPath) -or -not $handoffFullPath.StartsWith($repoRoot + [IO.Path]::DirectorySeparatorChar, [StringComparison]::OrdinalIgnoreCase)) {
        throw "Handoff path must be relative and inside the repository: $handoffPath"
    }
}
$promptFile = if ([IO.Path]::IsPathRooted($PromptPath)) { $PromptPath } else { Join-Path $repoRoot $PromptPath }
$promptFile = (Resolve-Path -LiteralPath $promptFile).Path
$codexCommand = (Get-Command codex.cmd -ErrorAction Stop).Source
foreach ($extraPath in $AdditionalDirectory) {
    if (-not (Test-Path -LiteralPath $extraPath -PathType Container)) { throw "Additional directory missing: $extraPath" }
}
if (-not $LogPath) {
    $LogPath = Join-Path (Split-Path $promptFile -Parent) ('codex_' + (Get-Date -Format 'yyyyMMdd_HHmmss_fff') + '.log')
}
if (-not [IO.Path]::IsPathRooted($LogPath)) { $LogPath = Join-Path $repoRoot $LogPath }
if (Test-Path -LiteralPath $LogPath) { throw "Refusing to overwrite existing log: $LogPath" }
if (-not (Test-Path -LiteralPath (Split-Path $LogPath -Parent) -PathType Container)) { throw 'Log directory missing' }
$promptText = Get-Content -LiteralPath $promptFile -Raw -Encoding UTF8
if ([string]::IsNullOrWhiteSpace($promptText)) { throw 'Prompt must not be empty' }
$guard = @'
[CROSSCHECK_WORKER]
Do not start another AI or orchestration script. Perform only the assigned stage.
For authorized Git commands that write metadata or access the network (pull, fetch, add, commit, push, ls-remote), use sandbox_permissions=require_escalated with a clear justification on the FIRST attempt. The workspace-write sandbox protects .git; do not intentionally run these commands unprivileged first. Read-only local status/log/diff may run normally. If access is still denied, report the exact error. Do not disable the sandbox.
If approvals are unsupported or rejected, report the exact action and reason and leave Git handoff incomplete. Never claim completion without verifying the commit and remote branch.
Do not read the other AI's findings during a blind stage. Stage only explicitly assigned output files.
Complete the Git handoff of assigned result reports unless the user explicitly forbids Git changes. Commit only those reports, push, and verify the remote branch; report any incomplete handoff.
'@
$codexArguments = @('exec', '-C', $repoRoot, '--approve-for-me', '--skip-git-repo-check')
foreach ($extraPath in $AdditionalDirectory) { $codexArguments += @('--add-dir', $extraPath) }
$codexArguments += '-'
Write-Host "Codex stage: workspace-write + automatic approval review. Log: $LogPath"
# Native stderr contains normal CLI progress. Preserve it without treating each line as a PowerShell exception.
$logStream = [IO.File]::Open($LogPath, [IO.FileMode]::CreateNew, [IO.FileAccess]::Write, [IO.FileShare]::Read)
$logWriter = [IO.StreamWriter]::new($logStream, [Text.UTF8Encoding]::new($false))
$logWriter.AutoFlush = $true
$logWriteFailed = $false
$ErrorActionPreference = 'Continue'
try {
    ($guard + "`nAssigned Git handoff files: " + ($HandoffFiles -join ', ') + "`n`n" + $promptText) | & $codexCommand @codexArguments 2>&1 | ForEach-Object {
        try { $logWriter.WriteLine($_.ToString()) } catch { $logWriteFailed = $true; throw }
        Write-Output $_.ToString()
    }
    $stageExitCode = $LASTEXITCODE
} finally {
    $logWriter.Dispose()
    $logStream.Dispose()
}
$ErrorActionPreference = 'Stop'
if ($logWriteFailed) { throw 'Codex log write failed' }
$logText = Get-Content -LiteralPath $LogPath -Raw -Encoding UTF8
$headerText = ($logText -split '(?m)^--------\s*$', 3)[1]
if (-not $headerText -or $headerText -notmatch '(?m)^approval:[ \t]*on-request[ \t]*\r?$' -or $headerText -notmatch '(?m)^sandbox:[ \t]*workspace-write(?:[ \t]+\[[^\r\n]*\])?[ \t]*\r?$') {
    throw "Approval policy verification failed; inspect $LogPath"
}
if ($stageExitCode -ne 0) { throw "Codex exited with code $stageExitCode; inspect $LogPath" }
foreach ($handoffPath in $HandoffFiles) {
    & git -C $repoRoot ls-files --error-unmatch -- $handoffPath > $null
    if ($LASTEXITCODE -ne 0) { throw "Untracked/missing handoff: $handoffPath" }
    $pendingReport = & git -C $repoRoot status --porcelain -- $handoffPath
    if ($LASTEXITCODE -ne 0 -or $pendingReport) { throw "Uncommitted handoff: $handoffPath" }
}
$branchName = & git -C $repoRoot branch --show-current
if ($LASTEXITCODE -ne 0 -or -not $branchName) { throw 'Cannot verify detached or invalid branch' }
$headSha = & git -C $repoRoot rev-parse HEAD
if ($LASTEXITCODE -ne 0) { throw 'Cannot read local HEAD' }
$remoteLine = & git -C $repoRoot ls-remote origin "refs/heads/$branchName"
if ($LASTEXITCODE -ne 0 -or -not $remoteLine -or ($remoteLine -split '\s+')[0] -ne $headSha) { throw 'Git handoff incomplete: local HEAD and remote branch differ or remote query failed' }
Write-Output "VERIFIED_GIT_HANDOFF $headSha $($HandoffFiles -join ',')"
