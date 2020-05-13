def uppercase(func):
    def wrap():
        f = func()
        return f.upper()

    return wrap


def split_string(func):
    def wrap():
        f = func()
        return f.split()

    return wrap


@split_string
@uppercase
def hello():
    return 'hello world'


print(hello())
