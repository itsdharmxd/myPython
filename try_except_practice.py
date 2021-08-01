def div(a,b):
    return a//b

try:
    
    div(int(input('enter  number=')),int(input('enter number=')))
except ZeroDivisionError :
    print('cannot divide by zero')
except ValueError:
    print('invalid input')
except :
    print('unexpected error')        
