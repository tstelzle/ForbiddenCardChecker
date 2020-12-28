import sys

from api.modules.module_check import check_forbidden_cards
from api.modules.module_helper import print_list
from api.modules.module_read_data import read_deck, get_forbidden_cards


def main():
    link_german = "https://img.yugioh-card.com/de/gameplay/detail.php?id=1166"
    link_english = "https://img.yugioh-card.com/oc/gameplay/detail.php?id=1155"
    update = False
    if len(sys.argv) < 2:
        print('Not enough input.')
        return
    else:
        if len(sys.argv) == 3:
            if sys.argv[2] == '-u':
                update = True
        deck_file = sys.argv[1]

    forbidden_cards_german = get_forbidden_cards(link_german, update, False)
    forbidden_cards_english = get_forbidden_cards(link_english, update, False)
    deck_cards = read_deck(deck_file)

    forbidden_deck_german = check_forbidden_cards(forbidden_cards_german, deck_cards)
    forbidden_deck_english = check_forbidden_cards(forbidden_cards_english, deck_cards)

    print('Verbotene Karten in deinem Deck:')
    print_list(forbidden_deck_german[0])
    print('\nVerbotene Karten in deinem Deck (Typo):')
    print_list(forbidden_deck_german[1])
    print('\nForbidden Cards in your deck:')
    print_list(forbidden_deck_english[0])
    print('\nForbidden Cards in your deck (Typo):')
    print_list(forbidden_deck_english[1])


if __name__ == '__main__':
    main()
