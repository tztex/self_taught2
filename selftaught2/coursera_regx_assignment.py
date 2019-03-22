import re
hand = open('regex_sum_189079.txt')
numlist = list()
for line in hand:  # read through file
    # print(line)
    line = line.rstrip()  # strips white space
    stuff = re.findall('[0-9]+', line)  # 0-9 one or more times
    # print(len(stuff))
    if len(stuff) > 0:  # list length of stuff is > 0
        numlist += stuff  # add each number to list as a string
        continue

intsum = sum([int(i) for i in numlist])  # list comprehension create to variable with summed integers from list
# total = sum(newints)
print(intsum)

