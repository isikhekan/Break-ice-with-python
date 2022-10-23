def create_tuple():
    my_list = (i**2 for i in range(1,21))
    print(tuple(my_list))

create_tuple()