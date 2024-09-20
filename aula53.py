"""
enumerate - enumera iteráveis (índices)
"""
lista = ['Marcelo', 'José', 'Coccaro']
lista.append('Junior')


for  tupla_enumerada in enumerate(lista):
    print("FOR da tupla:")
    for valor in tupla_enumerada:
        print(f'\t{valor}')