s={i**2 for i in range(1,10) }# with for
print(s)
s={i**2 for i in range(1,10) if i%2==0 }# with if
print(s)
s={i**2 if i%2==0 else i for i in range(1,10) }# with if else
print(s)