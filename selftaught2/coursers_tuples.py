# unmodifiable list
# elements are indexed, max uses tuples
# tuples are immutable, strings are immutable
# cannot sort or append or reverse
# cannot use methods that make changes
# put tuple on right hand side of assignment statement
(x, y) = (4, 'fred')
print(x)

d = dict()
d['csev'] = 2
d['cwen'] = 4
for k, v in d.items():  # creates list of 2 tuples
    print(k, v)

tups = d.items()
print(tups)

# tuples are comparable and does element by element comparison
print((5, 2, 4) < (4, 3, 2))

# sorting list of tuples keys are unique
d = {'a': 10, 'c': 1, 'b': 6}
print(sorted(d.items()))

# sorted takes sequence and gives list that is sorted version
for k, v in sorted(d.items()):
    print(k, v)

# sort by values instead of key, make value key tuples
c = {'a': 10, 'c': 1, 'b': 6}
tmp = list()
for k, v in c.items():
    tmp.append((v, k))
print(tmp)

tmp = sorted(tmp, reverse=True)
print(tmp)

# ten most common words
fname = input('Enter file: ')
if len(fname) < 1: fname = 'romeo.txt'
fhand = open(fname)
counts = dict()
for line in fhand:  # outer loop through file
    words = line.split()  # creates each line in a list
    print(words)
    for word in words:  # inner loop through words
        counts[word] = counts.get(word, 0) + 1  # creates histogram key and value

lst = list()
for key, val in counts.items():  # loops through key and values
    newtup = (val, key)  # create value key tuple
    lst.append(newtup)  # append list
lst = sorted(lst, reverse=True)  # sort list in reverse
for val, key in lst[:10]:
    print(key, val)

# list comprehension
c = {'a': 10, 'b': 1, 'c': 22}
print([(v, k) for k, v in c.items()])
# for all create me tuples v, k for each k, v in dictionary
# runs 3 times
# 3 tuples list past right into sorted function
