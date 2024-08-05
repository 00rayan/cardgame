# Documentations

This documentation breaks down every mechanic of the game.


## Cards

Each card is an object of the class animal(). The animal class contains these properties; name, ATK, DEF, COST, ELEMENT, ABILITY. They are all stored for each card. 


## Decks

The default full deck is a 1D array which contains all of the cards as animal classes.

## Gameplay

### Game start

As the game begins, each player gets 3 random cards from the deck and 1 rabbit. There are 2 rows each of which contain a space for 3 cards to be placed. The objective of the game is for one player to reduce the other player's HP coins to 0.

### Gameplay loop
