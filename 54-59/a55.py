text = input("Please type text").split(" ")

for i in text:
    if i.isdigit() == False:
        text.remove(i)
print(text)
