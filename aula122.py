# Enrendendo self em classes Python
# Classe - Molde (geralmente sme dados)
# Instância de  class (objeto) -  Tem os dados
# Uma classe pode gerar várias instâncaias.
# Na classe o self é a própria instância
class Carro:
    def  __init__(self, nome):
        self.nome = nome 

    def acelerar(self):
        print(f'{self.nome} está acelerando...')
        

fusca = Carro('Fusca')
fusca.acelerar()
Carro.acelerar(fusca)
# print(fusca.nome)
# fusca.acelerar()

celta = Carro(nome='Celta')
celta.acelerar()
Carro.acelerar(celta)
# print(celta.nome)
# celta.acelerar()
