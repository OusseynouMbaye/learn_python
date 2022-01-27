class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        print('CALLED by rectangle')
        return self.length * self.width


class Square(Rectangle):
    def area(self):
        print('CALLED by square')
        return self.length ** 2


square = Square(5, 5)
print(square.area())

