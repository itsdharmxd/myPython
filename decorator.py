def div(a,b):
    print(a/b)

def new_div(func2):
     def inner2(a,b):
         if a>b:
             a,b=b,a
         return func2(a,b)
     return inner2

div2=new_div(div)

div2(2,4)