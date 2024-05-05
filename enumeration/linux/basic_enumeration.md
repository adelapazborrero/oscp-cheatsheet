
# Users
```bash
cat /etc/passwd
```

-----------------------

# Mounted fylesystems and disks
```bash
cat /etc/fstab
lsblk
lsmod
/sbin/modinfo libata
```

-----------------------

# Writable files
```bash
find / -writable -type d 2>/dev/null
```

-----------------------

# Installed applications
```bash
dpkg -l
```

-----------------------

# Scheduled tasks
```bash
ls -lah /etc/cron*
sudo crontab -l
cat /etc/crontab
```

-----------------------

# Listening ports
```bash
ss -anp
```

-----------------------

# Linux release 
```bash
cat /etc/issue
cat /etc/os-release
```

-----------------------


# SUID
```bash
find / -perm -u=s -type f 2>/dev/null
```

-----------------------

# SGID
```bash
find / -perm -g=s -type f 2>/dev/null
```

-----------------------

# search particular filename
```bash
find / -name "*GENERIC*" -ls
```

-----------------------

# print env variables
```bash
env
```
