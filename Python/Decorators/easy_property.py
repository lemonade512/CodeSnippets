#!/usr/bin/env python

import sys

def propget(func):
    locals = sys._getframe(1).f_locals
    name = func.__name__
    prop = locals.get(name)
    if not isinstance(prop, property):
        prop = property(func, doc=func.__doc__)
    else:
        doc = prop.__doc__ or func.__doc__
        prop = property(func, prop.fset, prop.fdel, doc)
    return prop

def propset(func):
    locals = sys._getframe(1).f_locals
    name = func.__name__
    prop = locals.get(name)
    if not isinstance(prop, property):
        prop = property(None, func, doc=func.__doc__)
    else:
        doc = prop.__doc__ or func.__doc__
        prop = property(prop.fget, func, prop.fdel, doc)
    return prop

def propdel(func):
    locals = sys._getframe(1).f_locals
    name = func.__name__
    prop = locals.get(name)
    if not isinstance(prop, property):
        prop = property(None, None, func, doc=func.__doc__)
    else:
        prop = property(prop.fget, prop.fset, func, prop.__doc__)
    return prop


# Example usage

class Example(object):

    def __init__(self):
        self.myattr = 10

    @propget
    def myattr(self):
        print "Getting myattr",
        return self._half * 2

    @propset
    def myattr(self, value):
        print "Setting myattr", value
        self._half = value / 2

    @propdel
    def myattr(self):
        print "Deleting myattr"
        del self._half

class Example2(object):

    def __init__(self):
        self._myattr = 5

    @propget
    def myattr(self):
        print "Getting myattr",
        return self._myattr

if __name__ == "__main__":
    e = Example()
    print "Half:", e._half
    print e.myattr
    e.myattr = 20
    print "Half:", e._half
    print e.myattr
    del e.myattr

    print "\n",
    e = Example2()
    print e.myattr
    try:
        e.myattr = 0
    except AttributeError:
        print "Cannot set myattr"
