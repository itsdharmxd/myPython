from numpy import *

arr=array('i',[])
n=int(input('enter the number of element to input '))
for i in range(0,n):
    arr.append(int(input('enter the valve')))

print(arr[0])
g=int(input('enter valve to find'))
print(arr.index(g))