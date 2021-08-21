# Challenge 28 Digital Duplicates

![DigitalDupes](../Event/NICE28a.png)

## Author
    Edna J.
    WGU NICE Challenge
    DASWebs Inc.
    June 27, 2021

## Challenge Details
Framework Category: Investigate
Specialty Area: Digital Forensics
Work Role: Law Enforcement/CounterIntelligence Forensics
Task Description: Create a forensically sound duplicate of the evidence (i.e., forensic image) that ensures the original evidence is not unintentionally modified, to use for data recovery and analysis processes. This includes, but is not limited to, hard drives, floppy diskettes, CDs, PDAs, mobile phones, GPS, and all tape formats. (T0048)

### Scenario
Recently Gary Thatcher our senior system administrator, came across a thumb drive attached to an employee's system. According to the employee, the thumb drive was attached without their consent and they are unsure of the origin of said drive. The drive was passed to Ione Leventis one of our security analysts. Ione has attached the drive to our sheep-dip system which in our case is the Security-Desk machine. However, Ione was called away on other matters and you are now entrusted with the task. According to current company policy the thumb drive must be inspected for any malicious agents that could threaten DAS Web's overall security. Your job is to create a forensically sound duplicate image of the thumb drive using dcfldd so it can be examined without the risk of inadvertently modifying potential evidence. SHA512 hashes should also be taken and compared between the original thumb drive which is already attached, but not mounted, to the system and the forensic image.

-----
## Meeting Briefing

![Meeting Info](./images/meeting.PNG)


---
## Tools used

 - dcfldd
 - Kali
 - SHA512


## Steps taken to complete the required actions

Starting off, I have the following machines available for me to access and checks left to complete

![VMsAvailable](./images/VMsAvailable.PNG)

I was given the following Network diagram map

![OM-map](./images/OM-map.jpg)

#### The tasks that I was working on completing were
1. Use dcfldd to make a forensically sound image and hash of the thumb drive

2. Store the image in /forensicimages/forensicimage.dd

3. Take a SHA512 hash of the thumb drive and compare it to the hash originally created with dcfldd.


### Task 1 Use dcfldd to make a forensically sound image and hash of the thumb drive

The first thing that I did was try to get familiar with the tool that was requested that I use for this task. I checked the man pages and googled the tool to read the online documentaion. I was able to find that this command `dcfldd` has a lot of options available. With that much information, I went and searched for a write up for the best way to complete the tasks I needed with this tool. I came across the blog [Imaging Using dcfldd](https://dfir.blog/imaging-using-dcfldd/) on DFIR.blog's webpage. This was an excellent blog to follow for this task.

The commands that I ran were:

```dcfldd man```

```ls -lha /dev | grep sd```
![Grep](./images/SecDeskGrepSD.PNG)

Seeing the results of the grep command, I was able to figure out that sda is the main drive, which makes sdb the flashdrive. With this information, I know that my target for imaging is /dev/sdb

The task required me to save the imaged file to a folder called forensicimages, I created that directory. 
```cd /```
```sudo mkdir /forensicimages```


### Task 2 Store the image in /forensicimages/forensicimage.dd

Using the dcfldd command, I created the forensic image and saved the hashlog to a text file.

```sudo dcfldd if=/dev/sdb of=/forensicimages/forensicimage.dd hash=sha512 hashlog=/forensicimages/forensicimage.txt```

![Forensics](./images/SecDeskForensicImageCreation.PNG)

### Task 3 Take a SHA512 hash of the thumb drive and compare it to the hash originally created with dcfldd

Using the vf option dcfldd command I'm able to verify that the original file and the forensic image have the same hash and that they match.

```dcfldd if=/dev/sdb vf=/forensicimages/forensicimage.dd verifylog=/forensicimages/forensicimage.txt```

![SHA512](./images/SecDeskVerifySHA512.PNG)


## Caveats
If you're working through this challenge and running into issues, the following might be the issue.
- You mounted the drive, this would make changes to the hash
- You used one of the partials, ex. sdb1 instead of the whole drive sdb


(Get this info before deploying challenge or after)
### NICE Framework KSA
    K0017. Knowledge of concepts and practices of processing digital forensic data.
    K0021. Knowledge of data backup and recovery.
    K0042. Knowledge of incident response and handling methodologies.
    K0060. Knowledge of operating systems.
    K0117. Knowledge of file system implementations (e.g., New Technology File System [NTFS], File Allocation Table [FAT], File Extension [EXT]).
    K0118. Knowledge of processes for seizing and preserving digital evidence.
    K0122. Knowledge of investigative implications of hardware, Operating Systems, and network technologies.
    K0132. Knowledge of which system files (e.g., log files, registry files, configuration files) contain relevant information and where to find those system files.
    K0133. Knowledge of types of digital forensics data and how to recognize them.
    K0304. Knowledge of concepts and practices of processing digital forensic data.
    S0047. Skill in preserving evidence integrity according to standard operating procedures or national standards.
    S0065. Skill in identifying and extracting data of forensic interest in diverse media (i.e., media forensics).
    S0067. Skill in identifying, modifying, and manipulating applicable system components within Windows, Unix, or Linux (e.g., passwords, user accounts, files).
    S0073. Skill in using virtual machines. (e.g., Microsoft Hyper-V, VMWare vSphere, Citrix XenDesktop/Server, Amazon Elastic Compute Cloud, etc.).
    S0089. Skill in one-way hash functions (e.g., Secure Hash Algorithm [SHA], Message Digest Algorithm [MD5]).

### CAE Knowledge Units
    Cybersecurity Principles
    Digital Forensics
    IT Systems Components
    Operating Systems Concepts

### NICE Framework 1.0 Mapping (August 2012 - August 2017)
480 - Create a forensically sound duplicate of the evidence (i.e., forensic image) that ensures the original evidence is not unintentionally modified, to use for data recovery and analysis processes. This includes, but is not limited to, hard drives, floppy diskettes, compact discs (CD3), personal digital assistants (PDAS), mobile phones, global positioning satellite devices (GPSS), and all tape formats

#### NICE Framework 1.0 KSA
217. Skill in preserving evidence integrity according to standard operating procedures or national standards
24. Knowledge of basic concepts and practices of processing digital forensic data
287. Knowledge of file system implementations (e.g., New Technology File System [NTFS], File Allocation Table [FAT], File Extension [EXT])
29. Knowledge of data backup, types of backups (e.g., full, incremental), and recovery concepts and tools
290. Knowledge of processes for seizing and preserving digital evidence (e.g., chain of custody)
346. Knowledge of which system files (e.g., log files, registry files, configuration files) contain relevvant information and where to find those system files
386. Skill in using virtual machines
61. Knowledge of incident response and handling methodologies
90. Knowledge of operating systems

#### NICE Framework 1.0 Competencies
    Computer Forensics
    Cryptography
    Data Management

## References:

https://dfir.blog/imaging-using-dcfldd/

https://www.computerhope.com/unix/sha512sum.htm


## Note:
This challenge also had this alternative flyer
![DigitalDupes](../Event/NICE28.png)