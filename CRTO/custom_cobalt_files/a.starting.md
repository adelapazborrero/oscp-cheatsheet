# Todo On Start

1. Build artifacts (iterate until threatcheck is clean)
2. Build resources (iterate until threatcheck is clean)
3. Build mimikatz
4. Load our custom profile and start server
5. Load our custom aggressor script
6. Create our custom AMSI bypass
7. Create listeners
8. Create all payloads
9. Host manual amsi bypass

# Create new profile Start server on teamserver

# sudo ./teamserver 10.10.5.50 Passw0rd! c2-profiles/normal/typ0.profile

```bash
# create service
sudo vim /etc/systemd/system/teamserver.service

[Unit]
Description=Cobalt Strike Team Server
After=network.target
StartLimitIntervalSec=0

[Service]
Type=simple
Restart=always
RestartSec=1
User=root
WorkingDirectory=/home/attacker/cobaltstrike
ExecStart=/home/attacker/cobaltstrike/teamserver 10.10.5.50 Passw0rd! c2-profiles/normal/typ0.profile

[Install]
WantedBy=multi-user.target

# reload daemon and start service
sudo systemctl daemon-reload
sudo systemctl status teamserver.service
sudo systemctl start teamserver.service
sudo systemctl enable teamserver.service
```
