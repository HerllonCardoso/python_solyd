print("Você já está pronto para fazer parte das Forças Armadas do Brasil?")

idade = (int(input("Qual sua idade? ")))
peso = (float(input("Quanto você pesa? ")))
altura = (float(input("Qual é a sua altura? ")))

# print(type(idade), type(peso), type(altura))

if idade >= 18 and peso >= 60 and altura >= 1.70:
    print('Voce está apto a servir')
else: 
    print('Voce nao está apto')