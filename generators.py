def printer(n):
    for i in range(1,n+1):
        yield (i)
print(type(printer(4)))        
for i in printer(34):
    print(i)        