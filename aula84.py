# List comprehension em Python
# List comprehension é uma forma rádida para criar listas
# a partir de iteráveis
# print(list(range(10)))
import pprint

def p(v):
    pprint.pprint(v, sort_dicts=False,  width=40)





lista = []
for numero in range(10):
    lista.append(numero)
#print(lista)

lista = [
    numero * 2
    for numero in range(10)
]
# print(lista)


maior = range(10)

maiores = [num for num in maior if num > 5]
# print(maiores)
# print()
# Mapeamento de dados em list comprehension

produtos = [
    {'nome': 'p1', 'preco': 20},
    {'nome': 'p2', 'preco': 10},
    {'nome': 'p3', 'preco': 30},
]

novo_produtos = [
    {**produto, 'preco': produto['preco'] * 1.05} 
    if produto['preco'] > 20 else {**produto}
    for produto in produtos
]

# print(*novo_produtos, sep='\n') # aqui foi desempacotado e uma quebra de linha
#p(novo_produtos)

# lista = [n for n in range(10) if n < 5]
# print(lista)
# 
# Filtro de dados em list comprehension

novo_produtos = [
    {**produto, 'preco': produto['preco'] * 1.05} 
    if produto['preco'] > 20 else {**produto}
    for produto in produtos
    if (produto['preco'] >= 20 and produto['preco'] * 1.05) > 10
]
p(novo_produtos)