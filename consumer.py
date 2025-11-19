import redis
import boto3
import base64
from botocore.exceptions import ClientError
from datetime import datetime

r = redis.Redis(host="localhost", port=6379)
pubsub = r.pubsub()
pubsub.subscribe("demo")

s3 = boto3.client(
    "s3",
    endpoint_url="http://192.168.7.38:9000",
    aws_access_key_id="admin",
    aws_secret_access_key="admin123"
)

uuid = __import__('uuid')
bucket = "my-bucket"
<<<<<<< Updated upstream
filename = "messaggio.txt"
count = 0
=======
filename = "cyberchallenge.zip"
uuidkey = str(uuid.uuid4()) + ".zip"
>>>>>>> Stashed changes

try:
    s3.head_bucket(Bucket=bucket)
except ClientError:
    s3.create_bucket(Bucket=bucket)

print("In attesa di messaggi...")

for msg in pubsub.listen():
    if msg["type"] == "message":
<<<<<<< Updated upstream
        text = msg["data"].decode()
        print("Ricevuto:", text)

        # TODO 1: convertire il messaggio in uppercase.

        # TODO 2: creare una variabile dove inserire un numero progressivo (ad ogni iterazione aumenta di 1).

        # TODO 3: creare una variabile per memorizzare un timestamp locale (datetime)


        # TODO 4: costruire il messaggio finale.
        # Deve contenere:
        # - numero progressivo
        # - timestamp
        # - messaggio in uppercase
        # Formato consigliato:
        # "3 | 2025-01-01T12:30:00 | MESSAGGIO 1"

        # TODO 5: salvare il messaggio finale su MinIO.
=======
        encoded = msg["data"].decode()
        try:
            file_bytes = base64.b64decode(encoded)
            s3.put_object(Bucket=bucket, Key=uuidkey, Body=file_bytes)
            print(f"Caricato '{filename}' nel bucket '{bucket}' come oggetto '{uuidkey}'")
        except Exception as e:
            print("Errore nella decodifica o nel caricamento:", e)
>>>>>>> Stashed changes
