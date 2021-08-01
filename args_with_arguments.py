def po(n,*args):
     return [ i**n for i in args ]
     
lis1=[1,2,3,4,5,6,7,8,9]
lis2=po(3,*lis1)
print(lis1)
print(lis2)