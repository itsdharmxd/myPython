print("using exponential operator")
e=int(input('enter a number='))**int(input('enter its power='))
print (e)
print('using loop')
a,b=input('enter number : power=').split(':')
a=int(a);b=int(b)
while b>1:
    a*=a
    b-=1
print(a)    
print('using recursion')
def powr(a,b) :
     if b==1 :
         return a
     else:
        return a*powr(a,b-1)

print(powr(int(input("enter a number=")),int(input('enter its power='))))     
