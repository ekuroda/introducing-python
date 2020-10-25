import redis
from datetime import datetime
from time import sleep

conn = redis.Redis()

while True:
    sleep(0.5)
    msg = conn.blpop('job', 10)
    len = conn.llen('job')
    if msg:
        print(f'process {msg}, remaining={len}, time={datetime.now()}')
