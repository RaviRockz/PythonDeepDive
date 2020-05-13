""""""

'''Preserved order of **kwargs and namedtuple'''


def func(**kwargs):
    for item in kwargs.items():
        print(item)


func(b=20, a=10, c=30)


from collections import namedtuple


def n_tuple(class_name, **fields):
    Struct = namedtuple('Struct', fields.keys())
    Struct.__new__.__defaults__ = tuple(fields.values())
    return Struct


Vector2D = n_tuple('Vector2D', x1=None, y1=None, x2=None, y2=None, origin_x=0, origin_y=0)
print(Vector2D._fields)
v1 = Vector2D(10, 10, 20, 20)
print(v1)
