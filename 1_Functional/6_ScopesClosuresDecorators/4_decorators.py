""""""

'''Decorators Part 1'''
'''
    --> Decorator function takes a function as an argument and returns a closure
    --> Closure usually accepts any combination of params, Runs some code in the inner function (closure)
    --> The closure function calls throw original function using args passed to the 
        closure and returns whatever by the function call
        
         ________________________________________
        | outer_function|(fn)|                   |
        |     __________|    |_________________  |
        |    | inner_function(*args, **kwargs) | |
        |    |      does something             | |
        |    |  returns fn(*args, **kwargs)    | |
        |    |_________________________________| |
        |________________________________________|
        
    --> Decorators using @ symbol
    --> if func is decorator, we decorate another function my_fun using
            my_func = func(my_func)
    --> Introspection
        
            def counter(fn):
                count = 0
                def inner(*args, **kwargs):
                    nonlocal count
                    count += 1
                    return fn(*args, **kwargs)
                return inner
                        _________________
            @counter <-|                 |
            def mult(a, b, c=1):         |
                return a * b * c         |----> equal
                                         |
            mult = counter(mult)_________|
            
        -> mult.__name__    -> inner not mult
        -> help(mult)       -> return help(inner)
        -> to fix this      -> override the __name__ and __doc__ prop of inner  (or using functools.wrap)
        -> inner = wraps(fn)(inner)  (or) decorate using @wrap(fn) to inner
'''
from functools import wraps


def counter(fn):
    count = 0

    @wraps(fn)
    def inner(*args, **kwargs):
        nonlocal count
        count += 1
        print(f'Function: {fn.__name__} id: {hex(id(fn))} was called {count} times')
        return fn(*args, **kwargs)

    return inner


@counter
def mult(a: int, b: int, c: int = 10):
    """Multiply three Values"""
    return a * b * c


mult = counter(mult)
print(mult.__closure__)
print(mult.__code__.co_freevars)
print(mult(10, 20))
print(mult.__closure__)
print(mult.__code__.co_freevars)
print(mult(30, 20))
print(mult.__closure__)
print(mult.__code__.co_freevars)
help(mult)


def capitalize(func):
    def uppercase():
        result = func()
        return result.upper()

    return uppercase


@capitalize
def say_hello():
    return "hello"


print(say_hello())


def square(func):
    def multiply(*args):
        f = func(*args)
        return f * f

    return multiply
