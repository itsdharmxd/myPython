

lis1=[1,6,7,8,9]
lis2=[5,6,7,8,9]
#lis=list(map(lambda a: a for j in lis2 if ,iter1=lis1))
lis=list(set(lis1)-set(lis2))
print(lis)