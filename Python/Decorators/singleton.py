#!/usr/bin/env python

def singleton(cls):
    instance = cls()
    instance.__call__ = lambda: instance
    return instance

#
# Sample use
#

@singleton
class Highlander:
    x = 100
    # Of course you can have any attributes or methods you like.

if __name__ == "__main__":
    Highlander() is Highlander() is Highlander #=> True
    id(Highlander()) == id(Highlander) #=> True
    Highlander().x == Highlander.x == 100 #=> True
    Highlander.x = 50
    Highlander().x == Highlander.x == 50 #=> True
