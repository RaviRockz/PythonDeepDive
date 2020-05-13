""""""

'''Lambda Expressions'''
'''
    --> Anonymous functions
        -> another way to create functions without def keyword
    --> lambda [params]: expression
        -> lambda x: x**2
        -> lambda x, y: x + y
        -> lambda : 'hello'
    --> Assign lambda to a variable
        -> function object
    --> No annotations
    --> No assignments
    --> single logical line
    --> passing quick function to another function
'''


sqr = lambda x: x ** 2
print(sqr)
print(type(sqr))
print(sqr(2))
print(sqr(4))
print(sqr(5))


power = lambda x, n: x ** n
print(power(x=2, n=5))


def square(n, fn):
    return fn(n)


print(square(5, lambda x: x**2))


'''Lambda and Sorting'''
lst = [1, 4, 0, 3, 2, 7, 9]
print(sorted(lst))
lst = ['X', 'Z', 'a', 'y', 'A', 'B']
print(sorted(lst))
print(sorted(lst, key=lambda s: s.upper()))
d = {'def': 300, 'abc': 200, 'ghi': 100}
for e in d:
    print(e)
print(sorted(d))
print(sorted(d, key=lambda e_: d[e_]))


def dist_sq(x):
    return x.real ** 2 + x.imag ** 2


print(dist_sq(1+1j))
lst = [3+3j, 1-1j, 0, 3+0j]
print(sorted(lst, key=dist_sq))
print(sorted(lst, key=lambda x_: x_.real ** 2 + x_.imag ** 2))


lst = ['Cheese', 'RoseMilk', 'Cappuccino', 'Curd']
print(sorted(lst, key=lambda s: s[-1]))
print(sorted(lst, key=lambda s: s[2]))


'''Randomize an iterable using sorted'''
import random
print(sorted(lst, key=lambda s: random.random()))
