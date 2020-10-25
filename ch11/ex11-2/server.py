import zmq
from datetime import datetime

host = '127.0.0.1'
port = 8000

context = zmq.Context()
server = context.socket(zmq.REP)
server.bind(f"tcp://{host}:{port}")

while True:
    request_bytes = server.recv()
    if request_bytes == b'time':
        time = datetime.now().astimezone().isoformat()
        data = time.encode('utf-8')
        server.send(data)
        print('sent', data)
