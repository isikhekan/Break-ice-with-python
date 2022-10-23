class has2method:
    def __init__(self, input):
        self.input = input
    def getString(self):
        print(self.input)
    def printString(self):
        print(self.input.upper())


x = input("Bir string giriniz.")

myclass = has2method(x)
myclass.getString()
myclass.printString()