from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

driver = webdriver.Chrome()
drzave = []
cene = []
driver.get('https://www.worldeconomics.com/Indicator-Data/Inequality/Inequality-Index.aspx')

content = driver.page_source
soup = BeautifulSoup(content, features="html.parser")
for element in soup.findAll('tr', attrs={'class': 'trRegular'}):
    model = element.find('td', attrs={'class': 'tb1'})
    price = element.find('td', attrs={'class': 'tb5'})
    drzave.append(model.text)
    cene.append(price.text)

df = pd.DataFrame({'Drzava': drzave, 'Index': cene})
df.to_csv('EqualityIndex.csv', index=False, encoding='utf-8')
