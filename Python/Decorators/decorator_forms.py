#!/usr/bin/env python

from sys import stdout, stderr
from pdb import set_trace as bp

class DecoTrace(object):
    """ Decorator class with no arguments

    This can only be used for functions or methods where the instance
    is not necessary.
    """

    def __init__(self, f):
        self.f = f

    def _showargs(self, *args, **kwargs):
        print >> stderr, "T: enter {} with args={}, kw={}".format(
                self.f.__name__, str(args), str(kwargs))

    def _aftercall(self, status):
        print >> stderr, "T: exit {} with status={}".format(
                self.f.__name__, str(status))

    def __call__(self, *args, **kwargs):
        """ Pass *just* function arguments to wrapped function. """
        self._showargs(*args, **kwargs)
        ret = self.f(*args, **kwargs)
        self._aftercall(ret)
        return ret

    def __repr__(self):
        return self.f.func_name

class DecoTraceWithArgs(object):
    """ Decorator class with ARGUMENTS

    This can be used for unbounded functions and methods. If this wraps a
    class instance, then extract it and pass to the wrapped method as the
    first arg.
    """

    def __init__(self, *dec_args, **dec_kwargs):
        """ The decorator arguments are passed here. Save them for runtime. """
        self.dec_args = dec_args
        self.dec_kwargs = dec_kwargs

        self.label = dec_kwargs.get("label", "T")
        self.fid = dec_kwargs.get("stream", stderr)

    def _showargs(self, *args, **kwargs):

        print >> self.fid, "{}: enter {} with args={}, kw={}".format(
            self.label, self.f.__name__, str(args), str(kwargs))
        print >> self.fid, "{}: passing decorator args={}, kwargs={}".format(
            self.label, str(self.dec_args), str(self.dec_kwargs))

    def _aftercall(self, status):
        print >> self.fid, "{}: exit {} with status={}".format(
            self.label, self.f.__name__, str(status))

    def _showinstance(self, instance):
        print >> self.fid, "{}: instance={}".format(self.label, instance)

    def __call__(self, f):
        def wrapper(*args, **kwargs):
            """
                Combine decorator arguments and function arguments and pass to
                wrapped class instance-aware function/method.

                Note: The first argument cannot be "self" because we get a
                parse error "takes at least 1 argument" unless the instance is
                actually included in the argument list, which is redundant. If
                this wraps a class instance, the "self" will be the first
                argument.
            """

            self._showargs(*args, **kwargs)

            # merge decorator keywords into the kw argument list
            kwargs.update(self.dec_kwargs)

            # Does this wrap a class instance?
            if args and getattr(args[0], '__class__', None):

                # Pull out the instance and combine function and
                # decorator args
                instance, args = args[0], args[1:] + self.dec_args
                self._showinstance(instance)

                # call the method
                ret = f(instance, *args, **kwargs)
            else:
                # Just send in the given args and kwargs
                ret = f(*(args + self.dec_args), **kwargs)

            self._aftercall(ret)
            return ret

        # Save wrapped function reference
        self.f = f
        wrapper.__name__ = f.__name__
        wrapper.__dict__.update(f.__dict__)
        wrapper.__doc__ = f.__doc__
        return wrapper

@DecoTrace
def FirstBruce(*args, **kwargs):
    """ Simple function using simple decorator. """
    if args and args[0]:
        print args[0]

@DecoTraceWithArgs(name="Second Bruce", standardline="G'day, Bruce!")
def SecondBruce(*args, **kwargs):
    """ Simple function using decorator with arguments. """
    print "{}:".format(kwargs.get("name", "Unknown Bruce"))

    if args and args[0]:
        print args[0]
    else:
        print kwargs.get("standardline", None)

class Bruce(object):
    """ Simple class. """

    def __init__(self, id):
        self.id = id

    def __str__(self):
        return self.id

    def __repr__(self):
        return "Bruce"

    @DecoTraceWithArgs(label="Trace a class", standardline="How are ya Bruce?",
                       stream=stdout)
    def talk(self, *args, **kwargs):
        """ Simple function using decorator with arguments. """

        print "{}:".format(self)
        if args and args[0]:
            print args[0]
        else:
            print kwargs.get("standardline", None)

if __name__ == "__main__":
    ThirdBruce = Bruce("Third Bruce")

    SecondBruce()
    FirstBruce("First Bruce: Oh, Hello Bruce!")
    ThirdBruce.talk()
    FirstBruce("First Bruce: Bit crook, Bruce.")
    SecondBruce("Where's Bruce?")
    FirstBruce("First Bruce: He's not here, Bruce")
    ThirdBruce.talk("Blimey, s'hot in here, Bruce.")
    FirstBruce("First Bruce: S'hot enough to boil a monkey's bum!")
    SecondBruce("That's a strange expression, Bruce.")
