#Add a square_list class variable to a class called Square so that every time you
# create a new Square object, the new object gets added to the list.
class Square():
    square_list = []

    def __init__(self, l):
        self.l = l
        self.square_list.append(l)
        print("""the length of the shape is {}.""".format(self.l))


a_square = Square(3)
a1_square = Square(4)
print(Square.square_list)

#Change the Square class so that when you print a Square object, a message prints
# telling you the len of each of the four sides of the shape. For example, if you
# create a square with Square(29) and print it, Python should print 29 by 29 by 29
# by 29.

#Write a function that takes two objects as parameters and returns True if they are
# the same object, and False if not.

class Object_Test():
    def __init__(self,):
        self.name = "Tom"
Tom = Object_Test()
tom_1 = Tom
print(Tom is tom_1)

#another example
def compare(obj1, obj2):
    return obj1 is obj2

print(compare("a", "b"))

