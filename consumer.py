import redis
import boto3
import ast

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
                text = msg["data"].decode()
                text_dict = ast.literal_eval(text)
                text_dict["value"] += 10
                text = str(text_dict)
                count += 1
                filename = f"file-{count}.txt"
                s3.put_object(Body=text, Bucket=bucket, Key=filename)
                print("Ricevuto:", text)

        # TODO 1: convertire la stringa ricevuta in dizionario (cercare su internet).

        # TODO 2: modificare il valore ricevuto 'value' aggiungendo +10.

        # TODO 3: ricreare una stringa dal dizionario modificato (cercare su internet).

        # TODO 4: Nome file nuovo per ogni messaggio

        # TODO 4: salvare su MinIO l’oggetto aggiornato.


        print("Salvato:", filename)
