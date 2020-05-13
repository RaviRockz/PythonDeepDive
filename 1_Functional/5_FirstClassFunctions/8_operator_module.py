""""""

'''Operator Module'''
'''
    --> Operator module contains 
        -> Arithmetic
        -> Comparison and Boolean
        -> Sequence and Mapping
        -> Item Getters -> itemgetter
        -> Attribute getters -> attrgetter
'''

import operator as opr

print(opr.add(20, 4))
print(opr.sub(20, 4))
print(opr.mul(20, 4))
print(opr.truediv(20, 4))
print(opr.floordiv(20, 4))
print(opr.mod(20, 4))

print(opr.lt(20, 4))
print(opr.gt(20, 4))
print(opr.le(20, 4))
print(opr.ge(20, 4))
print(opr.eq(20, 4))
print(opr.ne(20, 4))

print(opr.truth(None))
print(opr.truth(1))

lst = [1, 2, 3, 4, 5]
print(opr.getitem(lst, 4))
opr.setitem(lst, 4, 6)
print(lst)
opr.delitem(lst, 3)
print(lst)

f = opr.itemgetter(1, 2, 3)
print(f(lst))


class MyClass:
    def __init__(self):
        self.a = 10
        self.b = 20
        self.c = 30

    def test(self):
        print('a: {0}, b: {1}, c: {2}'.format(self.a, self.b, self.c))


obj = MyClass()
f = opr.attrgetter('a')
print(f(obj))
test_ = opr.attrgetter('test')(obj)
test_()


