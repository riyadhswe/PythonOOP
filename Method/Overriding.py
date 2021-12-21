class Phone:
    def __init__(self):
        print("I am in Phone Class")

class Samsung(Phone):
    def __init__(self):
        super().__init__()
        print("I am in Samsung class")

s = Samsung()