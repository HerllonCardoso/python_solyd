frase = 'Oi, tudo bem ?'
lista_nomes = ['Joao', 'Maria', 'Guilherme', 'Diego', 'Joao', 'Herllon']
# lista_nomes.append('Geralda') #Adicionar item no array
# lista_nomes.append('Lorena') #Adicionar item no array
# lista_nomes.remove('Joao') #Remover item no array
# lista_nomes.append('Joao') #Adicionar item no array
# lista_nomes.insert(0, 'Herllon') #Inserir na posicaoo declarada item no array


contador_joao = lista_nomes.count('Herllon') #Conta quantos Herllon tem na lista

print(frase.lower()) #passar a frase toda para minusculo
print(frase.upper()) # passar a frase para maisculo

frase_separada = frase.split(',') #Separou a frase na virgula e transformou em lista
print(frase_separada)

frase_nova = frase + ' Como vai você ?' #concatenar a variavel frase com a nova string.
print(frase_nova)


print(len(lista_nomes)) #Conta quantos items tem na lista

print(lista_nomes.pop())
 #pega o ultimo da lista e remove
print(lista_nomes)

print(lista_nomes)
print(contador_joao)

