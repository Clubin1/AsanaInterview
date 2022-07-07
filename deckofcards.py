import enum
from unittest import suite
from abc import ABC, abstractmethod

class Suite(enum):
    CLUB, SPADES, HEARTS, DIAMOND = 1, 2, 3, 4

class Card:
    def __init__(self, suite, value):
        self.suite = suite
        self.value = value

    def adjustValue(self):
        if self.value > 10:
            return 10
        return self.value

    def getValue(self):
        return self.value
    
    def getSuite(self):
        return self.suite
    
class Deck:
    def __init__(self):
        self.cards = []
        self.__buildDeck()
        self.shuffleDeck() 
    
    def buildDeck(self):
        pass

    def shuffle(self):
        pass

    def hitDeck(self):
        pass

class Player(ABC):
    def __init__(self, id):
        self.id = id
        self.cards = []
        self.countAces = 0

    def getTotal(self):
        pass

    def addCard(self, card):
        if card.getActualValue() == 1:
            self.countAces += 1
        self.cards.append(card)

class Dealer(Player):
    def __init__(self):
        super().__init__(id)

class BlackJackPlayer(Player):
    def __init__(self):
        super().__init__(id)

class Game:
    def __init__(self):
        self.deck = Deck()
        self.dealer = Dealer(0)
        self.player = BlackJackPlayer(1)

        def play(self):
            pass
            
        def getWinner(self):
            pass
