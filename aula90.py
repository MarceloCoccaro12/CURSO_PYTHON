""" 
Generator expression (funções que sabem pausar), 
Iterables(dete os valores sequencialmente, varios valores ) e 
Interators(entrega um valor por  vez, entrega só o próximo valor) em Python
"""
import sys


iterable = ['Eu','Tenho', '__iter__']
iterator = iter(iterable) # tem __iter__ e __next__

lista = [n for n in range(1000000)]
generator = (n for n in range(1000000))
print(sys.getsizeof(lista))
print(sys.getsizeof(generator))

for n in generator:
    print(n)