""""""

'''Rational Numbers'''
'''
    --> Rationals are Fraction of integers
        -> 1/2, -22/7
    --> real number with a finite number of digits after decimal point also a rational
        -> 0.45 = 45/10
        -> 8.3/4 = 83/40
        ->8.3/1.4 = 83/10 / 14/10 = 83/10 * 10/14 = 83/14
    --> In Python, Fraction is represented as:
        -> from fractions import Fraction
    --> Negative Sign
        -> Always attached to the numerator
    --> Constructors
        -> Fraction(numerator=0, denominator=0)
        -> Fraction(other_fraction)
        -> Fraction(decimal)
        -> Fraction(string)
    --> Operations
        -> +, -, *, / -> result is fraction object
    --> attributes
        -> Fraction.numerator
        -> Fraction.denominator
    --> float object as finite precision (any float can be written as fraction)
    --> float to fraction --> important caveat <--
                1/8 -> float representation -> 0.125 (exact float repr)
                3/10 -> float representation -> (5404319552844595, 18014398509481984) wrong
                    because not a finite
                format(0.3, '.5f) -> 0.30000
                format(0.3, '.25f) -> 0.2999999999999999888977698
    --> limit denominator for closest float fraction
        x = Fraction(math.pi)   -> Fraction(884279719003555, 281474976710656)
        3.141592653589793          3.141592653589793
        x.limit_denominator(10) -> Fraction(22, 7)
        3.142857142857143          3.142857142857143
'''
from math import pi
from fractions import Fraction

x = Fraction(1)
print(x)
x = Fraction(1, 2)
print(x)
x = Fraction(-22, 7)
print(x)
x = Fraction(0.125)
print(x)
x = Fraction('22/7')
print(x)

x = Fraction(2, 3)
y = Fraction(3, 4)
print(x + y)
print(x - y)
print(x * y)
print(x / y)

x = Fraction(2, -3)
print(x.numerator, x.denominator)

print(format(0.3, '.5f'))
print(format(0.3, '.25f'))
x = Fraction(0.3)
print(x)
x = x.limit_denominator(10)
print(x)

x = Fraction(pi)
print(pi)
print(float(x))
print(x)
x = x.limit_denominator(10)
print(x)
print(float(x))
