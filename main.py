# -*-encoding:utf-8-*-
# filename:main.py

import html2pdf
import parse_body
import parse_menu

from urlparse import urlparse

url = 'http://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000/001386818214042e9c46552422e42d8a00f019e088506ce000'
domain = '{uri.scheme}://{uri.netloc}'.format(uri=urlparse(url))

htmls = []
menulist = parse_menu.menu(url,domain)
for index,menu in enumerate(menulist):
    html = parse_body.body(menu)
    f_name = ".".join([str(index),'html'])
    with open(f_name,'wb') as f:
        f.write(html)
    htmls.append(f_name)

html2pdf.html2pdf(htmls,"pythonbyliao")
