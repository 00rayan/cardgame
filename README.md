# Documentation

This documentation breaks down every mechanic of the game.

# Cards

Each card is an object of the class animal(). The animal class contains these properties; name, ATK, DEF, COST, ELEMENT, ABILITY. They are all stored for each card. 

## Card Cost

Some cards are marked with a number of knives on the corner. This is stored as COST in animal(). The cost is the number of cards that must be sacrificed in order to play that card. Some cards eg. Rabbit are free and don't need any sacrifices (its a dogshit card anyway)

## Decks

The default full_deck[] is a 1D array which contains all of the cards as animal classes.

# Gameplay

## Game Start

As the game begins, each player gets 3 random cards from the deck and 1 rabbit. There are 2 rows each of which contain a space for 3 cards to be placed. The objective of the game is for one player to reduce the other player's HP coins to 0. Each player's hand is stored in 2D arrays player1_hand[] and player2_hand[]

## Gameplay Loop

Each player is given a time limit of 30 seconds per turn, or until they pass manually. The player will pick either a bunny or a card from the full deck. He may play as many cards as he likes, each being placed in the correct spot in p_row[0] or p_row[1] row 0 being front. If he does not play any cards he can pick another card from the deck. The cards can be placed at any spot in the front row, and cards can be placed in the back row if there is a card in front of it in the front row; this card remains hidden until the card in front dies, and then it takes it's place. In order to do damage to the opponent, a card must be placed without any cards in front of it, in which case it does 1 damage to the player for every turn it is there. However, if there is a card in front of it, that card absorbs the damage indicated on the attacking card. Damage on cards is stacked, ie. A shark with 3 ATK attacks a card with 1 HP remaining and kills it, the remaining 2 damage carry over to the card behind.



