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

for msg in pubsub.listen():
        if msg["type"] == "message":
                count += 1
                filename = f"msg_{count}.txt"
                s3.put_object(Bucket=bucket, Key=filename, Body=msg["data"].decode().upper())
