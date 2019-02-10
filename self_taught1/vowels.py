import re
string = "pencil"
vowels = "aeiou"
for i, c in enumerate(string):
    if c in vowels:
        print(i)
        break

new_string = ""
new_string = string[i:] + string[: i] + "ay"
print(new_string)
print(string[0:])

gifts = {"Tom": {"ring": "target", "necklace": "pennys"},
         "Mom": {"book": "amazon"}}
answer = input("pick a name")
try:
    print(gifts[answer])
except KeyError:
    print("please enter a valid name ")
print(gifts.keys())
print(len(gifts))
