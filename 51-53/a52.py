class CustomException(Exception):

    def __init__(self,message):
        self.message = message



x = int(input())


try:
    if x > 10:
        raise CustomException("x more than 10")
    elif x<10:
         raise CustomException("x less than 10")
except CustomException as ce:
    print("Error raised:" + ce.message)
