Set-Location "J:\Desktop\공학\ai-crosscheck"
Get-Content -Raw -Encoding UTF8 "round40\prompt.txt" | codex.cmd exec -C "J:\Desktop\공학\ai-crosscheck" --sandbox workspace-write --approve-for-me --add-dir "J:\Desktop\XLPR" --skip-git-repo-check - *> "round40\run.log"
"EXIT $LASTEXITCODE" | Out-File -Append -Encoding utf8 "round40\run.log"
