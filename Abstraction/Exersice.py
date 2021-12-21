"""
01) Hierarchical Inheritance
"""
from abc import ABC,abstractmethod
class Shape(ABC):
    def __init__(self, d1, d2):
        self.d1 = d1
        self.d2 = d2
    @abstractmethod
    def area(self):
        pass

class Triangle(Shape):
    # Override
    def area(self):
        area = 0.5 * self.d1 * self.d2
        print("Area of triangle : ", area)

class Rectangle(Shape):
    # Override
    def area(self):
        area = self.d1 * self.d2
        print("Area of Rectangle : ", area)
S1 = Shape(10,20)
S1.area()
T1 = Triangle(10,20)
T1.area()
R1 = Rectangle(10,20)
R1.area()