from threading import Thread, Lock
from time import sleep

# Initialize the global counter variable
counter = 0

# Define the thread function to increase the counter by a given value using a lock
def increase(by, lock):
    global counter

    # Acquire the lock to ensure exclusive access to the shared counter
    lock.acquire()

    # Create a local copy of the counter to perform the update
    local_counter = counter
    local_counter += by

    # Simulate some time-consuming work using sleep
    sleep(0.1)

    # Update the global counter with the new value
    counter = local_counter
    print(f'counter={counter}')

    # Release the lock to allow other threads to access the shared counter
    lock.release()

# Create a Lock object to synchronize access to the shared counter
lock = Lock()

# Create two threads, each incrementing the counter by a different value
t1 = Thread(target=increase, args=(10, lock))
t2 = Thread(target=increase, args=(20, lock))

# Start the threads
t1.start()
t2.start()

# Wait for the threads to complete their execution
t1.join()
t2.join()

# Print the final value of the counter
print(f'The final counter is {counter}')
