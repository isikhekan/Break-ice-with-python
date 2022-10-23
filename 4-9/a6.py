from math import sqrt
C  = 50
H = 30
def calc(D):
    print( round(sqrt((2*C*D)/H)))

x = input("Sayilari giriniz.").split(",")

for i in x:
    calc(int(i))