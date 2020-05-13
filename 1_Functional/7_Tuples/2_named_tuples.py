""""""

'''Named Tuples'''
'''
    --> Position of object gave meaning
            pt = (10, 20) --> x, y
            x = pt[0]
            y = pt[1]
    --> Using class instead -> mutable
            class Point2D:
                def __init__(self, x, y):
                    self.x = x, self.y = y
            
            pt = Point2D(10, 20)
            x = pt.x
            y = pt.y
    --> Immutable and positions mean
    --> namedtuple is a class factory -> generating a class
        -> Point2D = namedtuple('Point2D', ['x', 'y'])
        -> Point2D = namedtuple('Point2D', 'x', 'y')
        -> Point2D = namedtuple('Point2D', 'x y')
            pt = Point2D(10, 20)
            x = pt.x
            y = pt.y
            pt.x = 20 # will not work because immutable
    --> Valid field_name
        -> age, name -> valid
        -> _sex -> not valid
        -> if rename=True:
        ->     _sex = _2(index)
    --> Introspection
        -> _fields
            return all field_names as tuple
        -> _source
            return all code section
        -> _asdict()
            return all field_names and values as OrderedDict
'''
from collections import namedtuple

Point2D = namedtuple('Point2D', ['x', 'y'])
pt = Point2D(10, 20)
print(pt)
print(pt.x)
print(pt.y)

Point2D = namedtuple('Point2D', 'x y _x', rename=True)
pt1 = Point2D(10, 20, 30)
print(pt1)
print(pt1.x)
print(pt1.y)
print(pt1._2)
print(pt1._fields)
print(pt1._source)
d = pt1._asdict()
print(d['x'])
