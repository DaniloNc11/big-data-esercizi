import redis
import base64

# Connessione a Redis
r = redis.Redis(host="localhost", port=6379)

# Leggi e codifica il file
with open("C:\\Users\\A829apulia\\Desktop\\Cyberchallenge.zip", "rb") as f:
    file_bytes = f.read()
    encoded = base64.b64encode(file_bytes).decode()

# Pubblica il messaggio codificato
r.publish("demo", encoded)

print("Inviato: cyberchallenge.zip codificato in base64")
