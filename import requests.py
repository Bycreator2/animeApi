


import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import json
 
 
# Making a GET request
url = 'https://www.animeworld.tv/play/fairy-tail.Nqevg/XAfbR'

driver = webdriver.Chrome(executable_path='C:/Users/Utente/Desktop/chromedriver.exe') 
driver.get(url) 

time.sleep(5)

html = driver.page_source

soup = BeautifulSoup(html, "html.parser")
all_divs = soup.find('a', {'id' : 'alternativeDownloadLink'})

linkOttenuti = []

episodiFinali = []

pagina = 0;
  
for link in soup.find_all('li', {'class':'episode'}):
    ss = link.findChildren('a' , recursive=False)
    print(ss[0].get('href'))
    linkOttenuti.insert(1, ss[0].get('href'))
    
    if ss[0].get('href') in linkOttenuti == True:
        print("Ngia trovato")
    
    driver.get('https://www.animeworld.tv'+ss[0].get('href'))
    time.sleep(5)
    
    pag2 = driver.page_source

    pppp = BeautifulSoup(pag2, "html.parser")


    all_divs = pppp.find('a', {'id' : 'alternativeDownloadLink'})
    episodiFinali.insert(len(episodiFinali), {"Ep{}".format(all_divs.findChildren('span' , recursive=False)[0].text.strip()) : all_divs.get("href")})
    print(json.dumps(episodiFinali))
    
    driver.get(url)
    time.sleep(5)
    link.clear()

# printing top ten job profiles
#print(all_divs.get('href'))
  
driver.close() # closing the webdriver