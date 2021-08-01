from time import *
def calculate_time(func):
    def inner_f(a,b):
        print('ytrehjhgfdfghjkjhgfdh')
        print('ejghgryruktjhfgdrgjkfh')
        print('ghgmrhjfghyjrhgjyrmhg')
        return func(a,b)
    return inner_f
@calculate_time# add=calculate_time(add)
def add(a,b):
    return a+b     
a=time()    
print(add(2,6))
b=time()
print('time=',b-a)
