l = []
while(True):
    x = input("Please enter  name, age, score").split(",")
    if not x[0]:
        break
    else:
        l.append(x)
print(l)
x =sorted(l)
print(x)

