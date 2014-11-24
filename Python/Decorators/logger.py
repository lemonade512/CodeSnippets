#!/usr/bin/env python

import functools, logging

log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)

class log_with(object):
    """ Logging decorator that allows you to log with
    a specific logger.
    """

    # Customize these messages
    ENTRY_MESSAGE = "Entering {}"
    EXIT_MESSAGE = "Exiting {}"

    def __init__(self, logger=None):
        self.logger = logger

    def __call__(self, func):
        """ Returns a wrapper that wraps func. The wrapper will
        log the entry and exit points of the function with
        logging.INFO level.
        """
        # Set logger if it was not set earlier
        if not self.logger:
            logging.basicConfig()
            self.logger = logging.getLogger(func.__module__)

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            self.logger.info(self.ENTRY_MESSAGE.format(func.__name__))
            f_result = func(*args, **kwargs)
            self.logger.info(self.EXIT_MESSAGE.format(func.__name__))
            return f_result
        return wrapper

# Sample use and output

if __name__ == "__main__":
    logging.basicConfig()
    log = logging.getLogger("custom_log")
    log.setLevel(logging.DEBUG)
    log.info("ciao")

    @log_with(log)
    def foo():
        print "This is foo"
    foo()

    print
    @log_with()
    def foo2():
        print "This is foo2"
    foo2()
