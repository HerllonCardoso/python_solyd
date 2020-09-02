def maiorValor(colecao):
    maior_item = colecao[0]
    for item in colecao:
        if item > maior_item:
            maior_item = item
    return maior_item


def menorValor(colecao):
    menor_item = colecao[0]
    for item in colecao:
        if item < menor_item:
            menor_item = item
    return menor_item
    
        

print(maiorValor((1,2,3,4,5,6)))
print(menorValor((1,2,3,4,5,6)))