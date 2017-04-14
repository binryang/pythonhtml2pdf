# -*- encoding:utf-8 -*-
# filename:parse_menu.py

import requests
from bs4 import BeautifulSoup

hds = {
    'User-Agent': 'Mozilla AppleWeb/5.0 (Macintosh; Intel Mac OS X 10_7_0)Kit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11'
}

def menu(url,domain):
    response = requests.get(url,hds)
    soup = BeautifulSoup(response.content,'html.parser')
    menu_tag = soup.find_all(class_='uk-nav uk-nav-side')[1]
    for li in menu_tag.find_all('li'):
        href =  li.find("a").get("href")
        if not href.startswith("http"):
            href = "".join([domain,href])
        yield href

