# 2 loops types 1. for loops used for iterating
# ex 1. name = "Ted"
# for character in name:
#     print(character)
#ex. 2 shows = ["GOT", "Narcos", "Vice"]
#for show in shows
#print(show)
#code is same through tuple like a list
#dictionary example people = {"Barney: "Always Sunny",
                                #"Stephen": "King"
                                #}
                                #for character in people
                                #print(character) this prints just the key

#change items to all upper case
#tv = ["GOT", "Narcos", "Vice"]
#i = 0 "i is the index variable and hold integer representing index in inerable

# also use for loops to move data between iterables
tv = ["Got", "Narcos", "Vice"]
coms = ["Arrested Development", "friends", "Always Sunny"]
all_shows = []
for show in tv:
    show = show.upper()
    all_shows.append(show)
for show in coms:
    show = show.upper()
    all_shows.append(show)
print(all_shows)

#change items to all upper case by iterating through the list
tv = ["GOT", "Narcos", "Vice"]
i = 0
for drama in tv:
    new = tv[i]
    new = new.upper()
    tv[i] = new
    i += 1
print(tv)

#use range to create sequence of intergers and use for loop to iterate throught them
for i in range(1, 11):
    print(i)

#print each item in following list:
shows = ["The Walking Dead", "Entourage", "The Sopranos", "The Vampire Diaries"]
for horror in shows:
    print(horror)

# Print all the numbers from 25 to 50.
for i in range(25,51):
    print(i)

#Print each item in the list from the first challenge and their indexes.
#Enumerate is a built-in function of Python. Its usefulness can not be summarized
# in a single line. It allows us to loop over something and have an automatic
# counter. Here is an example:

shows = ["The Walking Dead", "Entourage", "The Sopranos", "The Vampire Diaries"]
for index, horror in enumerate(shows):
    print(index, horror)

names = ["Tom", "bILL", "TIM", "JASON"]
i =0
for first in names:
    new = names[i]
    new = new.capitalize()
    names[i] = new
    i += 1
print(names)

for index, first in enumerate(names):
    print(index, first)

list1 = [4, 3, 5, 8]
list2 = [5, 3, 2, 1]
added = []
for i in list1:
    for j in list2:
        added.append(i + j)
print(added)




