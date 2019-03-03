# figure out who has sent the greatest number of mail messages
# The program looks for 'From ' lines and takes the second word of those lines as the person
# who sent the mail.
#  creates a Python dictionary that maps the sender's mail address to a count of the number of
#  times they appear in the file. After the dictionary is produced, the program reads through
#  the dictionary using a maximum loop to find the most prolific committer.

counts = dict()  # create empty dictionary
email = list()
handle = open("C:\\Users\\tmzan\\Downloads\\mbox-short.txt")
for line in handle:  # loop through file
    line = line.rstrip()  # strip white space and read each line
    if not line.startswith('From '):  # skip lines we are not interested
        continue
    words = line.split()  # gives each word in own line
    email.append(words[1])  # adding each email occurrence to email list
for word in email:  # loop through email list
    counts[word] = counts.get(word, 0) + 1  # adds to dicitonary and adds one for each occurrence
    continue

bigcount = None
bigemail = None
for word, count in counts.items():  # loops through the dicitonary key values
    if bigcount is None or count > bigcount:  # compares count to bigcount
        bigemail = word
        bigcount = count
print(bigemail, bigcount)