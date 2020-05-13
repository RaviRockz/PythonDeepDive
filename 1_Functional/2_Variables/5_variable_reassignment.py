""""""

'''Variable Re-Assignment'''
'''
    --> Python dynamically changing memory address based on the object.
            my_var = 10  ----------->   int[10] ----> 0x1000
            my_var = 15  ----------->   int[15] ----> 0x1034  
'''

my_var = 10
print(my_var)
print(type(my_var))
print(hex(id(my_var)))
print(hex(id(10)))
print(hex(id(15)))

my_var = 15
print(my_var)
print(type(my_var))
print(hex(id(my_var)))
print(hex(id(10)))
print(hex(id(15)))

my_var = my_var + 20
print(my_var)
print(type(my_var))
print(hex(id(my_var)))

a = 100
b = 100
print(a)
print(type(a))
print(hex(id(a)))
print(b)
print(type(b))
print(hex(id(b)))
