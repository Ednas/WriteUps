# Linux Administration 201: 101 + Network Integration

## Challenge Details
Challenge #T0144
Interns & HR on the Domain Controller
Author: Malcolm Reed Jr.
Framework Category: Operate and Maintain
Specialty Area: Systems Administration
Work Role: System Administrator
Task Description: Manage accounts, network rights, and access to systems and equipment.

### Scenario
Recently we concluded our first intern program here at DASWebs. 
While we expected it to be valuable to the intern, Rob, after working with our techs for a while on our network he brought to our attention that he could access critical systems with his basic domain credentials. 
After which we reviewed how things were setup we found that many domain users have access to servers and shares they shouldn't. The techs and I have already outlines the basic start to fixing these issues and we want you to handle it. Refer to the Work Order Ticket for more details.

### Additional Information
More details and objectives about this challenge will be introduced during the challenge meeting, which will start 
once you begin deploying the challenge.

-----
## Meeting Briefing

`Gilly Bates @gbates`:
Maybe we should have internships more often... not sure how no one noticed these glaring configuration issues before.

`Sergio Chanel @schanel`:
Yup, yup! Clearly you guys have got plenty to do now!

`Richard LeGrand @rlegrand`:
THAT WILEY INTERN ROB! WHAT HE DID TO OUR COMPANY WAS JUST UNSPEAKABLE. LETS MAKE SURE HE HASN'T FOUND A WAY TO OUR MONEY. SENT FROM MY PHONE- DICTATED BUT NOT READ.

`Brimlock Stones @bstones`:
@rlegrand everything is fine (nothing wrong with the bank accounts), Rob did not DO anything to the company... From my understanding he merely pointed the issues out.

`Gary Thatcher @gthatcher`:
Correct @bstones, Rob just found issues already there. Did us more of a service than anything. Anywho... @playerone let me get you caught up. Turns out anyone with a domain account can log into any domain controlled servers and access the HR and accounting shares. We need to correct this asap.

`Gilly Bates @gbates`:
@playerone, based on what we (Gary and Myself) have discussed, we want you to fix this by going onto the Domain Controller server and creating some basic security groups for our non-technical users. AKA Brimlock and Sergio. These security groups should be named HRSec (for HR) and AccountingSec (for Accounting). 
Once you've made them, you'll need to put Brimlock in the Accounting Security Group and Sergio in the HR Security Group. While you're at it, also make another security group named Miscellaneous and place all other non-Admin users in that group.

`Gary Thatcher @gthatcher`:
Indeed! And after that you will use the security groups to create limitations on the users therein! Restrict both security groups from logging in to anything but the Workstation. Then limit the security groups access to the special file shares. 
Only HR should have read/write/list permissions on the domain network HR share and only Accounting should have read/write/list permissions on the domain network Accounting share. You should explicity deny all permissions on the Accounting share to the HRSec and Miscellaneous groups and explicity deny all permissions on the HR share to the AccountingSec and Miscellaneous groups. These shares are hosted from the domain but they reside on the Fileshare server in case you did not know. 
If they're not already mapped, you can use a file browser to navigate to \\BSDFILESHARE\ to access the shares.

`Gilly Bates @gbates`:
Don't forget domain admins! We will need access to both of those shares so we can manage them!

`Gary Thatcher @gthatcher`:
Thanks @gbates, almost forgot. Yeah, along with HRSec and AccountingSec respectively, both shares will need to give full access to the domain admin group. 
Oh, and now that I'm looking at it... @playerone do a little house keeping for me and disable Rob's domain account. I'd do it myself, but I somehow got removed from the Domain Admins group. Could you also add me back in?

`Gilly Bates @gbates`:
Yeah, if you could do that it'd save me some time. Just add @gthatcher back to the Domain Admins group, as he needs full access to the network shares as well.

`Gary Thatcher @gthatcher`:
Thanks. You'll need to cut access to both of those shares for all users that don't need access.
 
