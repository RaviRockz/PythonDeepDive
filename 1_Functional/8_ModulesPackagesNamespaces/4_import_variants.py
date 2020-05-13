""""""

'''
    --> Efficient
        -> import math
        -> not from math import sqrt
'''

import sys

import cmath
print('cmath' in sys.modules)
print('cmath' in globals())
del sys.modules['cmath']


import cmath as c_math
print('cmath' in sys.modules)
print('cmath' in globals())
print('c_math' in sys.modules)
print('c_math' in globals())
del sys.modules['cmath']
del globals()['c_math']

from cmath import exp
print('cmath' in sys.modules)
print('cmath' in globals())
print('exp' in sys.modules)
print('exp' in globals())
