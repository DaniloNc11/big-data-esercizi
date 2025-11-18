import redis
import boto3
from botocore.exceptions import ClientError

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

try:
    s3.head_bucket(Bucket=bucket)
except ClientError:
    s3.create_bucket(Bucket=bucket)

print("In attesa di messaggi...")

for msg in pubsub.listen():
    if msg["type"] == "message":
        text = msg["data"].decode()
        print("Ricevuto:", text)

        #TODO: trasformare il messaggio in upper case

        #TODO: inserire l'oggetto dentro il bucket