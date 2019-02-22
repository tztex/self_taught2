# file handles are portal between file and our program
# ex. fhand = open('input.txt', r)
# \n is newline character
# text file is sequence of lines of characters punctuated by new lines
# \n represents the enter button
# file handle open for read is treated as sequence of strings
# use the for statement to iterate through  sequence

# xfile = open('mbox.txt')
# for cheese in xfile:
#   print(cheese)

# reading whole file
# fhand = open('mbox-short.txt')
# inp = fhand.read()
# print(len(inp))
# print(inp[:20]

# fhand = open('mbox-short.txt')
# for line in fhand:
# line = line.rstrip():
# if not line startswith('from'):
# continue
# print(line)
# print adds new line to each line

# fname = input('enter the file name:  ')
# fhand = open(fname)
# count = 0
# for line in fhand:
# if line startswith('subject'):
# count = count + 1
# print(count)

# quit() function at end of except to not continue

xfile = open("C:\\Users\\tmzan\\Downloads\\input.txt", 'r')
for cheese in xfile:
    cheese = cheese.rstrip()
    if not cheese.startswith("Delivered"):
        continue
    print(cheese)


# prompt for file name that reads and prints in upper case
#fname = input("Enter file name: ")
#fh = open(fname)
#inp = fh.read().upper().rstrip()
#print(inp)

#fname = input("Enter file name: ")
#fhand = open(fname)
#inp = fhand.read().rstrip()
#print(inp)

# does same as code above
# fh = open("C:\\Users\\tmzan\\Downloads\\words.txt")
#for line in fh:
    # print(line.rstrip().upper())

# code below just prints information about the file object
# fh = open("C:\\Users\\tmzan\\Downloads\\words.txt")
#print(fh)

fname = input("Enter file name: ")
fh = open(fname)  # set file handle
average = 0
count = 0
for line in fh:  # create loop through file using fh
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    line = line.rstrip()  # strip space before printing to avoid blank line
    print(line)
    pos = line.find(" ")  # find the space position which is right of semicolon
    val = line[pos:].rstrip()  # get value which is right of space
    val = float(val)
    count = count + 1
    average = average + val

print("Average spam confidence:", average / count)