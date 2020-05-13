""""""

'''Formatted string literals'''

print('{} % {} = {}'.format(10, 3, 10 % 3))
print('{0} % {1} = {2}'.format(10, 3, 10 % 3))
print('{2} % {1} = {0}'.format(10 % 3, 3, 10))
print('{a} % {b} = {mod}'.format(a=10, mod=10 % 3, b=3))
a = 10
b = 3
c = 10 % 3
print(f'{a} % {b} = {c}')

square = lambda x: x**2

for i in range(1, 6):
    print(f'Square Of {i} is {square(i)}')
