# Save as server.py 
# Message Receiver
import os
from socket import *
class client:
    def __init__(self, host):
        self.host = host

    host = ""
    port = 13000
    buf = 1024
    addr = (host, port)
    UDPSock = socket(AF_INET, SOCK_DGRAM)
    UDPSock.bind(addr)
    print("Waiting to receive messages...")
    while True:
        (data, addr) = UDPSock.recvfrom(buf)
        data = str(data)[2:-1]
        print("Received message: " + data)
        if data == "exit":
            break
    UDPSock.close()
    os._exit(0)
