# Save as server.py 
# Message Receiver
import os
from socket import *
host = ""
port = 13001
buf = 1024
addr = (host, port)
UDPSock = socket(AF_INET, SOCK_DGRAM)
UDPSock.bind(addr)
print("Waiting to receive messages...")
i = 0
n = 0
x = 0
namelist = []
y = 0
while True:
    (data, addr) = UDPSock.recvfrom(buf)
    data = str(data)

    if data[2:7] == 'name:':
        print("checking name..")

        name = data[8:-1]
        namelist.append(name)
        print(namelist)

        print(y)


        #print("name is :" + name)
        name = namelist[y] + ": "
        nametest = 'yes'
        namegame = 'yes'
        #print("name test is: ",nametest)
        #data = data[2:-1]
        if nametest == 'yes':
           # print(name + ":" + data[2:-1]) #delete me
            n = 1
            namegame = 'yes'

        else:
            print("Anonymous: " + data[2:-1])
            n = 0
            namegame = None
        i = 0

    if n == 1 and namegame == 'yes':
        print(name + data[2:-1])

    elif n == 0 and namegame != 'yes':
        print("Anonymous: " + data[2:-1])
    y += 1


UDPSock.close()
os._exit(0)
