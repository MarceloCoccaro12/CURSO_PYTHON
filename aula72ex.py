
# Exercícios com funções
# 
# - Crie uma função que multiplica todos os argumentos 
# não nomeados recebidos.
# - Retorne o total para uma variavel e mostre o valor 
# da variável.


def multiplicar(*args):
    total = 1
    for numero in args:
        total *= numero
    return total

multiplicacao = multiplicar(1, 2, 3, 4, 5, 6)
print(multiplicacao)

print('-' * 15)
# - Crie uma função fala se um número é par ou impar.
# - Retorne se o número é par ou ímpar.

def par_impar(numero):
    multiplo_dois= numero % 2 == 0

    if multiplo_dois:
        return f"{numero} é par"
    return f"{numero} é ímpar"

print(par_impar(3))
print(par_impar(5))
print(par_impar(4))
print(par_impar(6))