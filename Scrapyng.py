import requests
from bs4 import BeautifulSoup
import re 
import pandas as pd 
import match

url = 'https://www.cnnbrasil.com.br/tecnologia/'
noticias =  []
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'}
r= requests.get (url, headers=headers)
soup = BeautifulSoup(r.content, 'html.parser')
body = soup.find_all('div', class_=re.compile("home__list__tag"))


print(body)