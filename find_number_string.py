str=input('enter a string=')
for i in range(len(str)):
    if str[i]>='0' and str[i]<='9':
        print("it contain a number!")
        break
else:
    print("it not contain a number")    