# -*- coding:utf-8 -*-
# Author : JerryChu
import requests
from pyquery import PyQuery as pq
forms = ['.png', '.jpeg', '.jpg', '.gif', '.bmp']

def getPage(num):
    url='http://jandan.net/ooxx/page-'+str(num)
    html = requests.get(url=url)
    doc = pq(html.content)
    return doc

def Endswith(string):
    for f in forms:
        if string.endswith(f):
            return f
    return ''

def saveImg(link,n,f):
    pic = requests.get(link, timeout=30)
    string = 'pic\\' + str(n) +f
    fp = open(string, 'wb')
    fp.write(pic.content)
    fp.close()

i=1
for n in range(1,11):
    doc=getPage(n)
    for d in doc('img').items():
        link = d.attr('src')
        f = Endswith(link)
        if f:
            if link.startswith('http'):
                print link
                saveImg(link,i,f)
                i=i+1

            elif link.startswith('//'):
                link='http:'+link
                print link
                saveImg(link, i,f)
                i = i + 1




