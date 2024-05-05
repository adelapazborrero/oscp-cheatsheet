# Checking wifi driver
```bash
sudo airmon-ng
```
-----------------------

# Check USB devices
```bash
sudo lsusb -vv
```
-----------------------

# Check loaded Modules for wifi driver
```bash
sudo modinfo <driver>
sudo modinfo iwlwifi # in thinkpad t480
```
-----------------------

# Change parameters in drivers
```bash
sudo modprobo <driver>
sudo modprobe ath9k_htc blink=0 # turn blink off
```
-----------------------

# List all modules
```bash
lsmod | grep iwlwifi
```
-----------------------

# Unloading modules for driver
```bash
sudo rmmod ath
```
-----------------------

# List wireless devices
```bash
iw list
```
-----------------------

# List AP (access points) within range
```bash
# dev wlan0 specifies our device
sudo iw dev wlan0 scan | grep SSID

# also get DS Parameter set
sudo iw dev wlan0 scan | egrep "DS Parameter set|SSID:"
```
-----------------------

# Create VIF (Virtual interface) in monitor mode
```bash
# Create the interface
sudo iw dev wlan0 interface add wlan0mon type monitor

# Is down by default, we set it UP
sudo ip link set wlan0mon up

# Test that is up by siffing with tcpdump
sudo tcpdump -i wlan0mon

# Once finished we delete the interface
sudo iw dev wlan0mon interface del

# Verify it's deleted
sudo iw dev wlan0mon info
```
-----------------------

# Check current regulatory domain
```bash
sudo iw reg get
```
-----------------------

# Update regulatory domain for current country
```bash
# Check ISO/IEC 3166-1 alpha 2 list for country initials
iw reg set <COUNTRY>

# For permanent change update the following file
/etc/default/crda 
# Update value of the following variable with contry initials
REGDOMAIN

```

-----------------------

# List WiFi and bluetooth devices (only able to block at soft level)
```bash
sudo rfkill list

# Soft blocked: blocked at software level
# Hard blocked: blocked at hardware or BIOS level
```
-----------------------


# Block and Unblock WiFi or Bluetooth
```bash
sudo rfkill list

sudo rfkill block 1     # Blocks Device 1
sudo rfkill list 1      # Verify Device 1 blocked
sudo rfkill unblock 1   # Unblock Device 1
sudo rfkill block all   # Block all
```
-----------------------

