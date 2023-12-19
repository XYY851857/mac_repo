import time

from selenium import webdriver
from selenium.webdriver.common.by import By

wd = webdriver.Chrome()

wd.get('https://www.google.com.tw/')

element = wd.find_element(By.ID, 'APjFqb')

search = wd.find_element(By.CLASS_NAME,  'gNO89b')

element.send_keys('hello ')
time.sleep(0.1)
search.click()
input()
