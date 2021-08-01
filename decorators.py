def decorators(func,func3):
   
    print('this is best function')
        
        
@decorators
def func1():
    print("its function 1")
@decorators    
def func2():
    print("its function 2")

func1()
