from jinja2 import Environment, FileSystemLoader, select_autoescape
from http.server import HTTPServer, SimpleHTTPRequestHandler
from text_parser import get_wine_by_categories
import datetime


since_year = 1920
current_year = datetime.datetime.now().year
company_age = current_year - since_year
wine_by_categories = get_wine_by_categories()

env = Environment(
    loader=FileSystemLoader("."), autoescape=select_autoescape(["html", "xml"])
)
template = env.get_template("template.html")
rendered_page = template.render(
    company_age=company_age, wine_categories=wine_by_categories
)

with open("index.html", "w", encoding="utf8") as file:
    file.write(rendered_page)


server = HTTPServer(("0.0.0.0", 8000), SimpleHTTPRequestHandler)
server.serve_forever()
