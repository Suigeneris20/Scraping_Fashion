import pandas as pd
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver import ChromeOptions
import requests

def page_content(url):
    option = ChromeOptions()
    option.add_argument("--headless=new")
    driver = webdriver.Chrome(options=option)
    driver.get(url)
    content = driver.page_source
    print(driver.current_url)
    driver.quit()
    return content


def image_harvester(item_url, class_tag, tag='img', link_source='src'):
    '''
    Takes clothing_item link, div class name, tag name, and link source. For example:
    (item_url, class='product-detail', tag='img', source='src')
    Returns list of all images in gallery for specific item
    '''
    list_of_image_links = []
    content = page_content(item_url)
    soup = bs(content, 'html.parser')
    for image in soup.find_all(attrs={'class': class_tag}):
        name = image.find(tag)
        link = name.get(link_source)
        if link not in list_of_image_links:
            list_of_image_links.append(f'https:{link}')


    return list_of_image_links    

'''
https://harvestandmill.com/products/pants-black
class="product__image"
'''
