# This is the main file.
import random
import pygame
from pathlib import Path
from animal_card import animal
from decks import full_deck
from decks import fd_assets

# Core game variables
player1_hp = 5 # Set up players HP and deck 
player2_hp = 5
player1_hand = [[],[]]
player2_hand = [[],[]]
p2_row1 = [['','','',''],[]] # Table of placed cards, arrays ordered top to bottom as if on screen, array[1] is for the positions of each of the cards
p2_row2 = [['','','',''],[]]
p1_row2 = [['','','',''],[]]
p2_row1 = [['','','',''],[]]
won = False # Boolean that ends the game when true.

# Procedure for each turn
def player_turn(player_hp, player_hand,p_id):
    over = False
    while not over:
        print(f"Player {p_id} turn.")
        print(f"HP: {player_hp}")
        print(f"Your hand:")
        for index in range(0,len(player_hand)):
            card = player_hand[index]
            # Find card position.
            card_pos = 0
            for search in range(0,len(full_deck)-1): # Search for card in array
                if full_deck[index] == card:
                    card_pos = search
                    break # Exit loop
            print(card)
            card_name = fd_assets[card_pos]
            card_image = pygame.image.load(f'./assets/cards_original/{card_name}.png').convert_alpha() # Get asset name and filepath
            card_image = pygame.transform.scale(card_image, (78,123))
            card_rect = card_image.get_rect()
            screen.fill(white)
            screen.blit(background, bg_rect)
            screen.blit(card_image, card_rect)
            pygame.display.flip()
        confirmation = input("Press ENTER to continue... ")
    return player_hp, player_hand, p_id
# Game start
def game_start(d):
    # Deck
    deck = d
    print(f"There are {len(deck)} cards left in the deck")
    
    # Give players cards
    player1_hand[0].append(animal('rabbit',0,1,0,'earth'))
    player2_hand[0].append(animal('rabbit',0,1,0,'earth'))
    for index in range (3):
        # Give player 1 card
        card_pos = random.randint(0,len(deck)-1)
        card = deck[card_pos]
        card_name = fd_assets[card_pos]
        deck.pop(card_pos)
        player1_hand[0].append(card)
        card = pygame.image.load(f'./assets/cards_original/{card_name}.png').convert_alpha()
        # Give player 2 card
        card_pos = random.randint(0,len(deck)-1)
        card = deck[card_pos]
        card_name = fd_assets[card_pos]
        deck.pop(card_pos)
        player2_hand[0].append(card)
    print(f"There are {len(deck)} cards left in the deck")
# Main procedure for the game
def game_loop(p1hp,p2hp,p1hand,p2hand,d):
    # Ran on human player turn 
    player_turn(p1hp,p1hand,'1')
    # Ran on player 2 turn
    player_turn(p2hp,p2hand,'2')
# Pygame setup
pygame.init()
white = 255, 255, 255
resolution = width, height = 450, 800
screen = pygame.display.set_mode((resolution))
background = pygame.image.load('./assets/backgrounds/bg1_scaled.png').convert()
bg_rect = background.get_rect()
running = True  
game_start(full_deck) # Start game
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    game_loop(player1_hp,player2_hp,player1_hand,player2_hand,full_deck)
