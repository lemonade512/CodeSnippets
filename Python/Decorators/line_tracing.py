#!/usr/bin/env python

import sys
import os
import linecache

def trace(f):
    def globaltrace(frame, why, arg):
        if why == "call":
            return localtrace
        return None

    def localtrace(frame, why, arg):
        if why == "line":
            # record the file name and line number of every trace
            filename = frame.f_code.co_filename
            lineno = frame.f_lineno
            bname = os.path.basename(filename)
            print "{}({}): {}".format(bname,
                                      lineno,
                                      linecache.getline(filename, lineno)),
        return localtrace

    def _f(*args, **kwargs):
        sys.settrace(globaltrace)
        result = f(*args, **kwargs)
        sys.settrace(None)
        return result

    return _f

@trace
def my_func(a, b, c):
    print "a:", a
    print "b:", b
    print "c:", c
    d = a + b + c
    print "d:", d

if __name__ == "__main__":
    my_func(1, 2, 3)
