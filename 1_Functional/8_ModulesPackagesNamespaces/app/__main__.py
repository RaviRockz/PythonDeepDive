# __main__.py
import timing

print(f'Loading run.py: __name__ = {__name__}')

code = '[x**2 for x in range(1_000)]'

result = timing.timeit(code, 1000)
print(result)
