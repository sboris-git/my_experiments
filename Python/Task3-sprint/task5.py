class Test:
    class_variable = 10

    def __init__(self):
        self.string = ''

    def getString(self):
        self.string = input('Type a string: ')

    def printString(self):
        print(self.string.upper())

obj = Test()
obj.getString()
obj.printString()