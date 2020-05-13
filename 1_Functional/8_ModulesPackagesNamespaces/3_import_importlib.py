import sys
print(sys)
import collections
print(collections)
try:
    import mod_name
except Exception as e:
    print(e)

mod_name = 'math'
import importlib
importlib.import_module(mod_name)
print('math' in sys.modules)

try:
    print(math.sqrt(2))
except Exception as e:
    print(e)

math = importlib.import_module(mod_name)
print(math.sqrt(2))

print(id(math))
print(id(sys.modules['math']))
import builtins
print(builtins)
