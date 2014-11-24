#!/usr/bin/env python

from threading import Thread
import time

def synchronized(lock):
    """ Synchronization decorator. """

    def wrap(f):
        def new_function(*args, **kwargs):
            lock.acquire()
            try:
                return f(*args, **kwargs)
            finally:
                lock.release()
        return new_function
    return wrap

# Example usage:
from threading import Lock
my_lock = Lock()
print_lock = Lock()

count = 0

@synchronized(print_lock)
def atomic_print(*args):
    print(args)

def critical1(thread_name):
    global count
    while count < 20:
        atomic_print(thread_name, "Before:", count)
        count += 1
        atomic_print(thread_name, "After:", count)


def run_2(thread_name):
    global count
    while count < 100:
        critical2(thread_name)
        time.sleep(0.01)

@synchronized(my_lock)
def critical2(thread_name):
    global count
    if count < 100:
        print thread_name, "Before:", count
        count += 1
        print thread_name, "After:", count

if __name__ == "__main__":
    print "Unsynchronized critical section"
    t1 = Thread(target=critical1, args=("Thread-1",))
    t2 = Thread(target=critical1, args=("Thread-2",))
    t3 = Thread(target=critical1, args=("Thread-3",))
    t1.start()
    t2.start()
    t3.start()
    t1.join()
    t2.join()
    t3.join()

    print "\n"
    print "Synchronized critical section"
    t1 = Thread(target=run_2, args=("Thread-1",))
    t2 = Thread(target=run_2, args=("Thread-2",))
    t3 = Thread(target=run_2, args=("Thread-3",))
    t1.start()
    t2.start()
    t3.start()
    t1.join()
    t2.join()
    t3.join()
