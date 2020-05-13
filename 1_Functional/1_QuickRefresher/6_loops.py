""""""

'''For loop'''
print('Using For Loop')
for i in range(1, 6):
    print('Square Of %d is %d' % (i, i ** 2))

for i in [(1, 2), (3, 4)]:
    print('x:', i[0])
    print('y:', i[1])


'''While loop'''
print('Using While Loop')
i = 1
while i < 6:
    print('Square Of %d is %d' % (i, i ** 2))
    i += 1

'''Break'''
i = 1
while i < 6:
    if i > 2:
        break
    print('Square Of %d is %d' % (i, i ** 2))
    i += 1

'''Continue'''
i = 0
print('Printing Even Numbers From 1 to 5')
while i < 6:
    i += 1
    if not i % 2 == 0:
        continue
    print(i)
