fname = input('Enter file: ')
if len(fname) < 1: fname = 'clown.txt'
hand = open(fname)

di = dict()  # make a dictionary
for lin in hand:  # go through the file
    lin = lin.rstrip()  # remove white space
    wds = lin.split()  # splits into words
    for w in wds:
        di[w] = di.get(w, 0) + 1  # di sub w = get old value set 0 and add 1 to dictionary
print(di)
tmp = list()
for k, v in di.items():
    # print(k, v)
    newt = (v, k)  # new local tuple value, key
    # print(newt)
    tmp.append(newt)  # list of tuples in value, key into tmp list
tmp = sorted(tmp, reverse=True)
for v, k in tmp[: 5]:
    print(k, v)