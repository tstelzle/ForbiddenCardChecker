from flask import Flask
from flask_restful import Api, Resource
import json

from modules.module_check import check_forbidden_cards
from modules.module_read_data import get_forbidden_cards

app = Flask(__name__)
api = Api(app)


class ForbiddenCard(Resource):

    def get(self, names: str):
        link_german = "https://img.yugioh-card.com/de/gameplay/detail.php?id=1166"
        link_english = "https://img.yugioh-card.com/oc/gameplay/detail.php?id=1155"

        forbidden_cards_german = get_forbidden_cards(link_german, False)
        forbidden_cards_english = get_forbidden_cards(link_english, False)

        deck_cards = [card.lower() for card in names.split(';')]

        forbidden_deck_german = check_forbidden_cards(forbidden_cards_german, deck_cards)
        forbidden_deck_english = check_forbidden_cards(forbidden_cards_english, deck_cards)

        forbidden_cards = forbidden_deck_german[0] + forbidden_deck_english[0]
        typo_forbidden_cards = forbidden_deck_german[1] + forbidden_deck_english[1]

        return json.dumps([forbidden_cards, typo_forbidden_cards]), 200


api.add_resource(ForbiddenCard, "/forbiddenCard/<string:names>")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
