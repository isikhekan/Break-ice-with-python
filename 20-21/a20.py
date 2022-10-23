l = []
class division():
    def  divisible_seven(self,n):
        for i in range(0,n+1):
            if i % 7 == 0:
                l.append(i)

myCLass = division()
myCLass.divisible_seven(70)
print(l)

