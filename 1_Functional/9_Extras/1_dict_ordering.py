""""""

'''Dict Ordering'''


d = {'b': 20, 'a': 10, 'c': 30}
print(d)
print(d.items())

del d['b']
print(d)
print(d.items())

d['b'] = 25
print(d)
print(d.items())

print(d.popitem())
print(d)
