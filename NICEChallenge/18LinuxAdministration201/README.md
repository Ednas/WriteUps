# Challenge 18 Linux Administration 201: 101 + Network Integration

## Challenge Details
Challenge #T0129 
Linux Administration 201: 101 + Network Integration
Author: Jeff Echlin
Framework Category: Operate and Maintain
Specialty Area: Network Services
Work Role: Network Operations Specialist
Task Description: Integrate new systems into existing network architecture.

### Scenario

Dedeker Randolph, a new temporary security consultant, requires a workstation. Ms. Randolph started today and does not have access to her Kali Linux workstation, nor is that workstation setup to access the network properly. Company network policy dictates that all devices on the network must have the IP address, gateway, and DNS server statically assigned in it by our IT staff (i.e. you). Company policy also dictates that all systems have a up to date DNS entry in the DNS server. This system will be integrated into the overall network but will not be managed by Active Directory. This is due to the nature of Dedeker's work which is highly sensitive. Thus, her system will be on the network and she will need a local account on her workstation, not our single sign-on solution

### Additional Information

Once you have completed the requested tasks, you will need to document the methodology you used with as much detail and professionalism as necessary. This should be done on the documentation tab within the workspace once the challenge is deployed. Below the main documentation section be sure to include a tagged list of applications you used to complete the challenge.

Until the IP address is set correctly all but one of the checks will be orange and display the status "unknown".

-----
## Meeting Briefing


`Dedeker Randolph @drandolph`: 
Hello, I was scheduled to begin work today but I seem to have no access to my workstation. 
The workstation at my desk does not really seem to be setup at all! Please help!

`Richard LeGrand @rlegrand`:
I JUST GOT THIS EMAIL FROM THE NEW TEMPORARY SECURITY CONSULTANT. MS. RANDOLPH DOES NOT YET HAVE
 AN ACCOUNT OR CONNECTED SYSTEM THIS SHOULD HAVE BEEN DONE LONG AGO AND I DON'T HAVE TIME FOR THIS, FIX IT.

`Gary Thatcher @gthatcher`:
Hello @playerone as you can see things are a bit stressful lately and I have not had time to work on 
some of these more trivial matters, many other things have taken my attention so I 
leave the task in your capable hands. @gbates will tell you more.

`Gilly Bates @gbates`:
Hi @playerone, I have been assigned to help you along with adding Ms. Randolph, 
our new temporary security consultant, to our network. There are certain considerations that must be taken into account. 
Her workstation should be assigned 172.16.30.6 for the IP address; 
make sure to set the right subnet mask as well. We are a /24 network if you didn't know. 
Based on the IP address that would mean her workstation is in the Internal subnet and the gateway you set should reflect as such. 
The DNS server address also needs to be manually set on her workstation so it can resolve internal and external names. 
Since our DNS server also happens to be our Domain-Controller, you can find it's IP address on the network map. 
Oh! Almost forgot, you will need to add a DNS entry for her workstation in the DNS server on the Domain-Controller. 
Her workstation FQDN should be SecConsultantKali.ad.daswebs.com and to make it all match up the workstation hostname needs to be set to SecConsultantKali.

`Gilly Bates @gbates`:
So.. that takes care of all the network stuff I think. 
Once you are done with that you need to make sure she has sufficent local machine access so she can get her sensitive work done. 
Our naming guidelines are always first initial plus last name (all lowercase) for usernames so we will just do that here for Ms. Randolph. 
Not sure how you usually create users but just make sure her user account also gets a home directory in the usual /home/herusername/ way. 
Also, since I'm not sure what she is doing, or if we should ask, just give her full sudo access on her workstation. Anything else @drandolph?

`Dedeker Randolph @drandolph`:
All that sounds fine to me. As one other thing I'd like @playerone, make sure my default shell is bash. Other then that we are good! Thanks!

---
## Steps taken to complete the required actions

Starting off, I have the following machines available for me to access and checks left to complete

![VMsAvailable](./images/VMsAvailableAndChecks.PNG)

I was given the following Network diagram map

![OM-map](./images/OM-map.jpg)


Going into the Kali Security machine, I proceeded with the following steps

## USER SETUP

First, check if user exists
`less /etc/passwd`

Then let's add drandolph to the users

`sudo useradd -m drandolph`

Now I need to add the bash terminal as the users terminal.

`sudo usermod --shell /bin/bash drandolph`

And then I check to make sure that went through
`grep drandolph /etc/passwd`

Another option that I came across for for shell
`chsh -s /bin/bash drandolph`

Now to add drandolph to the list of sudoers

`sudo usermod -a -G sudo drandolph`

## NETWORKING

Next I need to make sure this machine is set up and connected to the network.

First I tried to change a file

`sudo nano /etc/resolvconf/resolv.conf.d/head`
This worked a little at first, but then I realized that it should be in 

`sudo nano /etc/resolv.conf`


domain daswebs.com
search ad.daswebs.com
nameserver 172.16.30.5
nameserver 8.8.8.8

Now I need to update the interfaces file

`nano /etc/network/interfaces`

address 172.16.30.6
netmask 255.255.255.0
gateway 172.16.30.2
network 172.16.30.5
broadcast 172.16.30.255

and added the networking there as well. To refresh I ran:

`ifup eth0`

I would like to check if I'm able to connect to the network, so I ping the Domain Controller

`ping 172.16.30.5`

Now to set the host name on the Kali box I ran:

`hostname SecConsultantKali`

![KaliNetwork](./images/KaliNetworking.PNG)

## UPDATES ON THE DOMAIN CONTROLLER


On the domain controller, went to Server Manager > Roles > DNS Server > DNS > W2K8-AD-DHCP > Forward Lookup Zones > ad.daswebs.com 

In here I right clicked the white space to add a new A record for SecConsultantKali, I proceeded through the prompts and also checked to add a new PTR record.

Next I went up to Reverse Lookup Zones, for ad.daswebs.com added new PTR record
Host IP Address 172.16.30.6
SecConstultantKali.ad.daswebs.com

![Domain Controller](./images/DomainController.PNG)

Once all of these steps were completed, I had finished my task, which I was able to verify by the green checkmarks next to the required tasks.

![Green Checkmarks](./images/NICEChallengeSubmissions.PNG) 

### NICE Framework KSA
A0055. Ability to operate common network tools (e.g., ping, traceroute, nslookup).
A0058. Ability to execute OS command line (e.g., ipconfig, netstat, dir, nbtstat).
A0059. Ability to operate the organization's LAN/WAN pathways.
K0011. Knowledge of capabilities and applications of network equipment including routers, switches, bridges, servers, transmission media, and related hardware.
K0029. Knowledge of organization's Local and Wide Area Network connections.
K0050. Knowledge of local area and wide area networking principles and concepts including bandwidth management.
K0061. Knowledge of how traffic flows across the network (e.g., Transmission Control Protocol [TCP] and Internet Protocol [IP], Open System Interconnection Model [OSI], Information Technology Infrastructure Library, current version [ITIL]).
K0076. Knowledge of server administration and systems engineering theories, concepts, and methods.
K0111. Knowledge of network tools (e.g., ping, traceroute, nslookup)
K0332. Knowledge of network protocols such as TCP/IP, Dynamic Host Configuration, Domain Name System (DNS), and directory services.
S0162. Skill in applying various subnet techniques (e.g., CIDR)
CAE Knowledge Units
Basic Networking
Network Technology and Protocols
Operating Systems Administration
