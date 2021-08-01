lis=[]
n=int(input('enter number of elements='))
for i in range(0,n):
     #lis[i]=int(input("enter a number="))
      lis.insert(i,int(input('entr number=')))

def ispalindrome(i):
    for a in range(2,i):
        if not i%a:
            return False
    return True        

for i in lis:
    if(ispalindrome(i)):
        print(i)
        
