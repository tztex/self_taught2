# 10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour
# of the day for each of the messages. You can pull the hour out from the 'From ' line by finding
# the time and then splitting the string a second time using a colon.

# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
time = list()
counts = dict()
lst = list()
name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
for line in handle:
    line = line.rstrip()
    if not line.startswith('From '):  # skip lines we are not interested
        continue
    words = line.split()[5].split(':')  # gives each word in own line
    time.append(words[0])
for hour in time:  # inner loop through words
    counts[hour] = counts.get(hour, 0) + 1  # creates histogram key and value
for key, val in counts.items():  # loops through key and values
    newtup = (key, val)  # create value key tuple
    lst.append(newtup)  # append list
lst = sorted(lst)  # sort list in reverse
for key, val in lst:
    print(key, val)
