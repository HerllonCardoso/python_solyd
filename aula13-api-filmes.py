import requests
import json

def requisicao(titulo):
    try:
        req = requests.get('http://www.omdbapi.com/?t='+titulo+'&type=movie&apikey=13189dfc')
        dicionario = json.loads(req.text)
        return dicionario
    except:
        print("Erro na requisição")
        return None

def print_details(filme):
    print('Titulo:', filme['Title'])
    print('Ano:', filme['Year'])
    print('Diretor:', filme['Director'])
    print('Atores:', filme['Actors'])
    print('Nota:', filme['imdbRating'])
    print('Premios: ', filme['Awards'])
    print('Poster: ', filme['Poster'])

sair = False
while not sair:
    op = input('Escreva um nome de um filme ou SAIR para fechar: ')

    if op == 'SAIR':
        sair = True
    else:
        filme = requisicao(op)
        if filme['Response'] == 'False':
            print('Filme nao encontrado')
        else:
            print_details(filme)


