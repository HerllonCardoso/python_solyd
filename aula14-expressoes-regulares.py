import re
import requests

requisicao = requests.get('http://www.aalborg-industries.com.br/general.php?ix=9')

# tentar = 'petropolis@bramilemcasa.com.br'

padrao = re.findall(r'[\w\.-]+@[\w-]+\.[\w\.-]+', requisicao.text)

if padrao:
    print(padrao)
else:
    print("Padrao nao encontrado")