import requests
from bs4 import BeautifulSoup

#requests
url = 'http://www.columbia.edu/~fdc/sample.html'
response = requests.get(url)

#bs4
page = BeautifulSoup(response.text, 'html.parser')

a = page.title
texto = a.text.split(' ')[1].upper()
texto