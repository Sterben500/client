import socket
import threading
import time
import platform

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('0.0.0.0', 4000))
server_socket.listen()

clients = []
nicknames = []


def broadcast(message):
    for client in clients:
        client.send(message)
    return True

def send_message(message):
    for client in clients:
        client.send(message)
    return True

    return platform.system()


#when receive os message send platform message
def on_message(client, message):
    global clients
    global nicknames
    global server_socket
    global clients
    global nicknames
    global server_socket
    global clients
    global nicknames

    if message.startswith('nick'):
        nicknames.append(message.split('nick ')[1])
        platform = get_platform()
        send_message(nicknames[0] + ' ' + platform)
        

def handle(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast(f'{nickname} left the chat!'.encode('ascii'))
            nicknames.remove(nickname)
            break

def receive():
    while True:
        client, address = server_socket.accept()
        print(f'Connected with {str(address)}')
        client.send('NICK'.encode('ascii'))
        nickname = client.recv(1024).decode('ascii')
        nicknames.append(nickname)
        clients.append(client)
        print(f'Nickname of the client is {nickname}!')
        broadcast(f'{nickname} joined the chat!'.encode('ascii'))
        client.send('Connected to the server!'.encode('ascii'))
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()
receive()


# turn off 