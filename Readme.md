# Yu-Gi-Oh Forbidden Card Checker

## Idea
This script shall help you with checking if card in your deck is forbidden.

This tool will check for german and english cards.

## Starting the script
You will need to install the python dependencies.
Do this with running the following command.

```bash
pip install -r requirements.txt
```

To run the script you will have to make a '.txt' file with the cards of your deck. Each card shoudl be in a separate line. 
Watch out for typing errors, as the script will otherwise not be able to check the card.

This file name needs to be your first parameter to the script.
If the file is not in the same directory as the script please obviously put in the whole path.

The second paramater is conditionally. As the script will always save the forbidden cards into a '.csv' file it will not download the cards if this file exits.
Witht setting '-u' as second parameter you will force it to update the forbidden cards.

## Examples
```bash
python3 script.py aqua_deck.txt 
```
```bash
python3 script.py main_deck.txt -u
```
