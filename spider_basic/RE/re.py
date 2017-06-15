# -*- coding:utf-8 -*-
# Author : JerryChu
import re

secret_code='gfhfggdxxixxdfgdffdgdfgwetqwtyxxlovexxqrretryrxxyouxxgf'

# .的使用举例  点就是一个占位符
# a='xz123'
# b=re.findall('x.',a)
# print b

# *的使用举例 找到全部
# a='xyxy123'
# b=re.findall('x*',a)
# print b

# ?的使用举例 匹配前面的支付 0 次或者 1次
# a='xy123'
# b=re.findall('x?',a)
# print b

# .* 的使用举例  尽可能的吃更多的东西
b =re.findall('xx.*xx',secret_code)
print b

# .*? 的使用举例  非贪心算法  少量多餐
c =re.findall('xx.*?xx',secret_code)
print c

# .*? 的使用举例  使用括号和不使用括号的区别   括号里是需要的内容
c =re.findall('xx(.*?)xx',secret_code)
print c

s='''fghsexxhelllo
xxhghjgxxworldxxmn
'''
c =re.findall('xx(.*?)xx',s)
print c

c =re.findall('xx(.*?)xx',s,re.S)  # re.S 表示包括换行符
print c,"c%"

# 对比findall 和search 的区别
s2='asdfxxIxx123xxlovexxert'
f=re.search('xx(.*?)xx123xx(.*?)xx',s2)
print f.group(),f.group(1),f.group(2)

f2=re.findall('xx(.*?)xx123xx(.*?)xx',s2)
print f2[0][0]

info = re.findall('xx(.*?)xx',secret_code,re.S) # re.S 表示包括换行符
for each in info :
    print each

a='dsfsdf12345678dsfrgr'
b=re.findall('(\d+)',a)[0]
print b