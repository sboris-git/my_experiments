class Rectangle:

    def __init__(self, lengt, width):
        self.lengt = lengt
        self.width = width

    def area(self):
        return self.lengt * self.width


obj = Rectangle(5, 6)
print(obj.area())