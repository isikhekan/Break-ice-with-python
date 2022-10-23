class carNames():
    def __init__(self,carName = "Car"):
        self.name = carName


x  = carNames()
y  = carNames("Toyota")
print(x.name)
print(y.name)