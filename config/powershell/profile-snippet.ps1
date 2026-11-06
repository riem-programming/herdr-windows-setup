# Append to the PowerShell 7 profile ($PROFILE).
# zoxide: `z <name>` jumps to a frequently used directory, `zi` opens an interactive picker.
Invoke-Expression (& { (zoxide init powershell | Out-String) })
