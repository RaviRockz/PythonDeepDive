""""""

'''Python Optimization Interning'''
'''
    --> sys.intern for string is much faster for string comparison
    --> Equality comparison using is operator is much faster than == operator.
    --> Python numeric calculations at compile time even without invokes
        -> Constant expressions can be pre-calculated
    --> In string sequences < 20 are pre-calculated
    --> In Membership tests mutables are replaced by immutables
        -> set membership is much faster than list or tuple 
'''


def my_func():
    a = 24 * 60
    b = (1, 2) * 5
    c = 'abc' * 3
    d = 'ab' * 11
    e = 'the quick brown fox' * 5
    f = ['a', 'b'] * 3


print(my_func.__code__.co_consts)


def my_func1(n):
    if n in [1, 2, 3]:
        pass


print(my_func1.__code__.co_consts)


def my_func2(n):
    if n in {1, 2, 3}:
        pass


print(my_func2.__code__.co_consts)

import string
import time

ascii_chars = string.ascii_letters
char_list = list(ascii_chars)
char_tuple = tuple(ascii_chars)
char_set = set(ascii_chars)
print(char_list)
print(char_tuple)
print(char_set)


def membership_test(n, sequence):
    start_time = time.perf_counter()
    for i in range(n):
        if 'z' in sequence:
            pass
    end_time = time.perf_counter()
    return end_time - start_time


print('List Membership Test:', membership_test(10000000, char_list))
print('Tuple Membership Test:', membership_test(10000000, char_tuple))
print('Set Membership Test:', membership_test(10000000, char_set))
