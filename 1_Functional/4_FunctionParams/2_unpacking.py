""""""

'''Unpacking'''
'''
    --> a, b = 2, 3
    --> a = [1, 2, 3]
    --> a, b, c = [1, 2, 3]
    --> Using * and ** (key value pairs)
    --> list and tuple ordered
    --> sets and dict unordered
    --> nested unpacking
'''

a, b = 2, 3
print(a, b)
a = [1, 2, 3]
print(a)
a, b, c = [1, 2, 3]
print(a, b, c)

lst = [1, 2, 3, 4, 5, 6]
a, b = lst[0], lst[1:]
print(a, b)
a, *b = lst
print(a, b)
a, *b = 'ABCDEF'
print(a, b)
a, b, *c = 'ABCDEF'
print(a, b, c)
a, b, *c, d = 'ABCDEF'
print(a, b, c, d)

lst1 = [1, 2, 3]
lst2 = [4, 5, 6]
l_ = [*lst1, *lst2]
print(l_)
lst1 = [1, 2, 3]
lst2 = 'XYZ'
l_ = [*lst1, *lst2]
print(l_)


d1 = {'a': 1, 'b': 2}
c = {'a': 10, 'c': 3, **d1}
print(c)
c = {**d1, 'a': 10, 'c': 3}
print(c)
c = {'a': 10, **d1, 'c': 3}
print(c)

lst = [1, 2, [1, 2]]
a, b, c = lst
print(a, b, c)
a, b, (c, d) = lst
print(a, b, c, d)

a, *b, (c, *d) = [1, 2, 3, 'python']
print(a, b, c, d)
