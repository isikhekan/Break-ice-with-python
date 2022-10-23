x = input("Değerleri giriniz.").split(",")
myList = []
for i in x:
    if len(i) != 4:
        x.remove(i)
for j in x:
    if int(j)% 5 == 0:
        myList.append(int(j))
print(sorted(myList))

