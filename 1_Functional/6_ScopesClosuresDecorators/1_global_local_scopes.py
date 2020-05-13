""""""

'''Global and Local Scopes'''
'''
    --> python will search namespace in local module first
    --> If namespace not found in local module it moves to global module
    --> After that it goes to built-in modules whether on imported modules
    --> Built-In globally available objects
        -> print, None, True False..., -> can be used anywhere
            
                Built-In                ___
                    |                  |   |->Local
                    |                  |
                    |__|->Global-------|
                    
                    
    --> module1.py -> print(True)
        -> search print in current module, if not found goes to built-in
    --> module2.py -> print(a)
        -> search a in current module, if not and also not in built-in, (RuntimeError raises)
    --> Access global scope variables inside the function is allowed
    --> But not to change, if change we use global keyword
    --> Inside the function we call the same function this is called recursion
    --> To change nonlocal variables using nonlocal keyword
'''

a = 5
print(a)


def my_func():
    a = 100
    print(a)


my_func()


def my_func():
    global a
    print(a)
    a = 12


my_func()
print(a)

'''Without nonlocal'''


def outer_func():
    x = 'hello'

    def inner():
        x = 'python'
        print('inner:', x)
    inner()
    print('outer:', x)


outer_func()

'''With nonlocal'''


def outer_func():
    x = 'hello'
    print('outer(before):', x)

    def inner():
        nonlocal x
        x = 'python'
        print('inner:', x)
    inner()
    print('outer(outer):', x)


outer_func()


outer_func()

'''Without global'''
x = 'Hai'


def outer_func():
    global x
    print('global(before):', x)
    x = 'hello'
    print('outer(before):', x)

    def inner():
        global x
        x = 'python'
        print('inner:', x)
    inner()
    print('outer(outer):', x)


outer_func()
print('global(after):', x)

b = 10
print(b)


def outer():
    global b
    a = 100
    x = 'python'
    b = 20
    print(hex(id(a)))
    print(hex(id(b)))
    print(hex(id(x)))
    print(b)

    def inner():
        global b
        nonlocal a  # if not specified as same
        a = 10
        b = 30
        print(hex(id(a)))
        print(hex(id(b)))
        print(hex(id(x)))
        print('{0} rockz!'.format(x))
        print(b)
    return inner()


outer()
print(b)
