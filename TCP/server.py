import threading
import socket

host = 'localhost'
port = 12345

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

clients = []
nicks = []

def broadcast(mes):
    for client in clients:
        client.send(mes)

def handle(client):
    while True:
        try:
            mes = client.recv(1024)
            broadcast(mes)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nick = nicks[index]
            broadcast('{} left!'.format(nick).encode('utf-8'))
            nicks.remove(nick)
            break

def listen():
    while True:
        try:
            client, address = server.accept()
            print("User connected with {}".format(str(address)))
            client.send('NICK'.encode('utf-8'))
            nick = client.recv(1024).decode('utf-8')
            nicks.append(nick)
            clients.append(client)
            print("User nickname is {}".format(nick))
            broadcast("{} join!".format(nick).encode('utf-8'))
            client.send('Join to server!'.encode('utf-8'))
            thread = threading.Thread(target=handle, args=(client,))
            thread.start()
        except:
            break

listen()