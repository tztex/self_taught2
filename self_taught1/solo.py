def add(x, y):
  return x + y

def do_twice(func, x, y):
  return func(func(x, y), func(x, y)) #runs inner parenths first then func(x15,y15)


a = 5
b = 10

print(do_twice(add, a, b))