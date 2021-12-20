class Student:
    def __init__(self, roll, gpa):
        self.roll = roll
        self.gpa = gpa

    def display(self):
        print("This is %s", self.roll, " And ID is ", self.gpa)


rahim = Student(101, 102)
rahim.display()
