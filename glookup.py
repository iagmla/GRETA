def convert_to_card(lookup, deck):
    rtn_deck = []
    for x in range(26):
        card = lookup[deck[x]]
        rtn_deck.append(card)
        print(card, end=' ')
    return rtn_deck


red = ["AH", "2H", "3H", "4H", "5H", "6H", "7H", "8H", "9H", "10H", "JH", "QH", "KH", "AD", "2D", "3D", "4D", "5D", "6D", "7D", "8D", "9D", "10D", "JD", "QD", "KD"]
black = ["AC", "2C", "3C", "4C", "5C", "6C", "7C", "8C", "9C", "10C", "JC", "QC", "KC", "AS", "2S", "3S", "4S", "5S", "6S", "7S", "8S", "9S", "10S", "JS", "QS", "KS"]
#deckA = [2, 17, 15, 10, 0, 5, 23, 6, 16, 9, 7, 20, 3, 8, 4, 24, 11, 22, 18, 14, 19, 13, 25, 21, 1, 12]
#deckB = [3, 13, 16, 25, 24, 8, 20, 11, 15, 0, 19, 6, 21, 5, 2, 7, 18, 12, 10, 17, 1, 4, 9, 22, 23, 14]
deckA = [10, 0, 5, 23, 6, 16, 9, 7, 20, 3, 8, 4, 24, 11, 22, 18, 14, 19, 13, 25, 21, 1, 12, 2, 17, 15]
deckB = [16, 25, 24, 8, 20, 11, 15, 0, 19, 6, 21, 5, 2, 7, 18, 12, 10, 17, 1, 4, 9, 22, 23, 14, 3, 13]
deck_black = convert_to_card(black, deckA)
print(deck_black)
deck_red = convert_to_card(red, deckB)
print(deck_red)
