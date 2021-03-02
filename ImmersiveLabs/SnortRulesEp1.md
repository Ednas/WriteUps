About:
A network sensor known as an Intrusion Detection System (IDS) or Intrusion Protection System (IPS) is a key part of any network security strategy. A commercial IDS will typically come with its own pack of rules but also allows analysts to create signature-based rules. This lab focuses on creating Snort-based signatures.

MITRE ATT&CK 
T1059 Command-Line Interface, https://attack.mitre.org/versions/v6/techniques/T1059/
T1068 Exploitation for Privilege Escalation, https://attack.mitre.org/versions/v6/techniques/T1068/

Lab:

example
alert tcp 10.10.10.0/24 any -> 192.168.0.0/24 443 (msg: “Test Rule”; content: “This is some content”; sid: 5000001; rev: 1;)

Question 1
Create a Snort rule that will alert on traffic using TCP with a destination port of 443. Validate the rule in the PCAP scanner and enter the token.
alert tcp any any -> any 443  (msg: "Testing Alert" ; sid:1000002)

Question 2
What is the name of the content modifier that can be used to alert on HTTP Status Codes?
http_stat_code

Question 3
What is the token generated when you create a Snort rule that will detect outbound traffic using TCP to ports 443 and 447?

alert tcp any any -> any 447 (msg: "Testing Alert" ; sid:1000001)
alert tcp any any -> any 443  (msg: "Testing Alert" ; sid:1000002)

Question 4
What is the token generated when you create a Snort rule that will detect all ICMP traffic?
alert icmp any any -> any any (msg: "Testing Alert" ; sid:1000001)

Question 5
Modify this rule, so that it only alerts if the content matches in the first three bytes: 'alert tcp any any -> any any (msg:"Immersive Labs Question 5"; content:"|37 e1 a4|"; sid:1000001;)', then enter the token that is generated.
Need to add depth: 3; after the content
alert tcp any any -> any any (msg:"Immersive Labs Question 5"; content:"|37 e1 a4|"; depth: 3; sid:1000001;)