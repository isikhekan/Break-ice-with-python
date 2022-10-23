def write_tuple():
    tuple = (1,2,3,4,5,6,7,8,9,10)
    new_tuple = []
    for i in range(len(tuple)):
        if i%2 ==0:
            new_tuple.append(i)
    print(new_tuple)
write_tuple()