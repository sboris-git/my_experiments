class Number:

    def __init__(self, num):
        self.num = num

    def square(self):
        return self.num ** 2


obj = Number(5)
print(obj.square())
