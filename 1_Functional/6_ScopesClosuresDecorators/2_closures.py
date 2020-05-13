""""""

'''Closures'''
'''
    --> Free Variables and Closures
        -> func defined inside another func can access the outer(nonlocal) variables
        -> nonlocal variables is also called free variables
        -> outer runs then inner is created -> closures
        -> returns inner, are actually returning closure and assign to a variable
    --> Python cells and Multi-Scoped variables
    
        def outer():                -> value of x is shared b/w two scopes
            x = 'python                 -> outer
            def inner():                -> closure(inner)
                print(x)            -> two different scopes refer same value
            return inner            
    --> python done this by creating a cell as intermediary object
            
        outer.x            
           |---------> cell -> 0xA500 -> oxFF100 || oxFF100 -> python (indirect reference)
        inner.x            

        -> both outer.x and inner.x has pointing to a same cell
            
    --> Extended scope
        -> every time closure is called the free variable is referenced
        -> by calling closure inner nonlocal variable is scoped out(extended scope)
    --> Introspection
        -> inner.__code__.co_freevars -> ('x',) free variables
        -> inner.__closure__ -> (<cell> at 0xA500: str object at 0xFF100)
        -> memory address is value referenced
    --> Modifying the free variables using --> nonlocal
    --> every time run a func, a new scope is created
    --> func generates a closure, a new closure is created every time as well 
    --> Shared Extended Scopes
        -> if multiple closures found, free variables are scoped,
           when any closure is generated same variable is bounded
    --> nested closures         
'''


def outer():
    x = 'python'

    def inner():
        print(x)

    return inner


fn = outer()
fn()
print(fn.__code__.co_freevars)
print(fn.__closure__)


def outer():
    x = [1, 2, 3]
    print(hex(id(x)))

    def inner():
        # y = [1, 2, 3]
        y = x
        print(hex(id(y)))

    return inner


fn = outer()
fn()
print(fn.__code__.co_freevars)
print(fn.__closure__)


def outer():
    count = 0

    def inc():
        nonlocal count
        count += 1
        return count
    return inc


fn = outer()
print(fn.__code__.co_freevars)
print(fn.__closure__)
print(fn())
print(hex(id(0)))
print(fn.__code__.co_freevars)
print(fn.__closure__)
print(hex(id(1)))
print(fn())


def outer():
    count = 0

    def inc1():
        nonlocal count
        count += 1
        return count

    def inc2():
        nonlocal count
        count += 1
        return count
    return inc1, inc2


fn1, fn2 = outer()
print(fn1.__code__.co_freevars, fn2.__code__.co_freevars)
print(fn1.__closure__, fn2.__closure__)
print(0, hex(id(0)), fn1(), hex(id(1)), fn2(), hex(id(2)))
print(fn1.__code__.co_freevars, fn2.__code__.co_freevars)
print(fn1.__closure__, fn2.__closure__)


def pow(n):
    def inner(x):
        return x ** n
    return inner


square = pow(2)
print(square.__code__.co_freevars)
print(square.__closure__)
print(hex(id(2)))
print(square(5))
print(square.__code__.co_freevars)
print(square.__closure__)

cube = pow(3)
print(cube(3))


def adder(n):
    def inner(x):
        return x + n
    return inner


add_1 = adder(1)
add_2 = adder(2)
add_3 = adder(3)

print(add_1.__code__.co_freevars, add_2.__code__.co_freevars, add_3.__code__.co_freevars)
print(add_1.__closure__, add_2.__closure__, add_3.__closure__)
print(add_1(10))
print(add_2(10))
print(add_3(10))
