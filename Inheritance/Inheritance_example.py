class Phone:
    def call(self):
        print("You can call")

    def message(self):
        print("You can message")

class Samsung(Phone):  #ingeritance
    def photo(self):
        print("You can photo")

s = Samsung()
s.message()