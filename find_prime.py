n=int(input("enter as number="))

lis=n*[True]
lis[0]=lis[1]=False
for i in range(2,n):
    if lis[i]:
        print(i)
        for j in range(2*i,n,i):
            lis[j]=False
            