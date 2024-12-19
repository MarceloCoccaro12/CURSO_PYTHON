# Encapsulamento (modificadores de acesso: public, protected, private)
# Python NÃO TEM modificadores de acesso
# Mas podemos seguir as seguintes convenções
#   (sem underline) = public
#       pode ser usado em qualquer lugar
# _ (um underline) = protected
#       não DEVE ser usado fora da classe
#       ou suas subclasses.
# __ (dois underlines) = private
#       "name mangling" (desfiguração de nomes) em Python
#       _NomeClasse__nome_attr_ou_method
#       só DEVE ser usado na classe em que foi
#       declarado.
from functools import partial

class Foo:
    def __init__(self):
        self.public = 'isso é público'
        self._protected = 'isso é protegido'
        self.__private = 'isso é private'


    def metodo_publico(self):
        # self._medoto_protected()
        # print(self._protected)
        print(self.__private)
        self.__medoto_private()
        return 'metodo_publico'
    
    def _medoto_protected(self):
        print('_medoto_protected')
        return '_medoto_protected'
    
    def __medoto_private(self):
        print('__medoto_private')
        return '__medoto_private'
    
f = Foo()
# print(f._protected)
# print(f.public)
print(f.metodo_publico())
