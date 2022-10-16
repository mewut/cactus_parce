import requests
from requests import get
from bs4 import BeautifulSoup
import time
import random

url = 'https://darvin-market.ru/catalog/rasteniya/komnatnye_rasteniya/zasukhoustoychivye/'

cactus = []
count = 1

while count <= 5:
    url = 'https://darvin-market.ru/catalog/rasteniya/komnatnye_rasteniya/zasukhoustoychivye/?PAGEN_2=' + str(count)
    print(url)
    response = get(url)
    html_soup = BeautifulSoup(response.text, 'html.parser')

    cactus_data = html_soup.findAll('div', class_='items-cells')
    if cactus_data:
        cactus.extend(cactus_data)
        value = random.random()
        scaled_value = 1 + (value * (9 - 5))     # рандомная задержка для обращений на сайт
        print(scaled_value)
        time.sleep(scaled_value)
    else:
        print('Все')
        break
    count += 1

print(len(cactus))
print(cactus[1])
print()

n = int(len(cactus)) - 1
count = 0
while count <= n:
    info = cactus[int(count)]
    price = info.find('strong', {'class': 'new-price'}).text
    title = info.find('div', {'class': 'name'}).text
    print(title, ' ', price)
    count += 1
