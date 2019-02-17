n = 5
while n > 0:
    print("hello")
    n = n - 1
print("done")
# break gets out of loops and continue goes to top of line
# indefinite loops
# definite loops are finite like for loop

for i in range(5):
    print(i)
print('blastoff')
friends = ['Tom', 'Glen', 'Sally']
for friend in friends:
    print(friend)

largest_so_far = -1
print('before', largest_so_far)
for the_num in [5, 34, 6, 77]:
    if the_num > largest_so_far:
        largest_so_far = the_num
        print(the_num)
    print(largest_so_far, the_num)  # print needs to be under if to print all values
print('after', largest_so_far)

smallest_so_far = None  # flag value
print('before')
for the_num in [5, 34, 6, 77, 3]:
    if smallest_so_far is None: # will always be false second time through loop
        smallest_so_far = the_num
    elif the_num < smallest_so_far:
        smallest_so_far = the_num
    print(smallest_so_far, the_num)
print('after', the_num)

# assignment 5.1 py4e
num = 0
tot = 0.0
while True:
    sval = input('enter a number')
    if sval == 'done':
        break
    try:
        fval = float(sval)
    except:
        print('invalid input')
        continue
    print(fval)
    num = num + 1
    tot = tot + fval

print('all done')
print(tot, num, tot/num)

print()

# assignment 5.2 py4e
largest = None
smallest = None
numbers = []
while True:
    num = input('Enter a number: ')
    if num == 'done':
        break
    try:
        inum = int(num)
        numbers.append(inum)
    except:
        print('Invalid input')
        continue
largest = max(numbers)
smallest = min(numbers)
print("Maximum is", largest)
print("Minimum is", smallest)

