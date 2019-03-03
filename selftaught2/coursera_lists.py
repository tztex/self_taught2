# use functions to calculate average
# total = 0
# count = 0
# while True:  # if I was reading file it would be for loop
#     inp = input('enter a number: ')
#     if inp == 'done': break
#     value = float(inp)
#     total = total + value
#     count = count + 1
# average = total / count
# print('Average: ', average)

# do same thing with a data structure to accumulate values
# numlist = list()
# while True:
#     inp = input('enter a number: ')
#     if inp == 'done': break
#     value = float(inp)
#     numlist.append(value)
#
# average = sum(numlist) / len(numlist)
# print('Average: ', average)

# lists and strings work together
# split built in function takes a string and gives us a list
# you can specify the delimeter
# abc = 'with three words'
# stuff = abc.split() # returns a list
# print(stuff)
# print(len(stuff))
# print(stuff[0])

# for w in stuff:  # loop runs 3 times and prints word each time
#     print(w)
#
# fhand = open('C:\\Users\\tmzan\\Downloads\\mbox-short.txt')  # open file
# for line in fhand:  # loop
# #     line = line.rstrip()  # strip white space
#     if not line.startswith('From '):  # skip lines we are not interested
#         continue
#     words = line.split()
#     print(words[2])
#
# # The double split pattern
# words = line.split()
# email = words[1]
# pieces = email.split('@')
# print(pieces[1])

# assigment 8.4
# open file romeo.txt for each line split it into a list of words program builds list of words
# for each word check if it is in the list. if not append to it
# sort and print
# fh = open("C:\\Users\\tmzan\\Downloads\\romeo.txt")
# lst = list()  # create list
# for line in fh:  # read each line
#     words = line.split() # breaks out words from each sentence
#     # print(words)
#     for word in words:  # evaluate all words in words
#         if word not in lst:
#             lst.append(word)
# lst.sort()
# print(lst)

# assignment 8.5
# open mbox-short and pull out email address
# line format is From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008

# fhand = open('C:\\Users\\tmzan\\Downloads\\mbox-short.txt')  # open file
# count = 0
# for line in fhand:  # loop
#     line = line.rstrip()  # strip white space
#     if not line.startswith('From '):  # skip lines we are not interested
#         continue
#     count = count + 1  # counts lines we are interested in
#     words = line.split()
#     print(words[1])  # must indent it to print as inside for loop
#
# print("There were", count, "lines in the file with From as the first word".format(count))


# do some parsing with lines that begin with 'from '
fhand = open('C:\\Users\\tmzan\\Downloads\\mbox-short.txt')  # open file
for line in fhand:
    line = line.rstrip()
    # print(line)
    wds = line.split()
    # print(wds)
    if len(wds) < 1:  # guardian
        continue
    if wds[0] != 'From':
        continue
    print(wds[2])

