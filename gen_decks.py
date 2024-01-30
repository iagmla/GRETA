from os import urandom

def gen_card_deck() -> tuple[list, list]:
    half_deck_red = []
    half_deck_black = []
    while len(half_deck_red) < 26:
        num = ord(urandom(1))
        if (((num >= 0) and (num <= 25)) and
            num not in half_deck_red):
                half_deck_red.append(num)
    while len(half_deck_black) < 26:
        num = ord(urandom(1))
        if (((num >= 0) and (num <= 25)) and
            num not in half_deck_black):
                half_deck_black.append(num)
    return (half_deck_red, half_deck_black)
