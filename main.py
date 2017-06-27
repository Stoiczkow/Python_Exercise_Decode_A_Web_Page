import requests
from bs4 import BeautifulSoup

url = 'https://www.nytimes.com/'
payload = {'q': 'pawel',}
r = requests.get(url)
html = r.text


soup = BeautifulSoup(html, 'html.parser')
arts = soup.find_all(class_='story-heading')

for title in arts:
    if title.a:
        print(title.a.text.replace("\n", " ").strip())
    else:
        print(title.contents[0].strip())