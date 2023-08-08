from threading import Thread
from time import sleep


counter = 0

# define a function that increases the value of the counter variable by a number:
def increase(by):
    global counter

    local_counter = counter
    local_counter += by

    sleep(0.1)

    counter = local_counter
    print(f'counter={counter}\n')


# create two threads. 
# first thread increases the counter by 10 
# second thread increases the counter by 20:
t1 = Thread(target=increase, args=(10,))
t2 = Thread(target=increase, args=(20,))

# start the threads
t1.start()
t2.start()


# wait for the threads to complete
t1.join()
t2.join()


print(f'The final counter is {counter}')