import pandas as pd
import requests
import numpy as np
import time, random
import scipy
import tensorflow as tf
import keras
from requests.exceptions import ChunkedEncodingError

n = []


user_agent_list = [
  'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
  'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0',
  'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
  'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:77.0) Gecko/20100101 Firefox/77.0',
  'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
]

print('how many tickers?')
tickerscount = int(input())
for x in range(tickerscount):
    print('enter ticker')
    tick = input()
    tick = tick.upper()
def datagetter(link):
    try:
        user_agent = random.choice(user_agent_list)
        headers = {'User-Agent': user_agent}
        r = requests.get(link, headers=headers)
        data = pd.read_html(r.text)
        data = data[0]
        close = data[['Close*']]
        return close
    except ConnectionResetError or ChunkedEncodingError:
        return pricelist[-1]


link = 'https://finance.yahoo.com/quote/TSLA/history?p=TSLA'
link = link.replace("TSLA", tick)


tesla = []
price = []

price = (datagetter(link))
price = price.values.tolist()
tesla.append(price)
print(tesla)
tesla[0].pop(-1)
print(tesla)
print(len(tesla[0]))

looper = 1

pricelist = tesla
print(pricelist)

pricelist = tf.keras.utils.normalize(pricelist, axis=1)
print(pricelist)