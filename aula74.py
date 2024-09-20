"""
Closure são funções que retornam outras funções
"""
def criar_saudacao(saudacao):
    def saudar(nome):
        return f'{saudacao}, {nome}!'
    return saudar

falar_bom_dia = criar_saudacao('Bom dia')
falar_boa_noite = criar_saudacao('Boa noite')

print(falar_bom_dia("Marcelo"))
print(falar_boa_noite("Marcelo"))
print(falar_bom_dia('Mãe'))
print(falar_boa_noite('Mãe'))

print('-' * 10)


for nome in ['Marcelo', 'José', "Cecília"]:
    print(falar_bom_dia(nome))
   