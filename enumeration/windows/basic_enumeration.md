# operating system, version and architecture
```bash
systeminfo
```
-----------------------

# launch powershell
```bash
powershell -ep bypass
```
-----------------------

# list my user
```bash
whoami
```
-----------------------
# list my priv
```bash
whoami /priv
```

-----------------------
# list my groups
```bash
whoami /groups
Get-LocalGroup
```
-----------------------

# list users
```bash
net user
Get-LocalUser
```
-----------------------

# list my users details
```bash
net user <name>
Get-LocalUser <name>
```
-----------------------

# list account policy
```bash
net accounts
```
-----------------------

# existing groups
```bash
Get-LocalUser
Get-LocalGroup
Get-LocalGroupMember <GROUP-NAME>
```
-----------------------

# network information
```bash
ipconfig /all
route print
netstat -ano
```
-----------------------

# get env variables
```bash
dir env:
```

-----------------------

# get task list
```bash
tasklist /svc
tasklist /v
```
