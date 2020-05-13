""""""

'''If'''
a = 5
b = 6
if a < b:
    print('a less than b')

'''If-Else'''
a = 5
b = 4
if a < b:
    print('a less than b')
else:
    print('a not less than b')

'''If-Elif-Else'''
a = 5
b = 5
if a < b:
    print('a less than b')
elif a > b:
    print('a greater than b')
elif a == b:
    print('a equals b')

y = 'a less than b' if a < b else 'a is not less then b'
print(y)
