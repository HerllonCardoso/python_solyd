my_list = ['Gui', 'Joao'] #LIST  

my_tuple = ('Gui', 'Joao') #TUPLE  Can modified, but cant removed.   Limited number of objects. Used when you have a defined number of stuff.

my_dictionary = {'name': 'Herllon', 'age': 20}   #Similar as JSON in JS.    DICT

my_set = {'Gui', 'Joao'}     #Does not have repeated elements and keys.

print(my_tuple[1])


for nome in my_tuple:
    print(nome)

my_tuple[0]


if 'Gui' in my_tuple:
    print('Gui esta na colecao')


print(my_dictionary['age'])


if 'Herllon' in my_dictionary.values():
    print("Herllon esta no dicionario")

lista = []
tupla = ()
dicionario = {}
conjunto = set()