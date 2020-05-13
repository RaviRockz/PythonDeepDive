""""""

'''Function Introspection'''
'''
    --> Function had some attributes
        __doc__
        __annotations__
    --> Also attach our own attributes
        func.attr = value
        print(func.attr)
    --> dir()
        -> returns a list of valid attributes for passed object
    --> __name__, __defaults__, __kwdefaults__
        -> name of function
        -> position param defaults
        -> keyword param defaults
    --> __code__, __code__.co_varnames, __code__.co_argcount
        -> return code object
        -> params an local variables
        -> param count ( does not count *args and **kwargs)
    --> Inspect using inspect module
        -> ismethod(obj), isfunction(obj), isroutine(obj)
            -> method -> attribute that is callable is method
            -> function -> without an instance callable is function
            -> routine -> both method and function
        -> getsource(func)
            -> get string containing our entire statement , docstring, annotations etc
        -> getmodule(func)
            -> to find out in which module our func is created
        -> getcomments(func)
            -> # TODO:
        -> signature(func).parameters.values()
            -> key, values pair -> metadata about param
            -> kind
                -> POSITIONAL_OR_KEYWORD
                -> VAR_POSITIONAL
                -> KEYWORD_ONLY
                -> VAR_KEYWORD
                -> POSITIONAL_ONLY       
'''


def my_func(a: 'mandatory positional',
            b: 'optional positional' = 1,
            c=2,
            *args: 'add extra positional here',
            kw1,
            kw2=100,
            kw3=200,
            **kwargs: 'provide extra kw-only here') -> 'does nothing':
    """This function does nothing but have various params and annotations"""
    i = 10
    j = 20


print(my_func.__doc__)
print(my_func.__annotations__)
my_func.new_attr = 'New Attr'
print(my_func.new_attr)
print(dir(my_func))
print(my_func.__name__)
print(my_func.__defaults__)
print(my_func.__kwdefaults__)
print(my_func.__code__)
print(my_func.__code__.co_varnames)
print(my_func.__code__.co_argcount)

import inspect

print(inspect.ismethod(my_func))
print(inspect.isfunction(my_func))
print(inspect.isroutine(my_func))
print(inspect.getsource(my_func))
print(inspect.getmodule(my_func))
print(inspect.signature(my_func).parameters.values())
print(inspect.signature(my_func).return_annotation)
