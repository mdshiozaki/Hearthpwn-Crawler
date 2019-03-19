from hearthstone.deckstrings import Deck
from hearthstone.enums import FormatType

# Create a deck from a deckstring
# deck = Deck()
# deck.heroes = [7]  # Garrosh Hellscream
# deck.format = FormatType.FT_WILD
# # Nonsense cards, but the deckstring doesn't validate.
# deck.cards = [(1, 3), (2, 3), (3, 3), (4, 3)]  # id, count pairs
deck = Deck.from_deckstring("AAEBAQcAAAQBAwIDAwMEAw==")
print(deck)  # "AAEBAQcAAAQBAwIDAwMEAw=="

# Import a deck from a deckstring
