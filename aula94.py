# Try, except, else e finally 
# finally vai ser executado msm que tenha erro

try:
    print('ABRIR ARQUIVO')
    # 8/0
except ZeroDivisionError:
    print('DIVIDIU ZERO')

finally:
    print('FECHAR ARQUIVO')