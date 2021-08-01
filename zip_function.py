
lis1=[1,2,3,4,5]
lis2=[3,4,5,6,7]
lis3=[9,8,7,6,5]
#*args=lis1,lis2,lis3
re=lambda *args : [ sum(i)//len(i)  for i in zip(*args) ] 
li=re(lis1,lis2,lis3)
print(li)
