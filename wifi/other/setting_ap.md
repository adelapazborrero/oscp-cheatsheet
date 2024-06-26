# Setting up an Access Point
  Setting up an access point requires two distinct network interfaces, and involves five steps:

  1. Configure Internet access on the system.
  2. Set up a static IP for the wireless interface.
  3. DHCP server set up, to provide automatic IP configuration for Wi-Fi clients.
  4. Add routing to provide Internet access to the Wi-Fi clients.
  5. Configure the Wi-Fi interface in AP mode.

-----------------------

# Set static IP for wireless interface
```bash
sudo ip link set wlan0 up
# Use an IP that is not yet assigned
sudo ip addr add 192.168.2.32/24 dev wlan0
```
-----------------------

# Setup DHCP server

Create dnsmasq.conf
```bash
# Main options
# http://www.thekelleys.org.uk/dnsmasq/docs/dnsmasq-man.html
domain-needed
bogus-priv
no-resolv
filterwin2k
expand-hosts
domain=localdomain
local=/localdomain/
# Only listen on this address. When specifying an 
# interface, it also listens on localhost.
# We don't want to interrupt any local resolution
listen-address=192.168.2.32


# DHCP range
dhcp-range=192.168.2.100,192.168.2.199,12h
dhcp-lease-max=100
# Router: wlan0
dhcp-option=option:router,192.168.2.32
dhcp-authoritative

# DNS: Primary and secondary Google DNS
server=8.8.8.8
server=8.8.4.4
```

Start DNS
```bash
sudo dnsmasq --conf-file=dnsmasq.conf

# To confirm
sudo tail /var/log/syslog | grep dnsmasq
```
-----------------------

# Add routing

Enable IP forwarding
```bash
echo 1 | sudo tee /proc/sys/net/ipv4/ip_forward
```
Add routing
```bash
sudo apt install nftables
sudo nft add table nat
sudo nft 'add chain nat postrouting { type nat hook postrouting priority 100 ; }'
sudo nft add rule ip nat postrouting oifname "eth0" ip daddr != 10.0.0.1/24 masquerade
```
-----------------------

# Create access point

Create hostapd.conf config file
```bash
interface=wlan0
ssid=BTTF
channel=11

# 802.11n
hw_mode=g
ieee80211n=1

# WPA2 PSK with CCMP
wpa=2
wpa_key_mgmt=WPA-PSK
rsn_pairwise=CCMP
wpa_passphrase=GreatScott
```
Start AP
```bash
sudo hostapd hostapd.conf
```
