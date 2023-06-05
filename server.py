import socket

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(('localhost', 9090))

server.listen()

client, address = server.accept()
print('')



flag = True

while flag == True:
    name = input('')
    message = client.recv(1024).decode('utf-8')
    if message == '':
        flag = False
    else:
        print(f'{name}: {message}')
    client







