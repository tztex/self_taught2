fname = raw_input("Enter file name: ")
fh = open(fname)
average = 0
count = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    pos = line.find(" ")
    val = line[pos:].rstrip()
    val = float(val)
    count = count + 1
    average = average + val
        
print "Average spam confidence:", average/count 
