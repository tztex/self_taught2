#count vowels in text with for loop
word = "apple"
vowels = "aeiouy"
count = 0 #track number of vowels

for c in word: #iterating through word
    if c in vowels:
        count += 1
print(count)

#take string and turn to pig latin
#paris = arispay everything before first vowel at end + ay
string = "paris"
vowels = "aeiouy"
for i, c in enumerate(string): #enumerate keeps track of index of character
    if c in vowels:
        break
new_string = "" #create new string cause strings are imutable
new_string = string[i:] + string[: i] +"ay"
print(new_string)

#reverse string using a stack
string = "hello"
stack = []
for c in string: #iterate through string
    stack.append(c)
print(stack)

new_string = ""
for i, c in enumerate(string):
    new_string = new_string + stack.pop()
print(new_string)
print(string[::-1])

#random gift suggestion
#what is best data structure
#gifts for different people, mapping gifts to people
#use dictionary data structure
import random
gifts = {"Bobbi": ["ring,Tiffanys", "book, Barnes and Noble"],
         "Mom": ["phone, Ebay", "Book, Amazon"],
          "Dad": ["gloves, Amazon", "Book, Barnes and Noble"]
         }
answer = input("pick a person").strip().capitalize()
#print(gifts[answer]len(random.randint[key])
#[random.randint(0,len(gifts[answer]))])
surprise = len(gifts[answer])
print(surprise)
ran_surprise = random.randint(0, surprise - 1)
print(gifts[answer][ran_surprise])

