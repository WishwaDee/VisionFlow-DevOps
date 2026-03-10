from fastapi import FastAPI
import redis
import os

app = FastAPI()

# Get Redis host from environment variable (Best practice for DevOps)
# 'redis-server' is the name we gave it in docker-compose.yml
REDIS_HOST = os.getenv("REDIS_HOST", "redis-server")

# Connect to Redis
r = redis.Redis(host=REDIS_HOST, port=6379, decode_responses=True)

@app.get("/")
def read_root():
    return {"status": "VisionFlow API is Online", "version": "1.0.0"}

@app.post("/upload")
def upload_image(image_name: str):
    # This simulates putting a 'ticket' in the Redis queue
    r.lpush("image_queue", image_name)
    return {"message": f"Image '{image_name}' added to the queue for processing."}