# Save as client.py
# Message Sender
#it
import os
from socket import *
import random, string


host = "192.168.178.34" # set to IP address of target computer
port = 13001
addr = (host, port)
UDPSock = socket(AF_INET, SOCK_DGRAM)
name = input("what's your name? ")
name = "name: " + name
UDPSock.sendto(bytes(name, "utf-8"), addr)
#---creates id---#
s = string.ascii_lowercase + string.digits
userid = ''.join(random.sample(s,4))
while True:
    data = input("Enter message to send or type 'exit': ")
    data = userid + data

    UDPSock.sendto(bytes(data, "utf-8"), addr)
    if data == "exit":
        break
UDPSock.close()
os._exit(0)
