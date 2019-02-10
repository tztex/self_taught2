from random import shuffle
#define classes for A card, A deck, A player and The game

class Card:
    suits = ["spades", "hearts", "diamonds", "clubs"]  #class variable

    values = [None, None, "2", "3", "4", "5", "6", "7", "8",
              "9", "10", "Jack", "Queen", "King", "Ace"] #class variable, None allows index=card

    def __init__(self, v, s): #card object with two values
        """suit + value are ints"""
        self.value = v
        self.suit = s

    def __lt__(self, c2): #magic method to compare 2 card objects in expression
        if self.value < c2.value:
            return True
        if self.value == c2.value:
            if self.suit < c2.suit:
                return True
            else:
                return False
        return False

    def __gt__(self, c2): #magic method to compare 2 card objects
        if self.value > c2.value:
            return True
        if self.value == c2.value:
            if self.suit > c2.suit:
                return True
            else:
                return False
        return False

    def __repr__(self): #magic method to look up cards value and returns them so you can print card
        v = self.values[self.value] + " of " + self.suits[self.suit]
        return v
#test code
card1 = Card(12,3) #calls magig method lt on the card1 object passes card 2 as parameter
card2 = Card(11,4)
card3 = Card(12,3)
print(card3 < card1)
print(card1)

class Player: #represents each player 3 instance varibales
    def __init__(self, name):
        self.wins = 0
        self.card = None
        self.name = name


class Deck: #when you initianlize the Deck object code creates card objects representing all cards
    def __init__(self):
        self.cards = []
        for i in range(2, 15): #starts at 2 and ends at ace 2-14(15-1)
            for j in range(4): #each time thru outer loop is value and inner loop in suit
                self.cards.append(Card(i, j)) #appends object with new instances in method
        shuffle(self.cards)

    def rm_card(self):
        if len(self.cards) == 0:
            return
        return self.cards.pop()
deck = Deck()
for card in deck.cards:
    print(card)

class Game:
    def __init__(self):
        name1 = input("p1 name ") #collect player names and save in instance variables
        name2 = input("p2 name ")
        self.deck = Deck() #create new deck object
        self.p1 = Player(name1) #create new player objects
        self.p2 = Player(name2)

    def wins(self, winner): #prints whoever won that round
        w = "{} wins this round"
        w = w.format(winner)
        print(w)

    def draw(self, p1n, p1c, p2n, p2c): #takes name and card and prints card they drew
        d = "{} drew {} {} drew {}"
        d = d.format(p1n, p1c, p2n, p2c)
        print(d)

    def play_game(self): #starts game
        cards = self.deck.cards
        print("beginning War!")
        while len(cards) >= 2: #continues while there are 2 or more cards in deck
            m = "q to quit. Any " + "key to play:"
            response = input(m)
            if response == 'q':
                break
            p1c = self.deck.rm_card()  #each time through the loop 2 cards 1 for each player
            p2c = self.deck.rm_card()
            p1n = self.p1.name
            p2n = self.p2.name
            self.draw(p1n, p1c, p2n, p2c)
            if p1c > p2c:
                self.p1.wins += 1 #increment wins instance variable based on who won
                self.wins(self.p1.name)
            else:
                self.p2.wins += 1
                self.wins(self.p2.name)

        win = self.winner(self.p1, self.p2)  #when deck runs out of cards user winner method to see
                                                # who won game

        print("War is over.{} wins".format(win))

    def winner(self, p1, p2):
        if p1.wins > p2.wins:
            return p1.name
        if p1.wins < p2.wins:
            return p2.name
        return "It was a tie!"


game = Game()
game.play_game()