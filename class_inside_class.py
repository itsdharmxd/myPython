class student:
    def __init__(self,name,clas,brand,ram,cpu):
        self.name=name
        self.clas=clas
        self.lap=self.laptop(brand,ram,cpu)
    def show(self):
        print(f"name={self.name}\nclass={self.clas}")    
    class laptop:
        def __init__(self,brand,ram,cpu):
              self.brand=brand
              self.ram=ram    
              self.cpu=cpu
        def show(self):
            print(f'brand={self.brand}\nram={self.ram}\ncpu={self.cpu}')

s1=student('dharmesh','12th','HP','4gb','ryzen3')
print(s1)
s1.show()
lap2=student.laptop('inytex','14gb','inter i5')
lap2.show()
