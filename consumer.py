import redis
import boto3
from botocore.exceptions import ClientError
from datetime import datetime

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
filename = "messaggio.txt"
count = 0

try:
    s3.head_bucket(Bucket=bucket)
except ClientError:
    s3.create_bucket(Bucket=bucket)

print("In attesa di messaggi...")

for msg in pubsub.listen():
    if msg["type"] == "message":
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