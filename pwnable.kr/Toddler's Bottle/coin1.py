from pwn import *

def create_mesg(N1, N3):
    mesg = ''
    for i in range(N1, N3):
        mesg += str(i) + ' '

    return mesg

def main():
    shell = remote('pwnable.kr', 9007)
    shell.recvuntil('- Ready? starting in 3 sec... -\n')
    shell.recvuntil('N=')
    data = shell.recvline()
    data = data.split('C=')   
    N = int(data[0])
    C = int(data[1])
    print N, C
    
    N1 = 1
    N2 = 0
    N3 = N
    
    for i in range(0, 100):
        for j in range(C+1):
            N2 = (N1 + N3) / 2
            #print j
            mesg = create_mesg(N1, N2)
            #print mesg
            shell.sendline(mesg)
            
            counterfeit_check = shell.recv(2048)

            if ("Correct" in counterfeit_check):
                print counterfeit_check
                break

            if(int(counterfeit_check)%10==9): #counterfeit coin
                N3 = N2 + 1

            elif (int(counterfeit_check)%10==0):
                N1 = N2

        data = shell.recv(1024)
        
        if ("ngrats!" in data):
            print data
            break
        
        data = data.split(' ')
        N = int(data[0][2:])
        C = int(data[1][2:])
        
        N1 = 1
        N2 = 0
        N3 = N
        
        print N, C
    
    print shell.recv(1024)
    
main()
