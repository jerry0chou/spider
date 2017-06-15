# -*- coding:utf-8 -*-
# Author : JerryChu
import requests
from pyquery import PyQuery as pq

url = 'http://www.avavav1.com/tag/Prestigechupin/'

# user = {'source':'index_nav','form_email':'18670026041','form_password':'qq6355815'}
# html=requests.post(url=url,data=user).content
header = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36'
}
html = requests.get(url=url, headers=header).content

# 使用COOkies
cookies = {}
# raw_cookie=''
# for line in raw_cookie.split(';'):
#     key,value=line.split('=',1) # 代表之分一次，得到两个数据
#     cookies[key]=value
#
# html = requests.get(url=url,cookies=cookies).content





doc = pq(html)
print doc
print doc('title').text()

forms = ['.png', '.jpeg', '.jpg', '.gif', '.bmp']


def Endswith(string):
    for f in forms:
        if string.endswith(f):
            return f
    return ''


def saveImg(link, n, f):
    pic = requests.get(link, timeout=30)
    string = 'pic/' + str(n) + f
    fp = open(string, 'wb')
    print '正在保存图片' + string
    fp.write(pic.content)
    fp.close()


i = 1
for d in doc('img').items():
    link = d.attr('src')
    f = Endswith(link)
    if f:
        if link.startswith('http'):
            print link
            saveImg(link, i, f)
            i = i + 1

        elif link.startswith('//'):
            print link
            link = 'http:' + link
            saveImg(link, i, f)
            i = i + 1
