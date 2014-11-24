#!/usr/bin/env python

import sys
import logging

class LogPrinter:
    """ LogPrinter class which serves to emulate a file object and logs
    whatever it gets sent to a Logger object at the INFO level.
    """
    def __init__(self):
        """ Grabs the specific logger to use for log printing. """
        self.ilogger = logging.getLogger('logprinter')
        il = self.ilogger
        logging.basicConfig()
        il.setLevel(logging.INFO)

    def write(self, text):
        """ Logs written output to a specific logger. """
        self.ilogger.info(text)

def logprintinfo(func):
    """ Wraps a method so that any calls made to print get logged instead. """
    def pwrapper(*args, **kwargs):
        stdobak = sys.stdout
        lpinstance = LogPrinter()
        sys.stdout = lpinstance
        try:
            return func(*args, **kwargs)
        finally:
            sys.stdout = stdobak
    return pwrapper

@logprintinfo
def my_func():
    print "Hello"

if __name__ == "__main__":
    my_func()
