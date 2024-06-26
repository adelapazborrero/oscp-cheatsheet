# PowerView

https://github.com/PowerShellMafia/PowerSploit

```bash
powershell-import C:\Tools\PowerSploit\Recon\PowerView.ps1

# Get Domain info
powerpick Get-Domain

# Get Domain Controller info
powerpick Get-DomainController | select Forest, Name, OSVersion | fl

# Get Forest Domain info
powerpick Get-ForestDomain

# Get Domain policy data (Good for finding password policy)
powerpick Get-DomainPolicyData | select -expand SystemAccess

# Get info about domain user
powerpick Get-DomainUser -Identity jking -Properties DisplayName, MemberOf | fl
powerpick Get-DomainUser -Properties DisplayName, MemberOf | fl

# Return all computers in the domain
powerpick Get-DomainComputer -Properties DnsHostName | sort -Property DnsHostName

# Search for all organization units (OUs) or specific OU objects
powerpick Get-DomainOU -Properties Name | sort -Property Name

# Return all domain groups or specific domain group objects.
powerpick Get-DomainGroup | where Name -like "*Admins*" | select SamAccountName

# Return the members of a specific domain group.
powerpick Get-DomainGroupMember -Identity "Domain Admins" | select MemberDistinguishedName

# Return all Group Policy Objects (GPOs) or specific GPO objects
powerpick Get-DomainGPO -Properties DisplayName | sort -Property DisplayName

# Returns all GPOs that modify local group membership through Restricted Groups or Group Policy Preferences
powerpick Get-DomainGPOLocalGroup | select GPODisplayName, GroupName

# Enumerates the machines where a specific domain user/group is a member of a specific local group
powerpick Get-DomainGPOUserLocalGroupMapping -LocalGroup Administrators | select ObjectName, GPODisplayName, ContainerName, ComputerName | fl

# Return all domain trusts for the current or specified domain.
powerpick Get-DomainTrust
```

---

# ADSearch LDAP searches

```bash
# Search users
execute-assembly C:\Tools\ADSearch\ADSearch\bin\Release\ADSearch.exe --search "objectCategory=user"

# Search for groups ending in Admin
execute-assembly C:\Tools\ADSearch\ADSearch\bin\Release\ADSearch.exe --search "(&(objectCategory=group)(cn=*Admins))"

# complex queries
execute-assembly C:\Tools\ADSearch\ADSearch\bin\Release\ADSearch.exe --search "(&(objectCategory=group)(cn=MS SQL Admins))" --attributes cn,member
```

---

# SharpView (C# viersion of PowerView) - no piping

```bash
execute-assembly C:\Tools\SharpView\SharpView\bin\Release\SharpView.exe Get-Domain
```
