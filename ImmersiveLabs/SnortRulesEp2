About: Snort DNS

As seen in Episode 1, Snort rules are powerful but difficult to write. In the rest of this series you will take real examples and construct Snort rules to detect malicious behaviour. 

In this episode we will take a closer look at alerting on Domain Name System (DNS) requests.


Lab:

Question 1
Create a Snort rule to detect all DNS Traffic, then test the rule with the scanner and submit the token.
alert udp any any <> any 53 (msg: "Testing Alert" ; sid:1000001)

Question 2
Create a rule to detect DNS requests to 'icanhazip', then test the rule with the scanner and submit the token.
alert udp any any -> $HOME_NET 53 (msg: "Alert"; sid:1000001; content: "|69 63 61 6e 68 61 7a 69 70|"; )

Question 3
Create a rule to detect DNS requests to 'interbanx', then test the rule with the scanner and submit the token.
alert udp any any -> $HOME_NET 53 (msg: "Alert"; sid:1000001; content: "|69 6e 74 65 72 62 61 6e 78|"; )

Question 4
Which of the following would cause DNS to use TCP instead of UDP?

	A. If the response is greater than 512 bytes

	B. Tasks like zone transfers

	C. Explicitly set by the DNS operator

	D. All of them

Answer: All of them


Example
https://github.com/dnlongen/Snort-DNS/blob/master/local.rules
log udp any 53 <> $HOME_NET any (sid:10000007; rev:001;)


Q2 attempts
ASCII
alert udp any any <> $HOME_NET 53 (msg: "Alert"; sid:1000001; content: "|09 105 099 097 110 104 097 122 105 112|"; )
HEX
alert udp any any <> $HOME_NET 53 (msg: "Alert"; sid:1000001; content: "|09|69 63 61 6e 68 61 7a 69 70|00|"; )
HEX w/out length
alert udp any any <> $HOME_NET 53 (msg: "Alert"; sid:1000001; content: "|69 63 61 6e 68 61 7a 69 70|"; )
	Matched 2 packages