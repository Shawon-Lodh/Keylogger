Set WshShell = WScript.CreateObject("WScript.Shell")

exeName = "C:\Users\shawon\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\test_main.exe"

statusCode = WshShell.Run (exeName, 1, true)