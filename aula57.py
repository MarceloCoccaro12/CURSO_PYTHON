"""
Lista de listas e seus indices
"""

salas = [
    # 0        1
    ['Maria', 'Helena'],  #0
    # 0 
    ['Elaine'],  #1
    # 0       1       2         
    ['Luiz', 'João', 'Eduarda'],  #2
]

#print(salas[1][0])
#print('-' * 10)
#
#print(salas[0][1])
#print('-' * 10)
#
#print(salas[0][1])
#print('-' * 10)


for sala in salas:
    print(f'A sala é {sala}')
    
    for aluno in sala:
        print(aluno)