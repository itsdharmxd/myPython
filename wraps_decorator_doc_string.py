from functools import wraps
def add_all(func):
    @wraps(func)
    def inner_func(a,b):
        ''' this is inner function '''
        return func(a,b)
    return inner_func
@add_all
def add(a,b):
    '''this is add function '''
    return a+b
print(add.__doc__)