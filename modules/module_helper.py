def format_link(link: str):
    return link.replace('.', '-').replace('/', '_')


def print_dict(given_dict: dict):
    for key, value in given_dict.items():
        print(key, ': ', value)


def print_list(given_list: list):
    if given_list is None:
        return
    if len(given_list) == 0:
        print('No files in list.')
    for elem in given_list:
        print(elem)
