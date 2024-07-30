from flask import Flask, render_template
from bs4 import BeautifulSoup
import requests
from random import choice

name = choice(['орел', 'решка'])

url = 'https://rg.ru/2022/01/26/reg-dfo/kakie-strany-i-rossijskie-regiony-bolshe-vsego-postradaiut-ot-globalnogo-potepleniia.html'
response = requests.get(url)
bs = BeautifulSoup(response.text,"lxml")
temp = bs.find('div', 'PageArticleContent_lead__gvX5C')
app = Flask(__name__)

url_2 = 'https://yandex.com.am/weather/?lat=55.75581741&lon=37.61764526'
response_2 = requests.get(url)
bs_2 = BeautifulSoup(response_2.text,"lxml")
temp_2 = bs_2.find('span', 'temp__value temp__value_with-unit')

@app.route("/")
def one():
    return render_template('index.html')


@app.route("/about")
def two():
    text = str(temp.text)
    return render_template('about.html', value=text)


@app.route("/temperature")
def three():
    text_2 = str(temp_2)
    return render_template('temperature.html', text_2=text_2)


@app.route("/videos")
def five():
    return render_template('videos.html')

@app.route("/maps")
def six():
    return render_template('maps.html')


@app.route('/comment')
def four():
    return render_template('comment.html')


app.run(debug=True)
