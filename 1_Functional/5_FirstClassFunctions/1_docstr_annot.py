""""""

'''Docstring and Annotations'''
'''
    --> first line of the function body
    --> using annotations is additional way to document our functions
'''


def add(a, b):
    """Addition of (a and b) and return a + b"""
    return a + b


help(add)
print(add.__doc__)


def add(a: int, b: int) -> int:
    """Addition of (a and b) and return a + b"""
    return a + b


help(add)
print(add.__doc__)
print(add.__annotations__)
