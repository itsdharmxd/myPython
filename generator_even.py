def ge(n):
    for i in range(1,n+1):
        if i%2==0:
            yield i
for i in ge(10):
    print('run')
    print(i)            