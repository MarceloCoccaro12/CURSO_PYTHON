#List comprehesion com mais de um for


lista = [
    (x, y)
    for x in range(3)
    for y in range(3)
]

print(lista)