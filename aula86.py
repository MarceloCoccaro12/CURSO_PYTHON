# Dictionary Comprehension e Set Comprehension

produto = {
    'nome': 'Caneta Azul',
    'preco': 2.5,
    'categoria': 'Escritório',
}

dc = {
    chave: valor.upper()
    if isinstance(valor, str) else valor
    for chave, valor
    in produto.items()
}

lista = [
    ('a', 'valor a'),
    ('b', 'valor a'),
    ('a', 'valor a'),
]

dc = {
    chave : valor 
    for chave, valor in lista
}

print(dc)

s1 = {2 ** i for i in range(10)}
print(s1)
