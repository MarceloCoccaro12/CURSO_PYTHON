# sys.args - Executando arquivos com argumentos no sitema
# Fonte = Fire Code 
import sys

argumentos = sys.argv
qnt_argumentos= len(argumentos)

if qnt_argumentos <= 1:
    print('Você não passou argumentos')
else:
    try:
        print(f'Você passou os argumentos {argumentos[1:]}')
        print(f'Faça alguma coisa com {argumentos[1]}')
        print(f'Faça outra coisa com {argumentos[2]}')
    except IndexError:
        print('Faltam algumentos')