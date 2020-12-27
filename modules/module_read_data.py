import csv
import os.path

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager

from modules.module_helper import format_link


def read_deck(file_name: str):
    cards = []
    file_reader = open(file_name, 'r')
    for line in file_reader:
        last_symbol = line[-1:]
        if last_symbol == '\n':
            line = line[:-1]
        cards.append(line.lower())

    return cards


def get_forbidden_cards(link: str, update: bool):
    cards_not_fetched = True
    error_fetching = False
    file_exists = os.path.isfile(format_link(link) + '.csv')

    entries = []

    if not file_exists or update:
        try:
            options = Options()
            options.headless = True
            driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=options)

            driver.get(link)

            forbidden_cards = driver.find_element_by_tag_name('table')
            forbidden_cards_tr = forbidden_cards.find_elements_by_css_selector('tr')

            for elem in forbidden_cards_tr:
                card_information = []
                line_skipped = False
                for cell in elem.find_elements_by_tag_name('td'):
                    cell_text = cell.text
                    if cell_text == 'Kartentyp' or cell_text == 'Card Type':
                        line_skipped = True
                        break
                    if cell_text == 'Link':
                        cell_text = cell.find_element_by_tag_name('a').get_attribute('href')

                    card_information.append(cell_text)
                if line_skipped:
                    continue
                all_empty = card_information.count(card_information[0]) == len(card_information)
                if all_empty:
                    continue

                entries.append(
                    {'type': card_information[0], 'name': card_information[1].lower(), 'advanced': card_information[2],
                     'traditional': card_information[3], 'comment': card_information[4],
                     'link': card_information[5]})

            write_dict(entries, format_link(link) + '.csv')
            cards_not_fetched = False
            print('Downloaded entries from ' + link + ' .\nSaved in ' + format_link(link) + '.csv .')

        except Exception:
            error_fetching = True

    if cards_not_fetched or error_fetching:
        if not file_exists:
            print('Something went wrong with downloading the cards and not old list does exists.',
                  'Maybe just try again.\n')
        else:
            with open(format_link(link) + '.csv', 'r') as csv_file:
                reader = csv.DictReader(csv_file, delimiter=',')
                for line in reader:
                    entries.append(line)

    if len(entries) == 0:
        return None
    return entries


def write_dict(cards_list: list, file_name: str):
    csv_columns = list(cards_list[0].keys())
    with open(file_name, 'w+') as csv_file:
        writer = csv.DictWriter(csv_file, csv_columns)
        writer.writeheader()
        for card in cards_list:
            writer.writerow(card)
