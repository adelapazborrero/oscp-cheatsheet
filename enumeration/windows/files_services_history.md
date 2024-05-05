# search files recursively
```bash
Get-ChildItem -Path C:\Users\ -Include *.kdbx -File -Recurse -ErrorAction SilentlyContinue
Get-ChildItem -Path C:\xampp -Include *.txt,*.ini -File -Recurse -ErrorAction SilentlyContinue
Get-ChildItem -Path C:\Users\ -Include *.txt,*.pdf,*.xls,*.xlsx,*.doc,*.docx -File -Recurse -ErrorAction SilentlyContinue
```

-----------------------
# get permissions
```bash
icacls auditTracker.exe
```

-----------------------
# get service info
```bash
Get-Service * | Select-Object Displayname,Status,ServiceName,Can*
Get-CimInstance -ClassName win32_service | Select Name,State,PathName | Where-Object {$_.State -like 'Running'}
type C:\xampp\mysql\bin\my.ini
```
(if password found, remember `runas /user:backupadmin cmd`)

-----------------------
# Search history
```bash
Get-History
(Get-PSReadlineOption).HistorySavePath
type C:\Users\dave\AppData\Roaming\Microsoft\Windows\PowerShell\PSReadLine\ConsoleHost_history.txt
type C:\Users\Public\Transcripts\transcript01.txt
```

-----------------------
# Connect to MSSQL database
```bash
impacket-mssqlclient Administrator:Lab123@192.168.50.18 -windows-auth
```
-----------------------

# installed apps (32 bit)
```bash
Get-ItemProperty "HKLM:\SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Uninstall\*" | select displayname
```
-----------------------

# installed apps (64 bit)
```bash
Get-ItemProperty "HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\*" | select displayname
```

-----------------------

# running processes
```bash
Get-Process
```
