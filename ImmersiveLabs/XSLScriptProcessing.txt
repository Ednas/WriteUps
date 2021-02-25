XSL Script Processing
Extensible Stylesheet Language (XSL) files are used for the processing and rendering of data within XML files. They support complex code operations and include support for embedded scripting in multiple languages. Microsoft developed a command utility to process these called msxsl.exe.
https://immersivelabs.online/labs/xsl-script-processing/

MITE ATT&CK XSL Script Processing
https://attack.mitre.org/versions/v6/techniques/T1220/

XSL Script Processing
Question 1
What does XSL stand for?
Extensible Stylesheet Language

Question 2
Analyse the stylesheet popPS.xsl. Which tag is responsible for executing the script?
JScript

Question 3
What language is the script written in?
JScript

Question 4
What is the correct usage of msxsl.exe?
Msxsl.exe XML XSL

Question 5
What is the token you receive after using the command ‘Get-Token’ in PSShell?
DefenceEvasionWithStyle

Opened Command Prompt
Saw there were 3 files on the desktop.
Ran this command:
msxsl.exe customers.xml popPS.xsl

This opened up another Command Prompt, but with PS as the initials, letting me know I'd be running PowerShell commands.
In here I ran:
Import-Module -Name C:\Users\Administrator\Get-Token
Followed by:
Get-Token
Which returned 

DefenceEvasionWithStyle