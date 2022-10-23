x = input("Type string...")
print(x)
d = {
    "lower":0,
    "upper":0
}
for i in x:
    if i.isupper() == True:
        d["upper"] +=1
    if i.islower() == True:
        d["lower"] +=1
print(d)