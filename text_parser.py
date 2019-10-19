import re
from collections import namedtuple


def get_text(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()


def find(pattern, text):
    res = re.search(re.compile(pattern), text)
    if res:
        return res[0]
    return None


def get_titles_and_category_blocks(text):
    arr = text.split("\n\n\n")
    titles = list(map(lambda x: x.replace("# ", ""), arr[::2]))
    cat_blocks = list(
        map(
            lambda a: a.strip(),
            arr[1::2]
        )
    )
    return titles, cat_blocks


def get_wine_blocks(category_block):
    return category_block.split("\n\n")


def get_dict_from_wine_block(wine_block):
    wine = {
        "name": find("(?<=Название: ).+", wine_block),
        "sort": find("(?<=Сорт: ).+", wine_block),
        "price": find("(?<=Цена: ).+", wine_block),
        "image": find("(?<=Картинка: ).+", wine_block),
        "discount": find("Выгодное предложение", wine_block),
    }
    return wine


def get_wine_items_from_category_block(cat_block):
    wine_blocks = get_wine_blocks(cat_block)
    wine_items = list(
        map(
            lambda a:get_dict_from_wine_block(a),
            wine_blocks
        )
    )
    return wine_items


def get_wine_by_categories(textfile="./wine.txt"):
    categorized_wine = namedtuple("wine", ["title", "items"])
    text = get_text(textfile)
    titles, cat_blocks = get_titles_and_category_blocks(text)
    wine_by_category = list(
        map(
            lambda cat: get_wine_items_from_category_block(cat),
            cat_blocks
        )
    )
    return list(
        map(
            lambda a: categorized_wine(*a),
            list(zip(titles, wine_by_category))
        )
    )
