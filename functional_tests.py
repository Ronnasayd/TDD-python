from selenium import webdriver
import os

path = os.path.dirname(os.path.abspath(__file__))
browser = webdriver.Chrome(path+'/chromedriver')
browser.get('http://localhost:8000')
assert 'Django' in browser.title
browser.quit()