Now that I think about it, that Miscellaneous group that @gbates asked you to make should work for that. Once you're done making the changes to all of the groups, you'll want to log into Fileshare and restart the smbd and nmbd services to upadte the proper group members. Or you can just restart the Fileshare box. 
That'll work as well. This will allow us to properly access the files we need access to. If you don't do this, it could take up to an hour afterward before I can get access to those shares. I need that access as soon as possible..

`Richard LeGrand @rlegrand`:
GUESS HE WAS FINE. THAT CRAZY ROB. WAIT. SOMEONE ELSE HAS TO GET ME COFFEE NOW. I AM NOT GOING TO BACK TO GETTING IT FOR MYSELF. SENT FROM MY PHONE- DICTATED BUT NOT READ.

-----

## Steps taken to complete the required actions

### For disabling Robs Account:

I opened Server Manager, drilled down Roles>Active Directory Domain Services>ActiveDirectory Users and Computers>
    ad.daswebs.com> Users
Clicked on Rob, right click on Rob, select 'disable account'



DasSecGroup
right click, add Group, Security, named it HRSec

Same for 
DasSecGroup
right click, add Group, Security, named it AccountingSec
Group scope, Global, Group type: security

I then following the same steps created a security group called Miscellaneous


Right click AccountingSec, select Properties. Go to Members of, add. Enter "Brimlock Stones" then check names.
I was not able to find Brimlock Stones this way, so I went to Users, went to Brimlock Stones, clicked properties.
In the Member Of tab, I clicked on add, typed in AccountingSec, check name and add.
I follow the same steps to ghet HRSec set up

Then I add all other users that I've not put into a group in to the Miscellaneous group


To add the Windows 7 workstation to the Security group
I went to the Computers, selected W7USER-PC, clicked properties, under Member Of I added HRSec and AccountingSec
Clicked Apply, then ok.

To restrict Brimlock Stones and Sergio Chanel from accessing computers other than the Windows 7
I went to the Users Tab, right clicked on the name. Went to the Member Of tab and removed the groups that were not either
HRSec or AccountingSec, which I first had to set as the primary group.
Then going to the Account tab, I click Logon To.., the select "The following computers" and I added W7USER-PC, then click OK, Apply, then OK again.

Add Gary Thatcher to Domain Admins group

### For the shares
I went to File Services > Share and Storage Management, I see that Accounting and HR have errors

Looking into the error, I see Folder C:\HR does not exist

Looking back at the directions from the meeting, I remembered that there was special information for this scenario.
Gary Thatcher said "If they're not already mapped, you can use a file browser to navigate to \\BSDFILESHARE\ to access the shares."
In file explorer, I found that folder and saw the Accounting and HR folders
I right clicked on both and mapped them to new drive letters, Accounting got Y:/ and HR got X:/

Going to Disk Management, I opened C:/ properties, going to Sharing, under Advanced Sharing, I checked Share this folder, then Ok twice

Doing some exploring on the File Explorer, I looked at the Network, which has 3 network shares there, I tried to RDP into them and got an error
This made me go check out DHCP Server, where I saw 1 error and 2 warnings. The error has the code Event 1046, DHCP-Server
The warning was Event 10020 and the details stated "This comuter has at least one dynamically assigned IPv6 address. For reliable DHCPv6 server operation, you should use only static IPv6 addresses.

Now that I've figured it's elsewhere, I right click on the folders Accounting and HR. Click on Properties and then Security
On this tab I add AccountingSec, HRSec, Miscellaneous and Domain Admins.
Going back to the instructions:
"Once you're done making the changes to all of the groups, you'll want to log into Fileshare and restart the smbd 
and nmbd services to upadte the proper group members. Or you can just restart the Fileshare box." 

Opening up the Fileshare box, I noticed that it's FreeBSD. I logged in, used the command "su -" to switch to root, then ran the command "reboot"

