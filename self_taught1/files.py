import os

#use python to read or write data to a file
#every file has a file path
#if path doesnt contain folder selftaught.txt python looks in folder program running
#us path function in os module ex. os.path.join()
from typing import TextIO

print(os.path.join("Users",
                   "tmzan",
                   "Documents",
                   "excercise1.txt"))

#use open to work with files (r=read, w=write, w+=read and write)
st = open("st4.txt", "w")
st.write("hi from Python!")
st.close()

#with action performs an action automatically when python finishes executing it
#better syntax for opening files. f is variable below that represents
# the file object. could be anything
with open("st2.txt", "w") as f:
    f.write("hi from Tom")

with open("st2.txt", "r") as f:
    print(f.read())


with open("C:\\Users\\tmzan\\Documents\\excercise1.txt", "r") as g:
    print(g.read())


#write program that asks user for input and prints to a file
with open("st3.txt", "w") as f:
    f.write(input("what is your name"))

#you can only call read once each time you open it so
# you should save contents of a file to a list if you need to use later
my_list = list()

with open("C:\\Users\\tmzan\\Documents\\excercise1.txt", "r") as g:
    my_list.append(g.read())
print(my_list)

