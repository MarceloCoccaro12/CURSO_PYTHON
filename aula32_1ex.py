"""
Faça um programa que peça ao usuário para digitar um número inteiro,
Informe se este número é par ou impar. Caso o usuário não digite um número
inteiro, informe que não é um número.
"""
num = input("Digite um número:")

try:
    num_int= int(num)
    par_impar= num_int % 2 == 0
    par_impar_texto= "ímpar"

    if par_impar:
        par_impar_texto= "par"
    print(f"O número {num_int} é {par_impar_texto}")

except:
    print("Você não digitou um número inteiro")






