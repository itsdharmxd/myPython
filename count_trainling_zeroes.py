e=int(input("enter a number="))
count=1
for i in range(1,e+1):
    count*=i
print(f"factorial of {e} is {count} having ",end='')
c=-1
d=0
while not d:
    d=count%10
    count=count//10 
    c+=1
    
print(c,' zeroes')       