"""
Imprecisão de ponto flutuante
Double-precision floating-point format IEEE 754

3 FORMAS DE CORRIGIR O NÚMERO FLUTUANTE
"""
import decimal

numero_1 = decimal.Decimal('0.1')
numero_2 = decimal.Decimal('0.7')
numero_3 = numero_1 + numero_2

print(numero_3)

print('-'* 10)

print(f'{numero_3:.2f}')

print('-'* 10)

print(round(numero_3 ,2))