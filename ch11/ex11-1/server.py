from datetime import datetime
import socket

address = ('localhost', 8000)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(address)
server.listen(5)

print('start')

client, addr = server.accept()

while True:
    data = client.recv(1024)
    if data == b'time':
        time = datetime.now().astimezone().isoformat()
        data = time.encode('utf-8')
        client.sendall(data)
        print('sent', data)

client.close()
server.close()
