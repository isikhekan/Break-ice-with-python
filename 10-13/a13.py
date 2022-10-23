x = input("Type something...").split(" ")
d = {
    "digit": 0,
    "string":0
}
for i in x:
    if i.isdigit() == True:
        d["digit"]+=1
    else:
        d["string"]+=1
print(d)