#!/usr/bin/env python

import collections
import functools


class memoized(object):
    """ Decorator that caches a functions return value each time it is called.
    If called later with the same arguments, the cached value is returned.
    """
    def __init__(self, func):
        self.func = func
        self.cache = {}

    def __call__(self, *args):
        if not isinstance(args, collections.Hashable):
            # Uncacheable. A list, for instance.
            # Better to not cache than blow up.
            return self.func(*args)
        if args in self.cache:
            return self.cache[args]
        else:
            value = self.func(*args)
            self.cache[args] = value
            return value

    def __repr__(self):
        """ Returns a functions docstring. """
        return self.func.__doc__

    def __get__(self, obj, objtype):
        """ Support for instance methods. """
        return functools.partial(self.__call__, obj)

def memoize(obj):
    """ Alternate memoize function. """
    cache = obj.cache = {}

    @functools.wraps(obj)
    def memoizer(*args, **kwargs):
        key = str(args) + str(kwargs)
        if key not in cache:
            cache[key] = obj(*args, **kwargs)
        return cache[key]

    return memoizer

@memoized
def fibonacci(n):
    """ Return the nth fibonacci number. """
    if n in (0, 1):
        return n

    return fibonacci(n-1) + fibonacci(n-2)

if __name__ == "__main__":
    print fibonacci(12)
