""""""

'''Floats'''
'''
    --> Floats uses a fixed number of bytes (64bits)
        sign                -> 1 bit
        exponent            -> 11 bits -> range(-1022, 1023) -> 1.5E-5 -> 1.5 x 10**-5
        significant digits  -> 52 bits -> 15-17 significant (base-10) digits
            -> all digits except leading and trailing zeros
                1.2345
                1234.5
                1234500000
                0.00012345
                1.2345e10
    --> Representing Decimal
        base-10 integers and fractions
        0.75    -> 7/10 + 5/100                                 -> 7 x 10**-1 + 5 x 10**-2
        0.256   -> 2/10 + 5/100 + 6/1000                        -> 2 x 10**-1 + 5 x 10**-2 + 6 x 10**-3
        123.456 -> 1x100 + 2x10 + 3x1 + 4/10 + 5/100 + 6/1000   -> 1x10**2 + 2x10**1 + 3x10**0 + 4x10**-1
                                                                  +5x10**-2 + 6x10**-3
        In general,
            d = n[E]1=-m di x 10i
            sign = 0 for positive
            sign = 1 for negative
            d = (-1)**sign n[E]1=-m di x 10i
'''

print(float(10))
print(float(10.4))
print(float(12.5))
print(float(22/7))

'''infinite'''
print(format(0.1, '.15f'))
print(format(0.1, '.25f'))

'''finite'''
print(1/8)
print(format(0.125, '.25f'))

a = 0.1 + 0.1 + 0.1
b = 0.3

print(a == b)
print(format(a, '.25f'))
print(format(b, '.25f'))

print('''Equality Testing''')
x = 0.125 + 0.125 + 0.125
y = 0.375
print(x == y)
print(format(x, '.25f'))
print(format(y, '.25f'))

a = 0.1 + 0.1 + 0.1
b = 0.3
print(a == b)
print(format(a, '.25f'))
print(format(b, '.25f'))

print('''Equality Using Round''')
a = round(a, 3)
b = round(b, 3)
print(a == b)
print(format(a, '.25f'))
print(format(b, '.25f'))


print('''Equality Using math.isclose()''')
import math
a = 0.1 + 0.1 + 0.1
b = 0.3
print(math.isclose(a, b))


print('''Equality Using math.isclose() rel_tol and abs_tol''')
a = 0.0000001
b = 0.0000002
print(math.isclose(a, b))
print(math.isclose(a, b, rel_tol=0.01))
print(math.isclose(a, b, rel_tol=0.01, abs_tol=0.01))
