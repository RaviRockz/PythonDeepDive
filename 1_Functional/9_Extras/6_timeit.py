""""""

'''Timing Using timeit'''

from timeit import timeit

import math
print(math.sqrt(2))


from math import sqrt
print(sqrt(2))

print(timeit(stmt='math.sqrt(2)', setup='import math'))
print(timeit(stmt='sqrt(2)', setup='from math import sqrt'))
print(timeit(stmt='math.sqrt(2)', globals=globals()))
