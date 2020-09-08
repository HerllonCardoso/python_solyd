import requests



cidade = input("Escreva sua cidade: ")


requisicao = requests.get('api.openweathermap.org/data/2.5/weather?q='+cidade+'&appid=1df3c07645b54fa1b7950907eeecbd8c')


print(requisicao.text)

