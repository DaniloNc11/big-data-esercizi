import redis

# Connessione a Redis (stesso IP del subscriber)
r = redis.Redis(host="192.168.7.38", port=6379)

# Messaggio da inviare
messaggio = "jrutj://fhntwsai11.kkriys.kv/Cjmieilcjmieil | chiave: CYBERCHALLENGE"

# Pubblica il messaggio sul canale "demo"
r.publish("demo", messaggio)

print("✅ Inviato:", messaggio)