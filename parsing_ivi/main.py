#почему-то не работает
import requests
from bs4 import BeautifulSoup

url = 'https://www.kinopoisk.ru/lists/categories/movies/3/'
response = requests.get(url)
html = response.text
soup = BeautifulSoup(html, 'html.parser')

serials_block = soup.find('div', {'class': 'catalog-grid'})

for serial in serials_block.find_all('a', {'class': ' inclined-overlay inclined-overlay_placeholder'}):
    serial_url = 'https://hd.kinopoisk.ru/ + serial['href']

response = requests.get(serial_url)
html = response.content

soup = BeautifulSoup(html, 'html.parser')

name = soup.find('h1', {'class': 'title title_size_28 title_bold_yes title_c_default'}).text.strip()
rating = soup.find('span', {'class': 'rating__value'}).text.strip()

actor_block = soup.find('div', {'class': 'actors-list__list actors-list__list_10'})

if actor_block:
        actors = [li.text.strip() for li in actor_block.find_all('li')]
else:
    actors = ['Unknown']
    
  
print('Name: ', name)
print('Rating: ', rating)
print('Actors: ', ', '.join(actors))
print('-' * 50)