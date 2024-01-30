from greta import GRETA
from gen_decks import gen_card_deck
from sys import argv

deckA = [2, 17, 15, 10, 0, 5, 23, 6, 16, 9, 7, 20, 3, 8, 4, 24, 11, 22, 18, 14, 19, 13, 25, 21, 1, 12]
deckB = [3, 13, 16, 25, 24, 8, 20, 11, 15, 0, 19, 6, 21, 5, 2, 7, 18, 12, 10, 17, 1, 4, 9, 22, 23, 14]

mode = argv[1]
infile = argv[2]
outfile = argv[3]
if mode == "-e":
    f = open(infile, "r")
    msg = f.read()
    f.close()
    g = GRETA(sub_rotor=list(deckA), control_rotor=list(deckB))
    ctxt = g.encrypt(msg)
    f = open(outfile, "w")
    f.write(ctxt)
    f.close
elif mode == "-d":
    f = open(infile, "r")
    ctxt = f.read()
    f.close()
    g = GRETA(sub_rotor=list(deckA), control_rotor=list(deckB))
    ptxt = g.decrypt(ctxt)
    f = open(outfile, "w")
    f.write(ptxt)
    f.close
