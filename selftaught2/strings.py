fruit = 'banana'
x = len(fruit)
print(x)

# index operator called sub
# while is indeterminate loop
index = 0
while index < len(fruit):
    letter = fruit[index]
    print(index, letter)
    index = index + 1

# definite loop
for letter in fruit:
    print(letter)

count = 0
for letter in fruit:  # letter is iteration variable
    if letter == 'a':
        count = count + 1
print(count)

print(fruit[::2])

# strings are objects
new_fruit = fruit.upper()  # upper and lower are methods
print(new_fruit)

pos = fruit.find('na')
print(pos)
nstr = fruit.replace('banana', 'Tom')
print(nstr)
print(fruit.startswith('T'))

data = 'tom.zanoli@gmail.com Sat. Dec'
atpos = data.find('@')
print(atpos)

sppos = data.find(' ', atpos)
print(sppos)

host = data[atpos+1:sppos]
print(host)

# extract number at end of line and make float
text = "X-DSPAM-Confidence:    0.8475"
new_text = text.replace(' ', '')
print(new_text)
spos = new_text.find(':')
print(spos)
print(float(new_text[spos+1:]))






