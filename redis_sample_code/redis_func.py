# redis_func.py
  
from redis import Redis

# connecting to redis instance
redis = Redis(host="phishblockercache.jc80zx.ng.0001.usw1.cache.amazonaws.com", port=6379, decode_responses=True)

if (redis.ping()):
    print("redis connection succeeded")
else:
    print("oops")

key_str = "bananas"
val_str = "tasty"

# setting a redis key
redis.set(key_str, val_str)

# getting a redis key and other information
print(redis.get(key_str))
print(redis.ttl(key_str))
print(redis.get("random"))