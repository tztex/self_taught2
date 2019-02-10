known_users = ["Alice", "Bob", "Tom", "Nance"]
while True:
    print("Hi my name is Travis")
    name = input("what is your name? \n").strip().capitalize()
    if name in known_users:
        print("hello {}".format(name))
        remove = input("would you like to be removed? y/n").strip().lower()
        if remove == "y":
            print(known_users)
            known_users.remove(name)
            print(known_users)
        elif remove == "n":
            print("no worries")

    else:
        print("Hmmm I don't think I have met you yet {}".format(name))
        add_me = input("Would you like to be added y/n? ").strip().lower()
        if add_me == "y":
            known_users.append(name)
        elif add_me == "n":
            print("great you are added")
