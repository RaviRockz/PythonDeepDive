""""""

'''Garbage Collection'''
'''
    Handle Circular References                    _________________
                             _________           |                 |
                            |Object A |          |            _____|___         
    my_var      -------->   |var_1____|__________|           |Object B |       
                            |__|______|                      |var_2    |
                               |                             |___|_____| 
                               |_________________________________|
                                                                 
                            
'''

import ctypes
import gc


def ref_count(address: int):
    return ctypes.c_long.from_address(address).value


def object_by_id(obj_id):
    for obj in gc.get_objects():
        if id(obj) == obj_id:
            return 'Object Exists'
    return "Object Doesn't Exists"


'''Circular References'''


class A:
    def __init__(self):
        self.b = B(self)
        print('A: self: {0}, b: {1}'.format(hex(id(self)), hex(id(self.b))))


class B:
    def __init__(self, a):
        self.a = a
        print('B: self: {0}, a: {1}'.format(hex(id(self)), hex(id(self.a))))


gc.disable()

my_var = A()
print(hex(id(my_var)))
print(hex(id(my_var.b)))
print(hex(id(my_var.b.a)))

a_id = id(my_var)
b_id = id(my_var.b)
print(hex(a_id))
print(hex(b_id))
print(ref_count(a_id))
print(ref_count(b_id))
print(object_by_id(a_id))
print(object_by_id(b_id))

my_var = None
print(ref_count(a_id))
print(ref_count(b_id))

print(object_by_id(a_id))
print(object_by_id(b_id))

gc.collect()

print(object_by_id(a_id))
print(object_by_id(b_id))

print(ref_count(a_id))
print(ref_count(b_id))
