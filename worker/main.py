import redis
import time
import os

# Connect to Redis
r = redis.Redis(host=os.getenv("REDIS_HOST", "redis-server"), port=6379, decode_responses=True)

print("!!! WORKER IS STARTING UP !!!", flush=True)

while True:
    try:
        # Check the queue
        task = r.brpop("image_queue", timeout=5)
        
        if task:
            image_name = task[1]
            print(f"[*] Found Task! Processing: {image_name}", flush=True)
            time.sleep(2)
            print(f"[SUCCESS] Finished {image_name}", flush=True)
        else:
            # Heartbeat to prove it's working
            print("Worker waiting for tasks...", flush=True)
            
    except Exception as e:
        print(f"ERROR: {e}", flush=True)
        time.sleep(5)