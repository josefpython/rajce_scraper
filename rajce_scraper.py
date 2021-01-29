import requests
from bs4 import BeautifulSoup
import responsivepathing as rp
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

PATH = "C:\Program Files (x86)\chromedriver.exe"
todownload = open(rp.here("mn.in"),"r").read().split("\n")

rajce_url = "https://litacijelen.rajce.idnes.cz/Suche_Poland_24.01._2021/"
rajce_main = requests.get(rajce_url)
soup = BeautifulSoup(rajce_main.content, "html.parser")
x = soup.find("div", id="thumbs-container")
idlsit = str(x).split("medium_")
all_ids = []


try:
    for item in idlsit:
        all_ids.append(item.split('data-medium-id="')[1].split('"')[0])
        
except Exception:
    pass



piclinks = []
browser = webdriver.Chrome(PATH)
n=0


for item in all_ids:
    
    if str(n) in todownload:

        print("downloading", n)

        url = rajce_url + item
        browser.get(url)
        html = browser.page_source

        soup = BeautifulSoup(html, "html.parser")
        image = soup.find("img", id="detail-image", src=True)["src"]

        response = requests.get(image)
        f = open(rp.here(str(n)+".jpg"), "wb")
        f.write(response.content)
        f.close()

        n+=1

    else:
        print("passing", n)
        n+=1
