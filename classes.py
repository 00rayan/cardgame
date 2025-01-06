# This file contains the animal card class.

# A template for an animal card.
class Animal:
    def __init__(self, name, attack, defense, cost, element):
        self.name = name
        self.attack = attack
        self.defense = defense
        self.cost = cost
        self.element = element # Can be earth, water or air.

class Player:
    def __init__(self, name):
        name = name
        self.hp = 5
        self.front_deck = [] * 4
        self.back_deck = [] * 4
        self.hand = []

class Game:
    def __init__(self):
        self.deck = []  # Main deck
        self.bunny_deck = []  # Bunny-only deck
        self.players = [Player("Player 1"), Player("Player 2")]
        self.turn = 0  # Track whose turn it is
        self.time_limit = 30  # Seconds per turn