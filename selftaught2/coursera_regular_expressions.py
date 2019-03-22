# provides way to match text referrred to as regex
# Python Regular Expression Quick Guide
# ^        Matches the beginning of a line
# $        Matches the end of the line
# .        Matches any character
# \s       Matches whitespace
# \S       Matches any non-whitespace character
# *        Repeats a character zero or more times
# *?       Repeats a character zero or more times
#          (non-greedy)
# +        Repeats a character one or more times
# +?       Repeats a character one or more times
#          (non-greedy)
# [aeiou]  Matches a single character in the listed set
# [^XYZ]   Matches a single character not in the listed set
# [a-z0-9] The set of characters can include a range
# (        Indicates where string extraction is to start
# )        Indicates where string extraction is to end

# import re to pull in regular expressions
# re.search() to see of a string matches a regular expression
# re.findall() extract portions of a string

# re.search() returns a true false depending on whether string matches regex
# if we want the matching strings to be extracted, we use re.findall()
# [0-9]+ is one or more digits, without the + it is just one digit
# warning greedy matching (* and +) push outward to match largest possible string
# greedy example ^F.+: (first char is F and . is any amount of chars followed by semicolon
# From: this is a greedy: sample returns From: this is a greedy: instead of just From:

# non greedy matching ^F.+?: returns ['From:']


import re

hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('From ', line):
        print(line)
print()
# use re.search() like find
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if line.find('From: ') >= 0:
        print(line)
print()
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('^From ', line):
        print(line)
print()
# use re.search() like find
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if line.startswith('From: '):
        print(line)

hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('^X.*:', line):  # ^match line start'.' is any char and '*' is any number of times
        print(line)
        print(line)
print()

hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('^X-\\S+:', line):  # ^start with X followed by - \S+: any non whitespace character followed by:
        print(line)

x = 'my 2 favorite numbers are 19 and 42'
y = re.findall('[0-9]+', x)
print(y)  # get back list of strings
y = re.findall('[AEIOU]+', x)  # any upper case vowels
print(y)

x = 'From stephen.marquard@uct.ac.za Sat Jan 5'
y = re.findall('\\S+@\\S+', x)  # one or more non blank followed by @ and one ore more non blanks
print(y)

y = re.findall('^From (\\S+@\\S+)',
               x)  # parenthesis start extracting after space with prefix of From but dont want From in results
print(y)

# extract host name using slice and string slicing
x = 'From stephen.marquard@uct.ac.za Sat Jan 5'
atpos = x.find('@')
print(atpos)
sppos = x.find(' ', atpos)
print(sppos)
host = x[atpos + 1: sppos]
print(host)
print()
# other way to get host using dual splits
words = x.split()
email = words[1]
pieces = email.split('@')
print(pieces)
print(pieces[1])
print()
# using regular expressions
print(x)
y = re.findall('@([^ ]*)', x)  # find @, [^ ] match everything but space, * means 0 or more times
print(y)
# another regex way to do it
y = re.findall('^From .*@([^ ]*)', x)  # start with From any number of chars up to @ and all non blank characters

print(y)
hand = open('mbox-short.txt')
numlist = list()
for line in hand:
    line = line.rstrip()
    stuff = re.findall('^X-DSPAM-Confidence: ([0-9.]+)', line)  # 0-9 and . to get float one or more times
    if len(stuff) != 1:
        continue
    num = float(stuff[0])
    numlist.append(num)
print('Maximum:', max(numlist))

test = 'right to the point a22 1dd is this what I am looking for a22:'
z = re.findall('[a-z0-9]', test)
print(z)

x = 'From: Using the : character'
y = re.findall('^F.+:', x)
print(y)

x = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
y = re.findall('\\S+@\\S+', x)  # any non blank followed by @ + non blanks
print(y)

z = re.findall('[a-z0-9]', x)
print(z)

r = re.findall('@(\\S+)', x)  # start extracting after the @ sign
print(r)
