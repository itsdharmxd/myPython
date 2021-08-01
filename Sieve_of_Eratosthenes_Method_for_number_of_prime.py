from math import sqrt
n=int(input("enter the number of elements="))
lis=n*[False]
lis[0]=lis[1]=True
count=0
for i in range(2,n):
    if not lis[i]:
        count+=1
        for j in range(2*i,n,i):
          lis.insert(j,True)
print(count)