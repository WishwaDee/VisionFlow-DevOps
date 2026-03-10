import redis
import time
import os

r = redis.Redis(host=os.getenv("REDIS_HOST", "redis-server"), port=6379, decode_responses=True)

print("--- Worker is online and waiting for images ---")

while True:
    task = r.brpop("image_queue") # This waits for a task
    if task:
        image_name = task[1]
        print(f"[*] Found Task! Processing: {image_name}")
        time.sleep(5) # Simulate work
        print(f"[SUCCESS] Finished {image_name}")