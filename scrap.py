from urllib.request import urlopen
from bs4 import BeautifulSoup

def trata_html(input):
    return ' '.join(input.decode('utf-8').split()).replace("> <", "><")

url = "https://alura-site-scraping.herokuapp.com/hello-world.php"

response = urlopen(url)
html = trata_html(response.read())

print(html)

soup = BeautifulSoup(html, 'html.parser')
print(soup.find('h1', {'class': 'sub-header'}).get_text())
