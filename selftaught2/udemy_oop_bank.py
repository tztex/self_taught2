# templates are called class to get an object
# each object is instance of class
# classes made up of variables known as states and functions known as methods
# states and methods make objects behave differently (behavior is methods)
# classes are templates for objects
# class methods need constructor __init__(self): self refers to current instance
# destructor is __del__(self) gets rid of class
# inheritance is where you can get access to variables and functions of parent class
# with things defined and put child in parent

# polymorphism overrides behavior where method has different form
# used the __str__(self) method to give nice output to object

class Account:
    def __init__(self, name, balance):  # constructor instances of the class
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance > amount:
            self.balance -= amount
        else:
            print('Sorry, not enough funds')

    def statement(self):
        print('Account Balance: ${}'.format(self.balance))

    def __del__(self):
        print('account closed')

class Current(Account):  # inherits from account class
    def __init__(self, name, balance):  # constructor includes options they must enter
        super().__init__(name, balance)  # pass data up to account

    def __str__(self):  # string function for objects name instead of memory address
        return "{}'s Current Account: Balnce ${}".format(self.name, self.balance)

# class Savings(Account):
#     def __init__(self, name, balance):
#         super().__init__(name, balance)  # pass data up to account
#     def __str__(self):  # string function for objects name instead of memory address
#         return "{}'s Savings Account: Balnce ${}".format(self.name, self.balance)

x = Current("Tom", 500)
x.deposit(300)
print(x.balance)
x.withdraw(800)
print(x.balance)
x.withdraw(1000)
x.statement()
print(x)
del x





