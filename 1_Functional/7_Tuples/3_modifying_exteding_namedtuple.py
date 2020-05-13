""""""

'''Modifying Extending namedtuple'''
'''
    --> namedtuple are Immutables
        -> so we create new tuple with modified values
    --> changing field values
    --> adding new fields
    --> Using _make
        -> create new named tuple with list
    --> Using _replace
        -> replacing values from keyword args
'''

from collections import namedtuple

Stock = namedtuple('Stock', 'symbol year month day open high low close')
djia = Stock('DJIA', 2018, 1, 25, 26313, 26458, 26260, 26393)
print(djia)

'''changing value'''
current = djia[:7]
djia = Stock(*current, 26394)
print(djia)
*current, _ = djia
djia = Stock(*current, 26395)
print(djia)
new_values = current + [26396]
djia = Stock._make(new_values)
print(djia)
djia = djia._replace(day=26, high=26459, close=26397)
print(djia)


'''Extending Fields'''
new_fields = Stock._fields + ('previous_close', )
StockExt = namedtuple('StockExt', new_fields)

'''Extending Values'''
djia_ext = StockExt(*djia, 26000)
print(djia_ext)
djia_ext = StockExt._make(djia + (26010, ))
print(djia_ext)
