"""
Retorno de valores das funções (return)
"""

def soma(x, y):
    if x > 10:
        return 10, 20 
    
    return x + y # retorna este valor. retornando este valor ele pode ir para onde ele quiser


soma1 = soma(2, 2)
soma2 = soma(3, 3)
print(soma1)
print(soma2)
print(soma(11, 55))