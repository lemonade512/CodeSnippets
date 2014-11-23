#!/usr/bin/env python

import warnings
import functools

def deprecated(func):
    """ This is a decorator which can be used to mark functions
    as deprecated. It will result in a warning being emitted
    when the function is used.
    """

    @functools.wraps(func)
    def new_func(*args, **kwargs):
        warnings.simplefilter('once', DeprecationWarning)
        warnings.warn_explicit(
            "Call to deprecated function {}.".format(func.__name__),
            category=DeprecationWarning,
            filename=func.func_code.co_filename,
            lineno=func.func_code.co_firstlineno + 1
        )
        return func(*args, **kwargs)
    return new_func

## Usage examples ##
@deprecated
def my_func():
    print "Using my_func"

#@other_decorators_must_be_upper
#@deprecated
#def my_func():
#    pass

if __name__ == "__main__":
    my_func()
