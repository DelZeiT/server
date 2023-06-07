import socket

clients = []
flag = True

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind((socket.gethostbyname(socket.gethostname()), 9090))

server.listen()

print('Сервер запущен!')

while flag:
    message, addr = server.recvfrom(1024)

    if addr not in clients:
        clients.append(addr)

    print(message.decode('utf-8'))
    for client in clients:
        if client != addr:
            server.sendto(message, client)

    if message == 'стоп':
        flag = False
        print('Сервер остановлен!')

server.close()