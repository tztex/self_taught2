# collection is a data structure more than one thing in variable
# list is linear collection and dictionary is a key value pair for each item
ccc = dict()
ccc['csev'] = 1
ccc['cwen'] = 1
print(ccc)
ccc['cwen'] = ccc['cwen'] + 1
print(ccc)
print('cssv' in ccc)

counts = dict()
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen', 'cwen']
for name in names:
    if name not in counts:
        counts[name] = 1
    else:
        counts[name] = counts[name] + 1
print(counts)

# get method checks to see if a key is already in a dictionary and set default value if not there
counts = dict()
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen', 'cwen']
for name in names:
    counts[name] = counts.get(name, 0) + 1
print(counts)
print()

# count the words in a line of text to split line into words then
# loop through the words and use a dictionary to track the count of each word

counts = dict()
print('enter a line of text')
line = 'this is s test to count to is is words'
words = line.split()
print('Words:', words)
print('counting...')
for word in words:
    counts[word] = counts.get(word, 0) + 1
print('Counts', counts)

# keys method gives list of keys
# values gives list of values
# items give both in tuples inside list
counts = {'chuck': 1, 'fred': 42, 'jan': 100}
for key in counts:
    print(key, counts[key])
print(list(counts))
print(counts.keys())
print(counts.values())
print(counts.items())
print(counts['chuck'])
print()

# two iteration variables
jjj = {'chuck': 1, 'fred': 42, 'jan': 100}
for key, value in jjj.items():  # go through dictionary to see all pairs
    print(key, value)
print()

handle = open("C:\\Users\\tmzan\\Downloads\\words.txt")
counts = dict()  # create empty dictionary
for line in handle:  # iterates through all lines
    words = line.split()  # gives each word
    for word in words:  # goes through each word to make histogram
        counts[word] = counts.get(word, 0) + 1
print(counts)
bigcount = None
bigword = None
for word, count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count
print(bigword, bigcount)
