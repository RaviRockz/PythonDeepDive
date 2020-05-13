""""""

'''Partial Functions'''
'''
    --> Reducing the function arguments
    --> functools --> partial
    --> beware params defaults
'''


def my_func(a, b, c, d):
    print(a, b, c, d)


def _partial(b, c, d):
    return my_func(10, b, c, d)


_partial(1, 2, 3)
from functools import partial
f = partial(my_func, 10)
f(1, 2, 3)


def pow_(base, exponent):
    return base ** exponent


square = partial(pow_, exponent=2)
cube = partial(pow_, exponent=3)
print(square(base=2), cube(base=2))
