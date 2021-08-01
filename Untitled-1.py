try :
         age=int(input("enter age="))
         
except ValueError:
       print('invalid input')
except:
        print('unidentyfie error')    
if age>18:
    print("granted")
else:
    print('not granted')    
    