""""""

'''Memory Reference'''
'''
    --> Python Memory Manager
        -> my_var_1 = 10
                              reference        ______                         reference  |  count
                    my_var_1  --------->      |      | 0x1000                 -----------|-------
                                0x1000        |      |                          0x1000   |    2
                                              |  10  |                                   |
                              reference       |      |                                   |
                    my_var_2  --------->      |______|
                                0x1000                          
        -> my_var_2 = my_var_1
                    
'''

import sys
import ctypes

my_var_1 = [1, 2, 3]
print(id(my_var_1))  # memory address
print(sys.getrefcount(my_var_1))  # reference count

my_var_2 = my_var_1
print(id(my_var_2))  # memory address
print(sys.getrefcount(my_var_1))  # reference count


def ref_count(address: int):
    return ctypes.c_long.from_address(address).value


print(ref_count(id(my_var_1)))
my_var_2 = None
print(ref_count(id(my_var_1)))
