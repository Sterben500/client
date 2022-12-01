import os
import socket
import threading
import platform

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('0.0.0.0', 4000))
server_socket.listen()

clients = []
nicknames = []
address = socket.gethostbyname(socket.gethostname())
print(f'Your ip address  is {address}')


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
        client.send('Type "help" to see the commands'.encode('ascii'))
        client.close()
        

def get_os():
    os = platform.system()
    if os == 'Windows':
        return 'cls'
    else:
        if os == 'Linux':
            return 'clear'
        else:
            return 'clear'

def broadcast(message):
    for client in clients:
        client.send(message)

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



def main():
    print("Welcome to the chat room!")
    print("Type 'quit' to exit the chat room")
    print("Type 'clear' to clear the screen")
    print("Type 'help' to see the commands")
    print("Type 'users' to see the users in the chat room")
    print("Type 'os' to see the operating system of the machine")
    print("Type 'ip' to see the ip address of the machine")

    while True:
        message = input('You: ')
        if message == 'quit':
            break
        if message == 'clear':
            os.system(get_os())
        if message == 'help':
            print("Type 'quit' to exit the chat room")
            print("Type 'clear' to clear the screen")
            print("Type 'help' to see the commands")
            print("Type 'users' to see the users in the chat room")
            print("Type 'os' to see the operating system of the machine")
            print("Type 'ip' to see the ip address of the machine")
        if message == 'users':
            print(nicknames)
        if message == 'os':
            print(platform.system())
        if message == 'ip':
            print(socket.gethostbyname(socket.gethostname()))
        broadcast(message.encode('ascii'))
        

if __name__ == '__main__':
    receive()
    main()