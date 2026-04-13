import time
import random

def monitor():
    while True:
        latency = random.uniform(0.05, 0.2)
        accuracy = random.uniform(0.85, 0.95)
        drift = random.uniform(0.0, 0.1)

        print(f"[Monitoring] Latency: {latency:.3f}s | Accuracy: {accuracy:.2f} | Drift: {drift:.2f}")
        time.sleep(5)

if __name__ == "__main__":
    monitor()
