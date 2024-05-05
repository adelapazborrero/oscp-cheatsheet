Good resource: https://book.hacktricks.xyz/network-services-pentesting/pentesting-snmp


# Download necessary stuff to deal with SNMP extended objects
```bash
sudo apt-get install snmp-mibs-downloader
download-mibs
sudo nano /etc/snmp/snmp.conf (comment line saying "mibs :")
```

-----------------------

# Enumerate all available communities, the wordlist can be downloaded from SecLists
```bash
onesixtyone -c common-snmp-community-strings-onesixtyone.txt 192.168.238.149 -w 100
```

-----------------------

# Simple walk
```bash
snmpbulkwalk -c public -v2c 192.168.238.149 > out.txt
snmpwalk -c public -v2c 192.168.202.149 .1
snmp-check 192.168.240.149 -p 161 -c public
```

-----------------------

# Enumerate extended objects
```bash
snmpwalk -v1 -c public 192.168.240.149 NET-SNMP-EXTEND-MIB::nsExtendObjects
snmpwalk -v1 -c public 192.168.240.149 NET-SNMP-EXTEND-MIB::nsExtendOutputFull
```
   
-----------------------
# MIB values usage

```bash
| 1.3.6.1.2.1.25.1.6.0   | System Processes |
| 1.3.6.1.2.1.25.4.2.1.2 | Running Programs |
| 1.3.6.1.2.1.25.4.2.1.4 | Processes Path   |
| 1.3.6.1.2.1.25.2.3.1.4 | Storage Units    |
| 1.3.6.1.2.1.25.6.3.1.2 | Software Name    |
| 1.3.6.1.4.1.77.1.2.25  | User Accounts    |
| 1.3.6.1.2.1.6.13.1.3   | TCP Local Ports  |
```

```bash
snmpwalk -c public -v1 192.168.50.151 1.3.6.1.4.1.77.1.2.25
```

