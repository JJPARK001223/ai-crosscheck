param([Parameter(Mandatory = $true, ValueFromRemainingArguments = $true)] [string[]] $Question)

$ErrorActionPreference = 'Stop'
& (Join-Path $PSScriptRoot 'orchestrate.ps1') @Question
exit $LASTEXITCODE
