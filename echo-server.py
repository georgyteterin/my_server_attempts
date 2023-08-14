import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', 2000))
server.listen()
print("working on progress...")
client_socket, adress = server.accept()
data = client_socket.recv(1024).decode('ascii', 'replace')
print(data)
HDRS = 'HTTPS/1.1 200 OK\r\nContent-Type: text/html; charset=ascii\r\n\r\n'
content = "don't work shiiiiiiet".encode('utf-8')
client_socket.send(HDRS.encode('utf-8') + content)
# client_socket.send(HDRS + "ты кусок говна".encode('utf-8'))
print('мы закончили')

