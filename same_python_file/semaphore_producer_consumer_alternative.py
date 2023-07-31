import threading
import time
import random

# Buffer size
BUFFER_SIZE = 5

# Semaphore to control access to the buffer
mutex = threading.Semaphore(1)

# Semaphore to count the empty slots in the buffer
empty = threading.Semaphore(BUFFER_SIZE)

# Semaphore to count the number of items in the buffer
full = threading.Semaphore(0)

# Buffer to store items
buffer = []

# The producer function, responsible for producing items
def producer():
    for _ in range(10):
        # Generate a random item to be produced
        item = random.randint(1, 100)

        # Acquire an empty slot in the buffer
        empty.acquire()

        # Acquire the mutex to ensure mutual exclusion when accessing the buffer
        mutex.acquire()

        # Add the item to the buffer
        buffer.append(item)

        # Print a message indicating the item is produced and the current buffer contents
        print(f"Producer: Produced item {item}. Buffer: {buffer}")

        # Release the mutex to allow other threads to access the buffer
        mutex.release()

        # Release a full slot in the buffer to signal that an item is available
        full.release()

        # Introduce a random delay to simulate variable production time
        time.sleep(random.uniform(0.1, 0.5))

# The consumer function, responsible for consuming items
def consumer():
    for _ in range(10):
        # Acquire a full slot in the buffer to check if an item is available for consumption
        full.acquire()

        # Acquire the mutex to ensure mutual exclusion when accessing the buffer
        mutex.acquire()

        # Remove the first item from the buffer
        item = buffer.pop(0)

        # Print a message indicating the item is consumed and the current buffer contents
        print(f"Consumer: Consumed item {item}. Buffer: {buffer}")

        # Release the mutex to allow other threads to access the buffer
        mutex.release()

        # Release an empty slot in the buffer to signal that a slot is available for production
        empty.release()

        # Introduce a random delay to simulate variable consumption time
        time.sleep(random.uniform(0.1, 0.5))

if __name__ == "__main__":
    # Create producer and consumer threads
    producer_thread = threading.Thread(target=producer)
    consumer_thread = threading.Thread(target=consumer)

    # Start the threads
    producer_thread.start()
    consumer_thread.start()

    # Wait for the threads to complete
    producer_thread.join()
    consumer_thread.join()

    # Print a message indicating that the simulation is completed
    print("Producer-Consumer simulation completed.")
