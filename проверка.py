from flask import Flask, render_template
from bs4 import BeautifulSoup
import requests

url = 'https://yandex.com.am/weather/?lat=55.75581741&lon=37.61764526'
response = requests.get(url)
bs = BeautifulSoup(response.text,"lxml")
temp = bs.find('span', 'temp__value temp__value_with-unit')

text_2 = str(temp.text)

print(text_2)