""""""

'''Default Docs and Values'''
'''
    --> namedtuple.__doc__
    --> namedtuple.field1.__doc__
    --> namedtuple.field2.__doc__
    --> help(namedtuple)
    --> We can also override doc strings
    --> _replace for default values
    --> Using __defaults__
    --> App returning multiple values 
'''

from collections import namedtuple

Vector2D = namedtuple('Vector2D', 'x1 y1 x2 y2 origin_x origin_y')
vector_zero = Vector2D(x1=0, x2=0, y1=0, y2=0, origin_x=0, origin_y=0)
print(vector_zero)
vector_zero = Vector2D(0, 0, 0, 0, 0, 0)
print(vector_zero)

'''Using _replace'''
v1 = vector_zero._replace(x1=10, x2=20, y1=30, y2=30)
print(v1)

'''Using __defaults__'''
Vector2D = namedtuple('Vector2D', 'x1 y1 x2 y2 origin_x origin_y')
Vector2D.__new__.__defaults__ = (0, 0, 0, 0, 0, 0)
v2 = Vector2D()
print(v2)


'''Generating Random Colors'''
from random import randint

RGB = namedtuple('GenerateRGB', 'red green blue')

generate_rgb = lambda: RGB(randint(0, 255), randint(0, 255), randint(0, 255))

rgb1 = generate_rgb()
rgb2 = generate_rgb()
print(rgb1)
print(rgb2)
