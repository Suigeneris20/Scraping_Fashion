import pandas as pd
from bs4 import BeautifulSoup as bs
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://harvestandmill.com/collections/menshop')

content = driver.page_source
soup = bs(content, 'html.parser')
results = []
for element in soup.findAll(attrs={'class':'product-details'}):
    link = element.find('a')
    link = link.attrs['href']
    results.append(f'https://harvestandmill.com{link}')

for elem in results: print(elem)
