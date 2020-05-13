""""""

'''Object Mutability'''
'''
    --> Changing the data inside the object is called modifying
        the internal state(data) of the object
    --> changing data without changing memory address
    --> Mutable
        -> an object whose internal state can be changed
            * Lists
            * Sets
            * Dictionaries
            * User-Defined Classes
    --> Immutable
        -> an object whose internal state can't be changed
            * Numbers (int, float, bool etc)
            * Strings
            * Tuples
            * Frozen Sets
            * Use-Defined Classes
'''

lst = [1, 2, 3]
print(type(lst))
print(id(lst))
lst.append(4)
print(id(lst))

lst = lst + [5]
print(id(lst))

t = ([1, 2], [3, 4])
print(type(t))
print(id(t))
print(id(t[0]))
print(id(t[1]))
t[0].append(5)
t[1].append(6)
print(id(t))
print(id(t[0]))
print(id(t[1]))
