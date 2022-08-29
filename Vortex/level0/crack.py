#!/usr/bin/env python3

import socket
import struct

with socket.create_connection( ("vortex.labs.overthewire.org", 5842)) as soc:
    sum = 0
    for i in range(0,4):
        
        tmp = soc.recv(4)
        tmp = struct.unpack("<I", tmp)[0]
        sum = (sum + tmp) % (2**32)

    # sent back sum number
    tmp = struct.pack("<I", sum)
    soc.send(tmp)
    print("sent " + str(tmp))

    # recieve response
    response=soc.recv(1024)
    print("recieved " + str(response))