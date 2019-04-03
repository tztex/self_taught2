def fact(n):
    if n == 1:
        return 1
    else:
        return (n * fact(n-1))
number = fact(5)
print(number)
print("hello")
