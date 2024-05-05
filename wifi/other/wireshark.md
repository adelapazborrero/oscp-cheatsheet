
# Set WiFi adapter in Monitor mode
```bash
sudo ip link set wlan0 down
sudo iwconfig wlan0 mode monitor
sudo ip link set wlan0 up
```
-----------------------

# Set WiFi adapter in Managed mode
```bash
sudo ip link set wlan0 down
sudo iwconfig wlan0 mode managed 
sudo ip link set wlan0 up
```
-----------------------

# Dumping traffic for available channels
```bash
sudo airodump-ng wlan0mon
```
-----------------------

# Wireshark binary help
```bash
wireshark --help
```
-----------------------

# Wireshark display interfaces
```bash
sudo wireshark -D
```
-----------------------

# Wireshark dump start
```bash
sudo wireshark -i wlan0mon -k
sudo wireshark -i 4 -k # 4 is number of interface
```
-----------------------

# Wireshark set interface in monitor and dump start
```bash
sudo wireshark -i wlan0 -I -k
```
-----------------------

# Wireshark open saved files
```bash
wireshark saved-file.pcap
```
-----------------------

# Dumping data with tcpdump
```bash
sudo tcpdump -i wlan1 -w - -U
```
-----------------------

# Dumping data with dumpcap 
```bash
sudo dumpcap -w - -P -i wlan1
```
-----------------------

# Dumping data with tshark
```bash
sudo tshark -w - -i wlan1
```
-----------------------

# Pipe dump output to wireshark
```bash
sudo tcpdump -U -w - -i wlan1 | wireshark -k -i -
```
-----------------------

# Named Pipe dump output to wireshark
```bash
# Create a pipe
mkfifo /tmp/named_pipe

# Forward dump to pipe
sudo wireshark -k -i /tmp/named_pipe

# Start dump
sudo tcpdump -U -w - -i wlan1 > /tmp/named_pipe
```
-----------------------

# Remotely dumping to local wireshark
```bash
ssh root@10.11.0.196 "sudo -S tcpdump -U -w - -i <interface>" | sudo wireshark -k -i -
```
-----------------------

