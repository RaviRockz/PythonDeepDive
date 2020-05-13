""""""

'''Complex'''
'''
    --> Constructor
        -> complex(x, y)
            x -> real
            y -> imag
    --> Instance and properties
        -> .real
        -> .imag
        -> .conjugate()
    --> operations
        -> supported
            +, -, /, *, **, ==, !=, cmath
        -> not supported    
            // and %, <, >, <=, >=, math
'''

a = complex(2, 3)
print(a)
b = 1 + 3j
print(b)
print(a.real)
print(a.imag)
print(a.conjugate())

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a == b)
print(a != b)

a = 0.1j
print(format(a.imag, '.25f'))
print(a + a + a == 0.3j)
print(format(0.3j.imag, '.25f'))

import cmath

print(cmath.sqrt(1 + 3j))
