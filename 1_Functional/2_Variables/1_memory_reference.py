""""""

'''In Python Everything Is An Object'''
'''
    --> Every object stores in memory like this
         ___________            reference for the memory address 0x1000
        |10_________| 0x1000    <--------------------------------------- (my_var_1 == 10)
        |___________| 0x1001
        |___________| 0x1002
        |___________| 0x1003
        |___________| 0x1004    reference for the memory address 0x1005
        |hello______| 0x1005    <--------------------------------------- (my_var_2 == 'hello')
        |___________| 0x1006
        |___________| 0x1007
        |___________| 0x1008
        
    --> my_var_1 references the object at 0x1000
    --> my_var_2 references the object at 0x1005
'''

'''id() to get the memory address of an object'''

my_var_1 = 10
print(my_var_1)
print(id(my_var_1))
print(hex(id(my_var_1)))

my_var_2 = 'hello'
print(my_var_2)
print(id(my_var_2))
print(hex(id(my_var_2)))
