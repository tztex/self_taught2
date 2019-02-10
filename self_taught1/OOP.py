import math
# eliminates global states
# store variables in obects
# create n object with a "class" is a blueprint for creating objects
# every object is an instance of class which means objects data type is class that created it
# ex str() has data type string cause python creates with string class
# class names start in upper case and camel case
# define method inside a class
# method names are lower case
# created is defined in method init. _init_ is called everytime and called MAGIC METHOD AND MUST ALWAYS
# ACCEPT A CHARACTER. CONVENTION IS TO ALWAYS NAME PARAMETER(self)
# need paramter cause python passes object method was called on as a parameter
# OOP allows you to model a has a relationship by storing an object as variable in another object which
# is called COMPOSITION
class Orange:  # class creates blueprint of orange use tocreate instances of orange objects
    def __init__(self):  # example of defining a method. method is like function you call on object
        print("Created!")  # when you use class to create object you call method


orange = Orange()  # creating an object is instantiating a class (instance of orange object)

print()


class Orange():
    def __init__(self, w, c):
        self.weight = w
        self.color = c
        print("Created!")


or1 = Orange(10, "dark orange")
or1.weight = 100
or1.color = "light orange"

print(or1.weight)
print(or1.color)


class Orange():
    def __init__(self, w, c):
        """weights are in oz"""
        self.weight = w
        self.color = c
        self.mold = 0
        print("Created!")

    def rot(self, days, temp):
        self.mold = days * temp


print()

orange = Orange(6, "orange")
print(orange.mold)
orange.rot(10, 98)
print(orange.mold)

print()


class Dog:
    def __init__(self, name, breed, owner):
        self.name = name
        self.breed = breed
        self.owner = owner


class Person:
    def __init__(self, name):
        self.name = name


mick = Person("Mick Jagger")
stan = Dog("Stanley",
           "Bulldog",
           mick)
print(stan.owner.name)

print()


class Rectangle():
    def __init__(self, w, l):
        self.width = w
        self.len = l

    def area(self):
        return self.width * self.len

    def change_size(self, w, l):
        self.width = w
        self.len = l


rectangle = Rectangle(10, 20)
print(rectangle.area())
rectangle.change_size(20, 40)
print(rectangle.area())

# excercise 1 Define a class called Apple with four instance variables that represent
# four attributes of an apple.
class Apple:
    def __init__(self, weight, color, brand, age):
        self.weight = weight
        self.color = color
        self.brand = brand
        self.age = age
#excercise 2 Create a Circle class with a method called area that calculates and returns its area.
# Then create a Circle object, call area on it, and print the result. Use Python's pi function
# in the built-in math module.
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return self.radius ** 2 * math.pi

a_circle = Circle(4)
print(a_circle.calculate_area())

print()
#Create a Triangle class with a method called area that calculates and returns its area.
# Then create a Triangle object, call area on it, and print the result.
class Triangle:  #class Triangle
    def __init__(self, base, height): #method that creates instance of object
        self.base = base
        self.height = height
    def calculate_area(self): #method that takes object as variable
        return self.height * self.base / 2

a_triangle = Triangle(10, 30)
print(a_triangle.calculate_area())

print()
#Make a Hexagon class with a method called calculate_perimeter that calculates and returns
# its perimeter. Then create a Hexagon object, call calculate_perimeter on it, and print
# the result.
class Hexagon:
    def __init__(self, sides, length):
        self.sides = sides
        self.length = length
    def calculate_perimeter(self):
        return self.sides * self.length
a_hexagon = Hexagon(4,6)
print(a_hexagon.calculate_perimeter())