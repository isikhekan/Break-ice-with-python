words = {

}

x = input("Enter words").split(" ")

for i in x:
    words[i] = 0

for i in x:
    words[i] +=1

print(words)