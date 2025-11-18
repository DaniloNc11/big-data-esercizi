import redis
import boto3

r = redis.Redis(host="localhost", port=6379)
pubsub = r.pubsub()
pubsub.subscribe("demo")

s3 = boto3.client(
    "s3",
    endpoint_url="http://localhost:9000",
    aws_access_key_id="admin",
    aws_secret_access_key="admin123"
)

bucket = "my-bucket"
count = 0

print("In attesa di messaggi...")

for msg in pubsub.listen():
    if msg["type"] == "message":
        raw = msg["data"].decode()
        print("Ricevuto:", raw)


        # TODO 0: estrarre la temperatura dal messaggio ricevuto usando split
        # # Il messaggio ha questo formato: sensor=S1;temp=55;power=3.2;time=...
        # # Obiettivo: prendere solo il numero della temperatura.

        # TODO 1: usare un if per controllare la temperatura.
        # Regola:
        # - se temperatura > 70 -> stampa "Scartato" e NON salvare niente.
        # - se temperatura <= 70 -> proseguire con il salvataggio.

        # TODO 2: trasformare il messaggio in uppercase solo se valido.

        # TODO 3: incrementare il contatore e creare un nome file unico.

        # TODO 4: salvare il messaggio valido su MinIO usando s3.put_object().
