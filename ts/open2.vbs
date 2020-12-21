SET oShell = WScript.CreateObject("Wscript.Shell")
Dim source_code_path
source_code_path = "E:\Education\4.2\keylogger_making\ts\sample.py" 

Dim currentCommand 
currentCommand = "cmd /c " & Chr(34) & source_code_path
WScript.echo currentCommand
oShell.run currentCommand,1,True