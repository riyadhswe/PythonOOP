class Student:
    name = " "
    roll = " "


    def SetValue(self,name,roll):
        self.name = name
        self.roll = roll


    def Display(self):
        print("This is ",self.name," And ID is ",self.roll)


rahim = Student()
rahim.SetValue("Rahim",101)
rahim.Display()

Karim = Student()
Karim.SetValue("Karim",102)
Karim.Display()
