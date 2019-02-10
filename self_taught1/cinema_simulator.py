films = {
    "Finding Dory":[3,5],
    "Bourne": [18,5],
    "Tarzan":[15,2],
    "Ghost Busteres": [12,5]
}
while True:
    choice = input("what film would you like to watch? ").strip().title()

    if choice in films:
        age = int(input("How old are you? ").strip())
        if age >= films[choice][0]:
            if films[choice][1] > 0:
                print("enjoy the film")
                films[choice][1] = films[choice][1] - 1
            else:
                print("we are sold out")
        else:
            print("You are too young")
    else:
        print("we don't have that film...")
