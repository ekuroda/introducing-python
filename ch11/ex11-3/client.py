from time import sleep
import xmlrpc.client


proxy = xmlrpc.client.ServerProxy('http://localhost:8000/')

while True:
    sleep(5)
    result = proxy.now()
    print(result)
