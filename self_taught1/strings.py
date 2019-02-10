import re
# strings are immutable cannot change characters in string
# add strings using + operator
#.upper() changes all to upper using upper method
#.capitalize() method capializes first letter
# format method to create string. it looks for curly brackets
# format ex. n= input("name") r = """ this is your {}""".format(n)
#split(".") is method to seperate a sting to two or more strings
#split ex. is """the cat in the hat. the box is read""".split("."
#join method adds new characters between characters
#join ex. first_two = "abc"  result = "+".join(first_two) a+b
# add a space using .join method ex.words = ["The", "Fox"] one_string = " ".join(words)
#strip() removes leading or trailing white space
# in keyword to check if something is in string
# to use double quotes inside string put a \ in front of them
# \n inside string represents a new line
# slicing from list list[0:3] - slices list 0-3, leave start empty if start at 0 and leave end empty if it is last item
# replace method replaces occurence with another string newlist = list("s","$")
# index method returns where character first appears ex. list.index("m")

word = "Camus"
print(word[0:])
print(word[1])
print(word[2])
print(word[3])
print(word[4])

response_one = input("what did you write")
response_two = input("who did you send it too")
response = "Yesterday I wrote a {}. I sent it to {}".format(response_one, response_two)
print(response)

author = "aldous Huxley was born in 1894.".capitalize()
print(author)


lst = "Where now? Who now? When now?".split("?")
print(lst)

#replace letter with another one
dollar = "A screaming comes across the sky."
dollar = dollar.replace("s","$")
print(dollar)

# find index of character m
heming = "Hemingway"
print(heming.index("m"))

#concatentate and multiply strings
x = "three"
newx = x + x + x
print(newx)
newx = x*3
print(newx)

#turn dialogue from book into string include quotes
book = "Dr. Delaware? I've got \"someone\" on the line, a Ms. Mars"
print(book)

#slice strings before the comma
cold = "It was a bright cold day in April, and the clocks were striking thirteen."
newcold = cold[:cold.index(",")]
print(newcold)

# turn into grammatically correct string
fox = ["The", "fox", "jumped", "over", "the", "fence", "."]
fox = " ".join(fox)
fox = fox[0:-2] + "."
print(fox)

word = "guess"
guess = 's'
indices = [i for i, a in enumerate(word) if a == guess]
print(indices)

number = "Arizona: 479, 501, 870. California: 209, 213, 650."
me = re.findall("\d", number)
print(me)

ghost = "The ghost that says boo haunts the loo."
m = re.findall(".oo", ghost)
print(m)

