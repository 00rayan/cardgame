# This is the main file.
import random
from pathlib import Path
from classes import *
from decks import *

# Core game variables
Player1 = Player("Player 1")
Player2 = Player("Player 2")

won = False # Boolean that ends the game when true.

# Procedure for each turn
def player_turn(current_Player, opposite_Player): # FOCUS ON THIS!
    turn_over = False
    for lane in range(0,3):
        front_card = current_Player.front_deck[lane]
        back_card = current_Player.back_deck[lane]
        opposite_front = opposite_Player.front_deck[lane]
        opposite_back = opposite_Player.back.deck[lane]

        if front_card == '' and back_card == '': # Damage player
            current_Player.hp -= 1
        else:
            front_card.hp -= opposite_front.attack # Damage card
            if front_card.hp <= 0: # Remove if card HP reaches 0
                front_card = back_card # Move back card to front.
                back_card = ''
    while not turn_over:
        player_draw = int(input("Select deck to draw from: 1. Bunny\n2. Main\n(1/2): "))
        player_action = int(input("Select action: 1. Pass\n2.Draw another card\n3.Place card\n(1/2/3): "))
    if player_action == 1 or player_action == 2:
        turn_over = True
    if player_action == 2:
        random_number = random.randint(0,len(Game.deck))
        card = Game.deck[random_number]
        Player.deck.append(card)
    elif player_action == 3:
        placed_card = int(input("Which card to place?"))
        position = int(input("Which row to place in? (1-4): ")) - 1
        if Player.front_deck[position] != '':
            if Player.back_deck[position] != '':
                print("Row full, place in another.")
            else:
                Player.back_deck

    while not turn_over:
        print(f"Player {Player.name} turn.")
        print(f"HP: {Player.hp}")
        print(f"Your hand:")
        for index in range(0,len(Player.hand)):
            card = Player.hand[index]
            # Find card position.
            card_pos = 0
            for search in range(0,len(Game.deck)-1): # Search for card in array
                if Game.deck[index] == card:
                    card_pos = search
                    break # Exit loop
            print(card)
        confirmation = input("Press ENTER to continue... ")
    return Player
# Game start
def game_start(deck): # FUNCTION FINISHED, MOVE ON!
    # Deck
    Game.deck = deck
    print(f"There are {len(Game.deck)} cards left in the deck")
    
    # Give players cards
    Player1.hand.append(Animal('rabbit',0,1,0,'earth'))
    Player2.hand.append(Animal('rabbit',0,1,0,'earth'))
    for index in range (3):
        # Give player 1 card
        card_pos = random.randint(0,len(Game.deck)-1)
        card = Game.deck[card_pos]
        Game.deck.pop(card_pos)
        Player1.hand.append(card)
        # Give player 2 card
        card_pos = random.randint(0,len(Game.deck)-1)
        card = Game.deck[card_pos]
        Game.deck.pop(card_pos)
        Player2.hand.append(card)
    print(f"There are {len(Game.deck)} cards left in the deck")
# Main procedure for the game
def game_loop():
    # Ran on human player turn 
    player_turn(Player1)
    # Ran on player 2 turn
    player_turn(Player2)
# Pygame setup

game_start(full_deck) # Start game
while True:
    game_loop()
