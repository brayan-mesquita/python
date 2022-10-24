import requests
from bs4 import BeautifulSoup

#requests
url = 'https://diof.ro.gov.br/'
response = requests.get(url)

page = BeautifulSoup(response.text, 'html.parser')
title_page = page.title

links = []
for link in page.find_all('a'):
    links.append(link.get('href'))

for link in links:
    print(link)
#fazer donwload
# file = 'arquivolocal.txt'
# request.urlretrieve(file_url , file )