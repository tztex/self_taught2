#remaining letters is list containing each character in variable word keeps
#track of remaining letters
#board is list of strings to keep track of game board
#win keeps tracks if player 2 won game
# print welcome to start off the game
# next part is loop that keeps game going as long is wrong variable is less than
# stages list - 1. subtract one cause stages starts at 0 and wrong at 1
#stages list starts at 0 and wrong starts at 1
#game continues until player 2 guesses more wrong letters than letters to complete
# hangman
#once inside loop print a blank line to make it look nice
#collect player guess and save in variable char. check if player 2 guessed
# correctly by looking at remaining letters and then update the board list.
#index function returns first occurrent of an index in a list to update board
# you use index function to
#find first occurrence of letter in remaining letters and replace underscore with
# letter they guessed
#replace letter guessed with a $
#if player 2 misses guess you increment wrong by one
#call the join method on a blank space"" and pass it variable board. this prints
# board so player 2 can see it
#to print the game you have to slice your stages list start at 0 and slice up to
# stage you are at
#represented by wrong +1 add one the end slice doesnt get included. 0 to integer
# +1 gives integers to print
#check if they are anymore underscores print "you win" set win to true and break
# out of loop
#if lose win is false. print hangman and word they couldnt guess

def hangman(word):
    wrong = 0 # wrong keeps track of incorrect guesses
    stages = ["",
             "________        ",
             "|               ",
             "|        |      ",
             "|        0      ",
             "|       /|\     ",
             "|       / \     ",
             "|               "
              ]
    rletters = list(word) #track remaining letters
    board = ["__"] * len(word) #list of strings to keep track of game board is 3
    win = False
    print("Welcome to Hangman")
    while wrong < len(stages - 1): #starts at 0 < 8-1
        print("\n")
        msg = "Guess a letter"
        char = input(msg) #char is the letter guessed
        if char in rletters:
            cind = rletters.index(char) #if guess c the index is 1
            board[cind] = char #replace underscore in board list with letter
            rletters[cind] = '$' #replace guess with $ "$" "a" "t"
        else:
            wrong += 1
            print((" ".join(board)))
        e = wrong + 1 #0 + 1
        print("\n".join(stages[0: e])) #slice stages list to print hangman first 0 + 1
        if "__" not in board:
            print("You win!")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n"
              .join(stages[0: wrong]))
        print("You lose! It was {}.".format(word))

hangman("cat")