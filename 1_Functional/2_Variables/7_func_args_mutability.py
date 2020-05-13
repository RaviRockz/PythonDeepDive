""""""

'''Function Arguments and Mutability'''
'''
    --> Immutable objects are safe from unintended side-affects
    --> Mutable objects are not safe from unintended side-affects
'''


def modify_string(s):
    s = s + ' World'
    return s


my_var = 'hello'
print(my_var)
print(id(my_var))
modify_string(my_var)
print(my_var)
print(id(my_var))


def modify_list(lst):
    lst.append(4)


my_list = [1, 2, 3]
print(my_list)
print(id(my_list))
modify_list(my_list)
print(my_list)
print(id(my_list))


def modify_tuple(tpl):
    tpl[0].append(4)


my_tpl = ([1, 2, 3], 'a')
print(my_tpl)
print(id(my_tpl))
modify_tuple(my_tpl)
print(my_tpl)
print(id(my_tpl))
