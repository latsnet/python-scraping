from urllib.request import urlopen
from bs4 import BeautifulSoup

def trata_html(input):
    return ' '.join(input.decode('utf-8').split()).replace("> <", "><")

url = "https://alura-site-scraping.herokuapp.com/index.php"

response = urlopen(url)
html = trata_html(response.read())

soup = BeautifulSoup(html, 'html.parser')

print(soup.img.attrs.keys())
print(soup.img.attrs.values())

print(soup.img['src'])
print(soup.img.get('src'))
print(soup.img.attrs['src'])

print(soup.findAll('img', limit = 2))

print(soup.findAll('p', {"class": "txt-value"}))

print(soup.findAll('p', text = "Belo Horizonte - MG"))

print(soup.findAll('img', alt = "Foto"))

for item in soup.findAll('img', alt = "Foto"):
    print(item.get('src'))

print(soup.findAll('p', class_= "txt-value"))
