# -*- coding:utf-8 -*-
# Author : JerryChu
import requests,re

# 利用正则表达式(.*?) 爬取百度首页

html =requests.get('http://www.baidu.com')
content=html.content
urls=re.findall('src=//(.*?) width',content,re.S)

i=0
for each in urls:
    url='http://'+each
    pic=requests.get(url)
    string = 'pic\\' + str(i) + '.png'
    fp = open(string, 'wb')
    fp.write(pic.content)
    fp.close()
    i += 1

