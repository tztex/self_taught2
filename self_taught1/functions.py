print()


# functions are reusable and must define use def
# returning values is not same as printing. return holds in memory
# returns none if no return in functions
# Variable scope 2 types. global and local
# functions create there own local scope and other cannot see inside
#
def num(x):
    return x ** 2


y = input("enter a number\n")
print(num(int(y)))


def word(string):
    print(string)


word("hello")


def fiveparam(x, y, z, b=49, c=44):
    return x + y + z - b - c


print(fiveparam(2, 4, 6, 3, 4))


def first(x):
    return x / 2

def second(x):
    return x * 4


b = first(3)
print(second(b))


# reverse
def rev(text):
    return text[::-1]


# scope examples, cannot change global inside function with same local
# you can use global variable but not change it
# can overwrite lists and dictionaries without global keyword
a = [1, 2, 3]


def f1():
    a[0] = 5
    print(a)


def f2():
    a = 50
    print(a)


f1()
f2()
print(a)


# parameter is in function definition
# arguments are what we pass to the function
# arguments match to parameter in specific order
# can enter in any order as long as we associate key word argument
# can assign default values
# default parameters must go at the end

def about(name, age, likes="Python"):
    sentence = "Meet {} They are {} years old and like {}".format(name, age, likes)
    print(sentence)


about(age=23, name="Tom")

# packing and unpackng variables, arguments and keyword arguments
# unpacking we take each item from iterbale data type and it becomes there own argument
# works for strings too
print(1, 2, 3, 4, 5)  # passing 5 arguments prints on one row
numbers = [1, 2, 3, 4, 5]
print(numbers)
print(*numbers)  # unpack list
print("abd")
print(*"abc")


# how to pack arguments and works inside function
def add(x, y):
    return x + y


print(add(10, 10))
print()


# instead of x and y pack in numbers, packs arguments into one tuple called numbers
# tuples are iterable and add them
# good when you dont know how many arguments
def add(*args):  # packs into one tuple
    total = 0  # inside function
    for number in args:  # loop through the tuple
        total = total + number
    return total


print(add(1, 2, 3, 4, 5, 6))  # all put into a tuple


# keyword arguments
def about(name, age, likes):
    sentence = "meet {} they are {} years old and the like {}".format(name, age, likes)
    print(sentence)


dictionary = {"name": "Tom", "age": 23, "likes": "python"}
about(**dictionary)  # two stars for keyword arguments


# pack keyword arguments using double stars
def foo(**kwargs):  # keyword arguments, produces a dictionary
    for key, value in kwargs.items():  # gives set of tuples with key and value
        print("{}:{}".format(key, value))


foo(huda="female", ziyad="male", john="male")
