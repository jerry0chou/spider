# -*- coding:utf-8 -*-
# Author : JerryChu
from selenium import webdriver
driver = webdriver.PhantomJS()
driver.get("http://hotel.qunar.com/")
data = driver.title
print data

driver.quit()