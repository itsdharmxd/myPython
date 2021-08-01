a,b,c=input("enter three number=").split(':')
a=int(a);b=int(b);c=int(c)
if a>b and a>c:
    print(a," is gretest")
elif b>a and b>c:
    print (b," is greatest")
else:
    print (c," is greatest")         