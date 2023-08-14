import socket
import time
import threading

ADDRESS = '192.168.1.102'
PORT = 1025


def read_sok():
    while 1:
        data = client.recv(1024)
        print(data.decode('utf-8'))


def send_sok():
    while True:
        print('enter message > ')
        message = input()
        client.sendto(message.encode('utf-8'), server)


try:
    server = (ADDRESS, PORT)
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print('enter message > ')
    hello_message = (input()).encode('utf-8')
    client.connect(server)
    client.sendall(hello_message)
    while True:
        # potok1 = threading.Thread(target=read_sok)
        # potok2 = threading.Thread(target=send_sok)
        # potok1.start()
        # potok2.start()
        # potok1.join()
        # potok2.join()
    # while True:
        print('enter message > ')
        message = input()
        client.sendall(message.encode('utf-8'))
        # time.sleep(5)
        # data = client.recv(1024)
        # print(data.decode('utf-8'))
except KeyboardInterrupt:
    print('\nyou said it not me')
