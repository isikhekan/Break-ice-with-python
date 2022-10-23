print(type("9"+"9"))
x = int(input("Enter integer"))

def sum_integer(integer):
    toplam = integer + integer*11 + integer*111 + integer*1111
    print(toplam)
sum_integer(x)