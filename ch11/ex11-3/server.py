from datetime import datetime
from xmlrpc.server import SimpleXMLRPCServer


def now():
    time = datetime.now().astimezone().isoformat()
    data = time.encode('utf-8')
    return data


server = SimpleXMLRPCServer(('localhost', 8000))
server.register_function(now, 'now')
server.serve_forever()
