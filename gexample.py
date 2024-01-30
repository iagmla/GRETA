from greta import GRETA
from gen_decks import gen_card_deck

msg = "HELLOMYNAMEISGRETAANDIAMANENCRYPTIONALGORITHMSUITABLEFORPLAYINGCARDS"
decks = gen_card_deck()
deckA = decks[0]
deckB = decks[1]

g = GRETA(sub_rotor=list(deckA), control_rotor=list(deckB))
ctxt = g.encrypt(msg)
print(ctxt)
g = GRETA(sub_rotor=list(deckA), control_rotor=list(deckB))
ptxt = g.decrypt(ctxt)
print(ptxt)
