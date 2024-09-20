# Métodos úteis dos dicionários em Python
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro

# pessoa = {
#      'nome': 'Luiz Otávio',
#      'sobrenome': 'Miranda',
#      'idade': 900,
# }
# print(len(pessoa))
# print('-' * 10)
# print(list(pessoa.keys()))
# print('-' * 10)
# print(list(pessoa.values()))
# print('-' * 10)
# print(list(pessoa.items()))
# print('-' * 10)
# print()

# d1 = {
#     'c1': 1,
#     'c2': 2,
#     'l1' : [0, 1, 2],
# }
# 
# d2 = d1.copy()
# 
# d2['c1'] = 1000
# d2['l1'][1] = 99999

# print(d1)
# print(d2)

p1 = {
       'nome': 'Luiz Otávio',
       'sobrenome': 'Miranda',
}
# print(p1.get('nome'))
# print()
# 
# nome = p1.pop('nome')
# print(nome)
# print(p1)
# print()

# ultima_chave = p1.popitem()
# print(ultima_chave)
# print(p1)

p1.update({
    'nome': 'novo valor',
    'idade':30,
})
print(p1)