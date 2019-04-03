# 10.2 Write a program to read through the mbox-short.txt and figure out the
# distribution by hour
# of the day for each of the messages. You can pull the hour out from the
# 'From ' line by finding
# the time and then splitting the string a second time using a colon.
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008

from operator import itemgetter

time = list()
counts = dict()
lst = list()
name = input("Enter file:")
if len(name) < 1: name = "mbox-short.txt"
handle = open(name)
for line in handle:
    line = line.rstrip()  # removes the new line
    if not line.startswith('From '):  # skip lines we are not interested
        continue
    # print(line)  From cwen@iupui.edu Thu Jan  3 16:29:07 2008
    words = line.split()[5].split(':')  # gives each word in own line ['16', '23', '48']
    time.append(words[0])  # creates list of hours in time
    # print(time)
for hour in time:  # inner loop through words
    counts[hour] = counts.get(hour, 0) + 1  # creates histogram key and value
print(counts)  # dictionary
for key, val in counts.items():  # loops through key and values
    newtup = (key, val)  # create value key tuple
    lst.append(newtup)  # append list
print(lst)
# lst = sorted(lst)  # sort list in reverse
lst.sort(key=itemgetter(0), reverse=True)
lst.sort(key=itemgetter(1))
for key, val in lst:
    print(key, val)
