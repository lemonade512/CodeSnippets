#!/usr/bin/env python

def dump_args(func):
    """ This decorator dumps out the arguments passed to a function
    before calling it.
    """
    argnames = func.func_code.co_varnames[:func.func_code.co_argcount]
    fname = func.func_name

    def echo_func(*args, **kwargs):
        print fname, ":", ', '.join('%s=%r' % entry
                            for entry in zip(argnames,args) + kwargs.items())
        return func(*args, **kwargs)

    return echo_func

@dump_args
def f1(a, b, c):
    print a + b + c

if __name__ == "__main__":
    f1(1, 2, 3)
