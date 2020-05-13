""""""

'''Tuples'''
'''
    --> Read-only list
    --> Tuples also as data records or structures
        -> position of value has a meaning
    --> Tuples                              Lists                               Strings
        containers                          containers                          containers
        order matters                       order matters                       order matters
        Hetero/Homo                         Hetero/Homo                         Homo
        indexable                           indexable                           indexable
        iterable                            iterable                            iterable
        immutable                           mutable                             immutable
        fixed length                        length can change                   fixed length
        fixed order                         order of elements can change        fixed order
                                                sort
                                                reversals
    --> Immutability of Tuples
        -> elements can't be added or remove
        -> order can't be changed
        -> well for repr data structures
            * Point(10, 20)      --> x-coordinate, y-coordinate 
            * Circle(0, 0, 10)   --> x-coordinate, y-coordinate , radius
        -> Data Records
            * london = ('London', 'UK', 8_780_000)
            * beijing = ('Beijing', 'China', 21_000_000)
    --> Extracting data from tuples
        -> indexing, slicing, *
        -> Dummy variables to ignore data
'''

x = (10, 20)
print(x)
print(x[0])

x = ('London', 'UK', 8780000)
city, _, population = x
print(city, population)
*city, population = x
print(city, population)
