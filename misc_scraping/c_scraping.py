import pandas as pd
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver import ChromeOptions


def page_content(url):
    option = ChromeOptions()
    option.add_argument("--headless=new")
    driver = webdriver.Chrome(options=option)
    driver.get(url)
    content = driver.page_source
    driver.quit()
    return content


content = page_content('https://launchaccelerator.co/#alumni-section')
soup = bs(content, 'html.parser')
results = {}

links = []
for element in soup.find_all(attrs={'class':'margin-wrapper'}):
    
    if(element.find('a')):
            item = element.find('a')
            link = item.get('href', '')
            if(link and link[0] == '/'):
                to_go = f'https://launchaccelerator.co{link}'
                new_content = page_content(to_go)
                sp = bs(new_content, 'html.parser')
                links.append(sp.find(attrs={'class':'responsive-wrapper'}).find('a').get('href', ''))
            else:
                
                links.append(link)
names = []
for l in links:
    name = ""
    if "." in l:
        index1 = l.find(".", 0)
        
        index2 = l.find(".", index1+1)
        
        if(index2 == -1):
            name = l[l.index("//")+2:index1]
        else:
            name = l[index1+1:index2]
    names.append(name)

res = pd.DataFrame({'Names' : names, 'Links' : links})
print(res)
#res.to_csv('/path_to_save/to/name_of_file.csv', index=False)

