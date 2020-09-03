numero_convidados = input("Quantas pessoas serão convidadas? ") 

lista_pessoas = []

i = 1
while i <= int(numero_convidados):
    nome_convidado = input("Digite o nome do convidado #"+ str(i) +" : ") 
    lista_pessoas.append(nome_convidado)
    i+=1


print('Serão', numero_convidados, 'convidados')

print('\nLISTA DE CONVIDADOS:')

for convidado in lista_pessoas:
    print(convidado)
  
    








