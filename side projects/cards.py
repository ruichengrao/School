#importing random
import random

#empty list for the deck of cards
deckOfcards = []

#list of the parts of the deck of cards
suits = ["Clubs","Diamonds","Heart", "Spades"]
ranks = ["2","3","4","5","6","7","8","9","10","Jack", "Queen", "King", "Ace"]

#class constructor
class Cards:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return "{} of {}".format(self.rank, self.suit)
        
#loop through the list of the parts creating the deck of cards
for x in suits:
    for y in ranks:
        deckOfcards.append(Cards(x,y))

#randomize everytime you press enter
randomize = input("Press Enter to Draw")

#shuffling the deck of cards
random.shuffle(deckOfcards)

#drawing the cards
while randomize == "":
#if the deck is empty then it stops the program
    if len(deckOfcards) == 0:
        print("Out of Cards")
        break
    print(deckOfcards.pop())
    randomize = input("Press Enter to Draw")
    
    