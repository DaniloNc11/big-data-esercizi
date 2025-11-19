import redis

r = redis.Redis(host="localhost", port=6379)

pubsub = r.pubsub()
pubsub.subscribe("sensore-1")

print("In attesa di messaggi...")

for msg in pubsub.listen():
    if msg["type"] == "message":
        print("Ricevuto:", msg["data"].decode())