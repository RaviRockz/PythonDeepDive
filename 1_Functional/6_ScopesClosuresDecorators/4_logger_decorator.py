def log(fn):
    from functools import wraps
    from datetime import datetime, timezone

    @wraps(fn)
    def inner(*args, **kwargs):
        run_dt = datetime.utcnow()
        result = fn(*args, **kwargs)
        print(f'{run_dt} : invoked {fn.__name__}')
        return result
    return inner


@log
def func_1():
    pass


@log
def func_2():
    pass


func_1()
func_2()
