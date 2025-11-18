import redis
import time
import random
from datetime import datetime

r = redis.Redis(host="localhost", port=6379)

while True:
    temperatura = random.randint(20, 90)
    potenza = round(random.uniform(0.5, 5.0), 2)
    timestamp = datetime.utcnow().isoformat()

    message = f"sensor=S1;temp={temperatura};power={potenza};time={timestamp}"
    r.publish("demo", message)

    print("Inviato:", message)
    time.sleep(2)
