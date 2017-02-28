import os
from socket import *

from time import *

host = "192.168.178.34" # set to IP address of target computer
rechost = ""
port = 13000
recport = 13001
buf = 1024
addr = (host, port)
recaddr = (rechost, recport)
send = socket(AF_INET, SOCK_DGRAM)
receive = socket(AF_INET, SOCK_DGRAM)
receive.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

receive.bind(recaddr)
i = 0
x = 0
while True:

    if i == 1:

        #print("waiting for received message")
        (data, recaddr) = receive.recvfrom(buf)

        data = str(data)
        nametest = False
        print(data[2:])
        if data[2:7] == 'name:':
            global name
            name = data[4:-1]
            nametest = True
        if nametest == True:
            print(name + data)
        else:
            print("Anonymous: ")
        i = 0

    elif x < 1:

        data = input('You: ')
        send.sendto(bytes(data, "utf-8"), addr)
        i = 1


        pass
receive.close()
send.close()
os._exit(0)

'''
receive = socket(AF_INET, SOCK_DGRAM)
receive.bind(addr)
print("Waiting to receive messages...")
while True:
    (data, addr) = receive.recvfrom(buf)
    data = str(data)[2:-1]
    print("Received message: " + data)
    if data == "exit":
        break
receive.close()
os._exit(0)
'''
