# NMAP port scanning
```bash
nmap -sC -sV <IP>
nmap -sS <IP> (Syn)
nmap -sT <IP> (Full TCP)
nmap -p- <IP>
nmap -sn <IP-RANGE> (network sweep)
sudo nmap -sU -p161 <IP>
proxychains nmap -sT --top-ports=100 -Pn <IP>
```

-----------------------

# Port scanning in windows
```bash
Test-NetConnection -Port 445 192.168.50.151
1..1024 | % {echo ((New-Object Net.Sockets.TcpClient).Connect("192.168.50.151", $_)) "TCP port $_ is open"} 2>$null
```

-----------------------

# Searching for exploits
```bash
searchsploit <SOFTWARE>

# Read exploit
searchsploit -x 1111

# Get exploit
searchsploit -m 1111
```

-----------------------

# Login with RDP
```bash
xfreerdp /cert-ignore /u:yoshi /p:"Mushroom!" /v:172.16.219.82
```

-----------------------

# KeePass database
```bash
kpcli --kdb=Database.kdbx
kpcli:/Database/Network> show -f 0

keepasssxc Database.kdbx
```

-----------------------

# Extract data from pdf
```bash
exiftool -a file.pdf 
```
