#!/usr/bin/env python
"""
This decorator will cause any function to, instead of running its code,
start a thread to run the code, returning a thunk (function with no args)
that waits for the function's completion and returns the value (or raises
the exception). Useful if you have Computation A that takes x seconds and
then uses Computation B, which takes y seconds. Instead of x+y seconds
you only need max(x,y) seconds.
"""

import threading
import sys
import functools
import traceback
import time

def lazy_thunkify(f):
    """ Make a function immediately return a function of no args which, when
    called, waits for the result, which will start being processed in another
    thread.
    """

    @functools.wraps(f)
    def lazy_thunked(*args, **kwargs):
        wait_event = threading.Event()

        result = [None]
        exc = [False, None]

        def worker_func():
            try:
                func_result = f(*args, **kwargs)
                result[0] = func_result
            except Exception, e:
                exc[0] = True
                exc[1] = sys.exc_info()
                string = "Lazy thunk has thrown an exception (will be raised"
                string+= " on thunk()):\n%s" % (traceback.format_exc())
                print string
            finally:
                wait_event.set()

        def thunk():
            wait_event.wait()
            if exc[0]:
                raise exc[1][0], exc[1][1], exc[1][2]

            return result[0]

        threading.Thread(target=worker_func).start()

        return thunk

    return lazy_thunked

if __name__ == "__main__":
    @lazy_thunkify
    def slow_double(i):
        print "Multiplying..."
        time.sleep(5)
        print "Done multiplying!"
        return i * 2

    def maybe_multiply(x):
        double_thunk = slow_double(x)
        print "Thinking..."
        time.sleep(3)
        time.sleep(3)
        time.sleep(1)
        if x == 3:
            print "Using it!"
            res = double_thunk()
        else:
            print "Not using it."
            res = None
        return res

    # Both take 7 seconds
    maybe_multiply(10)
    maybe_multiply(3)
