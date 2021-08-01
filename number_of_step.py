def step(n):
    if(n==1):
        return 2
    else:
        return 2*step(n-1)    


e=int(input("enter the number of disk=")) 
print(step(e)-1)
