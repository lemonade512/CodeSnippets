#!/usr/bin/python
'''
make_args_strings.py

This snippet is an example of a decorator. The decorator in
this case takes a functions arguments and turns them into
strings.

Author: Phillip Lemons
Date Modified: 2/16/2014
'''

def _make_arguments_strings(fn):
    def wrapped(*args, **kwargs):
	new_args = [str(arg) for arg in args]
	kwargs = {key:str(value) for key,value in kwargs.iteritems()}

	for arg in new_args:
	    assert(type(arg) == type(""))

	for value in kwargs.itervalues():
	    assert(type(value)==type(""))

	return fn(*new_args, **kwargs)
    return wrapped

@_make_arguments_strings
def my_function(num1, num2, *args, **kwargs):
    print "Num1:: " + num1 + ", Num2:: " + num2
    for i, arg in enumerate(args):
        print i, args[i]

    for key,value in kwargs.iteritems():
        print key + "::", value
    return

my_function(1,4,6,8,10,number=4)
