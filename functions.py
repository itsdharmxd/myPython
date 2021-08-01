def add_sub(c,x):
    return c+x,c-x


x=int(input('enter 1st number ='))
c=int(input('enter 2nd number='))
z,y=add_sub(c,x) 
print("sum=",end='')
print(z)   
print("diffrence =",end='')
print(y)