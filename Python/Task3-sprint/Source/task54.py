class Shape:

    def __init__(self, length=None, width=None):
        self.length = length
        self.width = width

    def area(self):
        return 0


class Square(Shape):

    def __init__(self, length=None):
        Shape.__init__(self, length)
        # self.length = length

    def area(self):
        return self.length ** 2


obj = Square(5)
print(obj.area())
