from jinja2 import Environment, FileSystemLoader, select_autoescape
from http.server import HTTPServer, SimpleHTTPRequestHandler
import datetime


since_year = 1920
current_year = datetime.datetime.now().year
company_age = current_year - since_year

wine_elements = [
    {
        "name": "Изабелла",
        "sort": "Изабелла",
        "price": 350,
        "image_src":"images/izabella.png"
    },
    {
        "name": "Гранатовый браслет",
        "sort": "Мускат розовый",
        "price": 350,
        "image_src":"images/granatovyi_braslet.png"
    },
    {
        "name": "Шардоне",
        "sort": "Шардоне",
        "price": 350,
        "image_src":"images/shardone.png"
    },
    {
        "name": "Белая леди",
        "sort": "Дамский пальчик",
        "price": 399,
        "image_src":"images/belaya_ledi.png"
    },
    {
        "name": "Ркацители",
        "sort": "Ркацители",
        "price": 499,
        "image_src":"images/rkaciteli.png"
    },
    {
        "name": "Хванчкара",
        "sort": "Александраули",
        "price": 550,
        "image_src":"images/hvanchkara.png"
    }
]

env = Environment(
    loader=FileSystemLoader('.'),
    autoescape=select_autoescape(['html', 'xml'])
)
template = env.get_template('template.html')
rendered_page = template.render(
    company_age=company_age,
    wines=wine_elements
)

with open('index.html', 'w', encoding="utf8") as file:
    file.write(rendered_page)


server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
server.serve_forever()