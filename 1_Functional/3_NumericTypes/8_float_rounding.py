""""""

'''ROunding Floats'''
'''
    --> round(x, n)
        x -> int -> int
        x -> float -> int
        x, n -> float, int -> float
'''

import math

print('''Using round''')
print(round(10))
print(round(10.4))
print(round(10.4, 2))
print(round(10.6, 2))
print(round(10.6))
print(round(1.23, 1))
print(round(1.26, 1))
print(round(-1.23, 1))
print(round(-1.26, 1))
print('''Bankers Rounding''')
print(round(1.25, 1))
print(round(1.35, 1))
print(round(3.25, 1))
print(round(3.35, 1))
print(round(15, -1))
print(round(25, -1))
print('''Common rounding for positive''')
print(int(10.3+0.5))
print(int(10.5+0.5))
print(int(10.9+0.5))
print('''Common rounding for negative''')
print(int(-10.3-0.5))
print(int(-10.5-0.5))
print(int(-10.9-0.5))
print('''Common rounding for positive and negative''')
print(int(10.3 + math.copysign(0.5, 10.3)))
print(int(10.5 + math.copysign(0.5, 10.5)))
print(int(10.9 + math.copysign(0.5, 10.9)))
print(int(-10.3 + math.copysign(0.5, -10.3)))
print(int(-10.5 + math.copysign(0.5, -10.5)))
print(int(-10.9 + math.copysign(0.5, -10.9)))
