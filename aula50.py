"""
Exercicio
Exiba os índices da lista
0 Maria
1 Helena
2 Luiz

"""

lista = ['Marcelo', 'José', 'Coccaro']
lista.append('Junior')

indice = range(len(lista))

for i in indice:
    print(i, lista[i])