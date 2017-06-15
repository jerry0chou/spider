# -*- coding:utf-8 -*-
# Author : JerryChu
import requests,re
head='http://www.jikexueyuan.com/course/?pageNum='
def singlepage(num,picnum):
    link=head+str(num)
    html=requests.get(link)
    content=html.content
    urls=re.findall('<div class="lessonimg-box">(.*?)</div>',content,re.S)

    for u in urls:
        picurl=re.findall('<img src="(.*?)"', u)[0]
        #print picurl
        form= re.split('\.',picurl)[-1]
        pic = requests.get(picurl,timeout=30)
        string = 'pic\\' + str(picnum) +"."+ form
        fp = open(string, 'wb')
        fp.write(pic.content)
        fp.close()
        picnum += 1
    return picnum

picnum=1
for num in range(1,96):
    picnum=singlepage(num,picnum)