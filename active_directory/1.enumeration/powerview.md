# Import the module for any of the following commands
```bash
powershell -ep bypass
Import-Module .\PowerView.ps1
```

-----------------------

# Find admin access with current user in other computers
```bash
Find-LocalAdminAccess
# client74.corp.com

Get-DomainComputer -Properties DnsHostName | Resolve-IPAddress | select IPAddress,ComputerName
```

-----------------------

# Check sessions computers
```bash
Get-NetSession -ComputerName files04 -Verbose
.\PsLoggedon.exe \\files04
```

-----------------------

# Get Domain
```bash
Get-NetDomain
```

-----------------------

# Get User information
```bash
Get-NetUser
Get-NetUser | select cn,pwdlastset,lastlogon
```

-----------------------

# Get Group information
```bash
Get-NetGroup
Get-NetGroup "Sales Department" | select member
```

-----------------------

# Get computers information
```bash
Get-NetComputer
Get-NetComputer | select cn,operatingsystem,dnshostname
```

-----------------------

# Get services running by service accounts
```bash
Get-NetUser -SPN | select samaccountname,serviceprincipalname
```

-----------------------

# Get Object permissions
```bash
Get-ObjectAcl -Identity stephanie
Convert-SidToName S-1-5-21-1987370270-658905905-1781884369-1104
"S-1-5-21-1987370270-658905905-1781884369-512","S-1-5-21-1987370270-658905905-1781884369-1104","S-1-5-32-548","S-1-5-18","S-1-5-21-1987370270-658905905-1781884369-519" | Convert-SidToName
Get-ObjectAcl -Identity "Management Department" | ? {$_.ActiveDirectoryRights -eq "GenericAll"} | select SecurityIdentifier,ActiveDirectoryRights
```

-----------------------

# Get Domain shares
```bash
Find-DomainShare -CheckShareAccess
ls \\dc1.corp.com\sysvol\corp.com\
```
