#!/usr/bin/env python

class CGIMethod(object):
    def __init__(self, title):
        self.title = title

    def __call__(self, fn):
        def wrapped_fn(*args):
            print "Content-Type: text/html\n\n"
            print "<HTML>"
            print "<HEAD><TITLE>{}</TITLE></HEAD>".format(self.title)
            print "<BODY>"
            try:
                fn(*args)
            except Exception, e:
                print
                print e
            print
            print "</BODY></HTML>"

        return wrapped_fn

@CGIMethod("Hello with Decorator")
def say_hello():
    print "<h1>Hello from CGI_Land</h1>"

if __name__ == "__main__":
    say_hello()
