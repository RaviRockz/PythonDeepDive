import sys

sys.path.append('app/app.zip')

from app import timing

code = '[x**2 for x in range(1_000)]'

result = timing.timeit(code, 100000)
print(result)
