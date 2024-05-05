import pandas as pd
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver import ChromeOptions
import requests
from _imageProcess import image_harvester

def page_content(url):
    option = ChromeOptions()
    option.add_argument("--headless=new")
    driver = webdriver.Chrome(options=option)
    driver.get(url)
    content = driver.page_source
    print(driver.current_url)
    driver.quit()
    return content


content = page_content('https://harvestandmill.com/collections/menshop')
soup = bs(content, 'html.parser')
results = {}
product_detail = {}

for element in soup.find_all(attrs={'class':'product-details'}):    
    link = element.find('a')
    link = link.attrs['href']
    results[element.find('h3').text] = f'https://harvestandmill.com{link}'


for prod_name, link in results.items():
    item_page = page_content(link)
    item_soup = bs(item_page, 'html.parser')
    
    short_desc = item_soup.find(attrs={'class': 'product__section-details__inner product__section-details__inner--product_description'}).find('p').text
    sustainability_list = []
    for impact in item_soup.find_all(attrs={'class': 'metric__value-box'}):
        val=impact.find(attrs={'class': 'metric__value'}).text
        unit=impact.find(attrs={'class': 'metric__unit'}).text
        desc=impact.find(attrs={'class': 'metric__description'}).text
        sustain_impact = val+' '+unit+' '+desc
        sustainability_list.append(sustain_impact)

    product_detail["description"] = short_desc
    product_detail["sustainability"] = sustainability_list
    product_detail["image_gallery"] = image_harvester(link, 'product-media-container')

    break

#print(product_detail["description"])
#print(product_detail["sustainability"])
#print(product_detail["image_gallery"])
#print(product_detail)
