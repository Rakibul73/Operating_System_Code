import random
import time
import threading
import logging
import queue

BSIZE = 8  # Buffer size
PWT = 2  # Producer wait time limit
CWT = 10  # Consumer wait time limit
RT = 10  # Program run-time in seconds

def myrand(n):
    return random.randint(1, n)

def producer(queue, state):
    index = 0
    while state:
        time.sleep(1)
        logging.info("\nProducer is ready now.")
        with queue.lock:
            if not queue.full():
                tempo = myrand(BSIZE * 3)
                logging.info(f"Job {tempo} has been produced")
                queue.put(tempo)
                logging.info(f"Buffer: {list(queue.queue)}")
            else:
                logging.info("Buffer is full, nothing can be produced!!!")
        wait_time = myrand(PWT)
        logging.info(f"Producer will wait for {wait_time} seconds")
        time.sleep(wait_time)

def consumer(queue, state):
    time.sleep(5)
    while state:
        time.sleep(1)
        logging.info("\nConsumer is ready now.")
        with queue.lock:
            if not queue.empty():
                job = queue.get()
                logging.info(f"Job {job} has been consumed")
                logging.info(f"Buffer: {list(queue.queue)}")
            else:
                logging.info("Buffer is empty, nothing can be consumed!!!")
        wait_time = myrand(CWT)
        logging.info(f"Consumer will sleep for {wait_time} seconds")
        time.sleep(wait_time)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(message)s')

    shared_queue = queue.Queue(BSIZE)
    shared_queue.lock = threading.Lock()
    state = True

    producer_thread = threading.Thread(target=producer, args=(shared_queue, state))
    consumer_thread = threading.Thread(target=consumer, args=(shared_queue, state))

    producer_thread.start()
    consumer_thread.start()

    time.sleep(RT)
    state = False

    producer_thread.join()
    consumer_thread.join()

    logging.info("\nThe clock ran out.")
