def fun(lis,boo=False):
    return [ i.title() if not boo else i[::-1].title() for i in lis]

lis=['dharmesh','lalit','upadhayay','dubey','sneha']
lis2=fun(lis,True)
print(lis2)
