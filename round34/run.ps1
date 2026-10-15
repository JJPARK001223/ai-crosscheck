$ErrorActionPreference='Continue'
Set-Location "J:\Desktop\공학\ai-crosscheck"
Get-Content -Raw -Encoding UTF8 "round34\prompt.txt" | codex exec -C "J:\Desktop\공학\ai-crosscheck" -s workspace-write --add-dir "J:\Desktop\XLPR" --skip-git-repo-check - *> "round34\codex_run.log"
"EXIT $LASTEXITCODE" | Out-File -Append -Encoding utf8 "round34\codex_run.log"
