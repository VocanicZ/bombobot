import requests
from bs4 import BeautifulSoup
import time

def get_crypto_price():
#Get the URL
    url = 'https://coinmarketcap.com/th/currencies/bombcrypto/'
    HTML = requests.get(url) 
    soup = BeautifulSoup(HTML.text, 'html.parser') 
    text = soup.find("div", attrs={'class':'priceValue'}).text
    return text