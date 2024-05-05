# Create password list from word
```bash
crunch 6 6 -t Lab%%% > wordlist
```

-----------------------

# Create user list from name
```bash
git clone https://github.com/therodri2/username_generator.git

echo "John Smith" > users.lst

python3 username_generator.py -w users.lst
```

-----------------------

# Create password list from website
```bash
cewl -w list.txt -d 5 -m 5 http://thm.labs
cewl http://192.168.159.61:8081 | grep -v CeWL > wordlist
cewl --lowercase http://192.168.159.61:8081 | grep -v CeWL > wordlist
```
