# This file contains the animal card class.
from dataclasses import dataclass
from pygame_cards.abstract import AbstractCard
from pygame_cards.set import CardsSet
@dataclass
# A template for an animal card.
class animal(AbstractCard):
    ATK: int
    DEF: int
    COST: int
    ELEMENT: str = "" # Can be earth, water or air.
