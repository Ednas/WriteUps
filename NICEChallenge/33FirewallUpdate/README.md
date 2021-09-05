# Challenge NUM  NAME OF CHALLENGE

## Author
Edna J.
WGU NICE Challenge
Pretty Safe Electronics
9/4/2021

## Challenge Details


### Scenario


-----
## Meeting Briefing

![Meeting Info](./images/Meeting.PNG)

`Ashley Steele`
So I was reading up on different firewall implementations and found out that iptables has actually been replaced by nftables.

`Ricardo Cortes`
Replaced? Are our systems at risk?

`Ashley Steele`
Not quite. Our current iptables rulesets on our machines will continue doing their jobs just fine, however it is recommended to migrate iptables rules to nftables and to configure all new firewalls with nftables instead.

`Ricardo Cortes`
Should we make the switch? Is it pretty difficult?

`Ashley Steele`
Newer linux distributions will be coming with nftables by default and it does have advantages, so I would recommend switching over. In fact, I would entirely remove iptables. Fortunately nftables uses many of the same concepts as iptables; switching is very doable.

`Ricardo Cortes`
Alright then, transition Security-Desk, Prod-Joomla, and Fileshare to nftables and uninstall iptables from each machine. @playerone I want you to handle this as soon as you can!

`Jacques Raffin`
Chiming in with a word of warning for @playerone. Pay extra attention to the loopback rule for Security-Desk, as you'll likely encounter some unwanted behavior if your rules don't account for loopback traffic. Found that out the hard way.

`Ashley Steele`
Oh, wow. Yes, @jraffin is correct. Don't make any assumptions when it comes to firewalls on Kali. If loopback traffic isn't explicitly accepted, you can VERY easily find yourself with a machine in an unrecoverable state.

`Ricardo Cortes`
Yikes! Be careful, @playerone.

`Ashley Steele`
@playerone you can find the respective iptables rules backup in the home folders of the machines. You should use the default package managers on each machine to install nftables, just to keep things clean. Make sure your nftables rules function the same as the iptables rules and make sure you enable the nftables service so that it is persistent across reboots.

`Ashley Steele`
Actually, since we're doing firewall updates anyway, please allow port 443 on Prod-Joomla. The backup has it disabled, but we'll need it allowed in the coming days, so just allow it now.

`Ashley Steele`
Oh, and please have the firewalls log SSH attempts with a the prefix 'SSH DETECTED' to make parsing the logs easier. In addition to specifically logging SSH, have Prod-Joomla log all dropped packets with a prefix of 'PACKET DROPPED'.

`Ashley Steele`
I also want you to forward nftables logs to the remote syslog server on Domain-Controller. Our linux machines are already set up to send syslogs to Domain Controller, but I had recently downloaded an updated version of the remote syslogger so that still needs to be configured. The installer should be on your Desktop on Domain-Controller. Once the logs are received on Domain Controller, have it export logs of severity 'Warning' or higher to CSV files in C:\Users\playerone\Documents\Logs\. If you don't filter the logs by severity, the CSV file will be flooded with useless information. Our MSP has requested that we encode those files in UTF-8, something about their systems not being able to handle UTF-16 yet.


---
## Tools used

 - List item 1
 - List item 2
 - List item 3


## Steps taken to complete the required actions

Starting off, I have the following machines available for me to access and checks left to complete

![VMsAvailable](./images/VMs-available.PNG)

I was given the following Network diagram map

![PD-map](./images/PD-map.jpg)

#### The tasks that I was working on completing were
 - List item 1
 - List item 2
 - List item 3


### Task 1 Heading

### Task 2 Heading




(Get this info before deploying challenge or after)
### NICE Framework KSA


### CAE Knowledge Units


## References:
