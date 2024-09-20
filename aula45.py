"""
Iterável -> str, range, etc (__iter__)
Iterador -> quem sabe entregar um valor por vez
next -> me entregue o próximo valor
iter -> me netregue seu iterador
"""
texto = 'Luiz' # iterável
iteratador = iter(texto) # iterator

while True:
    try:
        print(next(iteratador))
    except StopIteration:
        break