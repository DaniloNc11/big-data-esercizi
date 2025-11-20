import redis
import boto3
from botocore.exceptions import ClientError
from datetime import datetime
import uuid

# Redis setup
r = redis.Redis(host="192.168.7.38", port=6379)
pubsub = r.pubsub()
pubsub.subscribe("demo")
print("Subscriber connesso a Redis su 192.168.7.38, canale 'demo'.")

# MinIO setup
s3 = boto3.client(
    "s3",
    endpoint_url="http://192.168.7.38:9000",
    aws_access_key_id="admin",
    aws_secret_access_key="admin123"
)

bucket = "my-bucket"

# Verifica o crea il bucket
try:
    s3.head_bucket(Bucket=bucket)
    print(f"Bucket '{bucket}' trovato.")
except ClientError:
    s3.create_bucket(Bucket=bucket)
    print(f"Bucket '{bucket}' creato.")

print("In attesa di messaggi...")

count = 0  # Contatore progressivo

for msg in pubsub.listen():
    if msg["type"] == "message":
        raw_data = msg["data"].decode("utf-8")
        print("Ricevuto:", raw_data)

        # Uppercase
        upper_text = raw_data.upper()

        # Numero progressivo
        count += 1

        # Timestamp locale
        timestamp = datetime.now().isoformat(timespec="seconds")

        # Messaggio finale
        final_message = f"{count} | {timestamp} | {upper_text}"
        print("Messaggio finale:", final_message)

        # Salvataggio su MinIO
        try:
            file_bytes = final_message.encode("utf-8")
            uuidkey = f"{uuid.uuid4()}.txt"
            s3.put_object(Bucket=bucket, Key=uuidkey, Body=file_bytes)
            print(f"✅ Caricato su MinIO come '{uuidkey}'")
        except Exception as e:
            print("❌ Errore nel caricamento su MinIO:", e)