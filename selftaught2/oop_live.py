# self represents the whole thing
# use self to give object different attributes
class Orange:
    def __init__(self):  # self represents the orange object once created
        self.color = 'orange'
        self.weight = 100
        print(self)  # prints memory location of organge object


orange = Orange()
print(orange.color)
print(orange.weight)
print(orange)  # prints memory location object lives at

# create game where you guess a number from a list of numbers
# oop because happens in a class
import random


class Game:  # instatiated a class called gameruns as soon as we create object
    def __init__(self):
        self.number = random.randint(0, 10)

    def generate_number(self):
        self.number = random.randint(0, 10)

    def play_game(self):  # called method on game
        while True:
            guess = input('Guess a number ')
            if guess == 'q':
                break
            if int(guess) == self.number:
                print('you won the number was {}'.format(self.number))
                break
            else:
                print('you got it wrong the number was {} guess again'.format(self.number))
                self.generate_number()


game = Game()  # create game object
game.play_game()  # calling method within object


# make oop that reads data and writes data to file
class DataReaderWriter():
    def __init__(self, file_name):
        self.file_name = file_name

    def write_data(self):  # method that writes data to file
        data = input("what data would you like to write")
        with open(self.file_name, 'w') as f:
            f.write(data + '\n')

    def read_data(self):  # method
        with open(self.file_name, 'r') as f:
            print(f.read())


drw = DataReaderWriter('a_file.txt')
drw.write_data()
drw.read_data()


