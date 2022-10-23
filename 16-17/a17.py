

total = 0
while True:
    x = input("Process (W/D) and amount if you want exit type 1").split(",")
    print(x)
    if  x[0] == "1":
        break
    else:
        if x[0] == "d":
            total = total + int(x[1])
            print("+")
            print(total)
        if x[0] == "w" :
            total = total - int(x[1])
            print("-")
            print(total)

print(total)