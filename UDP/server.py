import socket
#import time

host = 'localhost'
port = 5000
clients = []

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host,port))
s.setblocking(0)
quitting = False
print("Server up!")

while not quitting:
    try:
        data, addr = s.recvfrom(1024)
        if "!exit" in str(data):
            clients.remove(addr)
        if addr not in clients:
            s.sendto((bytes("Welcome, to quit !exit", 'utf-8')), addr)
            clients.append(addr)
        print(str(addr) + ":" + str(data))
        for client in clients:
            if client != addr:	
                s.sendto(data, client)
    except:
        pass

s.close()
