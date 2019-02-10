def nameage():
    try:
        name = input("Please enter your name ")
        age = input("Please enter your age ")
        age = int(age)

        print("my name is " + name + " and my age is " + age)
    except (ValueError, TypeError):
        print("name is string and age is whole numer")
nameage()
