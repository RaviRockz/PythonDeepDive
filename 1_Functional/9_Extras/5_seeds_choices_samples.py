""""""

'''Random Seeds'''

import random


def get_rand(arg):
    for _ in range(5):
        print(f'Seed -> {arg} --> RandomNumber: {random.randint(10, 20)}')


get_rand('Not Set')
random.seed(10)
get_rand(10)
random.seed(20)
get_rand(20)
random.seed(10)
get_rand(10)
random.seed(20)
get_rand(20)


'''
    --> Random Choices
        -> k -> random k choices as list
        -> weights -> how much percent number presents
    --> Random Samples
        -> k <= len(sequence)
'''

