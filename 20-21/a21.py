import  math

x = input("Please insert in  order  up, down, left, right").split(",")
print("UP " + x[0], "DOWN " + x[1], "LEFT " + x[2], "RIGHT " + x[3])

horizontal = abs(int(x[2]) - int(x[3]))
vertical = abs(int(x[0]) - int(x[1]))
print(horizontal,vertical)
far_from_start = math.sqrt(horizontal*horizontal + vertical * vertical)
print(far_from_start)