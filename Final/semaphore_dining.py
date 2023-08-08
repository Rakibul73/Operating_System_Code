import threading
import time
import random

NUM_PHILOSOPHERS = 5
chopsticks = [threading.Semaphore(1) for _ in range(NUM_PHILOSOPHERS)]

def philosopher(philosopher_id):
    # Get the left and right chopsticks for the philosopher
    left_chopstick = chopsticks[philosopher_id]
    right_chopstick = chopsticks[(philosopher_id + 1) % NUM_PHILOSOPHERS]
    
    while True:
        # Thinking
        print(f"Philosopher {philosopher_id} is thinking.")
        time.sleep(random.random())

        # Pick up left chopstick
        left_chopstick.acquire()
        print(f"Philosopher {philosopher_id} picked up the left chopstick.")

        # Try to pick up right chopstick without blocking
        if right_chopstick.acquire(blocking=False):
            # Pick up right chopstick and start eating
            print(f"Philosopher {philosopher_id} picked up the right chopstick.")
            print(f"Philosopher {philosopher_id} is eating.")
            time.sleep(random.random())

            # Release right chopstick after eating
            right_chopstick.release()
            print(f"Philosopher {philosopher_id} put down the right chopstick.")
        
        # Release left chopstick after eating or if right chopstick is not available
        left_chopstick.release()
        print(f"Philosopher {philosopher_id} put down the left chopstick.")

if __name__ == "__main__":
    # Create philosopher threads and start them
    philosophers = [threading.Thread(target=philosopher, args=(i,)) for i in range(NUM_PHILOSOPHERS)]
    for p in philosophers:
        p.start()

    # Wait for all philosopher threads to complete
    for p in philosophers:
        p.join()
