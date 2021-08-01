from functools import wraps
def print_all_data(func):
    @wraps(func)
    def inner_func(a,b):
        return func(a,b)
    return inner_func    
@print_all_data
def add(a,b):
    '''
this is add function 
this function add two arguments   
    '''
    return a+b
@print_all_data   
def substract(a,b):
    ''' this is substract function 
        this function substract two arguments
    '''
    return a-b   
a=5;h=6
print(f'{add.__doc__}\n{add(a,h)}')     