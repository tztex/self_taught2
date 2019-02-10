import csv
my_list = [["Top Gun", "Risky Business", "Minority Report"],
           ["Titanic", "The Revenant", "Inception"],
           ["Training Day", "Man on Fire", "Flight"]]
with open("movies.csv","w") as f:
    write = csv.writer(f)
    for movies in my_list:
        write.writerow(movies)

#create new csv file
#with opens file and call writer method and pass it the file object "f" along wtih
#delimeter
with open("st.csv", "w", newline='') as f:
    write = csv.writer(f, delimiter=",")
    write.writerow(["one",
                    "two",
                    "three"])
    write.writerow(["four",
                    "five",
                    "six"])

#new practice creating tomcsv.csv
with open("tom2.csv", "w", newline="") as f:
    write = csv.writer(f,delimiter=",")
    write.writerow([1,
                    2,
                    3])
#read contents of file
#pass r to open for reading
#call reader method and returns iterable
#each time around loop you add a coma to print data as it appears in original file
with open("movies.csv", "r") as f:
    r = csv.reader(f, delimiter=",")
    for row in r:
        print(",".join(row))
#practice open
with open("tom2.csv", "r") as f:
    r = csv.reader(f, delimiter=",")
    for row in r:
        print(",".join(row))

