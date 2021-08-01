class computer:
    wheel=4
    def __init__(self,ram,cpu):
        self.ram=ram
        self.cpu=cpu
    def config(self):
        print("config is",self.ram,self.cpu)

com1=computer('5gb','intel i5')
com2=computer('8gb','ryzen 3')
com1.config()
com2.config()
com1.wheel=34
print(computer.wheel)
