number=int(input('enter the number of line='))
for i in range(number):
    for j in range(number):
        if i<j:
            continue
        else:
            print('*',end='')
    print('')        
