#---it's a chat application! complete with names!
#---to be used in the rpp,screem project, this program allows for 2 way text communication between 2 users.
#---(more might be possible, testing needed)
from time import *
from socket import *



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
n = 0
nametest = False
namegame = False
setname = input("what's your name? ")
setname = "name: " + setname
send.sendto(bytes(setname, "utf-8"), addr)

while True:

    if i == 1:

        print("waiting for received message")
        (data, recaddr) = receive.recvfrom(buf)

        data = str(data)


        if data[2:7] == 'name:':
            print("checking name..")
            global name
            name = data[8:-1]
            #print("name is :" + name)
            name = name + ": "
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
            print(name + data[6:-1])
        elif n == 0 and namegame != 'yes':
            print("Anonymous: " + data[6:-1])


    if x == 0:

        data = input('You: ')
        send.sendto(bytes(data, "utf-8"), addr)
        i = 1
receive.close()
send.close()
os._exit(0)
