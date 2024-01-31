from greta import GRETA
from gen_decks import gen_card_deck

msg = "HELLOMYNAMEISGRETA"
deckA = [2, 17, 15, 10, 0, 5, 23, 6, 16, 9, 7, 20, 3, 8, 4, 24, 11, 22, 18, 14, 19, 13, 25, 21, 1, 12]
deckB = [3, 13, 16, 25, 24, 8, 20, 11, 15, 0, 19, 6, 21, 5, 2, 7, 18, 12, 10, 17, 1, 4, 9, 22, 23, 14]
#decks = gen_card_deck()
#deckA = decks[0]
#deckB = decks[1]
#print(deckA, deckB)

g = GRETA(sub_rotor=list(deckA), control_rotor=list(deckB))
ctxt = g.encrypt(msg)
print(ctxt)
g = GRETA(sub_rotor=list(deckA), control_rotor=list(deckB))
ptxt = g.decrypt(ctxt)
print(ptxt)
