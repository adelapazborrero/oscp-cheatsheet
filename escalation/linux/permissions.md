# SUDO (GTFObins)
```bash
sudo -l
```

-----------------------

# SUID (GTFObins)
```bash
find / -perm -u=s -type f 2>/dev/null
```

-----------------------

# SGID (GTFObins)
```bash
find / -perm -g=s -type f 2>/dev/null
```

-----------------------

# CAPABILITIES (GTFObins)
```bash
/usr/sbin/getcap -r / 2>/dev/null
# If we find cap_setuid+ep 
```

-----------------------

# UNSHADOW 
```bash
cp /etc/passwd passwd
cp /etc/shadow shadow

unshadow passwd shadow > unshadow.txt

john --wordlist=/usr/share/wordlist/rockyou.txt unshadow.txt
```

 
