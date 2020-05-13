""""""

'''Reducing FUnctions'''
'''
    --> Recombine an iterable recursively and ending up with a single return value
        -> min, max
    --> functools -> reduce -> initializer (1)
    --> Built-in reducing functions
        -> min, max, sum, any, all
'''


min_finder = lambda a, b: a if a < b else b
max_finder = lambda a, b: a if a > b else b
summer = lambda a, b: a+b


def min_(lst: list):
    result = lst[0]
    for i in lst[1:]:
        result = min_finder(result, i)
    return result


def max_(lst: list):
    result = lst[0]
    for i in lst[1:]:
        result = max_finder(result, i)
    return result


lst_ = [1, 2, 3, 4, 5]
print(min_(lst_))
print(max_(lst_))
from functools import reduce
print(reduce(min_finder, lst_))
print(reduce(max_finder, lst_))
print(reduce(summer, lst_))
