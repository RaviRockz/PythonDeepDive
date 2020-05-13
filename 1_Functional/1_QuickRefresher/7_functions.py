""""""

lst = [1, 2, 3]
print(len(lst))

from math import sqrt

print(sqrt(24))

'''Without Param and Return'''


def base_fun():
    print('Executing Base Function')


base_fun()
'''With Param and Return'''


def add(a, b):
    return 'Addition of a and b is: %d' % (a + b)


print(add(4, 6))
'''With Param type and Return type'''


def add_str(a: str, b: str) -> str:
    return a + ' ' + b


print(add_str('Hello', 'World'))
'''Keyword Args'''


def add(a=0, b=0):
    return 'Addition of a and b is: %d' % (a + b)


print(add(a=20, b=5))
print(add(b=5))
print(add(a=20))
print(add())
'''Multi Args'''


def add(*n):
    x = 0
    for i_ in n:
        x += i_
    return 'Addition of Given numbers: %d' % x


print(add(1, 2, 3, 4, 5))
print(add(1, 2, 3))
print(add())


def add(**n):
    return 'Addition of a and b is: %d' % (n['a'] + n['b'])


print(add(a=20, b=5))
print(add(a=20, b=5, c=3, d=5))

'''Lambda Functions'''
power = lambda x: x ** x

for i in range(1, 6):
    print('Power Of %d is %d' % (i, power(i)))
