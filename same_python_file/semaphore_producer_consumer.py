import threading
import time

mutex = threading.Semaphore(1)
full = threading.Semaphore(0)
empty = threading.Semaphore(3)
x = 0

def producer():
    global mutex, full, empty, x
    empty.acquire()
    mutex.acquire()
    x += 1
    print(f"Producer produces item {x}\n")
    mutex.release()
    full.release()

def consumer():
    global mutex, full, empty, x
    full.acquire()
    mutex.acquire()
    print(f"Consumer consumes item {x}\n")
    x -= 1
    mutex.release()
    empty.release()

def main():
    while True:
        print("1. PRODUCER\n2. CONSUMER\n3. EXIT")
        n = int(input("ENTER YOUR CHOICE: \n"))
        if n == 1:
            if empty._value != 0:
                producer_thread = threading.Thread(target=producer)
                producer_thread.start()
            else:
                print("BUFFER IS FULL")
        elif n == 2:
            if full._value != 0:
                consumer_thread = threading.Thread(target=consumer)
                consumer_thread.start()
            else:
                print("BUFFER IS EMPTY")
        elif n == 3:
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
