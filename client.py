import socket
import threading
import sys
import platform
import os
import time
import json

def receive(socket, signal):
    while signal:
            data = socket.recv(32)           
            requet(str(data.decode("utf-8")))
            
host = 'localhost'
port = 5050
name=str(input('enter your name:'))

with open('test.json','r') as f:
    data=json.load(f)
    data['host']=host
    data['port']=port
    data['name']=name
    
with open('test.json','w') as f:
    json.dump(data,f)

try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((host, port))
except:
            print("Could not make a connection to the server")
            input("Press enter to quit")
            sys.exit(0)

receiveThread = threading.Thread(target = receive, args = (sock, True))
receiveThread.start()
def send_msg(msg):
    sock.sendto(str.encode(msg), (host,port))
send_msg(name)

def requet(msg):
 
    if(msg=='os'):
            send_msg(str(platform.system()))
    if(msg=='ip'):
        send_msg(str(socket.gethostbyname(socket.gethostname())))
    else:
        print(msg)
while True:
   
    message = input()
    sock.sendto(str.encode(message), (host,port))
