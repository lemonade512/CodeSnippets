#!/usr/bin/env python

# Annotation wrapper annotation method
def unimplemented(defaultval):
    if(type(defaultval) == type(unimplemented)):
        return lambda: None
    else:
        # Actual annotation
        def unimp_wrapper(func):
            # What we replace the function with
            def wrapper(*arg):
                return defaultval
            return wrapper
        return unimp_wrapper

@unimplemented("default_val")
def my_func():
    pass

if __name__ == "__main__":
    print "Return value of my_func:", my_func()
