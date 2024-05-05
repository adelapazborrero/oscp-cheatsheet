# Linux processes
```bash
ps aux
```

-----------------------

# Linux processes updating
```bash
watch -n 1 "ps aux | grep pass"
```

-----------------------

# Linux network connections
```bash
sudo tcpdump -i lo -A | grep "pass"
```

-----------------------

# Cron logs
```bash
grep "CRON" /var/log/syslog
```
