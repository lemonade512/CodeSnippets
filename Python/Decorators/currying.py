#!/usr/bin/env python

class curried(object):
    """ Decorator that returns a function that keeps returning functions
    until all arguments are supplied; then the original function is
    evaluated.
    """

    def __init__(self, func, *args):
        self.func = func
        self.args = args

    def __call__(self, *args):
        args = self.args + args
        if len(args) < self.func.func_code.co_argcount:
            return curried(self.func, *args)
        else:
            return self.func(*args)

@curried
def add(a, b):
    return a + b

if __name__ == "__main__":
    add1 = add(1)
    print add1(2)
