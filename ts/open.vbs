Set WshShell = WScript.CreateObject("WScript.Shell")

exeName = "E:\Education\4.2\keylogger_making\output\test_main.exe"

statusCode = WshShell.Run (exeName, 1, true)