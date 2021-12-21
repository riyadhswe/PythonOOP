class Shape:
    def __init__(self, d1, d2):
        self.d1 = d1
        self.d2 = d2

    def area(self):
        print("I am area method of shape class ")


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

"""
01) Hierarchical Inheritance
"""


T1 = Triangle(10,20)
T1.area()
R1 = Rectangle(10,20)
R1.area()
