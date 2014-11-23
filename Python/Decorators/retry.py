#!/usr/bin/env python

import time
import math

# TODO make docstring follow conventions
# Retry decorator with exponential backoff
def retry(tries, delay=3, backoff=2):
    """ Retries a function or method until it returns True.

    delay sets the initial delay in seconds, and backoff sets the factor by
    which the delay should lengthen after each failure. backoff must be
    greater than 1, or else it isn't really a backoff. tries must be at least
    0, and delay greater than 0.
    """

    if backoff <= 1:
        raise ValueError("backoff must be greater than 1")

    tries = math.floor(tries)
    if tries < 0:
        raise ValueError("tries must be 0 or greater")

    if delay <= 0:
        raise ValueError("delay must be greater than 0")

    def deco_retry(f):
        def f_retry(*args, **kwargs):
            mtries, mdelay = tries, delay # make mutable

            rv = f(*args, **kwargs) # first attempt
            while mtries > 0:
                if rv is True: # Done on success
                    return True

                mtries -= 1     # consume an attempt
                time.sleep(mdelay) # wait...
                mdelay *= backoff # Make future wait longer

                rv = f(*args, **kwargs) # Try again

            return False # Ran out of tries

        return f_retry # true decorator -> decorated function

    return deco_retry # @retry(arg[, ...]) -> true decorator

count = 0
@retry(3, delay=2)
def test_func():
    global count
    print "Trying", count
    if count > 1:
        return True
    else:
        count += 1
        return False

@retry(2, delay=1)
def test_func_2():
    print "Trying"
    return False

if __name__ == "__main__":
    print "Test func 1"
    print test_func()
    print "\n",

    print "Test func 2"
    print test_func_2()

