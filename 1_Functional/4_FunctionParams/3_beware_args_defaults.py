""""""

'''Parameter Defaults Beware'''
from datetime import datetime
import time


def log_this_msg(msg, dt=datetime.utcnow()):
    print('{0}: {1}'.format(dt, msg))


log_this_msg('Message1')
time.sleep(5)
log_this_msg('Message2')


def log_this_msg(msg, dt=None):
    dt = dt or datetime.utcnow()
    print('{0}: {1}'.format(dt, msg))


log_this_msg('Message1')
time.sleep(1)
log_this_msg('Message2')


def store_groceries(name, quantity, unit, grocery_list=[]):
    grocery_list.append('{0} -> {1} {2}'.format(name, quantity, unit))
    return grocery_list


store1 = store_groceries('milk', 2, 'liters')
print(store1)
store2 = store_groceries('soap', 4, 'item')
print(store2)


def store_groceries(name, quantity, unit, grocery_list=None):
    if not grocery_list:
        grocery_list = []
    grocery_list.append('{0} -> {1} {2}'.format(name, quantity, unit))
    return grocery_list


store1 = store_groceries('milk', 2, 'liters')
print(store1)
store2 = store_groceries('soap', 4, 'item')
print(store2)
