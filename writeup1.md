# Writeup 1 – Intended Path

## 🖥️ Initial Setup
When booting the Boot2Root machine, no IP address was provided. To establish connectivity:

- I configured a Host-Only Network in the VM settings.The virtual network automatically assigned an IP address to the machine.
- To discover the machine’s IP, I performed a network scan from my attacking machine using the following command:
```
    nmap 192.168.56.1/24
```
Nmap Results:

> Nmap scan report for 192.168.56.100<br>
Host is up (0.000071s latency).<br>
All 1000 scanned ports on 192.168.56.100 are in ignored states.<br>
Not shown: 1000 filtered tcp ports (proto-unreach)<br>
MAC Address: 08:00:27:C1:16:A0 (PCS Systemtechnik/Oracle VirtualBox virtual NIC)<br>
> Nmap scan report for 192.168.56.101<br>
Host is up (0.00031s latency).<br>
Not shown: 994 closed tcp ports (reset)<br>
PORT    STATE SERVICE<br>
21/tcp  open  ftp<br>
22/tcp  open  ssh<br>
80/tcp  open  http<br>
143/tcp open  imap<br>
443/tcp open  https<br>
993/tcp open  imaps<br>
MAC Address: 08:00:27:99:04:36 (PCS Systemtechnik/Oracle VirtualBox virtual NIC)<br>

From the scan, the target machine is 192.168.56.101.

## 🔍 Service Enumeration
The open ports identified on the target machine were:
```
21/tcp  open  ftp
22/tcp  open  ssh
80/tcp  open  http
143/tcp open  imap
443/tcp open  https
993/tcp open  imaps
```
Among these, SSH, FTP, HTTP, and HTTPS were of particular interest.

- ### Web Services :
    - Accessing http://192.168.56.101 showed a simple webpage containing only the word “hackme” with no additional content or functionality.Inspecting the page source and elements revealed no useful information or client-side code.

    - Checking the HTTPS site (https://192.168.56.101) at the root path.

- ### Subdomain Discovery:
    Further probing for possible subdomains on the HTTPS server uncovered several interesting web services:

    - phpMyAdmin — a web-based MySQL administration interface.

    - Webmailer — a webmail client interface.

    - Forum — a discussion board containing posts and user data.

    The forum was functional and allowed user logins, providing a potential entry point for further exploration.
## 🔍 Forum and Credential Harvesting
-  ### Forum Access :
    - Inside the forum, I found a post titled “Login problems” which contained logs of failed login attempts by a user named lmezard.
    
    - Upon closer inspection of the post content, I noticed what appeared to be a password entered into the login input box. Although it wasn’t linked to a username, I suspected this was a leaked password.
    
    - I tested this password by attempting to log in as lmezard on the forum itself, and it worked successfully.

    - Exploring lmezard’s profile, I found an associated email address.

- ### Webmailer Access
    - Using the same email address and the password from the forum, I logged into the webmailer service. The credentials were accepted, granting me access to lmezard’s mailbox.

    - Inside the mailbox, I discovered an email containing database credentials with the username root.

- ### Database Access 
    - After gaining database access, I created a SQL file on the server containing queries to execute system commands. This allowed me to run commands directly on the server.
    - While navigating the file system, I discovered a directory named LOOKATME. Inside this directory, there was a file named password.
    - I tested the contents of this password file in various authentication systems and services on the machine but initially found no success.
    - Eventually, I tried using this password as the authentication code for the FTP service. This attempt was successful, granting me access to the FTP server.

- ### Ftp Access
    - Inside the FTP server, I found several .pcap files. When I tried to open them with Wireshark, they did not appear to be valid .pcap files.
    - I manually inspected the files and noticed they contained scattered chunks of C code, but the code was out of order.
    - I gathered all the contents from these files into a single file, reconstructed the correct order of the code, and then compiled and executed it.
    - After running the executable, the program output:
        ```
        "MY PASSWORD IS : Iheartpawnage"
        ```
    - Alongside the .pcap files, there was also a Readme file that instructed me to hash the password and use the resulting hash as the SSH password for the user laurie.

    - I generated the hash using Python:
        
        >import hashlib<br>
        >hashlib.sha256(b'Iheartpawnage').hexdigest()

        Result :
        ```
        '330b845f32185747e4f8ca15d40ca59796035c89ea809fb5d30f4da83ecf45a4'
        ```
    This is the SSH password for the user laurie.
- ### Laurie Access
    







