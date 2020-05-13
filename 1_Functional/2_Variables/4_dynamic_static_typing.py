""""""

'''Dynamic Vs Static Typing'''
'''
    --> Static typing (C, C++, Java..,)
        -> defined with data type
            * String my_var = 'hello';
            * my_var = 10;  # type not matching error
            * does not change memory address
    --> Dynamic typing (Python)
        -> dynamically changing data based on user input
            * my_var = 'hello'
            * my_var = 20
            * dynamically changing memory address
'''

my_var = 'Hello'
print(my_var)
print(id(my_var))

my_var = 20
print(my_var)
print(id(my_var))
