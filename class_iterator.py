class data:
    def __init__(self,m1):
        self.m1=m1
    def __iter__(self):
        return self 
    def __next__(self):
      if(self.m1<10):
        var=self.m1
        self.m1+=1
        return var
      else:
          raise StopIteration  
d=data(3)
for i in d:
    print(i)               