class Circle():
    def __init__(self,radius):
        self.radius = radius

    def calculate(self):
        area = self.radius**2 * 3.14
        print(area)



circle = Circle(5)

circle.calculate()