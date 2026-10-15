$ErrorActionPreference='Continue'
Set-Location "J:\Desktop\공학\ai-crosscheck"
Get-Content -Raw -Encoding UTF8 "round35\prompt_B.txt" | codex exec -C "J:\Desktop\공학\ai-crosscheck" -s workspace-write --add-dir "J:\Desktop\XLPR" --skip-git-repo-check - *> "round35\run_B.log"
"EXIT $LASTEXITCODE" | Out-File -Append -Encoding utf8 "round35\run_B.log"
