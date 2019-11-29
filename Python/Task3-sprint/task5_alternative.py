class Five:

    def __init__(self):
        self.string = ""

    @classmethod
    def input(self):
        self.string = input('Type a string')

    @classmethod
    def to_upper(self):
        print(self.string.upper())


five = Five
five.input()
five.to_upper()