class American():
    def printAmerican(self):
        print("americanPrint")

class people(American):
    def printPeople(self):
        print("ım people")


american = American()


people = people()

people.printAmerican()