def write_yes(a):
    print(a.upper(),a.capitalize(),a)
    if a == "YES" or a == "Yes" or a == "yes":
        print("yes")
    else:
        print("no")
write_yes("no")