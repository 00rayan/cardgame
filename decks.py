# This file contains the deck(s).
from pygame_cards.set import CardsSet
from classes import animal
# Contains the cards for the full deck.
full_deck = [animal('bat',1,2,0,'air'), # Air
     animal('cockatil',1,1,0,'air'),
     animal('ghost',1,6,2,'air'),
     animal('owl',1,3,1,'air'),
     animal('pigeon',2,1,0,'air'),
    # Earth
    animal('brownbear',6,2,2,'earth'),
    animal('capybara',3,2,1,'earth'),
    animal('cat',2,4,2,'earth'),
    animal('chicken',0,3,1,'earth'),
    animal('cow',1,2,1,'earth'),
    animal('deer',3,3,2,'earth'),
    animal('feneco',4,2,2,'earth'),
    animal('flamingo',1,1,0,'earth'),
    animal('frog',1,2,0,'earth'),
    animal('lizard',3,1,1,'earth'),
    animal('mouse',3,1,1,'earth'),
    animal('panda',1,6,2,'earth'),
    animal('peacock',1,3,1,'earth'),
    animal('pug',1,4,1,'earth'),
    animal('rabbit',0,1,0,'earth'),
    animal('redfox',3,2,1,'earth'),
    animal('redpanda',4,4,3,'earth'),
    animal('sheep',1,2,1,'earth'),
    animal('snake',1,2,2,'earth'),
    animal('unicorn',1,2,1,'earth'),
    animal('whitefox',3,2,1,'earth'),
    # Water
    animal('alligator',4,2,2,'water'),
    animal('axolotl',2,2,1,'water'),
    animal('beluga',2,6,2,'water'),
    animal('bluewhale',1,6,1,'water'),
    animal('dolphin',3,2,1,'water'),
    animal('jellyfish',6,3,3,'water'),
    animal('killerwhale',1,3,0,'water'),
    animal('mantaray',2,1,0,'water'),
    animal('narwhal',3,3,2,'water'),
    animal('octopus',6,4,3,'water'),
    animal('pinkdolphin',2,3,1,'water'),
    animal('platypus',3,3,2,'water'),
    animal('shark',3,2,1,'water'),
    animal('squid',2,2,1,'water'),
    animal('turtle',1,6,1,'water'),
    animal('whaleshark',1,3,1,'water')]

# Contains the names of the cards in the full deck. 
fd_assets = ['air_bat', 'air_cockatil', 'air_ghost', 'air_owl', 'air_pigeon', 'earth_brownbear', 'earth_capybara', 'earth_cat', 'earth_chicken', 'earth_cow', 'earth_deer', 'earth_feneco', 'earth_flamingo', 'earth_frog', 'earth_lizard', 'earth_mouse', 'earth_panda', 'earth_peacock', 'earth_pug', 'earth_rabbit', 'earth_redfox', 'earth_redpanda', 'earth_sheep', 'earth_snake', 'earth_unicorn', 'earth_whitefox', 'water_alligator', 'water_axolotl', 'water_beluga', 'water_bluewhale', 'water_dolphin', 'water_jellyfish', 'water_killerwhale', 'water_mantaray', 'water_narwhal', 'water_octopus', 'water_pinkdolphin', 'water_platypus', 'water_shark', 'water_squid', 'water_turtle', 'water_whaleshark']
