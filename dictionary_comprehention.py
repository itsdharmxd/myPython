dic={ i:i**2 for i in range(1,11)}
print(dic)
dic={ i:i**2 for i in range(1,11) if i%2==0 }
print(dic)
dic={ i:( i**2 if i%2==0 else i) for i in range(1,11)}
print(dic)