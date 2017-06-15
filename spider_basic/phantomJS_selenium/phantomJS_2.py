# -*- coding:utf-8 -*-
# Author : JerryChu
from selenium import webdriver
from pyquery import PyQuery as pq
driver = webdriver.PhantomJS()
driver.get('http://huaban.com/favorite/beauty/')
#driver.maximize_window()
driver.save_screenshot("1.png")   #截图保存
#driver.execute_script('http://cpro.baidustatic.com/cpro/ui/i.js')
print driver.page_source
driver.quit()