import socket
import threading

nick = input("Nick: ")
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('192.168.211.134', 12345))

def receive():
    while True:
        try:
            mes = client.recv(1024).decode('utf-8')
            if mes == 'NICK':
                client.send(nick.encode('utf-8'))
            else:
                print(mes)
        except:
            print("ERROR")
            client.close()
            break

def write():
    while True:
        try:
            mes = '{}: {}'.format(nick, input(''))
            client.send(mes.encode('utf-8'))
        except:
            break


receive_thread = threading.Thread(target=receive)
receive_thread.start()
write_thread = threading.Thread(target=write)
write_thread.start()