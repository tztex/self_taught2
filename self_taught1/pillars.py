#1. Create Rectangle and Square classes with a method called calculate_perimeter
# that calculates the perimeter of the shapes they represent. Create Rectangle and
# Square objects and call the method on both of them.

class Rectangle():
    def __init__(self, l, w):
        self.width = w
        self.length = l
    def calculate_perimeter(self):
        return 2 * (self.width + self.length)

class Square():
    def __init__(self, l):
        self.length = l
    def calculate_perimeter(self):
        return 4 * self.length
a_rectangle = Rectangle(4, 2)
print(a_rectangle.calculate_perimeter())

a_square = Square(4)
print(a_square.calculate_perimeter())
print()

class Rectangle():
    def __init__(self, w, l):
        self.width = w
        self.length = l

    def calculate_perimeter(self):
        return (self.width + self.length) * 2

class Square():
    def __init__(self, sl):  # method always included in instance of a square
        self.sl = sl

    def calculate_perimeter(self):
        return 4 * self.sl

    def change_size(self, new_size):
        self.sl += new_size

a_square = Square(100)  # create a_square object
print(a_square.sl)

a_square.change_size(200)
print(a_square.sl)
print(a_square.calculate_perimeter())

# Create a class called Shape. Define a method in it called what_am_i that prints
# "I am a shape" when called. Change your Square and Rectangle classes from the
# previous challenges to inherit from Shape, create Square and Rectangle objects,
# and call the new method on both of them.

class Shape():
    def what_am_i(self):
        print("I am a shape.")

class Rectangle(Shape): #inherit from Shape
    def __init__(self, w, l):
        self.width = w
        self.length = l

class Square(Shape):
    def __init__(self, sl):  # method always included in instance of a square
            self.sl = sl

    def calculate_perimeter(self):
            return 4 * self.sl

    def change_size(self, new_size):
            self.sl += new_size
    def calculate_perimeter(self):
        return (self.width + self.length) * 2
a_rectangle = Rectangle(20,10)
a_rectangle.what_am_i()
a_square = Square(5)
a_square.what_am_i()

