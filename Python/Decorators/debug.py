#!/usr/bin/env python

import sys

# Add the parts you want to debug and the rest will be ignored
WHAT_TO_DEBUG = set(['io', 'core'])

class debug:
    """ Decorator which helps control what aspects of a program to debug
    on a per-function basis. Aspects are provided as list of arguments.
    It DOESN'T slowdown functions which aren't supposed to be debugged.
    """
    def __init__(self, aspects=None):
        self.aspects = set(aspects)

    def __call__(self, f):
        if self.aspects & WHAT_TO_DEBUG:
            def newf(*args, **kwargs):
                print >> sys.stderr, f.func_name, args, kwargs
                f_result = f(*args, **kwargs)
                print >> sys.stderr, f.func_name, "returned", f_result
                return f_result
            newf.__doc__ = f.__doc__
            return newf
        else:
            return f

@debug(['io'])
def prn(x):
    print x

@debug(['core'])
def mult(x, y):
    return x * y

if __name__ == "__main__":
    prn(mult(2, 2))
