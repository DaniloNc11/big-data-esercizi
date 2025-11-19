import redis

r = redis.Redis(host="localhost", port=6379)

message = "Messaggio 1"
canale="sensore-1"
r.publish(canale, message)
print("Inviato:", message)
