class Shape():
    def __init__(self):
        pass
    def area(self):
        return 0



class Square(Shape):

    def __init__(self,length = 0):
        Shape.__init__(self)
        self.length = length

    def area(self):
        return self.length * self.length


sqr = Square(5)

print(sqr.area())
print(Square.area())