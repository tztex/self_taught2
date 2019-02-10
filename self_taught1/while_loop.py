#while loop excutes as long as expression evaluates to true
# if you define while loop that always is true it will run forever called infinite loop
# keyword break terminates a loop
import random

health = 50
difficulty = 1
potion_health = int(random.randint(25,50) / difficulty)
health = health + potion_health
print(health)
print()

for i in range(5, 100):
    print(i)
    break
print()

x = 10
while x > 0:
    print('{}'.format(x))
    x -= 1
print("Happy New Year!")
print()

#use while loop to ask user for input until they type keyword to break
qs = ["What is your name?",
      "What is your color?",
      "what is your quest"]
n = 0
while True:
    print("type q to quit")
    a = input(qs[n])
    if a == "q":
        break
    n = (n+1) % 3
print(qs[0])
print()
# continue statement stops iteration and moves on
for i in range(1,6):
	if i == 3:
		continue
	print(i)
print()

#nesting loops are loops inside a loop
for i in range(1,4): #[] brackets are not subscriptable
	print(i)
	for letter in ["a", "b", "c"]:
		print(letter)
print()

#2 for loops to add numbers in a list to another list. iterates through list1 and
# list2
#i holds number from list 1 and j a number from list 2
# add i and j
list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]
added = []

for i in list1:
	for j in list2:
		added.append(i+j)

print(added)
print()

#nest a for loop inside a while loop
while input('y or n?') != 'n':
	for i in range(1,6):
		print(i)
print()

#excercise 1 infinite loop of numbers with option to type q to quit
#each time ask them number and tell whether they guesses correctly
numbers = int(random.randint(24,29))
while True:
    answer = input("Guess a number or type \"q\" to quit")
    if answer == "q":
        break
    try:
        answer = int(answer)
        if answer == numbers:
            print("good guess")
        else:
            print("guess again please")
    except ValueError:
        print("enter an integer please")
print()

#excercise 2 Multiply all the numbers in the list [8, 19, 148, 4]
# with all the numbers in the list [9, 1, 33, 83], and
# append each result to a third list.
list1 = [8, 19, 148, 4]
list2 = [9, 1, 33, 83]
multiply = []
for i in list1:
    for j in list2:
        multiply.append(i * j)
print(multiply)

#while loop practice
number = 1
while number <= 10:
    if number % 2 == 0:
        print(number)
    number = number + 1

L = []
while len(L) < 3:
    new_name = input("please add a new name: ").strip().capitalize()
    L.append(new_name)
print("sorry list is full")
print(L)
