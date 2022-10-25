import requests
from bs4 import BeautifulSoup
from datetime import datetime

#requests
url = 'https://diof.ro.gov.br/'
response = requests.get(url)

page = BeautifulSoup(response.text, 'html.parser')
title_page = page.title

def search_all_links():
    links_a = []
    for link in page.find_all('a'):
        links_a.append(link.get('href'))
    return links_a

def search_doe(lista, word):
    links_doe = []
    for x in lista:
        if word in x:
            links_doe.append(x)
    return links_doe 

links_doe = search_doe(search_all_links(), 'pdf')
for doe in links_doe:
    print(doe[-14:-4])#DOE-24.10.2022

#fazer donwload


#data_e_hora_atuais = datetime.now()
#data_e_hora_atuais = data_e_hora_atuais.strftime('%d/%m/%Y %H:%M')
links_com_pdf = [valor for valor in links_doe if 'pdf'  in valor ]