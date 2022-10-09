
import requests
from bs4 import BeautifulSoup

x = 0
print('Сколько нужно страниц?')
a = int(input())
for i in range(0,a):

    url = 'https://news.ycombinator.com/news?p=' + str(i)
    request = requests.get(url)
    soup = BeautifulSoup(request.text, 'html.parser')


    theme = soup.find_all('td', class_='title')
    for themes in theme:
        themes = themes.find('a')
        if themes is not None :
            link = themes.get('href')
            print(str(themes.text) + '\n' + str(link))
            print('====')
