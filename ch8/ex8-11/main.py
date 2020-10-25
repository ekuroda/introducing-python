import redis

conn = redis.Redis()
conn.hset('test', mapping={'count': 1, 'name': 'Faster Bestertester'})
print(conn.hgetall('test'))

conn.hincrby('test', 'count', 3)
print(conn.hget('test', 'count'))
