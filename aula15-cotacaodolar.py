import requests
import json
import time
import datetime

while True:
    requisicao = requests.get('https://economia.awesomeapi.com.br/json/all/')
    cotacao = json.loads(requisicao.text)

    print('\nAtualizado as: ', datetime.datetime.now(),'\n')
    print('Cotação do Dolar:', cotacao['USD']['high'])
    print('Cotação do Euro:', cotacao['EUR']['high'])
    print('Cotação do Euro:', cotacao['BTC']['high'])
    time.sleep(2)





