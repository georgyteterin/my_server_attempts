import socket
import threading

ADDRESS = '192.168.1.102'
PORT = 1025


def read_sok():
    while True:
        new_data = server.recv(1024)
        print('[client ' + str(client.index(address) + 1 ) + '] ' + new_data.decode('utf-8'))


def send_sok():
    while True:
        print('enter message > ')
        message = ("[server for client " + str(client.index(address) + 1) + '] ' + input()).encode('utf-8')
        server.sendto(message, address)


try:
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server.bind((ADDRESS, PORT))
    client = []
    print('Start Server')
    while True:
        data, address = server.recvfrom(1024)
        if address not in client:
            client.append(address)
            print('client ' + str(client.index(address)+1) + ' joined server')
        for clients in client:
            if clients == address:
                potok1 = threading.Thread(target=read_sok)
                potok2 = threading.Thread(target=send_sok)
                potok1.start()
                potok2.start()
                potok1.join()
                potok2.join()
                # while True:
                #     print('enter message > ')
                #     message = ("[server for client " + str(client.index(address) + 1) + '] ' + input()).encode('utf-8')
                #     server.sendto(message, address)

                # print(data.decode('utf-8'))
except KeyboardInterrupt:
    print('\nyou said it not me')