""""""

'''Shared References and Mutability'''
'''
    --> Shared References
        -> two variables referencing the same object(memory address)
                                       ____
                a = 10  ----------->  |    | 0X1000
                                      | 10 |
                b = a   ----------->  |____|
    --> So python mem man automatically re-uses the memory references. --> Safe
    --> The py mem man will never create shared ref for mutable objects
'''

a = 10
b = a
print(a, b)
print(id(a), id(b))
a = 15
print(a, b)
print(id(a), id(b))

lst = [1, 2, 3]
lst1 = lst
print(lst, lst1)
print(id(lst), id(lst1))
lst.append(4)
print(lst, lst1)
print(id(lst), id(lst1))

a = 500
b = 500
