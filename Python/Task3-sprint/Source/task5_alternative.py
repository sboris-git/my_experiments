class Five:

    def __init__(self):
        self.string = ""

    @classmethod
    def input(cls):
        cls.string = input('Type a string')

    @classmethod
    def to_upper(cls):
        print(cls.string.upper())


# five = Five()
# five.input()
# five.to_upper()
#
Five.input()
Five.to_upper()