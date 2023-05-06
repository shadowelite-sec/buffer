#!/bin/python3
import sys

code = sys.argv[1]
print("{}".format(code))
print(bytes.fromhex(code).decode('ascii'))

