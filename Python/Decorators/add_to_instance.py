#!/usr/bin/env python

import types

class Foo:
    def __init__(self):
        self.x = 42

def addto(instance):
    def decorator(f):
        f = types.MethodType(f, instance, instance.__class__)
        setattr(instance, f.func_name, f)
        return f
    return decorator

if __name__ == "__main__":
    foo = Foo()

    @addto(foo)
    def print_x(self):
        print self.x

    foo.print_x()
