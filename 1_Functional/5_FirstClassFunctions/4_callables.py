""""""

'''Callables'''
'''
    --> () operator -> always return a value
    --> like functions and methods
    --> Types of callables
        -> built-in functions
        -> built-in methods
        -> user-defined functions -> using def and lambda
        -> methods -> functions bound to and object
        -> classes
        -> class instances -> __call__        
'''

print(callable(print))
print(callable(str.upper))
print(callable(10))


class MyClass:
    def __init__(self, x=0):
        print('Initializing...')
        self.counter = x


print(callable(MyClass))
a = MyClass(100)
print(a.counter)


class MyClass:
    def __init__(self, x=0):
        print('Initializing...')
        self.counter = x

    def __call__(self, x=1):
        print('Updating counter...')
        self.counter += x


b = MyClass()
print(b.counter)
MyClass.__call__(b, 10)
print(b.counter)
MyClass.__call__(b, 10)
print(b.counter)
MyClass.__call__(b, 10)
print(b.counter)
