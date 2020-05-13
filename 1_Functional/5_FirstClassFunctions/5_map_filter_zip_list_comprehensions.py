""""""

'''Map, Filter, Zip and List Comprehensions'''
'''
    --> map(func, *iterables)
    --> filter(func, iterable)
    --> zip(*iterables)
    --> List Comprehensions

'''


def sqr(x):
    return x ** 2


lst = [1, 2, 3, 4, 5]
sqr_lst = list(map(sqr, lst))
print(sqr_lst)


def get_even(x):
    return False if x % 2 else True


lst = [1, 2, 3, 4, 5]
sqr_lst = list(filter(get_even, lst))
print(sqr_lst)

lst = [1, 2, 3, 4, 5]
lst1 = [6, 7, 8, 9]

for i, j in zip(lst, lst1):
    print(i, j)

print([x + y for x, y in zip(lst, lst1)])
print([x for x in lst if x % 2 == 0])
