x = input("enter password")
""" requirements
    At least 1 letter between [a-z]
    At least 1 number between [0-9]
    At least 1 letter between [A-Z]
    At least 1 character from [$#@]
    Minimum length of transaction password: 6
    
    Maximum length of transaction password: 12
"""
l = []
d = {
    "a-z":False,
    "A-Z":False,
    "0-9":False,
    "$#@":False
}

def checkPassword(password):
    count = 0
    if len(password) <= 12 and len(password) >= 6:
        for i in password:
            if i.isdigit() == True:
                count +=1
                print("0-9 okay")
                break
        for i in password:
            if i.islower() ==True:
                count += 1
                print("a z okay")
                break
        for i in password:
            if i.isupper() == True:
                count += 1
                print("A Z  okay")
                break
        for i in password:
            if i=='@' or i=='#'or i=='$':
                count += 1
                print(" @ # okay")
                break
        if count ==  4:
            print("You can use this password")
        else:
            print("You can't use this password")


checkPassword(x)