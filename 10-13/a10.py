x = input("Enter string").split(" ")
mySet = set({})

mySet.update(x)
mySet = sorted(mySet)
for i in mySet:
    print("".join(i))