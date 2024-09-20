"""
Escopo de funções em Python
Escopo significa o local onde aquele código pode atingir.
Existe o escopop global e local.
O escopo global é o escopo onde todo o código é alcançavel.
O escopo local é o escopo onde apenas nomes do mesmo local 
podem ser alcançados.
"""
x = 1


def escopo(): # tudo o que definir no escopo, fica somente lá
    x = 10

    def outra_funcao(): # só posso fazer algo com este Y dentro desta função
        x = 11
        y = 2
        print(x, y)

    outra_funcao()
    print(x) 


escopo()

print(x) # X fora da função