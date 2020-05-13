""""""

'''Booleans'''
'''
    --> bool class to represent booleans
    --> bool is sub class of int
    --> True and False are singletons
    --> bool as int, but not Same memory (is vs ==)
        -> True = 1 = same, but not memory
        -> False = 0 = same, but not memory
    --> Constructor
        -> bool(x) -> returns True when x is True and False when x is False
    --> Truthy and Falsy
        -> anything is empty it is false
            * [] -> False, [1, 2, 3] -> True
            * 0 -> True, 100 -> False
            * class -> True, False -> __bool()__
    --> operators
        -> and or not
'''

print(issubclass(bool, int))
print(isinstance(True, int))
print(isinstance(1, int))
a = 1
b = 0
print(id(a), id(b))
print(id(True), id(False))
a = True
b = False
print(id(a), id(b))
print(id(True), id(False))

a = []
print(bool(a))
a = [1, 2, 3]
print(bool(a))
print(bool(int))
print(int.__bool__(1))
print(int.__bool__(0))
print(bool(None))

x = [0, 0, 1, 1]
y = [0, 1, 0, 1]
op = ['and', 'or']

print('X Y X and Y X or Y')
for a, b in zip(x, y):
    print('{0} {1}    {2}      {3}     '.format(a, b, eval('a ' + op[0] + ' b'),
                                                eval('a ' + op[1] + ' b')))
