& (Join-Path (Split-Path $PSScriptRoot -Parent) 'Invoke-CodexStage.ps1') -PromptPath (Join-Path $PSScriptRoot 'prompt.txt') -HandoffFiles 'round41/codex.md'
