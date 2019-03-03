fname = input('Enter file: ')
if len(fname) < 1: fname = 'clown.txt'
hand = open(fname)

di = dict()  # make a dictionary
for lin in hand:  # go through the file
    lin = lin.rstrip()  # remove white space
    wds = lin.split()  # splits into words
    print(wds)
    for w in wds:
        # print(w)
        # oldcount = di.get(w, 0)  # assume it is zero if the key is not there
        # print(w, 'old', oldcount)
        # newcount = oldcount + 1  # add 1 if key already in dictionary
        # di[w] = newcount

# this code replaces code above with idiom: reirieves, updates, create counter
        di[w] = di.get(w, 0) + 1  # di sub w = get old value set 0 and add 1 to dictionary
# get function replaces if else to accompish same thing
# if w in di:
#     di[w] = di[w] + 1  # set the value of key and increment by one
#     print('**Existing**')
# else:
#     di[w] = 1  # insert value if it is not there
#     print('**NEW**')
# print(w, di[w])  # takes on all words of file
print(di)
# no we want to know the most common word in dictionary
largest = None
theword = None
for k, v in di.items():  # k and v take on values of key values
    if largest is None or v > largest:
        largest = v
        theword = k  # capture remember the word that was largest
print(theword, largest)

