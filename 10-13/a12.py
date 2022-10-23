
l = []
for i in range(1000,3001):
    counter = 0
    for j in str(i):
        if int(j) % 2 == 0:
            counter +=1
    if counter == 4:
        l.append(i)

print(l)