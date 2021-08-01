b=input('enter the binary value=')
num=0
po=0

for i in range(len(b)-1,-1,-1):
      if int(b[i])==1:
             num=num+2**po
      po+=1
print(num)          

