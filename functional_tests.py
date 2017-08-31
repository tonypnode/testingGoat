from selenium import webdriver

browswer = webdriver.Firefox()
browswer.get('http://localhost:8000')

assert 'Django' in browswer.title

