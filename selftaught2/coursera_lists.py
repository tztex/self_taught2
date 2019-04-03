
# do some parsing with lines that begin with 'from '
fhand = open('C:\\Users\\tmzan\\Downloads\\mbox-short.txt')  # open file
wds = list()
counts = dict()
for line in fhand:
    line = line.rstrip()
    # print(line)
    if not line.startswith('Received'):
        continue
    # print(line)
    words = line.split()[2].split('.')  # gives each word in own line ['16', '23', '48']
    for wordy in words:
        counts[wordy] = counts.get(wordy, 0) + 1
        continue
# bigcount = None
# bigword = None
# for wordy in wds:
#     counts[wordy] = counts.get(wordy, 0) + 1
#     continue
print(counts)



