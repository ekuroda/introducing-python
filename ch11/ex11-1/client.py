import socket
from time import sleep

address = ('localhost', 8000)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(address)

print('start')

while True:
    sleep(5)
    client.sendall(b'time')
    data = client.recv(1024)
    print(data)

client.close()
