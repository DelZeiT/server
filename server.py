
import socket

clients = []    #список адресов клиеннтов
flag = True

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((socket.gethostbyname(socket.gethostname()), 9090))     #назначаем адрес для сервера

server.listen(5)        #прослушиваем указанный порт на получение сигналов
print('Сервер запущен!')

conn, addr = server.accept()
print(f'{addr}  - присоединился к чату')

while flag:
    message, addr = server.recv(1024).decode('utf-8')     #не понял для чего. Вроде для получения данных от клиента в размере 1 Кб

    if addr not in clients:                 #если нету адреса клиента в списке уже подключенных клиентов
        clients.append(addr)

    print(message.decode('utf-8'))          #отправляем задекодированное сообщение
    for client in clients:
        if client != addr:                  #чтобы клиент не видел свое же сообщение
            server.send(message)

    if message == 'стоп':                   #если мы хотим остановить сервер
        flag = False
        print('Сервер остановлен!')

server.close()