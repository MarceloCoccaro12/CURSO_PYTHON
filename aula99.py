# from sys import path

# from aula99_package.modulo import soma_do_modulo
# import aula99_package.modulo
# from aula99_package import modulo
# from aula99_package.modulo import * # má prática, porque tem que espeficicar tudo que vira


# # print(path, sep='\n')
# print(soma_do_modulo(1, 2))
# print(aula99_package.modulo.soma_do_modulo(1, 2))
# print(modulo.soma_do_modulo(1, 2))
# print(variavel)
# print(nova_variavel)
# from aula99_package.modulo import soma_do_modulo, fala_oi

# print(__name__)
# fala_oi()

# todas as importações dentro do programa, devem ser relativas ao main

from aula99_package import fala_oi,soma_do_modulo

print(soma_do_modulo(2, 3))
fala_oi()