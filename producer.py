import redis
import time

r = redis.Redis(host="localhost", port=6379)

while True:
    data = {
        "sensor": "S1",
        "value": 50
    }

    message = str(data)
    r.publish("demo", message)
    print("Inviato:", message)
    time.sleep(2)