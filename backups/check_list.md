# Looking for initial foothold
  - ( ) Site gobuster
  - ( ) Site feroxbuster
  - ( ) LFI
  - ( ) File upload
  - ( ) Remote Mouse
  - ( ) Exposed Git

# Privesc Linux

# MS01 Initial foothold
  - ( ) SharpUp
  - ( ) Check privileges (token?)
  - ( ) Check AD users for spraying
  - ( ) Check stored credentials `cmdkey /list`
  - ( ) If password is available, Kerberoast
  - ( ) Check history files
  - ( ) Look for kdbx files
  - ( ) Check processes
  - ( ) Check files on User directories
  - ( ) Dirtypipez?
  - ( ) Windows.old?

# MS01 Post exploit
  - ( ) If Admin user and is on local and need domain access use web service to get a shell
  - ( ) Dump hashes
  - ( ) Spray hashes/pass to MS02 (winrm)
  - ( ) Spray hashes/pass to MS02 (smb)
  - ( ) Spray hashes/pass to MS02 (mssql)
  - ( ) Spray hashes/pass to MS02 (passrdp)
  - ( ) Spray hashes/pass to local-auth
  - ( ) Kerberoast
  - ( ) AS-REProast

# MS02 Initial foothold
  - ( ) SharpUp
  - ( ) Check privileges (token?)
  - ( ) Check AD users for spraying
  - ( ) Check stored credentials `cmdkey /list`
  - ( ) If password is available, Kerberoast
  - ( ) Check history files
  - ( ) Look for kdbx files
  - ( ) Check processes
  - ( ) Check files on User directories
  - ( ) Dirtypipez?
  - ( ) Windows.old?

# MS02 Post exploit
  - ( ) Dump hashes
  - ( ) RDP?
