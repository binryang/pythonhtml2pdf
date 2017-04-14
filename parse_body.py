# -*-encoding:utf-8-*-
# filename:parse_body.py

import requests
from bs4 import BeautifulSoup
import re
from urlparse import urlparse

hds = {
    'User-Agent': 'Mozilla AppleWeb/5.0 (Macintosh; Intel Mac OS X 10_7_0)Kit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11'
}


html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
</head>
<body>
{content}
</body>
</html>
"""

url = 'http://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000/001386818214042e9c46552422e42d8a00f019e088506ce000'
domain = '{uri.scheme}://{uri.netloc}'.format(uri=urlparse(url))

def match(m):
    if not m.group(2).startswith("http"):
        return "".join([m.group(1),domain,m.group(2),m.group(3)])
    else:
        return "".join([m.group(1),m.group(2),m.group(3)])

def body(url):
    response = requests.get(url,hds)
    soup = BeautifulSoup(response.content,'html.parser')
    body = soup.find(class_='x-wiki-content')

    #获取标题，并且居中
    title = soup.find('h4').get_text()
    center_tag = soup.new_tag("center")
    title_tag = soup.new_tag("h1")
    title_tag.string = title
    center_tag.insert(1,title_tag)
    body.insert(1,center_tag)

    html_body = str(body)

    #image图片地址补全
    pattern = r'(<img .*?src=")(.*?)(")'
    html_body = re.sub(pattern,match,html_body)

    html = html_template.format(content=html_body).decode("utf-8")#解码出问题 解决办法
    html = html.encode("utf-8")
    return html
