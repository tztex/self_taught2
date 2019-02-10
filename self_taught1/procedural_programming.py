# style of do this then do that
# store data in global variables and manipulate with functions
# run into issues with large programs
# ex global variable x = 150 and is one of 500 global variables
# side effects accidentally incrmenting a variable
x = 2
y = 4
z = 8
xyz = x + y + z
print(xyz)
print()

authors = []


def collect_authors():
    answer = None
    while answer != "q":
        answer = input("Who is your favorite author?")
        if answer != "q":
            authors.append(answer)
        print(authors)
collect_authors()