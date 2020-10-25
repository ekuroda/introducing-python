import zmq
from time import sleep

host = '127.0.0.1'
port = 8000

context = zmq.Context()
client = context.socket(zmq.REQ)
client.connect(f"tcp://{host}:{port}")

while True:
    sleep(5)
    client.send(b'time')
    data = client.recv(1024)
    print(data)
