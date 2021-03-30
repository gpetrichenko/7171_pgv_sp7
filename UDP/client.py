import socket
import threading
import time 

threadLock = threading.Lock()
shutdown = False

host = '192.168.211.1'
port = 5000
server = ('192.168.211.134', 5000)
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host, port))
s.setblocking(0)

def receiving(name, sock):
    while not shutdown:
        try:
            threadLock.acquire()
            while True:
                data, addr = sock.recvfrom(1024)
                print (str(data))
        except:
            pass
        finally:
            threadLock.release()

def sending(name, sock):
    while not shutdown:
        try:
            threadLock.acquire()
            while True:
                data, addr = sock.sendmsg(1024)
        except:
            pass
        finally:
            threadLock.release()

rThread = threading.Thread(target=receiving, args=("RecvThread", s))
rThread.start()
sThread = threading.Thread(target=sending, args=("SendThread", s))
sThread.start()

name = input("Nick: ")
s.sendto(bytes(name + " Welcome! .",'utf-8'), server)
time.sleep(0.3)

message = input()

while message != '!exit':
    if message != '':
        s.sendto(bytes(name + ": " + message, 'utf-8'), server)
        time.sleep(0.3)
    message = input()

s.sendto(bytes(name + " left.", 'utf-8'), server)

shutdown = True
rThread.join()
sThread.join()
s.close()