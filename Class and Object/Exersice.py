class Triangle:
    def __init__(self,base,height):
        self.base = base
        self.height = height

    def calculate(self):
        print(0.5*(self.base*self.height))


t1 = Triangle(10,10)
t2 = Triangle(20,20)
t1.calculate()
t2.calculate()