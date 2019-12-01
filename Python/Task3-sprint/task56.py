class CustomException(Exception):
    '''Question 56  Define a custom exception class which takes a string message as attribute.
       message -- explanation of the error
    '''

    def __init__(self, message):
        self.message = message


a = 6
try:
    if a < 5:
        raise CustomException("The number is less than 5")
    elif a > 5:
        raise CustomException("The number is greater than 5")
except CustomException as err:
    print("Error: " + err.message)