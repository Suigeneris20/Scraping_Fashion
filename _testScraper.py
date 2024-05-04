import pandas as pd
from bs4 import BeautifulSoup as bs
from selenium import webdriver
import requests

driver = webdriver.Chrome()
driver.get('https://harvestandmill.com/collections/menshop')
content = driver.page_source

soup = bs(content, 'html.parser')
results = {}
product_detail = {}
for element in soup.find_all(attrs={'class':'product-details'}):
    
    link = element.find('a')
    link = link.attrs['href']
    results[element.find('h3').text] = f'https://harvestandmill.com{link}'

print(len(results))

for prod_name, link in results.items():
    driver = webdriver.Chrome()
    driver.get(link)
    
    item_page = driver.page_source
    driver.quit()
    item_soup = bs(item_page, 'html.parser')
    
    short_desc = item_soup.find(attrs={'class': 'product__section-details__inner product__section-details__inner--product_description'}).find('p').text
    #print(driver.current_url)
    print(short_desc)
    
    for impact in item_soup.find_all(attrs={'class': 'metric__value-box'}):
        
        print(impact.find(attrs={'class': 'metric__value'}).text)
        print(impact.find(attrs={'class': 'metric__unit'}).text)
        val=impact.find(attrs={'class': 'metric__value'}).text
        unit=impact.find(attrs={'class': 'metric__unit'}).text
        desc=impact.find(attrs={'class': 'metric__description'}).text
        sustain_impact = val+' '+unit+' '+desc
        print(sustain_impact)
    break
