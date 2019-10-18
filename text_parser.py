import re
from collections import namedtuple


class Empty:
    def __iter__(self):
        return self

    def __next__(self):
        return ""


default_textfile = "./wine.txt"
wine = namedtuple("Wine", ["name", "sort", "price", "image"])
group = namedtuple("Group", ["title", "items"])
patterns = {
    "title": re.compile("(?<=# ).+"),
    "fragment": re.compile("(?<=# )[а-яА-Яa-zA-Z0-9\n :\/_.]+"),
    "name": re.compile("(?<=Название: ).+"),
    "sort": re.compile("(?<=Сорт: ).+"),
    "price": re.compile("(?<=Цена: ).+"),
    "image": re.compile("(?<=Картинка: ).+"),
}


def get_file_data(filename):
    if filename:
        with open(filename, "r", encoding="utf-8") as file:
            return file.read()


def get_wine_items_from_text(text, mock=Empty()):
    names = re.findall(patterns["name"], text) or mock
    sorts = re.findall(patterns["sort"], text) or mock
    prices = re.findall(patterns["price"], text) or mock
    images = re.findall(patterns["image"], text) or mock
    return list(map(lambda tup: wine(*tup), zip(names, sorts, prices, images)))


def get_wine_groups_from_text(
    text=get_file_data(default_textfile), patterns=patterns
):
    group_items = []
    titles = re.findall(patterns["title"], text)
    fragments = re.findall(patterns["fragment"], text)
    for fragment in fragments:
        wine_items = get_wine_items_from_text(fragment)
        group_items.append(wine_items)
    wine_groups = list(map(lambda tup: group(*tup), zip(titles, group_items)))
    return wine_groups


if __name__ == "__main__":
    print(get_ntuple_from_text())
