import re
from collections import namedtuple


def get_text_from_textfile(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()


def find(pattern, text):
    res = re.search(re.compile(pattern), text)
    if res:
        return res[0]
    return None


def get_titles_and_category_blocks(text):
    arr = text.split("\n\n\n")
    titles = [x.replace("# ", "") for x in arr[::2]]
    cat_blocks = [a.strip() for a in arr[1::2]]
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
    wine_items = [get_dict_from_wine_block(a) for a in wine_blocks]
    return wine_items


def get_wine_by_categories(file_path="./wine.txt"):
    categorized_wine = namedtuple("wine", ["title", "items"])
    text = get_text_from_textfile(file_path)
    titles, cat_blocks = get_titles_and_category_blocks(text)
    wine_by_category = [
        get_wine_items_from_category_block(cat_block)
        for cat_block in cat_blocks
    ]
    return [categorized_wine(*a) for a in zip(titles, wine_by_category)]
