
def num(x):
    return x ** 2
y = input("enter a number\n")
print(num(int(y)))

def word(string):
    print(string)
word("hello")

def fiveparam(x,y,z,b=49,c=44):
    return x + y + z - b - c
print(fiveparam(2,4,6,3,4))

def first(x):
    return x / 2
def second(x):
    return x * 4
b = first(3)
print(second(b))


