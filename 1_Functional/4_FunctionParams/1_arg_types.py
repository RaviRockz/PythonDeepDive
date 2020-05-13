""""""

'''Argument Types'''
'''
    --> Positional Args
        -> order is important
    --> Default args
    --> Keyword or optional args
    --> *args ->
    --> after * --> no positional args -> only pass keyword args
        
        def func(a, b=1, *args, d, e=True):              def func(a, b=1, *, d, e=True):
            pass                                             pass
    --> **kwargs -> no params after this
        -> access like dicts
'''

print('''Position Args''')


def my_func(a, b, c):
    print(a, b, c)


my_func(1, 2, 3)

print('''Default and Keyword Args''')


def my_func_1(a, b=10, c=20):
    print(a, b, c)


my_func_1(1, 2, 3)
my_func_1(1, 2)
my_func_1(1)
my_func_1(1, c=2, b=3)
my_func_1(c=1, a=2, b=3)

print('''*args''')


def my_func_2(*args):
    for arg in args:
        print(arg, end=' ')
    print()


my_func_2(1, 2, 3, 4, 5)
my_func_2(1, 2, 3)


def my_func_3(a, b, *args, d):
    print(a, b, args, d)


my_func_3(1, 2, 3, 4, d=5)
my_func_3(1, 2, 3, 4, 5, 6, 7, 8, d=5)
my_func_3(1, 2, d=5)


def my_func_4(a, b=5, *, d):
    print(a, b, d)


my_func_4(1, 2, d=5)
my_func_4(1, d=5)


print('''**kwargs''')


def my_func_5(*args, **kwargs):
    print(args, kwargs)


my_func_5(a=1, b=2, c=4)
my_func_5(2, 2, 3, 3, a=1, b=2, c=4)
