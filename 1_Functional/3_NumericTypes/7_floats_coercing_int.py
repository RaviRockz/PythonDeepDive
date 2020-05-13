""""""

'''Floats: Coercing To Integers'''
'''
    --> math.trunc (int)
        integer part only
    --> math.floor
        smallest integer less than x
    --> math.ceil
        largest integer greater than x
'''

import math

print('''Using Trunc''')
print(math.trunc(10.4))
print(math.trunc(10.5))
print(math.trunc(10.6))
print(math.trunc(-10.4))
print(math.trunc(-10.5))
print(math.trunc(-10.6))

print('''Using int''')
print(int(10.4))
print(int(10.5))
print(int(10.6))
print(int(-10.4))
print(int(-10.5))
print(int(-10.6))

print('''Using Floor''')
print(math.floor(10.4))
print(math.floor(10.5))
print(math.floor(10.6))
print(math.floor(-10.4))
print(math.floor(-10.5))
print(math.floor(-10.6))

print('''Using Ceil''')
print(math.ceil(10.4))
print(math.ceil(10.5))
print(math.ceil(10.6))
print(math.ceil(-10.4))
print(math.ceil(-10.5))
print(math.ceil(-10.6))
