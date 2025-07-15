# Mounting and Editing ISO Files in Linux

## What is an ISO?

An **ISO file** is a disk image that contains the exact structure and contents of a CD, DVD, or Blu-ray. It is commonly used to distribute OS images (like Ubuntu), installers, or backups. Most ISO files use the **ISO 9660 filesystem**, which is **read-only by design**.

---

## Why You Cannot Mount ISO Files with Write Access

ISO 9660 is inherently **read-only**, meaning:
- You **cannot modify** its contents directly when mounted.
- Even if you use mount options like `-o rw`, they have no effect.
- To make changes, you'll need to **extract the contents**, **edit them**, and (optionally) **create a new ISO**.

---

## Step 1: Mount an ISO (Read-Only)

To mount the ISO:

```bash
sudo mkdir /mnt/iso
sudo mount -o loop BornToSecHackMe-v1.1.iso /mnt/iso
```

### Explanation:

* -o loop tells the system to treat the ISO file as a block device.

* /mnt/iso is the mount point (create it if it doesn’t exist).

* The contents will now be accessible at /mnt/iso, but not writable.

## Step 2: Copy ISO Contents to a Writable Directory

```
mkdir ~/iso-modified
cp -r /mnt/iso/* ~/iso-modified/
```

## Step 3: Extract filesystem.squashfs Using unsquashfs

```
cd ~/iso-modified
sudo unsquashfs casper/filesystem.squashfs
```
### Explanation:

* unsquashfs is a tool from squashfs-tools that extracts a read-only compressed root filesystem.

* This creates a directory called squashfs-root/ which contains the entire root filesystem.

## 🔍 Step 4: Investigate `.bash_history` File

After extracting the ISO and unpacking `filesystem.squashfs`, you may want to inspect user activity within the live environment. One useful file is the `~/.bash_history` file, which stores the commands executed by users in the shell.

### 🔸 Navigate to the Home Directory

If you've extracted `filesystem.squashfs` (e.g. to `squashfs-root/`), navigate into the expected home directory:

```bash
sudo cat squashfs-root/root/.bash_history
```
Finding
While inspecting the history, we found the following command:
```
adduser zaz
```
This indicates that a new user named zaz was added during the creation or modification of the image.

Immediately following that, we observed what appears to be zaz password:

```
646da671ca01bb5d84dbb5fb2238dc8e
```

we can now user exploit_me to gain root access like in writeup1.