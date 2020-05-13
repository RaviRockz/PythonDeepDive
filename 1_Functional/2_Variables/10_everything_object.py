""""""

'''Everything Is An Object'''
'''
    --> Many Data Types
        -> Integers(int)       -> Operators(+, -, *, ...)  
        -> Booleans(bool)      -> Functions
        -> Floats(float)       -> Classes
        -> Strings(str)        -> Types
        -> Lists(list)         
        -> Tuples(tuple)           
        -> Sets(set)           
        -> Dictionaries(dict)          
        -> None(NoneType)  
        
    --> Common is, they are all objects(instances of classes)
    --> Every Object has memory address        
'''


def square(n):
    return n ** 2


def cube(n):
    return n ** 3


f = square
print(id(f), id(square))
print('f is square', f is square)
print(f(2))


def do_it(opt, n):
    if opt == 1:
        return square(n)
    elif opt == 2:
        return cube(n)


print(do_it(1, 2))
print(do_it(2, 2))
