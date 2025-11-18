import redis

r = redis.Redis(host="localhost", port=6379)

message = "Messaggio 1"
r.publish("demo", message)

print("Inviato:", message)