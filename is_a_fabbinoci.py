e=int(input("enter a number="))
a=0;b=1;sum=0
while a <= e:
    if a is e:
        print(f"IS a fibbonaci number={e}")
        break
    sum=a+b
    a=b
    b=sum     
else:
  print("NO fibbonaci present")        