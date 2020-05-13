""""""

'''Variable Equality'''
'''
    --> Variable equality in two different ways
        -> is (and) is not (or) not
            * to compare memory addresses
        -> == (and) !=
            * to compare object state(data)
    --> None Object
        -> empty value or null pointer
        -> python use all None values as same shared memory address
'''

a = 10
b = a
print(a, b)
print('a is b', a is b)
print('a == b', a == b)

a = 'hello'
b = 'hello'
print(a, b)
print('a is b', a is b)
print('a == b', a == b)

a = [1, 2, 3]
b = [1, 2, 3]
print(a, b)
print('a is b', a is b)
print('a is not b', a is not b)
print('a == b', a == b)

a = 10
b = 10.0
print(a, b)
print('a is b', a is b)
print('a is not b', a is not b)
print('a == b', a == b)

a = None
b = None
c = None
print('a is b', a is b)
print('a is b', a is c)
print('a is b', b is c)
