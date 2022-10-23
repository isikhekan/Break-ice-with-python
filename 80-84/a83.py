l = [12,24,35,70,88,120,155]

l = [l[i] for i in range(len(l)) if i < 3 or i>4]
print(l)