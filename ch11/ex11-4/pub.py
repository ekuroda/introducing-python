import redis
import random
from time import sleep

conn = redis.Redis()
kinds = ['a', 'b', 'c', 'd']

while True:
    sleep(random.random())
    c = random.choice(kinds)
    len = conn.rpush('job', c)
    print(f'pub {c}, len={len}')
