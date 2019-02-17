#shortcut to combine variables for loops and if statement
even_numbers = [x for x in range(1, 101) if x % 2 == 0]
print(even_numbers)
#we have a variable x is what is stored in list
#x loops through range only keep when % 2
odd_numbers = [x for x in range(1, 101) if x % 2 != 0]
print(odd_numbers)
#works for all data types
words = ["The", "quick", "brown", "fox", "jumps", "over", "dog"]
answer = [[w.upper(), w.lower(), len(w)]for w in words] #double brackets cause list of list
print(answer)

