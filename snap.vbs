Dim oShell
Set oShell = WScript.CreateObject ("WScript.Shell")
oShell.run "C:\path\snap.bat", 0, False
Set oShell = Nothing