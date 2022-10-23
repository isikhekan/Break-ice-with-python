x  = input("enter number").split(",")
l = []
for i in x:
    if int(i) % 2 != 0:
        l.append(int(int(i)*int(i)))
l.sort()
l = str(l)
print(" ".join(l))
