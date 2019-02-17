#fizzbuzz
#3 fizz, 5 buzz, 3,5 fizzbuzz
def fizz_buzz():
    for i in range(1,101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)
fizz_buzz()
print()
#search algorithm
#looking for a card in deck you do it sequentially and stop when you find card
#or you made it through deck
numbers = range(1, 101)
def ss(number_list, n):
    found = False
    for i in number_list:
        if i == n:
            found = True
            break
    return found
result = ss(numbers, 105)
print(result)
print()
#a palindrome is word spelled same way forward and backward
#reverse and test to see if they are the same
def is_palindrome(word):
    word =  word.lower()
    return word[::-1] == word
result = is_palindrome("mom")
print(result)

print()
#anagram is word formed by rearranging letters of other word
def is_anagram(w1, w2):
    w1 = w1.lower()
    w2 = w2.lower()
    return sorted(w1) == sorted(w2)
result = is_anagram("iceman", "cinema")
print(result)

print()
#count characters in a string
def count_characters(string):
    count_dict = {}
    for c in string:
        if c in count_dict:  # go through each character
            count_dict[c] += 1  # if in count you add 1
        else:
            count_dict[c] = 1  # add to dictionary as key with value of 1
    print(count_dict)  #  contains key value pair for each character. key is character and value is number of times it occurred
count_characters("hello")
