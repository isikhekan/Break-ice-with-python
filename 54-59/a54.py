email = input("please type email").split("@")


dm = email[1].split(".")
print(dm[0])