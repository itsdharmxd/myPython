def add(a,b):
    if type(a) is int and type(b) is int :
        return a+b
    else:
        raise TypeError('input not valid')



print(add(2,'3'))       