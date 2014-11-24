#!/usr/bin/env python

import functools as ft
import operator as op

def summed(f):
    return lambda *xs: sum(f(*xs))

def averaged(f):
    def aux(acc, x):
        return (acc[0] + x, acc[1] + 1)

    def out(*xs):
        s, n = ft.reduce(aux, f(*xs), (0, 0))
        return s / n if n > 0 else 0

    return out

if __name__ == "__main__":
    @averaged
    def producer2():
        yield 10
        yield 5
        yield 2.5
        yield 7.5

    assert producer2() == (10 + 5 + 2.5 + 7.5) / 4

    @summed
    def producer1():
        yield 10
        yield 5
        yield 2.5
        yield 7.5

    assert producer1() == (10 + 5 + 2.5 + 7.5)
