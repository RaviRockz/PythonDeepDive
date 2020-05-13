""""""

'''Decimals'''
'''
    --> Decimal constructors
        -> Decimal(x)
            x -> integers (recommended)
            x -> other decimal objects
            x -> strings (recommended)
            x -> tuples (recommended) --> (sign,(significant digits),exponent)) -> (1,(3, 1, 4, 1, 5),-4) 
            x -> floats (not recommended)
            
    --> decimal
        -> finite numbers after precision
        -> exact decimal
        -> context controls precision, round
        -> context can be global and local
    --> context affect math operations but not storage
        -> a = Decimal('0.12345)
        -> b = Decimal('0.12345)
        decimal.getcontext().prec = 2
        -> c = a + b --> c = 0.25(2 precision)
    --> performance
        -> much slower than floats
        -> more memory overhead   
'''

from decimal import Decimal
import decimal
import math

x = Decimal(1)
print(x)
x = Decimal('0.01')
print(x)
x = Decimal('-3.1415')
print(x)
x = Decimal((1, (3, 1, 4, 1, 5), -4))
print(x)

print(format(0.1, '.25f'))
x = Decimal(0.1)
print(x)

a = Decimal('0.12345')
b = Decimal('0.12345')
c = a+b
print(c)
decimal.getcontext().prec = 2
c = a+b
print(c)
with decimal.localcontext() as ctx:
    ctx.prec = 3
    c = a + b
    print(c)

decimal.getcontext().prec = 28
x = 2
x_dec = Decimal('2')

math_sqrt = math.sqrt(x)
math_sqrt1 = math.sqrt(x_dec)
dec_sqrt = x_dec.sqrt()
print(format(math_sqrt, '1.27f'))
print(format(math_sqrt1, '1.27f'))
print(format(dec_sqrt,))
print(format(math_sqrt * math_sqrt, '1.27f'))
print(format(math_sqrt1 * math_sqrt1, '1.27f'))
print(format(dec_sqrt * dec_sqrt))

import sys
import time

a = 3.1415
b = Decimal('3.1415')
print(sys.getsizeof(a))
print(sys.getsizeof(b))


def run(x_, n=1, dec=False):
    start_time = time.perf_counter()
    for i in range(n):
        if dec:
            x_.sqrt()
        else:
            math.sqrt(x_)
    end_time = time.perf_counter()
    return end_time - start_time


print('Float Time: ', run(3.1415, n=10000000))
print('Decimal Time: ', run(Decimal('3.1415'), n=10000000, dec=True))
