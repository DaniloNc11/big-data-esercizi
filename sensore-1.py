import redis

r = redis.Redis(host="localhost", port=6379)

x = "Messaggio 1"
canale = "sensore-1"

while True:
    r.publish(canale, x)
    print("Inviato:", x)

