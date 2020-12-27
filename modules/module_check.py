import copy

from fuzzywuzzy import fuzz


def check_forbidden_cards(given_forbidden_cards: list, deck_cards: list):
    forbidden_cards = []
    close_cards = []
    if len(given_forbidden_cards) == 0:
        return []
    for card in given_forbidden_cards:
        for deck_card in deck_cards:
            percentage = fuzz.ratio(card['name'], deck_card)
            if percentage == 100:
                forbidden_cards.append(card)
            elif percentage >= 75:
                new_card = copy.deepcopy(card)
                new_card['closest card'] = deck_card
                close_cards.append(new_card)

    return [forbidden_cards, close_cards]
