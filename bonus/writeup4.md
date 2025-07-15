### Step-by-Step: Boot to a Root Shell Using `init=/bin/sh`

## 1. Boot the ISO in VirtualBox

Start the VM and **quickly press `Esc` or `Shift`** during the boot splash to access the GRUB bootloader menu.

## 2. Enter Recovery Mode

Since recovery mode allows root-level access, we can **override the default init process** by appending `init=/bin/sh` to the kernel line.

![GRUB edit screen](../srcs/Screenshot%20From%202025-07-15%2023-29-45.png)
