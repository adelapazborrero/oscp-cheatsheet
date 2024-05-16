# Dictionary attack

```bash
hashcat.exe -a 0 -m 1000 ntlm.txt rockyou.txt -r rules\add-year.rule
```

---

# Mask attack

```bash

    ?l = abcdefghijklmnopqrstuvwxyz
    ?u = ABCDEFGHIJKLMNOPQRSTUVWXYZ
    ?d = 0123456789
    ?h = 0123456789abcdef
    ?H = 0123456789ABCDEF
    ?s = «space»!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
    ?a = ?l?u?d?s
    ?b = 0x00 - 0xff

hashcat -a 3 -m 1000  ntlm.txt ?u?l?l?l?l?l?d --force
```

---

# Mask attack and length

```bash
PS C:\> cat example.hcmask
?d?s,?u?l?l?l?l?1
?d?s,?u?l?l?l?l?l?1
?d?s,?u?l?l?l?l?l?l?1
?d?s,?u?l?l?l?l?l?l?l?1
?d?s,?u?l?l?l?l?l?l?l?l?1


hashcat -a 3 -m 1000 ntlm.txt example2.hcmask
```

---

# Combinator attack

PS C:\> cat list1.txt
purple

PS C:\> cat list2.txt
monkey
dishwasher

```bash
hashcat -a 1 -m 1000 ntlm.txt list1.txt list2.txt -j $- -k $!

ef81b5ffcbb0d030874022e8fb7e4229:purple-monkey!
```

---

# Hybrid attack

```bash
# Append dynamic values
hashcat -a 6 -m 1000 ntlm.txt list.txt ?d?d?d?d

be4c5fb0b163f3cc57bd390cdc495bb9:Password5555


# Prepend dynamic values
hashcat -a 7 -m 1000 ntlm.txt ?d?d?d?d list.txt

28a3b8f54a6661f15007fca23beccc9c:5555Password
```

---

# KwProcessor (https://github.com/hashcat/kwprocessor)

```bash
kwp64.exe basechars\custom.base keymaps\uk.keymap routes\2-to-10-max-3-direction-changes.route -o keywalk.txt
```

---
