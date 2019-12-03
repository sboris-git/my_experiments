class Door:

    color = 'black'

    def __init__(self, color):
        self.color = color

    @property
    def print_color(self):
        print(self.color)

    @classmethod
    # def print_color(cls):
    def print_color_cls(cls):
        print(cls.color)


print(Door.color)
Door.print_color_cls()
door = Door('red')
door.print_color