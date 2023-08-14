import socket

def read_client():
    while 1:
        data = client.recv(1024)
        print(data.decode('utf-8'))


server = ('127.0.0.1', 1025)
alias = input()
client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
message = (alias+' joined server').encode('utf-8')
client.sendto(message, server)
while True:
    message = input()
    client.sendto(('['+alias+'] '+message).encode('utf-8'), server)
    data = client.recvfrom(1024)
