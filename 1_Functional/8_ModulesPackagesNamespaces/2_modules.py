""""""

'''Modules'''
'''
    --> module is instances of ModuleType
        -> instance is instances of a class type
        -> filename is the module
    --> def func():
            return 10
        -> func --> <function __main__.func> -> memory address
            -> function --> type
            -> __main__ --> module
    --> globals()
        -> tells all the global namespaces
        -> f = globals()['func']
        -> f()
    --> locals() like globals()
        -> but inside local it is different
    --> create own module using ModuleType in types
    --> how python import modules
        -> import at runtime
        -> sys.prefix -> where python is installed
        -> sys.path -> PYTHONPATH to search modules when imported
'''

import math
import fractions

print(math)
print(fractions)
print(globals())
print(id(globals()['math']))

import sys
print(sys.modules['math'])  # not recommended because it returns topmost
print(id(sys.modules['math']))

import types
print(type(math))
print(isinstance(math, types.ModuleType))

add_module = types.ModuleType('add_module', 'Add Numbers')
print(add_module)
add_module.add = lambda x, y: x + y
print(add_module.add(2, 3))

print(sys.prefix)
print(sys.path)
del globals()['math']
print(globals())
