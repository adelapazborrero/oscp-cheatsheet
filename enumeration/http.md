
# Directory discovery
```bash
feroxbuster --url http://192.168.45.223
gobuster dir -t20 --wordlist /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -u http://192.168.216.121 -x aspx
gobuster dir -u http://192.168.232.121 -e -k -w /usr/share/wordlists/SecLists/Discovery/Web-Content/directory-list-lowercase-2.3-medium.txt -t 100 -x xml,aspx,asp --add-slash -o gobuster_scan
```

-----------------------

# Subdomain discovery
```bash
gobuster vhost --wordlist /home/kali/repos/projects/SecLists/Discovery/DNS/subdomains-top1million-110000.txt -u http://oscp.exam:8000 --exclude-length 334
wfuzz -c -f sub-fighter -w /usr/share/wordlists/SecLists/Discovery/DNS/subdomains-top1million-110000.txt -u 'http://analytical.htb' -H "Host: FUZZ.analytical.htb" --hw 10
```

-----------------------

# wfuzz
```bash
wfuzz -w /home/kali/repos/projects/SecLists/Discovery/DNS/subdomains-top1million-110000.txt http://192.168.238.150:8080/search?FUZZ=FUZZ
```

-----------------------

# kiterunner to enumerate API endpoints
```bash
kiterunner scan http://192.168.243.143/api/ -w routes-small.kite -x 20
```

-----------------------


# enumerate wordpress sites

```bash
# default enumeration
wpscan --url http://10.10.10.88/webservices/wp

# enumerates vulnerable plugins
wpscan --url http://10.10.10.88/webservices/wp --enumerate vp

# enumerates all plugins
wpscan --url http://10.10.10.88/webservices/wp --enumerate ap

# enumerate all plugins using proxy
wpscan --url http://10.10.10.88/webservices/wp/index.php --proxy socks5://127.0.0.1:8080 --enumerate ap

# enumerate everything
wpscan --url http://10.10.10.88/webservices/wp/index.php --proxy socks5://127.0.0.1:8080 --enumerate ap tt at
```
