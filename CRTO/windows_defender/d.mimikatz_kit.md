# Build and Load Mimikatz kit

```bash
cd /mnt/c/Tools/cobaltstrike/arsenal-kit/kits/mimikatz
./build.sh

# Check the binaries static signatures
C:\Tools\ThreatCheck\ThreatCheck\bin\Debug\ThreatCheck.exe -f C:\Tools\cobaltstrike\artifacts\mimikatz\mimikatz64.exe

# Check the binaries dynamic signatures
C:\Tools\ThreatCheck\ThreatCheck\bin\Debug\ThreatCheck.exe -f C:\Tools\cobaltstrike\artifacts\mimikatz\mimikatz64.exe -d

# Check the binaries dynamic signatures with the process ThreatCheck
C:\Tools\ThreatCheck\ThreatCheck\bin\Debug\ThreatCheck.exe -f C:\Tools\cobaltstrike\artifacts\mimikatz\mimikatz64.exe -d -p

# Load mimikatz.cna via the Cobalt Strike > Script Manager menu and clicking the Load button.
# After loading the CNA, Mimikatz will now function as expected.
```
