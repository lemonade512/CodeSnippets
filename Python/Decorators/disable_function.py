#!/usr/bin/env python

def unchanged(func):
    """ This decorator doesn't add any behavior. """
    return func

def disabled(func):
    """ This decorator disables the provided function, and does nothing. """
    def empty_func(*args, **kwargs):
        pass

    return empty_func

# define this as equivalent to unchanged, for nice symmetry with disabled
enabled = unchanged

#
# Sample use
#

GLOBAL_ENABLE_FLAG = True

state = enabled if GLOBAL_ENABLE_FLAG else disabled
@state
def special_function_foo():
    print "Function was enabled"

if __name__ == "__main__":
    special_function_foo()
