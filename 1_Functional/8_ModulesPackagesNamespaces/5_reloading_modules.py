import os


def create_module_file(module_name, **kwargs):
    """Create a module file named <module_name>.py
    Module has a single function (print_values) this will print the kwargs
    :param module_name:
    :param kwargs:
    :return:
    """
    module_file_name = f'{module_name}.py'
    module_rel_path = module_file_name
    module_abs_path = os.path.abspath(module_rel_path)

    with open(module_abs_path, 'w') as f:
        f.write(f'# {module_name}.py\n\n')
        f.write(f"print('Running {module_file_name}...')\n\n\n")
        f.write(f'def print_values():\n')
        for key, value in kwargs.items():
            f.write(f"\tprint('{str(key)}', {str(value)})\n")


create_module_file('test_module', k1=10, k2=20, k3=30)
import test_module
test_module.print_values()

import sys
print('test_module' in sys.modules)
print(id(test_module))
print(id(sys.modules['test_module']))
del sys.modules['test_module']

import test_module
print('test_module' in sys.modules)
print(id(test_module))
print(id(sys.modules['test_module']))

import importlib
importlib.reload(test_module)
print(id(test_module))
print(id(sys.modules['test_module']))
