#!/usr/bin/env python

#TODO find out how this works
#https://wiki.python.org/moin/PythonDecoratorLibrary#CA-e6b32ec67d709fe92640a7cc6caa6a033b9eae7d_14

import functools
import inspect

def decorator(func):
    """ Allow to use either with arguments or not. """

    def isFuncArg(*args, **kwargs):
        return len(args) == 1 and len(kwargs) == 0 and (
            inspect.isfunction(args[0]) or isinstance(args[0], type))

    if isinstance(func, type):
        def class_wrapper(*args, **kwargs):
            if isFuncArg(*args, **kwargs):
                return func()(*args, **kwargs)# create class before usa
            return func(*args, **kwargs)
        class_wrapper.__name__ = func.__name__
        class_wrapper.__module__ = func.__module__
        return class_wrapper

    @functools.wraps(func)
    def func_wrapper(*args, **kwargs):
        if isFuncArg(*args, **kwargs):
            return func(*args, **kwargs)

        def functor(userFunc):
            return func(userFunc, *args, **kwargs)

        return functor

    return func_wrapper


# ---------------- Examples: Uncomment 1 ---------------

@decorator
def apply(func, *args, **kwargs):
    return func(*args, **kwargs)

#@decorator
#class apply:
#    def __init__(self, *args, **kwargs):
#        self.args = args
#        self.kwargs = kwargs
#
#    def __call__(self, func):
#        return func(*self.args, **self.kwargs)

@apply
def test():
    return 'test'

assert test == 'test'

@apply(2, 3)
def test(a, b):
    return a + b

assert test is 5
