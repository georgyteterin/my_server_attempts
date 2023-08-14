import socket

server = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server.bind(('127.0.0.1',1025))
client = [] # Массив где храним адреса клиентов
print('Start Server')
# print(addres[0], addres[1])
data, address = server.recvfrom(1024)
while True:
    data, address = server.recvfrom(1024)
    if address not in client:
        client.append(address)# Если такого клиента нету , то добавить
        # print('we did it')
    for clients in client:
        if clients == address:
            print(client[1])
            # continue # Не отправлять данные клиенту, который их прислал
            # server.sendto(data, client[0])
            # print(data.decode('utf-8'))