from selenium import webdriver as web
from selenium.webdriver.chrome.service import Service

ser = Service('C:/Users/ampna/Github/work/pro/bombobot/src/chromedriver.exe')
bot = web.Chrome(service=ser)
bot.get('https://app.bombcrypto.io/')