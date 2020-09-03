nomes = ['Guilherme', 'Marcelo', 'Joao', 'Julia']
for nome in nomes:  #estrutura do for para percorrer o array.
    print(nome) 
    
print('\n######################\n')

for i in range(len(nomes)):
    print(nomes[i])

print('\n######################\n')

lista_de_numeros = range(5) #criou uma lista com 5 numeros

lista_de_numeros_com_passo = range(0, 100, 2) #criar lista de numeros que comece em 0, até 100 e passe de 2 em 2 

for item in lista_de_numeros_com_passo:
    print(item)


for item in lista_de_numeros:
    print(item)

print('\n######################\n')


i = 0
while i < 10:
    print("Loop Infinito: ", i)
    i+=1


palavra = 'Herllon Cardoso'

for letra in palavra:
    print(letra)

print('\n######################\n')



lista_frutas = [ 'Maça', 'Banana', 'Abacaxi', 'Uva', 'Goiaba']

print(len(lista_frutas))

for fruta in lista_frutas:
    print(fruta)



numero = 0

while True:
    print(numero)
    if numero == 20:
        break
    numero+=1