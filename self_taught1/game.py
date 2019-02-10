import random
class Player:
    def __init__(self, name):
        self.name = name
        self.gold = 0
        self.health = 100

class Monster:
    def __init__(self):
        self.attack = 25

class Barley:
    def __init__(self):
        self.extra_health = 30

class Game:
    def __init__(self):
        pass
    def first_aid(self, player):
        if player.gold < 50:
            print("you dont have enough gold to buy health")
        else:
            player.health += 25
            player.gold -= 50
            print(player.health)
    def attacked(self, player):
        n = random.randint(0, 3)
        if n == 3:
            print("you are getting attacked by a monster")
            monster = Monster()
            player.health -= monster.attack
            print("your players health is {}".format(player.health))
    def gold(self, player):
        r = random.randint(0, 1)
        if r % 2 == 0:
            gold = random.randint(0, 100)
            player.gold += gold
            print(("you found {} pieces of gold".format(gold)))
        else:
            lost_gold = random.randint(0, 25)
            player.gold -= lost_gold
            print("you lost {} pieces of gold".format(lost_gold))
        print("you have {} pieces of gold".format(player.gold))

    def play_game(self):
        name = input("What is your name?\n")
        player = Player(name)
        print("welcome to the game {}".format(player.name))
        turn = None
        while True and turn != "q":
            turn = input("press any key to continue press a to buy first aid kit or q to quit\n")
            if turn == "a":
                self.first_aid(player)
            self.gold(player)
            self.attacked(player)
            n = random.randint(0,3)
            if n == 2:
                barley = Barley()
                print("you found barley")
                player.health += barley.extra_health
                print("your health increased by {} and is not {}".format(barley.extra_health, player.health))


            if player.health <= 0:
                print("Game Over, player died")

game = Game()
game.play_game()
